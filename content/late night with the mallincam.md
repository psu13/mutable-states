Title: Late Night with the Mallincam
Date: 2011-05-04
Category: Astro
Author: psu

If there is one thing that I have learned in my now medium-long lifetime it's that in Western Pennsylvania you cannot count on clear skies lasting. So when the clouds parted last Friday night at 11:15pm, I had a short quandary. On the one hand, it was 11:15pm and I should be in bed. On the other hand, it might be the last window of clear sky for another month. April to this point had been nothing but gray skies, cold, and rain. After considering this for about 45 seconds, I started to set up the telescope.

As this was my second time out with the new mount and as the first time had gone pretty well (got set up and aligned in about 20 minutes) this time things went less smoothly. To make this work well, you need script and a list. And I forgot a few parts of the script. Here is how you set up.

First, we need short tangent on what we want the mount to do for us when we are done. By convention we keep track of the position of every cataloged astronomical object that we deal with using something called the equatorial coordinate system. This coordinate system is similar to the one we use on the Earth, with the longitude and latitude, except it that it's projected on the sky. The east/west coordinate, similar to longitude, is called Right Ascension or RA. I don't know why. RA is measured like time, in hours, minutes, seconds and so on. This turns out to be convenient because you are often interested in the time at which objects are visible or not. If you know the time of year and the RA of the object, you can compute whether or not you should be able to see it.

The North/South coordinate, similar to Latitude is called Declination, or DEC. This coordinate is measured in the familiar degrees, minutes, seconds, and so on.

Our equatorial mount, unsurprisingly, has two axes that go by these same names. The right ascension axis is also called the polar axis of the mount. 

The eventual goal of the setup is to align two things. First, we want to align the polar axis of the mount with the polar axis of the Earth. This alignment is called polar alignment and allows the mount to track objects in the sky while only driving the telescope along one axis. 

Second, we want to give the mount's computer an accurate picture of what is where in the sky so it can point the telescope automatically. I call this star alignment to distinguish it from polar alignment. When we are done, we should be able to tell the mount to point the telescope anywhere we want in the sky, and it can do some quick calculations to figure out exactly how to run the motors to pull that off. Then we sit back and watch the object come into the field of the eyepiece, or camera. So, here we go.

1. Take the mount outside. Point the right ascension axis of the mount roughly north.  

2. Attach the counterweight on the counterweight thingy.

3. Go back inside and grab the telescope. Attach the telescope to the mount using the quick release dovetail arrangement.

4. Balance the scope and the counterweight along the right ascension axis. To do this on my mount, you release the clutch on the RA axis. This lets you turn the mount by hand rather than with the motors. Now turn the mount until the shaft is horizontal and gently let go. If the telescope drops, move the counterweight further away from the telescope and try again. If the counterweight drops, move it closer to the telescope and try again. Iterate until the whole system is balanced.

5. Now balance the telescope along the declination axis. Tighten the RA clutch. Carefully loosen the DEC clutch turn the telescope until it is horizontal. Slooowly let go and see how the tube moves. With the Celestron telescopes you can then move the scope backward and forward in the quick release saddle until it balances.

6. Now turn the mount until the little index marks line up. When you are done doing this the scope is in its "zero" position and should be pointing North. If it's dark enough you can look in the finder scope and maybe see Polaris. Resist the urge to center Polaris in the finder. This will do you no good because the axis of the finder is not what you want to point at Polaris. I shoud know, I wasted my time doing this.

7. Instead what you want to do is look through a hollow in the RA axis and put Polaris into that hole. Then you know the polar axis is looking roughly at Polaris, which is more useful. To do this, loosen the DEC clutch and turn the tube to 90 degrees from where it was. You should now be able to look through the hole and see sky. 

	Get down on your knees and push the mount around and peer into this hole and see if you can see Polaris. It might take a few tries before you can see anything, depending on how dark it is. If you can't see it, use the following odd scheme to find it. First, you will note two long bolts with handles on them on the front and the back of the mount. These adjust altitude. They do not do it very well. In particular, it's hard to smoothly lower the altitude. So, on the theory that you are pointed too high, loosen the front lever and push the mount so it falls down a few degrees in altitude. Then, using the back lever raise the mount again and hopefully you'll see Polaris enter the field. If not, you might be off to the side a bit. Shove the mount sideways one way or another and try again until you get Polaris in the hole. The field of view through this hole is pretty wide so this isn't too hard.

