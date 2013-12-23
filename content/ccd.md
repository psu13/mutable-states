Title: C, C, and D
Date: 2012-08-12
Category: Astro
Author: psu

It all started with the hot pixels. The Mallincam video camera that I had bought provided wondrous views of the skies above, but these views were always accompanied by a collection of colorful extras: pixels activated by the heat of the camera would glow red, green or blue next to the object that I was looking at. I would try to ignore them, but they sat there staring me in the face.

M82 was still a sight to behold:

> <a href="http://www.flickr.com/photos/79904144@N00/7009939039/" title="M82-2012-03-22-single by psu13, on Flickr"><img src="http://farm8.staticflickr.com/7061/7009939039_7a2f8bc2be.jpg" width="500" height="375" alt="M82-2012-03-22-single"></a>

But I constantly thought "there must be something I can do about this noise."

First, where does the noise come from? To know this you have to know a bit about how CCD cameras work. A CCD is an integrated circuit that is made up of an array of "wells." Each of these wells makes a single photo-sensitive site. The hardware takes advantage of an effect from quantum physics called the <a href="http://en.wikipedia.org/wiki/Photoelectric_effect">photoelectric effect</a>.  In the late 1800s Heinrich Hertz observed that if you shine a light on some materials, they will give off electricity. CCDs use this effect to turn photon hits into electric charge. Conceptually, as light hits the chip electrons collect at the bottom of the wells. When the exposure is done, the charge at each site is read off one by one and turned into a small binary value. This collection of binary values can then be made into an image.

In the Mallincam the digital image is turned into an analog video signal by hardware in the camera itself. This signal goes over a composite or S-video cable to your computer where you turn it back into digital video with a capture card. All of this saves you the bother of processing the digital image yourself. But, it also prevents you from processing the digital image itself.

The reason you might want to process the digital image yourself is to manage noise. In a perfect world, the only thing making electrons at the bottom of those wells would be actual photons from the heavens. In addition, a perfect world would have circuits that can read the charge perfectly and without any error. Of course, this perfect world does not exist. All sorts of factors conspire to put false data into our digital images and this false data is what we call "noise."

If you spend any time at all looking at Mallincam pictures you can see a lot of different kinds of noise. There are the hot pixels which are caused by heat and dark current (see below). There is the greenish amp glow in the corner from the video amplifier. There is noise caused by the conversion to and from analog video. Finally, if you aren't careful, there is electrical noise caused by your power supply transmitting RF into the video cables.

The noise that I'm interested in tonight is called "dark current." Dark current is extra electrical noise created by the sensor hardware itself. This causes electrons to collect in wells even though no photons were captured. If the dark current is strong enough the pixel will register as having data when in fact it captured none. So you get false, or "hot" pixels.

The amount of dark current that you see depends on the temperature of the sensor. So, the first thing fancy CCD cameras do to combat dark current is to use sophisticated cooling hardware to make the chip as cold as possible. 

The second thing you can do to manage dark current noise is to take <em>dark frames</em>. Here you cover the CCD and shoot a picture with exactly the same exposure time and at the same temperature as you used for the picture you took. Then, you take the resulting data and subtract it from the data for the actual exposure (also called the "light" frame). If you are lucky, this will exactly cancel out any false data in the light frame.

This is what I wanted to do with my Mallincam pictures. But I couldn't. With the Mallincam you can't actually capture the light frame and dark frame <em>data</em>. All you can do is grab an image file that has bits in it that are the result of image processing in the camera, then a digital to analog conversion and then an analog to digital conversion. All of this processing destroys the integrity of the signal and makes it impossible to do dark subtraction. At least in my experience.

So I went out and got a small CCD camera to play with. I picked a Starlight Xpress SXV-M7 monochrome camera. Why?

1. It's about the same size and weight as the Mallincam, so I'm used to handling it.

2. It uses a similar sensor to the Mallincam, except that it's black and white only. These Sony sensors are pretty sensitive and low noise.

3. I got black and white so I would not have to worry about color. Color in the Mallincam was always the best and worst thing about it. Plus, it was galaxy season anyway.

I found the SX camera pretty much as easy to use as the Mallincam. The nicest thing was that I only needed a single USB cable to run the whole thing. The most complicated thingwas that I had to learn how to process the digital data myself. We'll get into that next time. But after a bit of practice, I did finally manage to get rid of those hot pixels:

> <a href="http://www.flickr.com/photos/79904144@N00/7371546650/" title="M51_2012_06_13_11x180_ABE-PS by psu13, on Flickr"><img src="http://farm9.staticflickr.com/8008/7371546650_38ae8a2771.jpg" width="500" height="363" alt="M51_2012_06_13_11x180_ABE-PS"></a>

It turns out that a few months with this camera taught that there is a lot more to noise in CCD imaging than I had considered at first. Next time we'll see that to a first approximation processing astronomical pictures is just one huge exercise in hiding the noise so that you can exaggerate the signal.
