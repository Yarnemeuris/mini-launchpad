# September 3th: Started working on the schematic.

Firstly I looked at the tutorial and made the button grid. I chose to use 4 16 pin IO expanders for this. Because I can see every button's state, and I can use interupt instead of polling. I chose to make the grid 8x8, because at that size you can do a lot with it, and it isn't too big. then I tried looking to how I wanted to make the control surface. I want to make it have an audio interface, so that you can output your pc sound via the DAC. But I can't find a usb to I²S chip in kiCad. My plan currently is to have a internal usb hub. That will have the pi and the usb interface connected to it. When you plug it in to a computer, the pi will send midi to Ableton, and to audio will go via the usb interface. But when you are not connected to a computer. It will play the midi notes via the line out itself. So you don't need a computer to use it. But I don't know if I will find a usb to I²S chip.

**Total time spent: 7h**

# September 6th: Continued working on the schematic.

I finally made a github repo. I didn't do it before because I wsan't sure of the name. But now that i have the repo I can use photo's. So this is what I ended up with today:

<img width="4960" height="3507" alt="schematic" src="https://github.com/user-attachments/assets/ced3b69d-bc24-4d4a-8467-5fec561f5ac5" />

I changed from a pico to the rp2040 itself. The only reason I did this was so that I could route the usb on the pcb and didn't have to use a cable. The only thing with not using the pico is that, I have to route the sensitve wires on the pcb. To connect the 2040 I followed the [hardware design with RP2040](https://datasheets.raspberrypi.com/rp2040/hardware-design-with-rp2040.pdf) datasheet from raspberry pi themself. But ot does say that a lot of component have to be close to the chip, like the decoupling caps. So it will be fun when I design the pcb. following the datasheet went pretty well. Until the crystal oscillator. I couldn't find the execpt part in KiCad and from reading the datasheet, it looks like I can't just choos some other random one I can find. So I used thzt part from [Calliahs designguide](https://github.com/calliah333/RP2040-designguide/tree/main). I also found a usb to I²S chip in KiCad:

<img width="879" height="656" alt="I²S switching" src="https://github.com/user-attachments/assets/86b3a1ea-4f61-4678-91db-11b3c9f7a5dd" />

So I connected it and added a quadrupel mux, to switch between the 2040 and usb. There are still some pins on the rp2040 which I probably should connect to something. But I'll do that next time.

**Total time spent: 3h**

# September 7th: Added encoders.

I added 8 encoders to another io expander.

<img width="826" height="572" alt="encoders" src="https://github.com/user-attachments/assets/f9119de1-496c-42c4-9e95-1593c8dbf1e2" />

The reason I use io expanders is just for the easy interupts. That way I have easier code anddon't have to poll the encoders at a fast rate to get every change. I'm also going to dupple dip with SoM so I downloaded the KiCad-wakatime plugin. Hopefully it will work well for me. That was it for today, I didn't do much.

**Total time spent: 0.5h**

# September 8th: Started adding the control buttons.

So I started adding some buttons for control. Like playing, pausing, changing mode, etc.

<img width="662" height="628" alt="control buttons" src="https://github.com/user-attachments/assets/18cf9ccd-b3ef-49f9-849e-cac2eca1cef6" />

But it has me questioning everything. What do I want it to do. Do I add those features, but then I should also add that.

I didn't make much progress today. But now I have more thing I can think about and decide during boring school lessons.

**Total time spent: 0.5h**

# September 11th: Added an amplifier.

So I finished the control buttons. I think I know what features I want.

<img width="413" height="421" alt="control buttons" src="https://github.com/user-attachments/assets/a72a33a3-ab01-42e5-98a0-14ab3d6aa7fd" />

There will be 4 buttons for moving, 1 for play/pause. 2 for switching between midi keyboard and clip start/stop with a led under each to show which is selected, this will also controll the what the encoders do. These 2 buttons are only for if you are connected to Ableton. The last button is for switching between midi device without a computer and being a controller for ableton, which will also have a led. I noticed while explaining all the buttons that I had one to many. Maybe I counted wrong or I kind of forgot what it was for.

I also added an amplifier:

<img width="277" height="411" alt="amp" src="https://github.com/user-attachments/assets/1e329193-d3be-45f5-ab40-5b1a62241e04" />

So that the line level output can be used to drive speakers or headphones. This was kind of complicated so I did a lot of research te previous days. That way there isn't a journal log, I just spent some time looking thinges up. first I thought I needed to create my own amp using a tranistor. But I found out that I can just use a chip for that. But because this seems likly to not work at all or perfectly, I will also add a pin header for the line output. The only things I think I still need is That and the connector for the DAC. Than the schematic should be done. I'm gonna ask if it is possible to review it, beacuse it's pretty complicated and I'm not sure I wired everything correctly.

**Total time spent: 3h**

# September 13th: Started on the pcb.

I finally finished the schematic. So I started working on laying everything out on the pcb. I'm gonna make it a 4 layer pcb. I started with adding the buttons:

<img width="509" height="576" alt="buttons" src="https://github.com/user-attachments/assets/7e5ebd27-4752-4e02-87bc-f6b5ea7f9100" />

I wanted to space them out 20 mm. But I messed somthing up and now they're 22.857. I will probiably change this tomorrow. Aside from the buttons and encoders I didn't do much on the pcb. I started with the usb and power ut that still needs a lot of components. I should also make some of the capasitors larger. Because this does not look good for the power circuit:

