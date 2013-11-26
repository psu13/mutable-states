Title: Tinkering with the Stars
Date: 2011-03-16
Category: Astro
Author: psu

Anybody who knows me knows that I am not a tinkerer. This may sound strange coming from a professional software engineer, but I've just never been very good at it. I never took things apart as a kid. I never built my own hardware back when you could still build your own hardware. I was never any good at assembly language. In fact, specifically <em>because</em> I write consumer software for a living, I have fairly high expectations about the required level of polish in the final user experience of such products. If I can't install your tool and make it work in three clicks, you are dead to me.

So lately I have surprised myself by taking on some telescope related projects that can only be described as tinkering. Telescopes are dangerously close to being the sort of finicky mechanical device that would have defeated me in the past. But, over the last 25 years or so they have slowly become more electronic and so, to me, more friendly. Still, you can't really say that the overall experience is polished. This is an industry still attached to the RS-232 cable. A lot of the most useful software packages are created by teams of one working in basements with Visual Basic or the Mac equivalent. If you are going to play in this world, you have to be careful. 

Late this summer, I hit upon the end goal of setting up a system that I could use mostly from my house and mostly for the  observation of deep sky objects. In particular, I wanted to take advantage of <a href="http://tleaves.com/2010/08/16/the-big-lie-solved/">a new class of astronomical video cameras</a> that make it possible to "see" more like a CCD camera does without a lot of the hassle of actual CCD imaging. One way do to this would be to hop on to the Internet and immediately pick up:

1. A <a href="http://mallincam.tripod.com/id52.html">Mallincam</a>.

2. A large aperture telescope with a fancy computerized tracking mount.

3. A large windows PC to control the telescope and camera.

4. Five or six software packages of various kinds to handle telescope pointing, camera control, focus control, image processing, wireless connectivity with the telescope and video broadcasting of the video images.

5. An observatory building.

6. A small windows PC to remote control the large Windows PC in the observatory.

This would have been a phenomenal outlay of cash. More importantly, after two months of being buried under the weight of all the equipment I would have either thrown it in the basement or sold it off on the Internet for a loss and gone back to taking bad digital pictures or riding my bike slowly. If you spend any time at all looking at telescope related classified ads, you notice that by far the majority are of the form "I bought all this stuff and I never used it" or "I bought more stuff than I'll ever use, and I'm selling it all to get something even bigger which I will sell in a month." In fact, I bought the scope used from a guy who was "upgrading", and I caught the same guy selling his new scope a few months later. So, I knew this was a bad plan.

The fundamental rules when dealing with unfamiliar technology are:

1. Know what your end goal is.

2. To minimize risk, add only one technical requirement to the system at a time.

The obvious first step in this was to figure out the telescope. Besides the camera it is the most expensive and most complicated piece of equipment in the whole stack. I went out into the Internet with the following telescope requirements:

1. Not too big.

2. Not too small.

3. Not too expensive.

4. Easy to set up.

5. Good automatic pointing.

These requirements are a good baseline for my definition of a minimally useable telescope. It also turns out that they are critical for effective use of the video camera, but I'll get to that later. Finally, in a turn of good fortune, it also turns out that the modern consumer telescope has been engineered with these specific requirements in mind. It doesn't matter what kind of tube you buy, you can probably stick it in a system that is streamlined to set up and can do computerized pointing. Even the <a href="http://www.obsessiontelescopes.com/accessories/ServoCAT/index.php">Dobsonians</a> do this now.

After some deliberation, I picked an orange tube 8 inch Celestron. This was, no doubt, a choice driven partly by misty-eyed nostalgia. Back when I was growing up Celestrons were <em>the</em> commercial telescope. They seemed completely out of reach to me. An expensive toy for rich folks (although the <em>really</em> rich folks bought <a href="http://www.company7.com/questar/telescopes/quest35.html">Questars</a>). Anyway <a href="http://atelescopeinthecity.blogspot.com/2011/04/telescope-in-city.html">the telescope ended up working very well</a>. I can set it up in ten miinutes. It points relatively accurately. It's easy to use, if a bit primitive.

Telescope in hand, the next step was software. Generally my rule is: when in doubt, avoid software.  Since I write the stuff for a living, I feel qualified to say that unless you already know it will do exactly what you want and exactly how you want to do it, software will usually just get in your way. So if you have a choice between direct control and software control, direct control is better. This has mostly proven to be true with telescope software. There are two main issues with telescope software:

1. It mostly runs on Windows. I hedge by using VMWare. But still, this is less than optimal.

2. A lot of it is written by amateurs. The market is full of byzantine installation and packaging schemes (like the skychart program that makes you install all the extra star catalogs by hand unzipping them in the right part of the file system, really?) and user interfaces that are straight out of the Visual Basic form builder (I'm looking at you <a href="http://eq-mod.sourceforge.net/eqaindex.html">EQMOD</a>).

But, I don't mean to disparage their achievements. The good stuff is executed at a high standard, and even the clunky stuff can have a lot of utility (like EQMOD). After a few false starts, I settled on <a href="http://www.skyhound.com/skytools.html"><em>SkyTools</em></a> for charting and observation logging under Windows, <a href="http://itunes.apple.com/us/app/equinox/id406854281?mt=12"><em>Equinox</em></a> as a basic planetarium program on the Mac side, <a href="http://www.stellarium.org/"><em>Stellarium</em></a> as  a secondary plantarium program (it's open source, and so more flakey than the others), and finally, <a href="http://itunes.apple.com/us/app/skysafari/id319159213?mt=8"><em>SkySafari</em></a> on the iPhone and iPad, although this gets less use than the others.

Surprisingly, after experimenting with the wireless mount control in <em>SkySafari</em>, I found that I didn't like it. I'd rather hit the big buttons on the hand controller. I've also had mixed luck controlling the mount directly from my laptop. So while I will bring the computer outside with me to reference charts and whatnot, I don't actually point the telescope with it. The mount is not quite accurate enough for that, and making small adjustments is much easier with the controller than with the laptop, especially when I'm staring down into the eyepiece anyway.

One of these days I'll get around to setting up <a href="http://uncle-rods.blogspot.com/2011/03/nexremote-nirvana.html">Nexremote</a> for this. And maybe I'll try to use those <a href="http://www.scopestuff.com/ss_jem1.htm">bluetooth serial adapters too</a>. But for now the "one requirement at a time" rule kicks in, and so it's time to stop.

After a couple of months with the telescope I had settled into the following routine. If the weather looked good (which is fairly rare in Pittsburgh) I would make a list of objects to look at in <em>Skytools</em>. Then I would set up the telescope, align it, and bring the laptop out with the screen dimmed and work through the list one by one. If I felt like playing around, I'd also hook the scope up to the laptop and point with <em>Skytools</em> or <em>NexRemote</em> but I have really only experimented with that a couple of times, and both times the telescope ended up acting funny by the end of the night. Having worked through about 50 Messier objects and a couple of dozen others out of the NGC catalog, I felt comfortable moving to the next step. So I ordered the video camera.

But that's the subject for the next article. 

While you wait for it, you can indulge yourself at <a href="http://www.cloudynights.com/">Cloudy Nights</a>, <a href="http://www.astromart.com">Astromart</a>, and of course, <a href="http://uncle-rods.blogspot.com/">Uncle Rod's blog</a>. Read Rod's book about SCT telescopes too. It will make you want one.