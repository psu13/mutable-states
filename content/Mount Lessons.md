Title: Mount Lessons
Date: 2012-05-02
Category: Astro
Author: psu

I've had my Astro-Physics Mach1GTO equatorial mount for about two months now. The mount has continued to perform better than I could have expected, and I expected a lot. So while it may seem like I have already <a href="http://mutable-states.com/value-for-money.html">gushed uncontrollably about it</a> I have just a few more things to say before I just go back to happily using the thing.

<h4>
Setup and Alignment</h4>

I have my setup routine pretty much down. Even though it takes more trips, it's actually faster than setting up the CG-5 for use with the camera. For visual use it would only be a bit slower. Here is what I do:

1. Put the portable pier down on my patio. I have a fixed spot for it.

2. Roll the mount out in its rolling box. Put it in the pier. Attach the three knobs that hold the mount on the pier.

3. Attach the counterweight shaft and the two weights.

4. Go in the house and get the telescope. Put it in the saddle.

5. Balance the telescope. I found this tricky at first because the axis bearings on the Mach1 are pretty stiff. You can't really balance the telescope by finding the point at which the telescope does not move when you undo the clutches. The axis tension tends to hold it in place. Instead you need to find the point where the motion along the axis is most smooth and uniform. It takes a bit of practice.

6. Set the mount in the "Park 1" position, where the RA axis is horizontal and the DEC axis has the telescope pointing north. The telescope tube and the counterweight shaft should be level.

7. Use the polar scope to align the mount on Polaris.

8. Plug everything in, Resume from Park 1 on the hand controller. 

9. Now I run one pass of the "quick drift" polar alignment scheme which is outlined in <a href="http://www.astro-physics.com/tech_support/mounts/keypad_v417.pdf">this pdf file</a>. While the description in the documentation is somewhat involved, the scheme is actually very simple and mostly involves pointing the telescope at two stars that you can pick. I'll provide details in a later section.

10. Now hook up the camera and laptop. Find a star near where you want to look at things. Point the mount there. Center it in the camera view. Focus. Hit "recalibrate" on the hand pad. Done. 

Here is what I like about this setup routine:

1. I only need two stars (the two used for polar alignment). It's easy to find two stars to use. It could sometimes be a pain to find six for the Celestron.

2. No complicated and fragile pointing model. The multi-point pointing models that the Celestron and Meade mounts use are all derived from the software used to make the alt-az fork mounts point and track objects for visual observation. To "align" these mounts you point them at various stars and the computer builds a little model to translate celestial coordinate to alt-az and the poor user does not have to mess about with "complications" like polar alignment. This is great but also annoying in some ways. If for whatever reason you accidentally shifted the telescope after building the model, your only real hope is to rebuild the model from scratch. With the Celestron GEM mounts this manifests itself as needing to redo pointing alignment after you have used the pointing model to find tune polar alignment. Which is unfortunate.

	Here is my epiphany about alignment: if your equatorial mount is well built and precise, the only alignment you need to do is polar alignment. The Astro-Physics literature actually says this, but I did not believe it. I was wrong.

	The various multi-star alignment routines that have been built to make life "easier" for users has actually worked to hide this fundamental fact from them and thus made the world ultimately more confusing. The latest high end mount from Meade (the LX-800) takes this even further. Check out <a href="http://www.cloudynights.com/ubbthreads/showflat.php/Cat/0/Number/5195001/page/0/view/collapsed/sb/5/o/all/fpart/all/vc/1">this thread about it</a> to see what I mean. In addition to multi-star "alignment" you now also have to deal with guider setup and plate solving before you can look at things in your telescope. Is this really easier to use?

<h4>
Stability and Consistency</h4>

In the last six weeks I've continued to make progress on my projects to make rudimentary video images of all the <a href="http://mutable-states.com/deep-sky-projects.html">Messier and Herschel 400 objects</a>. This has gone very well, and I've added images of a few dozen new objects to my little collection. Two nights of this work stand out. They might be the same night, but since I do not keep good notes, I have forgotten. On April 18th I captured what was for me a record number of images in a relatively short amount of time. You can see all 29 of them <a href="http://www.flickr.com/photos/79904144@N00/sets/72157629494796258/">here</a>. Being able to work that fast with the mount and the camera brings up the intriguing possibility of doing an entire Messier Marathon with the camera. But I'm not really interested in that. Anyway, the consistency of the mount allows you do work this way. Once aligned and calibrated the mount just never seems to go "off". Object after object can hit the small chip of the video camera. 

In addition, the mount seems impervious to wind. Wind is the enemy of stability and good tracking, yet one of the best nights I had in the last six weeks was on a night where the gusts were up to 20-25mph in my back yard. Remarkable.

<h4>
Meridian Games</h4>

The meridian is a something that hangs over every German equatorial mount. In this design the telescope sits on top of the declination axis and is counterweighted on the other side. Here is a poor schematic:

> <a href="http://4.bp.blogspot.com/-0NqQhog6Rv0/T6F-2YqDs-I/AAAAAAAAAdM/CW2fnVMfS4Y/s1600/Mount-1-284x300.png" imageanchor="1" style="margin-left:1em; margin-right:1em"><img border="0" height="300" width="284" src="http://4.bp.blogspot.com/-0NqQhog6Rv0/T6F-2YqDs-I/AAAAAAAAAdM/CW2fnVMfS4Y/s320/Mount-1-284x300.png" /></a>

In this design the telescope and the counterweights are always on opposite sides of the pier. When the mount is properly aligned, the RA axis will point straight north, which means the pier will be right on top of an imaginary line that runs North/South right down the middle of the sky which we call <em>the meridian</em>. Another bad picture:

