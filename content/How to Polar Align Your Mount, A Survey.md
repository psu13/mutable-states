Title: How to Polar Align Your Mount, A Survey
Date: 2013-04-13
Category: Astro
Author: psu

Polar Alignment is where you carefully make sure that the right ascension axis of your mount is exactly parallel with the rotational axis of the Earth. When you get this right, your mount can track any star in the sky just by rotating around its RA axis. If you get it wrong, stars slowly drift off of your field of view and the field will slowly rotate as you track from east to west. The amount of tracking error you get will be proportional to how far off you are. Finally, for various reasons, while an auto-guider and compensate for drift, it cannot compensate for the rotation.

Getting the polar alignment right is ultimately a problem of geometry. You want to measure the geometry of your mount with respect to the Earth's rotational axis. To understand how all of the various methods work you need to be able to visualize in your mind how deviations from the correct geometry will affect the tracking of the star. Sadly, I lack the graphical skills to really draw this out for you. But, because we have the Internet you can go and look at the excellent diagrams in <a href="http://celestialwonders.com/articles/polaralignment/MeasuringAlignmentError.pdf">this article by Frank Barrett</a> and it will teach you everything you need to know. With those pictures as a basis, here are some ways to get polar aligned.

0. Preliminaries

	Some terms you need to know. The <em>meridian</em> is an imaginary circle splits the night sky into east and west halves.  In my yard in Pittsburgh it runs through the north pole and around to the southern part of the sky. If your yard is in New Zealand, then it runs from the south pole up and around to the north.

	The <em>celestial equator</em> is the circle in the sky that has a declination value of zero. If you had a globe of the universe it would be the line that splits the sky into north and south halves.

	The North celestial pole is what you polar align to in the Northern hemisphere. If you live in the southern part of the world, then you want the south pole. Everything still works the same way, it's just upside down.

	Finally, you align your mount using mechanical adjustments on the base of the mount head. The mount have knobs that let you raise and lower the altitude of the RA axis and also spin the axis in azimuth. These are the controls you use to polar align the mount.

1. Polar Scope

	Most equatorial mounts that are used these days are of the so-call German design. GEMs are characterized by having the telescope ride on top of the declination (north to south) axis with a counterweight on the other side. The RA axis sits perpendicular to this arrangement. 

	Most GEMs also have a hollow RA axis. In the Northern hemisphere, this means you can usually get a rough polar alignment by sighting through the RA axis and putting Polaris in there. This will get you close enough for a lot of work, but it's not good enough for taking pictures.

	Some mounts have a small telescope that sits in the RA axis with a picture of some sort in it. The Losmandy style polar scopes have a little diagram with Polaris, Ursa Minor, Ursa Major and Cassiopeia in it. The idea is that if you can wiggle the mount until Polaris and two other stars are in the right holes, you'll be even closer than you were before. This works OK for some people, but I never had much luck.

	The Takahashi (and now Astrophysics and iOptron) mounts have a reticle that looks like a clock in them. You run some software that tells you where on the clock face Polaris should be and you stick it there. If the polar scope is well calibrated with the RA axis, you are polar aligned. If it's off, you'll still be off.

	The Tak mounts have the scope installed in the factory and are very well calibrated. The Astrophysics scope requires that you install and calibrate it yourself, so mine is a bit off. I could work harder to get it closer, but I lack the mechanical fortitude to get it really accurate. 

2. Pointing Model Alignment

	This is what most computerized mounts use for helping you polar align. The computer or hand box connected to the mount will ask you to center multiple "alignment stars" one at a time. As you do each one, the mount makes a note of the pointing error and builds a simple linear model of the relationship between where it thinks it should go and where things actually are. This model compensates for various sorts of errors that make pointing less accurate.

	Among other things, this model can compute how much of the pointing error is caused by polar alignment error. So, after building the model typically what you do is point at a star and the software will displace the mount according to the error it computed. You then center this star in the telescope my mechanically adjusting the altitude or azimuth of the polar axis, and you are done. I've used the Celestron version of a scheme like this and it works very well.

3. Drift Alignment

	Drift alignment is the classic astrophotographer's tool. If you read the pdf at the beginning of this article you'll already know how this works. Here is what you do. First put a high power retical eyepiece in your telescope and rotate it so that the lines correspond to north/south and east/west motions of the mount. Now point at a star near the intersection of the celestial equator and the meridian. Center the star carefully in a high power eyepiece. Now watch the star move in the eyepiece. if the star drifts north or south, you adjust the azimuth east and west respectively to fix the drift. Keep adjusting until there is no drift after a few minutes (or up to several minutes if you want to be really picky).

	Next point the telescope at a star fairly far to the east or west and also on the celestial equator. Do the same observation in the eyepiece but now if the star drifts north adjust the altitude higher, and if it drifts south lower the altitude.

	If you study the diagrams in the pdf and think about the geometry, its pretty clear why these are the right moves.

	There are two annoying things about drift alignment. First, it seems complicated. Second, it involves a lot of staring at small stars in high power eyepieces. Since its likely that you are going through all of this to take pictures with a CCD camera, the obvious thing to do it to use the camera to do it.

