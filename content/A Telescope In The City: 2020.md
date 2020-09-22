Title: A Telescope In The City: 2020
Date: 2020-09-04
Category: Astro
Author: psu

In the summer of 2010, through circumstances that I don't quite remember, I came across a web site where <a href="http://mutable-states.com/the-big-lie-solved.html">amateur astronomers were using the Internet to stream images</a> captured in their telescopes using small video cameras that could be programmed to do time exposures. Here, with just "a bit" more work than it took to try and see the same objects with your eyeballs you could actually see an image of the object that, while not approximating even longer time exposures with astronomical cameras taken through space telescopes, was at least more than a faint white patch barely peeking out through the haze and light pollution of my suburban sky. Clearly this required investigation.

Over the next year or so I <a href="http://mutable-states.com/tinkering-with-the-stars.html">slowly collected the equipment and skills</a> needed to set up a system like this for myself. The trick in all of this is to be patient and slowly move towards the goal one small step at time. Eventually I had put together a pretty powerful equatorially mounted telescope tube, camera system, and a bit of image processing know-how. I could set up and get stuff like this:

> <a data-flickr-embed="true" href="https://www.flickr.com/photos/79904144@N00/6271201264/in/album-72157629128096583/" title="M27-2011-10-22-Stacked-10-PS"><img src="https://live.staticflickr.com/6215/6271201264_63ae975e4a_w.jpg" width="400" height="300" alt="M27-2011-10-22-Stacked-10-PS"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

or this:

> <a data-flickr-embed="true" href="https://www.flickr.com/photos/79904144@N00/7030740283/in/album-72157629128096583/" title="M51-2012-03-29-stacked-5x"><img src="https://live.staticflickr.com/7278/7030740283_24db276d57_w.jpg" width="400" height="298" alt="M51-2012-03-29-stacked-5x"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

It was pretty easy. All you had to do each night was this "short" checklist of setup items to make the telescope point at the right place and take pictures in focus: <a href="http://mutable-states.com/grab-and-go.html">http://mutable-states.com/grab-and-go.html</a>.

Later on, of course, I dabbled with "real" astronomical CCD cameras and an even fancier mount and all of the attendant complications. I got <a href="https://www.flickr.com/photos/79904144@N00/albums/72157631169684214">some pretty good pictures</a> and then put it away when it got to be too much like work. I'll pick it up again later. Anyway, to set that system up you did this: <a href="http://mutable-states.com/maxim-dl-setup-and-workflow.html">http://mutable-states.com/maxim-dl-setup-and-workflow.html</a>.

The basic pieces that you need to take pictures of things in the sky are:

1. A telescope tube with a CCD camera attached to it.

2. A computerized mount that can point at things and automatically know where it is pointing.

4. Software to set up and control the pointing system and then later track objects that you are capturing over time so you can take long exposures.

3. Software to capture and combine the frames from the camera.

But, this list is just a high level summary. If you expand the list above into a more detailed list of everything you would want to maximize ease of use and automation, you actually end up with a list of a dozen or so bits and pieces that you need to set up every night.

Traditionally what the intrepid astronomy hobbyist would do is read the magazines and online forums, buy all of these bits and pieces of hardware and software to fulfill each of the above requirements and then hand integrate the pieces until they had something that they could use each clear night to capture images. The main thing that stands in the way of people using cameras more routinely for astronomy is the complexity and headache of setting up all this stuff.

What you really want is a system that works like this:

1. Put the telescope in the yard.

1. Point it somewhere and take a picture.

1. Plate solve (1) the picture so the mount knows where it is pointing.

1. Fine tune focus.

1. Take pictures.

This kind of operation was *possible* in 2011 and 2012 ... but it took a lot of manual integration work, and was much easier if you had a permanent installation. Still, one always wondered how many <a href="http://mutable-states.com/tens-of-dollars.html">tens of dollars</a> someone might make if they could build the whole stack in one box.

Well, 2020 is the year we start to find out. While bits and pieces of this sort of automation have started to show up in the high end and the low end of the telescope equipment market, no one had really tried to make a true one piece solution until now. I am here to report on one attempt at this, the <a href="https://unistellaroptics.com">Unistellar eVscope</a>.

The claim for this telescope is that you put it out in the yard, run some software on your phone to control it, and it shows you things in the sky that you can't see with your eyeballs in a normal telescope. I wrote this off as mostly hype until the beginning of this year when the machine finally shipped, and I found out that <a href="https://www.youtube.com/user/ProfMikeM">Mike Merrifield</a>, the astronomer from Brady Haren's <a href="https://www.youtube.com/user/sixtysymbols">Sixty Symbols</a> youtube channel, had bought one. And, early on in the worldwide pandemic lockdown of 2020 they made <a href="https://www.youtube.com/watch?v=glOWZoFnB8w">a video about it</a>. From the video it's apparent that all you do with this telescope is:

1. Load some software on your phone.

1. Put it out in the yard.

1. Point it somewhere with stars and take a calibration picture.

1. Fine tune focus using a provided focusing mask (2).

1. Tell it to show you stuff in the sky that you can't see with your eyeballs in a normal telescope.

I thought to myself: "what the fuck, it's a pandemic, might as well try it."

So I did. And it turns out here's what you do to use the eVscope:

1. Load some software on your phone.

1. Put it out in the yard.

1. Point it somewhere with stars and take a calibration picture.

1. Fine tune focus using a provided focusing mask (2).

1. Tell it to show you stuff in the sky that you can't see with your eyeballs in a normal telescope.

