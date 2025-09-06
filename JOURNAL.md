# September 3th: Started working on the schematic.

Firstly I looked at the tutorial and made the button grid. I chose to use 4 16 pin IO expanders for this. Because I can see every button's state, and I can use interupt instead of polling. I chose to make the grid 8x8, because at that size you can do a lot with it, and it isn't too big. then I tried looking to how I wanted to make the control surface. I want to make it have an audio interface, so that you can output your pc sound via the DAC. But I can't find a usb to I²S chip in kiCad. My plan currently is to have a internal usb hub. That will have the pi and the usb interface connected to it. When you plug it in to a computer, the pi will send midi to Ableton, and to audio will go via the usb interface. But when you are not connected to a computer. It will play the midi notes via the line out itself. So you don't need a computer to use it. But I don't know if I will find a usb to I²S chip.

**Total time spent: 7h**

#September 7th: Continued working on the schematic.

I finally made a github repo. I didn't do it before because I wsan't sure of the name. But now that i have the repo I can use photo's. So this is what I ended up with today:
<img width="4960" height="3507" alt="image" src="https://github.com/user-attachments/assets/ced3b69d-bc24-4d4a-8467-5fec561f5ac5" />

I changed from a pico to the rp2040 itself. The only reason I did this was so that I could route the usb on the pcb and didn't have to use a cable. The only thing with not using the pico is that, I have to route the sensitve wires on the pcb. To connect the 2040 I followed the [hardware design with RP2040](https://datasheets.raspberrypi.com/rp2040/hardware-design-with-rp2040.pdf) datasheet from raspberry pi themself. But ot does say that a lot of component have to be close to the chip, like the decoupling caps. So it will be fun when I design the pcb. following the datasheet went pretty well. Until the crystal oscillator. I couldn't find the execpt part in KiCad and from reading the datasheet, it looks like I can't just choos some other random one I can find. So I used thzt part from [Calliahs designguide](https://github.com/calliah333/RP2040-designguide/tree/main). I also found a usb to I²S chip in KiCad:
<img width="879" height="656" alt="image" src="https://github.com/user-attachments/assets/86b3a1ea-4f61-4678-91db-11b3c9f7a5dd" />

So I connected it and added a quadrupel mux, to switch between the 2040 and usb. There are still some pins on the rp2040 which I probably should connect to something. But I'll do that next time.

**Total time spent: 3h**