8. Also on the front of the mount you will notice two knobs that push the mount side to side. If Polaris is not centered side to side in the hole, use these knobs to move it around. To move the mount you loosen one knob and then tighten the other one. I don't remember how things are oriented so you will just have to try yourself until you figure it out.

	Starting with Polaris roughly in this hole turns out to be important. In my short experience, if you are too far off the star alignment which I will describe next never ends up working.

9. Now turn the scope back to the zero position and plug  in the power cord. Answer all the questions about time and date and such that the hand controller will ask you and start the two star alignment. Tell the mount to move the scope to the first star it suggests. If you can't find that star or its blocked, hit the undo key to try other stars until you get one you like. The mount will point the telescope at the star you picked and then you will use the arrow keys on the hand control to center the star in your finder then the eyepiece. The Celestron manual tells you to always make sure the final movements of the stars are driven by the Up and Right arrow keys. This minimizes the resulting backlash in the gears. I have no reason to doubt the manual on this point, so be careful about that.

The mount will then let you repeat this process on a second star. You will notice that by default both of these stars will be chosen from the western part of the sky. After you are done, the hand controller will ask you if you want to add "calibration" stars, all of which will be chosen from the eastern part of the sky. You can add up to four of these stars. Keep adding them until the pointing gets very accurate.

There are two important things to know about this procedure:

First, the east/west breakdown is important for mounts like the CG-5. The CG-5 is what we call a "German Equatorial Mount", or GEM. The geometry of the GEM is such that you have to be aware of the relative position of the telescope and an imaginary line called the meridian. The meridian is the line that runs North/South and splits the sky in half East/West. If you have set up your mount correctly, the middle of the tripod sits right on top of the meridian, and in a GEM this means that the scope is on one side of this line and the counterweight is on the other. The thing you have to remember is that GEMs have a hard time tracking past the meridian because when you go too far either the scope or the counterweight shaft will run into the mount. Bad news.

To get around this problem GEMs flip the scope around whenever they cross the meridian. You want to be able to do this and maintain pointing accuracy, so the Celestron software does allows you to do extra calibration to make sure this works right.

The second thing to remember about star alignment is not to try to do it when there are thin clouds around. This makes it easy to guess wrong and align on the wrong stars, or stars you cannot see. Then no matter how many stars you align to, the pointing never gets any better. If you notice this happening, the best thing to do is to reboot the mount and start over. I ended up in this situation at about 11:45pm. By then the sky had really cleared, so I buckled down and tried again. I turned the mount off, made sure that I got Polaris into that damned hole, and started again. Ten minutes later I was ready to move on.

10. Having fine tuned your star alignment, you can now engage a nifty little piece of software that is unique to the Celestron controllers. It is called "all star" polar alignment. Pick one of the stars that you used for the final calibration as long as it is not too close to either due North or zenith. Hit the Align button on the hand controller and navigate to the Polar Align menu and then choose Align Mount and hit Enter. The mount will think a bit and then move the telescope to point at the star you just picked. Use the hand control to center it just like you did before. When you are done, you tell the hand controller to start the Polar alignment. The telescope will think a bit and then move to another spot in the sky. This is where the alignment star would be the mount were in fact polar aligned. Now you get to get down on the ground again and use those knobs and levers from before to push the mount around in azimuth and altitude until the star is centered in your eyepiece. When you are done hit the Align button and you are done.

By this time your knees and shoulders should be a bit sore, but your mount will be well aligned for both pointing and tracking. I managed to get to this state by about 12:15am. So then I yawned and went in and got my camera.

While the CG-5 mount is bigger, heavier and more complicated than my old 8SE mount, it does have its advantages. First, I have found that the tripod is much more solid, so the telescope does not shake and shimmy when I'm trying to focus. Second, it's a lot easier to use the camera because I can stick it into the back of the telescope without worrying about it hitting the base of the forks. On the other hand, there are some things you want to be careful about.

If you do not firmly attach your eyepiece to the telescope, you may find that the mount can make it fall out as it turns and twists the telescope at all strange angles. This is bad. You may also find that the various cables that stick our from various ports in the mount and lodge themselves between the motor housings. I've had this happen twice now and I'm not sure why, but it does make the mount upset. Try to avoid this.