The telescope puts out a low power wifi network that you use to talk to it from the phone. The machine does a plate solve on the first calibration picture to figure out where it is pointing and fine tune the built-in mount a bit. Then when you point it at things, it goes to the general area, does a plate solve, and repoints based on where it computed itself to be pointing until it knows the object you wanted is close to the center of the field of view of the camera. Then it shows you pictures.

It has a "Live" video mode that can show you bright stars and things and another mode called "Enhanced vision" that does automatic image stacking. In the stacking mode it appears to take exposures that top out at about 15 to 30 seconds long depending on how the tracking is going. It then combines the frames together to improve the image quality over time. You can point it at something dim and have it chew for 10 or 20 minutes. The pictures get slowly better as the machine accumulates data and then you get images like this:

> <a data-flickr-embed="true" href="https://www.flickr.com/photos/79904144@N00/50304636386/in/album-72157715841088797/" title="20200903-eVscope-20200904-005620"><img src="https://live.staticflickr.com/65535/50304636386_e7acd03ffa_w.jpg" width="400" height="400" alt="20200903-eVscope-20200904-005620"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

or

> <a data-flickr-embed="true" href="https://www.flickr.com/photos/79904144@N00/50303952183/in/album-72157715841088797/" title="20200903-eVscope-20200904-011510"><img src="https://live.staticflickr.com/65535/50303952183_1ba75e672c_w.jpg" width="400" height="400" alt="20200903-eVscope-20200904-011510"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

or

<a data-flickr-embed="true" href="https://www.flickr.com/photos/79904144@N00/50304636371/in/album-72157715841088797/" title="20200903-eVscope-20200904-024455"><img src="https://live.staticflickr.com/65535/50304636371_7aef54eaf5_w.jpg" width="400" height="400" alt="20200903-eVscope-20200904-024455"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

These are about as good as I got stacking mallincam screen shots back in the day. And, the computer in the telescope is doing all of it. The machine stores the raw frames on an SD card and it might be possible at some point to fetch them off and fuss with them yourself. But that's not what this machine is for. This is for relatively quick and almost "live" views of dim objects that you have no hope of seeing from a suburban back yard, but which look pretty good in 5 to 10 (or up to 30) minutes through this tiny telescope.

The tube itself is a relatively small optic, only 4 inches across. Mounted to the tripod the thing weighs about 20lb and it easy to carry in one piece to the yard. The tube is permanently mounted to a motorized alt-az mount, like the small Celestrons. Instead of an eyepiece at the focus of the optical system there is a permanently mounted CCD video camera that does the image capture described above. The software for the "Enhanced" mode takes the individual time exposures and combines them into composite frames while also compensating for tracking errors and filtering out light pollution. All in all it's pretty amazing.

The small optics and limited resolution of the CCD mean that the telescope is best at medium sized deep sky objects that will look good even if you can't resolve a lot of fine detail. Dim extended things are not great because the optics are too small. Bright but small things like planets will be boring because they will be too small to show details. Where traditional telescopes are only really good for the moon and planets when observing from the city, the eVscope is sort of the opposite. The planets are no good at all, but dim "deep sky" objects that are normally either completely invisible in an eyepiece or at best ... uninspiring ... from suburban light pollution suddenly come to life and look a bit like the fancy photographs we are used to seeing now.

That said, this system will also *not* get you pictures that come close to the image quality what you would get with long exposures, equatorial mounts, and a dedicated cooled CCD camera. But hey, it's point and click and only takes 10 minutes, so what you do expect?

Personally I'm looking forward to using this thing to do more quick and dirty galaxy hunting. I always loved looking at galaxies. The last astrophotograph that I took with my high powered CCD system was also my favorite ... a medium deep shot of the galaxy cluster in Coma Berenices. Here it is, annotated with all the objects that you can see in the frame:

> <a data-flickr-embed="true" href="https://www.flickr.com/photos/79904144@N00/8748698122/in/album-72157631169684214/" title="NGC4889_2013_05_16_27x300s-annotated"><img src="https://live.staticflickr.com/7292/8748698122_0d500c4abc_w.jpg" width="400" height="300" alt="NGC4889_2013_05_16_27x300s-annotated"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

Galaxies are dim, but usually compact. So I think this small telescope will be able to do a decent job with them.

This scope will also be a great portable toy to take on trips to darker sky, assuming at some point it becomes possible to travel again without the possibility of spreading plague and death.

Finally, if I ever get back to doing "real" CCD pictures, having this thing around to look at other stuff while the main telescope chugs away will be endless fun.

All in all a great pandemic "what the fuck" purchase, if you have the spare cash lying around.

Here's the flickr album with my pictures. I'll add new ones there over time: <a href="https://www.flickr.com/photos/79904144@N00/albums/72157715841088797">https://www.flickr.com/photos/79904144@N00/albums/72157715841088797</a>

**Notes**

1. To "plate solve" is to use computer software to compute the celestial coordinates of a given field of view based on the stars that appear there. You do this by comparing the field with known stars in an atlas. The weird name comes from the fact that we used to do this by hand with pictures taken on glass plates. Consumer software for this has been around for 20 years or so, but it did not start to get cheap or reliable until more recently.
	
1. Focusing telescopes with a camera attached can be tedious because the nature of time exposures makes it hard to tell when the stars are really sharp. The solution is to use a special mask in front of the telescope called a <a href="https://en.wikipedia.org/wiki/Bahtinov_mask">Bahtinov mask</a>. When you have the focus right with the mask in place you get an easy to read diffraction pattern on a bright star. This telescope helpfully comes with one of these widgets built in to the dust cap for the tube. Nice.