# mini-launchpad

Mini launchpad is a midi devicde and control surface for Ableton. When connected to a computer it can: send midi notes, start and stop clips, be used as audio output, change the volume and change paramaters. When not connected to a computer it can: play notes and create sound with a synth.

## connected to Ableton

Mini launchpad is specificy designed to be used with Ableton Live. When you connect it to a computer, it uses an internal usb hub so you can use it as an audio output and send commands through Ableton. When connected it can be used as a midi keyboard or start and stop cilps in the session view.

## standalone

When mini launchpad is in standalone mode, you can only use the midi keyboard. This will send midi into a synthesizer, which will then play sound. The syth can be customized a bit via the encoders at the top, but you can customize it fully if you reprogram the pi.

## compontents

Mini Launchpad has an 8x8 grid of buttons, wired to 4 io expanders. There are also 8 encoders connected to another io expander. The io expanders are used so that the microcontroller doesn't have to poll for changes, but that it can use interupts instead. This way every button press will be registerd and you can press every button at the same time. There are also some extra controll buttons and lights that are wired directly to the microcontroller. But these will also use interupt.

For audio there is a PCM5100 I²S DAC. This will convert the digital audio to a line output. Then there is an amplifier that amplifies the sound. You can also just use the line out.

## playing notes

Actually playing notes is a big part of the luanchpad. There are 2 ways to do this.
- Option 1 is that the notes are layed out linearly. This means that in the bottom left corner is a C, moving right goes up a note and moving up goes up an octave. You can change the octave of the rows by moving up and down. This is also the default option when the launchpad boots up. It looks like this:

<img width="166" height="139" alt="layout 1" src="https://github.com/user-attachments/assets/b18e3a55-cdba-464b-ab1f-3098894ba2c5" />

- Option 2 is for the notes to be layed out in a c scale. The bottom left note is still a C and going right still goes up a note. But going up goes up a fourth instead of an octave. This layout is the default layout on the Ableton Push and lloks like this:

<img width="179" height="139" alt="layout 2" src="https://github.com/user-attachments/assets/f2c607f0-dc67-40d4-abfa-1c4f2ea058d4" />

## progress

The current progress.

- [x] Design the schematic.
- [x] Design the pcb.
- [x] Design the case.
- [x] Write the firmware.

I know not a lot of the features I talk about aren't implemented yet. But for SoM those won't be included. This is beacuse mini midi magic started pretty late and it doesn't really have an end date yet. So by the end of mini midi magic this will all be implemented. The current features that aren't implemented are:
- Connecting to Ableton Live.
- Playing and controlling things in Ableton Live.
- Having a more complex and better synthesizer.
- Being able to change the synthesizer.
- Using the launchpad as an audio interface.
- And I might even add more features.

  I am also unsure if any of the code works and if the case is fully correct. Because I don't have the physical board myself. This will also change before the end of mini midi magic.
