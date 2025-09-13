# mini-launchpad

Mini launchpad is a midi devicde and control surface for Ableton. When connected to a computer it can: send midi notes, start and stop clips, be used as audio output, change the volume and change paramaters. When not connected to a computer it can: play notes and create sound with a synth.

## connected to Ableton

Mini launchpad is specificy designed to be used with Ableton Live. When you connect it to a computer, it uses an internal usb hub so you can use it as an audio output and send commands through Ableton. When connected it can be used as a midi keyboard or start and stop cilps in the session view.

## standalone

When mini launchpad is in standalone mode, you can only use the midi keyboard. This will send midi into a synthesizer, which will then play sound. The syth can be customized a bit via the encoders at the top, but you can customize it fully if you reprogram the pi.

## compontents

Mini Launchpad has an 8x8 grid of buttons, wired to 4 io expanders. There are also 8 encoders connected to another io expander. The io expanders are used so that the microcontroller doesn't have to poll for changes, but that it can use interupts instead. This way every button press will be registerd and you can press every button at the same time. There are also some extra controll buttons and lights that are wired directly to the microcontroller. But these will also use interupt.

For audio there is a PCM5100 I²S DAC. This will convert the digital audio to a line output. Then there is an amplifier that amplifies the sound. You can also just use the line out.

## progress

The current progress.

- [x] Design the schematic.
- [ ] Design the pcb.
- [ ] Design the case.
- [ ] Write the firmware.