<img width="992" height="627" alt="small cap" src="https://github.com/user-attachments/assets/9ed5497f-c0cc-406e-add4-fbf64bb7fce9" />

The last thing that I did today was update the README. So now there's finally something there.

**Total time spent: 2h**

# September 14th: The pcb is almost finished.

<img width="1087" height="781" alt="pcb" src="https://github.com/user-attachments/assets/c2196c0f-5f25-4d2d-8406-c00b18cfd9b8" />

First I changed the buttons to be 20mm apart. It wasn't as bad as I though it would be. Then I connected the amp, the connector, usb hub. It just went pretty fast. So that now of the 952 pads, 242 nets there are only 20 unrouted connections. The only problem is the rp2040 chip.

<img width="898" height="604" alt="rp2040 connections" src="https://github.com/user-attachments/assets/62160f9f-2393-4daa-9618-28791c362550" />

It has so many connections and they are so close to together and everything has to be close to it. But there are only some gpio connections left, so it should not be too hard.

**Total time spent: 2h**

# September 15th: Finished the pcb.

This is the entire pcb:

<img width="1148" height="855" alt="full pcb" src="https://github.com/user-attachments/assets/33d461a5-5d00-4190-8ef4-16e03884f7f8" />

I connected the last pins, which were the hardest to connect. They were almost all on the rp2040 chip. I also switched the usb C connector, because I didn't like it's footprint. Probiably don't have to do much more on the pcb, just change a few components if jlc doesn't have these.

**Total time spent: 1h**

# September 16th: Added lcsc part numbers.

 I started adding lcsc part numbers to every component. Just to make sure jlcpcb uses the same part. But because this is all inside the fields, I can't really show a picture.

 **Total time spent: 0.5h**

#September 17th: Finished the pcb.

I finally finished the pcb.

<img width="1724" height="930" alt="pcb" src="https://github.com/user-attachments/assets/982d3d03-8f9a-4941-bdd6-4ddf489528b8" />

I added all the LCSC Part numbers. I check if everything worked on jlcpcb, there are some issues but you can set every part in jlcpcb. I did see that the price for the board is like $200 so I might change some things. The things you have to change when ordering are: some components aren't found in jlcpcb library or some other problems with the bom and because jlcpcb does the rotation diffrently you have to rotate most components in the viewer.
Today I also started on the cad but it isn't much yet.

**Total time spent: 2h**

#September 18th: Started designing the cad.

<img width="1359" height="779" alt="image" src="https://github.com/user-attachments/assets/cb70c6ca-e9bd-4e3b-af06-c3067e708cf7" />

This is what I designed so far. It's mostly just the buttons, encoders and a the audio port. It also includes some mounting internally with M3 bolts and inserts. I will probably change the pcb to make it smaller, because right now the case doesn't fit on my printers bed.

**Total time spent: 1h**

#September 20th: Changed the pcb again.

So with the case around the pcb it doesn't fit on my printers build plate. So of course the best thing to do is redisgn the hole pcb to be smaller. So every surface mount component is now placed on the back, still just one side to assamble but the opposite side. This way the pcb can be smaller but you just have to solder every thing on the other side manually. The final resualt:

<img width="1014" height="853" alt="smaller pcb" src="https://github.com/user-attachments/assets/7d8b44db-c21f-4c50-b098-9f3fb2d2043a" />

It is just 180mmx206mm. So with 6mm either side for the case, it still fits on my printer. The final connections I will do tomorrow.

**Total time spent: 1.5h**

#September 21th: Finished the pcb.

Today I think I finally finished the pcb. Theonly thing I think I might change is removing a button. It now looks like this:

<img width="967" height="854" alt="pcb v1.2" src="https://github.com/user-attachments/assets/65d30de7-8e6b-43b2-8d64-b270de32d37e" />

I also worked a bit on the case. It now looks like this:

<img width="924" height="827" alt="case" src="https://github.com/user-attachments/assets/07511cd6-10c4-40d5-878d-c369d71bd0c7" />

It is almost finished too. Just the volume, some ports and maybe some more dacals. Thise I will also print myself. I will just say to thhe slicer that it has multipul toolheads and the change gcoe is just a color change. So this is actually almost finished. I just hope that I will finish before the end of SoM. Because I don't know what will happend if it's not shipped by the end. JLCPCB says it will be $174 for the board. But I will still have to order some more copmonents that I have to solder on myself. It is all the top components so buttons, encoders, things like that. Tommorow I will probably finish the case and can start on the firmware.

**Total time spent: 3h**

#September 22th: Finished the pcb again.

Today I just removed the top and moved the potentiometer to the center. The pcb should actually be finished now.

<img width="632" height="588" alt="hopfully final pcb change" src="https://github.com/user-attachments/assets/1bab8135-b94f-4969-be56-89cb1fc7505c" />

**Total time spent: 0.5h**

#September 23th: I think I finished the cad.

A lot of the cad work was already done before this. The only things I did was add the power switch, usb-c port and knob at the top. The usb-c port and knob are geussed and I will probably move and change these when I have the actually pcb.

<img width="1423" height="818" alt="case" src="https://github.com/user-attachments/assets/6478afc5-b0af-4a4a-a2ee-6dd0da527859" />

**Total time spent: 0.5h**
