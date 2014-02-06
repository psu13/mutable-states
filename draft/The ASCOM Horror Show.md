Title: The ASCOM Horror Show
Date: 2014-2-05
Category: Things
Author: psu

In older and simpler times, telescopes were older and simpler. You put the tube on a mount. You stared at an atlas to figure out where the object was. You pointed the tube roughly at a bright star and then used the finder to move around until you could see the object in the telescope. Then you got on with your life. If you were really advanced you might use an equatorial mount with "setting circles" to get close to the object before tracking it down for good. A lot of people hopped from star to star though, since this was simpler. But the setting circle people sneered at them.

When the late 80s came around, people decided that they wanted to control the telescope more automatically. So they put a servo motor system into the mount controlled by a small computer. This computer knew where things were in the sky, and you could tell it to roughly point at things for you. No more moving the tube around by hand. This was basically automatic setting circles! So of course the star hopping people sneered.

Soon someone realized that you could hook a PC up to the mount controller and point the mount directly from star atlas software running in the computer. What you would do is run an RS232 cable to the controller box and send simple ASCII commands over the wire to tell the mount to do things. This was fairly straightforward, and soon everyone wanted to get in on the act. Unfortunately, every company that made mounts used a different set of ASCII commmands, so you had to have a special module in your star atlas program for each different kind of mount. There were maybe a half dozen. An outfit called Software Bisque made a program called TheSky that did all this, and people were happy.

Then digital cameras got into the mix. And you needed a different set of serial commands for each one of those. So Bisque wrote the code, and you could use TheSky to run the mount, and CCDSoft to run the camera. 

Then people got into all kinds of hardware. Guide scopes, domes, motorized focusing devices. Each one with their own scheme for serial control.

Sometime around the mid to late 90s an enterprising developer decided that there should be a shared library that could encapsulate all of these serial protocols behind one set of common abstractions. Then you could write programs against this "driver" framework instead of directly to the devices. His computer ran Windows ... in fact at the time *everyone's* computer ran Windows. So he based this driver framework on COM (and later .NET), the Windows infrastructure for creating such things. He then went and wrote his observatory control software based on these layers, and lobbied for various other enterprising developers to create drivers for all their favorite hardware.

Over time ASCOM became a wide success in the narrow marketplace of 35-65 year old white men who need to control telescopes with computers. Most of the major hardware platforms have drivers. And while they tend to be developed by single hobbyists in their proverbial basements, and while the user interfaces for these things are apparently stuck in a "late windows XP to early Windows Vista" sort of design mode, in general things sort of work. Most of the time.

Unless they don't. ASCOM in practice has a few warts. When things are working you don't really notice them. But they lurk down there beneath the surface and are the things of software architecture nightmares.

First, those guys at Software Bisque. They still make all their software, with their own serial modules. They even make some of their own hardware (very expensive mounts). What they dislike making is ASCOM drivers. They see it as a destruction of the proprietary value that they have toiled all these longs years to add to TheSky and such. And they are not completely wrong. Why should they tolerate a bunch of lowlifes giving away complicated drivers for free which they spent a long time building and integrating into their software stack?

Second, there is COM. Over time COM has evolved into .NET which evolved into what Microsoft sells you to configure and deploy custom large scale Enterprise Applications. The whole system is built around the assumption that you have a huge staff of minions whose only job is to make sure your Windows boxes are running exactly the right versions of everything in order for your large scale custom Enterprise Application to run correctly.

You know who doesn't have such a staff of minions? 35-65 year old white men trying to run a telescope. ASCOM takes the relatively simple task of hooking a cable to a computer and running a program to talk to it and replaces it with the ANSI standard Microsoft .NET version hell dance. I would estimate that over time at least 25% to 30% of all traffic to the various mailing lists that support computerized astronomical hardware is asking about how to set up .NET and troubleshooting versioning issues.

Third, there is the software itself. While a device-independent transport and communication layer for communicating with astro-devices sounds like a great idea, this isn't quite what ASCOM is. Yes it has an API that you implement that seems like a generic communication layer. But if you actually study it, what you find is that the API is the thinnest possible layer of abstraction over the devices that it might talk to. Examples abound:

1. The idea that you will talk ASCII over a serial port is deeply deeply embedded in the architecture. Want to talk to your device using, say, an Ethernet cable and your local network? You are sort of out of luck. You have to buy external software to emulate a serial port on a network port. ASCOM does not abstract away the transport so all the old drivers written for serial devices ONLY work on serial devices.

2. To build a camera driver in ASCOM, you need to implement various APIs that take two CCD devices as arguments. Why two? Because SBIG cameras have two CCDs (main and guider) and SBIG devices were one of the first major consumers of this API. So the idea that your camera might have two CCDs is *hard coded* into the API.