import _thread
import audiobusio # type: ignore
import audiocore # type: ignore
import board # type: ignore
import audiomixer # type: ignore
import array
from machine import *
import math
import usb_midi # type: ignore
import adafruit_midi # type: ignore

from adafruit_midi.note_off import NoteOff # type: ignore
from adafruit_midi.note_on import NoteOn # type: ignore

globalUpdates = {"pins": [], "noteBottem": 0, "noteLayout": "linear"}
notes = ["C", "D", "E", "F", "G", "A", "B"]
noteLayouts = ["linear", "scale"]
voices = [-1 for _ in range(8)]

#pins
midi = adafruit_midi.MIDI(
    midi_in=usb_midi.ports[0], in_channel=0, midi_out=usb_midi.ports[1], out_channel=0
)
dac = audiobusio.I2SOut(bit_clock=board.GP0, word_select=board.GP1, data=board.GP2)
mixer = audiomixer.Mixer(voice_count=8, sample_rate=8000, channel_count=1, bits_per_sample=8, samples_signed=False)

i2c = I2C(0, scl=Pin(1), sda=Pin(0))
PiI2s = Pin(25, Pin.OUT, value=0)
dacPower = Pin(13, Pin.OUT, value=0) # 0 is on
intPins = [Pin(i, Pin.IN, Pin.PULL_UP) for i in [0,1,2,3,6]]

movePins = [Pin(i, Pin.IN, Pin.PULL_UP) for i in [24,23,21,22]]
notePin = Pin(18, Pin.IN, Pin.PULL_UP)
pinStates = [[0 for _ in range(8)] for _ in range(8)]

#i²c setup
for i in range(0x20, 0x24+1):
    i2c.writeto_mem(i, 0x0A, 0b01010010)
    i2c.writeto_mem(i, 0x00, 0b11111111)
    i2c.writeto_mem(i, 0x01, 0b00000000)
    i2c.writeto_mem(i, 0x02, 0b00000000)
    i2c.writeto_mem(i, 0x03, 0b11111111)
    i2c.writeto_mem(i, 0x04, 0b11111111)
    i2c.writeto_mem(i, 0x05, 0b11111111)
    i2c.writeto_mem(i, 0x06, 0b11111111)
    i2c.writeto_mem(i, 0x07, 0b11111111)
    i2c.writeto_mem(i, 0x08, 0b00000000)
    i2c.writeto_mem(i, 0x09, 0b00000000)
    i2c.writeto_mem(i, 0x0C, 0b11111111)
    i2c.writeto_mem(i, 0x0D, 0b11111111)

dac.play(mixer)

# handel interupts
def getSetBits(byte, addvalue=0): #returns list of the indecies of all the bits that are set.
    if byte == 0: return []

    value = math.floor(math.log2(byte))
    return getSetBits(byte-2**value) + [value+addvalue]

def reverseByte(byte):
    return int(format(byte, "08b")[::-1], 2)

def I2CInterupt(pin):
    pinIndex = intPins.index(pin)
    data = list(i2c.readfrom_mem(0x20 + pinIndex, 0x0E, 4))

    data[0] = reverseByte(data[0]) #need to reverse the A gpio pins because they are wired in reverse to B
    data[2] = reverseByte(data[2])

    globalUpdates["pins"] = getSetBits(data[0], pinIndex*16) + getSetBits(data[1], pinIndex*16+8)

    for i in range(8):
        pinStates[pinIndex*2][i] = (data[2] & (2**(i+1))) != 0
        pinStates[pinIndex*2+1][i] = (data[3] & (2**(i+1))) != 0

def moveInterupt(pin):
    pinIndex = movePins.index(pin)

    if pinIndex == 0 or pinIndex == 2:
        globalUpdates["noteBottem"] -= (pinIndex-1)*8

def noteInterupt(pin):
    globalUpdates["noteLayout"] = noteLayouts[(noteLayouts.index(globalUpdates["noteLayout"])+1)%len(noteLayouts)]

# core 1 function
def core1():
    for pin in intPins:
        pin.irq(I2CInterupt, pin.IRQ_RISING)
    for pin in movePins:
        pin.irq(moveInterupt, pin.IRQ_RISING)
    
    notePin.irq(noteInterupt, notePin.IRQ_FALLING)

core1Thread = _thread.start_new_thread(core1)

def indexToNote(i):
    if globalUpdates["noteLayout"] == "linear":
        return notes[(i//8)%7] + str(8 - i%8 + globalUpdates["noteBottem"])

    elif globalUpdates["noteLayout"] == "scale":
        return notes[(i//8 + 4*((i)%8))%7] + str(math.floor(1+ (8-i%8)/2.4 + (i//8)/7)) # this should be correct without any transformations

def noteToFreq(note):
    return (440 / 32) * (2 ** ((note - 69) / 12))

def freqToSample(freq):
    length = 8000 // freq
    sine_wave = array.array("h", [0] * length)
    for i in range(length):
        sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * (2 ** 15))
    return sine_wave

while True:
    if globalUpdates["pins"].count != 0:
        for index in globalUpdates["pins"]:
            pin = pinStates[index//8][index%8]
            note = indexToNote(index)

            if pin == 0:
                midi.send(NoteOff(note, 0))

                voiceIndex = voices.index(note) if note in voices else -1
                if voiceIndex != -1:
                    mixer.stop_voice(voiceIndex)
                    voices[voiceIndex] = -1

            elif pin == 1:
                midi.send(NoteOn(note, 100))

                voiceIndex = voices.index(-1) if -1 in voices else -1
                if voiceIndex != -1:
                    sample = audiocore.RawSample(freqToSample(noteToFreq(note)))
                    mixer.play(sample, voice=voiceIndex, loop=True)
                    voices[voiceIndex] = note

        globalUpdates["pins"].pop(index)