Luckily, on this night, with the time nearing 12:30am, I had none of these issues and was able to happily go to my first target, the galaxy NGC 2903. There are two things to note here. First, you can see the cool spiral arms of the galaxy. Second, even with about a minute of exposure, the mount is still tracking pretty well.  I have found in general that a minute works well. Two minutes is a bit too long.

> <a href="http://3.bp.blogspot.com/-qyAX1mDrdPQ/TcHwTLmjT6I/AAAAAAAAAYo/zLFnGhDadUA/s1600/NGC2903-2011-04-29-1.png" imageanchor="1" style=""><img border="0" height="238" width="320" src="http://3.bp.blogspot.com/-qyAX1mDrdPQ/TcHwTLmjT6I/AAAAAAAAAYo/zLFnGhDadUA/s320/NGC2903-2011-04-29-1.png" /></a>


Second target of the night was the "Hockey Stick" galaxy, NGC 4656. This is a pretty dim object, I was happy to get a good view of it.

> <a href="http://1.bp.blogspot.com/-ZIJbrGAfd68/TcHwTaOYf0I/AAAAAAAAAYw/9rj4M_P0ivU/s1600/NGC4656-Hockey%2BStick-2011-04-29-1.png" imageanchor="1" style=""><img border="0" height="242" width="320" src="http://1.bp.blogspot.com/-ZIJbrGAfd68/TcHwTaOYf0I/AAAAAAAAAYw/9rj4M_P0ivU/s320/NGC4656-Hockey%2BStick-2011-04-29-1.png" /></a>


I then cruised through the galaxy clusters in Virgo and <a href="http://en.wikipedia.org/wiki/Coma_Berenices">Coma Berenices</a>. There was M64, M84, M86, M87, and M91. For two hours, everything I asked for hit right on the camera and the mount tracked with relative smoothness. I was using the camera with a .5x focal reducer, which means that the effective focal length of the telescope was 1000mm instead of 2000mm. This means that the field of view of the camera is roughly 20 by 15 arc minutes, which is pretty darned small. Overall I remain impressed by the ability of a 25 cent embedded processor to accurately point a 15 pound telescope  with this level of accuracy.

> <a href="http://4.bp.blogspot.com/-BoJXOIR33n0/TcH1BnB2FbI/AAAAAAAAAY4/xKG_weQ87LE/s1600/M64-2011-04-29-1.png" imageanchor="1" style=""><img border="0" height="239" width="320" src="http://4.bp.blogspot.com/-BoJXOIR33n0/TcH1BnB2FbI/AAAAAAAAAY4/xKG_weQ87LE/s320/M64-2011-04-29-1.png" /></a>


Somewhere around M87 I noticed the pictures looked funny, with ugly bloated stars. I didn't think about it too hard until I tried to look at M101 and it was all blurry. So, I turned the telescope to the globular cluster M3 and tried my best to refocus.

> <a href="http://2.bp.blogspot.com/-08fo04mZ4LQ/TcH1dE5uajI/AAAAAAAAAZA/vr3_jKiDb9g/s1600/M3-2011-04-29-1.png" imageanchor="1" style=""><img border="0" height="239" width="320" src="http://2.bp.blogspot.com/-08fo04mZ4LQ/TcH1dE5uajI/AAAAAAAAAZA/vr3_jKiDb9g/s320/M3-2011-04-29-1.png" /></a>


Having gotten closer, I went back to M101 and got the surprise of the night. Most of the objects I had looked at had been small with bright cores but not much in the way of larger scale detail. M101 was different. The arms spread out over the field of view with dim hints of dust lanes and other grand details. 

> <a href="http://1.bp.blogspot.com/-8w_MmPmmZp4/TcH1dRUIJdI/AAAAAAAAAZI/6CjkFK06f4w/s1600/M101-2011-04-29-1.png" imageanchor="1" style=""><img border="0" height="238" width="320" src="http://1.bp.blogspot.com/-8w_MmPmmZp4/TcH1dRUIJdI/AAAAAAAAAZI/6CjkFK06f4w/s320/M101-2011-04-29-1.png" /></a>


I finally shut down for the night at 2:45, sleepy but pretty happy. I was also hopeful that with a bit more practice I'd be able to tease even more out of these objects sitting above me in the sky. Who would have thought you could see this much with relatively little work in your backyard.