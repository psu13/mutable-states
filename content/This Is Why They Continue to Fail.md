Title: This Is Why They Continue to Fail
Date: 2017-05-21
Category: Photo
Author: psu

If I'm making a reference to Yoda you know it's bad. Today we're going to talk about just how little the companies that make cameras understand about how the people who buy cameras would like to be able to use them. A lot of recent camera bodies boast that they support a "wireless networking" mode so you can talk to the camera over a network. This all seems nice when you are looking at a checkbox on the marketing web page for the camera. I can think of a half dozen things that I'd like to be able to tell the camera to do over a network.

Off the top of my head, a few of these would be useful:

1. Wireless remote control of the camera from my phone.

2. Wireless transfer of the pictures in the camera to my laptop.

3. Maybe the camera could talk to the Internet to get the time, so I don't have to keep resetting its fucking clock whenever I move through a different time zone.

4. Automatic backup of the camera's storage card to DropBox or similar?

5. Wireless triggering of other camera-related devices from the camera or some other centralized device (i.e. flashes, multiple cameras, maybe still capture synced with video?).

6. ???

7. Profit!

If I had spent more than 10 minutes thinking about the above list, it would be twice as long.

All of these features depend on a few simple expectations for the networking stack in the camera:
 
1. It should always be on.

2. Using it should be as transparent as every other network device that we are used to using (i.e. your iPhone).

Here is what you realize when you actually try to use whatever wireless networking feature is built into a current high end digital camera: *These people have no fucking clue how the feature should work.*

This is not that all surprising. What I described above is how you want a networked computer to work (the iPhone is, when you think about it, the apotheosis of the networked personal computer, as originally designed and built at PARC in the 70s). Camera companies do not understand computers. Camera companies understand cameras as they have been built and used since being frozen in time in about 1979. 

To a camera company a camera is a box that captures pictures and then puts them in a box so you can take them somewhere else for the next stage. The box is as dumb as possible, while still being able to achieve this task. A lot of modern digital cameras have many "menus" that look like "software", but don't be fooled. These are just the bare minimum of user interface needed to set the few switches that the  company thinks you might need to do things like make the autofocus system not completely lock up. They will be presented to you as a single scrolling list of 15,000 settings sorted in no particular order. Each one is probably implemented by a different contractor. 

When you tell a camera company "I would like my camera to somehow take advantage of the ubiquitous data networking available to use all in 2017." they say "Hmm, Ok. I will hire a contractor to build networking box and attach it to your 1979-like camera device with the least work possible and call it a day."

Say you want to have your iPhone talk to your new Olympus OMD E-M1 Mark II. First, allocate a good fifteen to twenty minutes to get it set up, because there are a lot of steps.

Next, you turn on your camera and find the menu item for "Smartphone Connection". This menu item is one of 145856 choices inside the UI. As described above you basically have to scroll through each item one by one until you see the right one. Don't be fooled by other names that might involve "Wifi" or "Wireless" or something. Those are irrelevant, but the only way you'll know is to choose them.

Now, download the Olympus app for your iPhone and fire it up.

Now the camera will spend about ten seconds saying that it is "starting the Wi-Fi" and then it will who you a QR code that you are supposed to capture with your phone. I shit you not.

> <a data-flickr-embed="true"  href="https://www.flickr.com/photos/79904144@N00/34676124481/in/dateposted-public/" title="IMG_2163"><img src="https://c1.staticflickr.com/5/4274/34676124481_c0d86e45cd_z.jpg" width="640" height="480" alt="IMG_2163"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

At this point you are already sad. This code has been in the oven so long that when they started QR codes were still a thing.

But it gets worse. After opening the Olympus iPhone app and taking a picture of the code, you have to tap a few times to install the networking profile into the settings in your phone. You are assured that this is the only time you will need to do this. Don't believe it.

Now from the main screen of the iPhone app you have a few choices:

1. Remote control

2. Import Photos

3. Edit Photo

4. Add Geotag

I was  only interested in #1 above. I was thinking it would be nice to use my phone as a cable release, so I would not have to carry a cable release. I picked it, got the app into the wrong mode at first, reset it, then picked the cable release mode and took a couple of test shots. They seemed to work.

Then I picked the camera up and tried to take a few pictures without using the phone. "Hmm,", I thought, "I guess I have to exit this menu." So I hit the menu button to exit (that's what that cryptic message above with the text "End WiFi [Menu]" means). The camera then cheerfully told me that it was turning off the Wifi network and sure enough, the phone app was now lost.

So I went back and turned on the network again, and the camera told me to do  the whole QR code dance again (and the profile that I had previously installed did not seem to work anymore).

At this point it dawned on me that the intended usage for this whole feature was to put the dumb picture taking box into a *special mode* where the shutter button is on the phone. While in this mode, this is the only way you can take pictures with your dumb box. To do anything else (including set most of the other 15,475 switches that you can set in the menus) you must exit this mode, and then return to it again when you are ready. In other words, they went to all the trouble to put a network radio into their camera box (which can't have been easy, there is not much room in there) and the single thing they think you want to use it for is if you happen to have set up a shoot in your home studio and you'd like to use your phone to trigger the camera instead of a cable release (or radio remote).

Of course, the flow they have thought up to let you do this is 15 times slower and 25 times less convenient than setting up and using a radio remote. But whatever.

In addition, it's actually *even more insulting* than this. While in this mode, your dumb camera box can't even do all the things that it used to do when capturing pictures. For example, if you have the camera set to save pictures to two memory cards at once (for backups!), and you want to take a picture with your phone, well, you are out of luck. No backups for you!

Congratulations Olympus, you have developed the worst single feature that I have used in 2017, the year that slack brought you """threads""". The camera without this feature at all is actually better than the camera that includes it. At least there would be two or three fewer menu items in the custom settings. Maybe I'm being too hard on them though. As bad as the Olympus setup is, it at *least* does not require that you buy a special dongle with the networking radio in it like Nikon does.

To sum up: rather than build a networking stack and *integrate* it into usage model of the camera in a way that makes it ubiquitous and transparent (the way networking works, say, *on your phone*) the camera companies continue to put networking into the networking box, and use it as nothing more than a different way to push the shutter button on your camera and make it do that camera box thing. 

I have nothing more to say, except to quote Yoda again: "That, is why you fail."