4. Drift Alignment with a CCD Camera

	This works exactly the same way as the scheme above but you use computers to make it easier. First, since your mount can point itself, you use the pointing computer to find the stars. Second, you use your CCD and computer to watch the star for drift. Finally, if you want to get fancy, you use a third piece of software to analyze the drift and tell you how to adjust the mount.

	This is super convenient. You plop your mount outside, point it roughly at Polaris and then set up your camera (which you'd have done anyway). Then you let the computer stare at the star for a few minutes and when it's all done you are polar aligned. I've been using this scheme with a piece of software called PEMPro and it's great.

	Another scheme that does not require extra software is outlined here: <a href="http://www.observatory.digital-sf.com/Polar_Alignment_CCDv1-1.pdf">http://www.observatory.digital-sf.com/Polar_Alignment_CCDv1-1.pdf</a>.

5. Plate Solving

	Recall that a <a href="http://nova.astrometry.net">plate solver</a> analyzes the image that you took and calibrates the stars in the image with known catalog stars. It can then use the positions of those stars to compute the actual coordinates of the center of the picture. Plate solving is fantastically useful for various things involving pointing your telescope. It requires a computer and a large star catalog to work, so it is not used as much as it could be. But there are now free <a href="http://nova.astrometry.net">Internet plate solvers</a>, and the software fits into even cheap computers, so I think people will start using it more.

	Anyway, you can use a plate solver to compute polar alignment error. The idea is that instead of waiting for your mount to track to measure the drift,  you take two pictures, one at the initial point of the reference star and one offset by some fixed amount of RA. After taking each picture you use a <a href="http://nova.astrometry.net">plate solver</a> to find out where you are really pointing. You then compare the difference in position to what see if the declination drifted. At this point you can work out how to adjust the mount to improve the alignment. There are a few different software packages that do this automatically.

	What this scheme is really doing is shortcutting the drift alignment by moving the mount ahead all at once and then using the plate solver to compute the drift. People will quibble over whether this is as accurate as actually measuring the drift. It probably does not matter most of the time.

6. "Quick Drift" Alignment

	The Astro-Physics mounts have the following clever polar alignment scheme. It uses a feature of the mount control that lets you flip the mount over the meridian whenever you want to check alignment. All you need is a finder scope with a retical eyepiece that you can rotate. You want to rotate the retical so that one line is always on the E/W axis one is on the N/S.

	Now, pick a star near the meridian and near zenith and have the mount point your finder scope at it. Center the star and hit "recalibrate". Now shift the meridian either East or West by one hour depending on which side of the meridian you are on to make the mount flip over. If you are well aligned, the star will still be centered in the finder. Any shift East/West is the finder scope not being quite aligned with the mount. Any shift North/South is the mount not being quite aligned in altitude. Use the altitude adjustment to get rid of half the North/South error. Use the adjustment on your finder scope to get rid of half of the East/West error. Use the keypad to center the star the rest of the way. Flip the mount again. Iterate this process until the star stays centered.

	Now pick a second star that is at also near the meridian and at least 30 degrees away of the first star. Point the telescope there. If you are polar aligned, the star will again be centered in your finder. Any shift is a result of azimuth error, so with the azimuth adjuster to remove it. Now point back at the zenith star. If it is off center, center it with the keypad, hit recalibrate, and slew back to the second star. Adjust the azimuth again. Repeat this until the star stays centered as you slew back and forth. You are done.

	Again, if you think about the geometry of the problem as described in the pdf that I linked to, you'll sort of see how this works. The meridian flip simulates the E/W movement of drift alignment, and so if the star moves N/S after the flip you know the altitude is off. The second stage is similar to other iterative alignment schemes, the idea being that the pointing error on the second star is all accounted for by polar misalignment. Since you know the altitude is already right, you only have to move azimuth.

7. Notes

	There really was not any point in my writing all this down. The following pages actually can summarize all of this better than I can, so here you go.

<p>
<a href="http://celestialwonders.com/articles/polaralignment/polaralignmentsurvey.html">A General Survey</a>

<p>
<a href="http://celestialwonders.com/articles/polaralignment/MeasuringAlignmentError.pdf">Measuring Alignment Error</a>

<p>
<a href="http://celestialwonders.com/articles/polaralignment/PolarAlignmentAccuracy.pdf">Drift Alignment Math</a>

<p>
<a href="http://celestialwonders.com/articles/polaralignment/StarOffsetPositioning.pdf">Star Offset Positioning</a>