> <a href="http://1.bp.blogspot.com/-Kc6dgCw8ZEo/T6F_dLJ5p7I/AAAAAAAAAdY/zbeBAf7CSR4/s1600/Flip-181x300.png" imageanchor="1" style="margin-left:1em; margin-right:1em"><img border="0" height="300" width="181" src="http://1.bp.blogspot.com/-Kc6dgCw8ZEo/T6F_dLJ5p7I/AAAAAAAAAdY/zbeBAf7CSR4/s320/Flip-181x300.png" /></a>

The issue with German mounts is that as you track closer to the meridian you can end up in one of two bad situations:

1. The weights or scope can hit the pier.

2. The weights can end up above the scope, which is bad for balance.

So avoid these things, the controller forces you to follow some rules. The main rule is that if the scope is pointing East its body should be on the West side of the mount and vice versa. This keeps things from hitting the pier and keeps the weights below the scope.

Which brings us back to the meridian. What the above rule means is that if we want to go from looking at things in the East to looking at things in the West we need to flip the scope over the mount so it's on the opposite side:

> <a href="http://2.bp.blogspot.com/-K11tChJBs4Q/T6F_1rBQvVI/AAAAAAAAAdk/jLOoJOfGEss/s1600/Meridian-198x300.png" imageanchor="1" style="margin-left:1em; margin-right:1em"><img border="0" height="300" width="198" src="http://2.bp.blogspot.com/-K11tChJBs4Q/T6F_1rBQvVI/AAAAAAAAAdk/jLOoJOfGEss/s320/Meridian-198x300.png" /></a>

This is a rather drastic and potentially destructive move. Things in your telescope can get out of alignment. You can catch wires on knobs. And, it can throw off your pointing. So, users of German mounts tend to try and avoid flipping at all costs. But, this is annoying since the exact time when you want to look at most objects is when they cross the meridian, because that&#8217;s when they are highest.

The Mach1 mount does a few things to make this better. First, the geometry of the mount allows it to track far past the meridian if you want it to. So you can pick up an object on the East side and follow it across its highest position in the sky without needing to flip anything around. Second, the build quality of the mount assures that when you do flip over, all you need to do to restore good pointing is to calibrate with the position of one bright star on the new side. I ended up always needing to do this with the Celestron mount anyway, even with all the fancy alignment software.

Finally, the control software in the mount allows you to shift where the mount thinks the meridian is, and thus delay or force flips when you want to. So, if you want to pick up an object that is 30min East of the meridian and track it until it is low in the West without flipping, you can tell the mount that the meridian is actually one hour further East than it really is. It will then dutifully flip the scope over as if the object is already in the West and then track it for hours without flipping. Just make sure nothing hits the tripod when you start this maneuver. If you are really a mount dork, you can read more about this <a href="http://www.astrocruise.com/articles/mount/mount.htm">here</a> or in the <a href="http://www.astro-physics.com/index.htm?products/mounts/mach1gto/mach1gto">AP documentation at their web site</a>.

Astro-Physics even has a clever scheme that uses flips to make sure your polar axis is aligned. This is the basis of the "quick drift" alignment scheme I mentioned before. Here is how it works. First, set up a finder scope on your main telescope that has a crosshair that you can rotate so that one direction corresponds to East/West and the other to North/South. Orion makes a good one that can do this.

Now, pick a star near the meridian and near zenith and have the mount point your finder scope at it. Center the star and hit "recalibrate". Now shift the meridian either East or West by one hour depending on which side of the meridian you are on to make the mount flip over. If you are well aligned, the star will still be centered in the finder. Any shift East/West is the finder scope not being quite aligned with the mount. Any shift North/South is the mount not being quite aligned in altitude. Use the altitude adjustment to get rid of half the North/South error. Use the adjustment on your finder scope to get rid of half of the East/West error. Use the keypad to center the star the rest of the way. Flip the mount again. Iterate this process until the star stays centered.

Now pick a second star that is at also near the meridian and at least 30 degrees away of the first star. Point the telescope there. If you are polar aligned, the star will again be centered in your finder. Any shift is a result of azimuth error, so with the azimuth adjuster to remove it. Now point back at the zenith star. If it is off center, center it with the keypad, hit recalibrate, and slew back to the second star. Adjust the azimuth again. Repeat this until the star stays centered as you slew back and forth. You are done.

There are a few things to like about this scheme:

1. It's easy. In particular, once the finder scope is set up well it usually only takes one or two iterations to get aligned.

2. It's stateless. You can redo the procedure any time you want without worrying about confusing any software. All you are doing is adjusting the mount's geometry relative to the sky. The control software is not keeping any sort of score.

3. It uses a nice ergonomic finder on top of the telescope. No fussing with polar scopes that are hard to look through. I use the polar scope to get a rough alignment, but always do this scheme for finer adjustments.

<h4>
Small Details</h4>

Finally, here are some small things that make the mount a pleasure to use.

1. The cables are great. The power cable has a locking mechanism so it won't work its way loose without you knowing it. The motor and keypad cables are all these cool XLR connectors like for pro audio equipment. It all just works.

2. I like the LED keypad display. It works better than the LCDs I've used before.

3. The documentation and support are great.

There isn't too much more to say. If you are in the market for a really really good telescope mount and you have the funds, I can't imagine doing better than the Astro-Physics product. It is a well-built no nonsense straightforward piece of equipment that just works and is gloriously free of useless bells and whistles. It's a reminder that it's still possible to achieve great things by building in small numbers and paying careful attention to detail.
