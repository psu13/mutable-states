Title: To The Fog!
Date: 2014-06-14
Category: Computers
Author: psu

A wise man once said:
>A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable.

Since you are no doubt an erudite reader, you'll know that the wise man was Leslie Lamport, a computer scientist, who among other things studied the problems inherent in making groups of computers accomplish things cooperatively. It's more complicated than you might imagine. 

As far as I can tell Lamport said this in 1987, and the systems that he was talking about might have consisted of a network of a few dozen or a few hundred machines spread over a relatively small area of land. For example, around this time the school where I went to college, Carnegie Mellon University, had just deployed a system of workstations that could transparently share data and computing resources over a network that reached from the computing center to all the dorm rooms. Pretty futuristic for back then. There was even _multi-media_ email!

Of course, these days everyone uses the Internet to share things. And, from what you read in the tech press, the next frontier for this will be something that no one quite understands, but which everyone calls "The Cloud". What is all that about? The answer is sort of complicated, and we need to first consider how computing resources have been organized over time.

The fundamental rule of organizing computing resources is this:
>You centralize and/or share what is expensive. You distribute what is cheap.

In the early days of computing (say, up until the early 1970s) _everything_ was expensive. Thus you had entire buildings dedicated to one computer that a few dozen people could use at the same time as long as they were in the building and sitting in front of dedicated (and also shared) terminal screens.

Eventually resources became cheap enough that you could plop an entire computer in front of every user. Xerox started playing with this idea as early as 1973 and the PARC research lab developed the technological framework for personal computing that is still in use even today: <a href="http://en.wikipedia.org/wiki/Xerox_Alto">the networked, single user, graphical workstation</a>.

It took a while for commercial computers to reach this state, but by the early 1990s (only a bit more than fifteen years from research lab to Fortune 500, not bad) Windows PCs on local networks filled the halls of businesses all over the world running all of the office drone software that we have come to love.

Even with computing distributed to individual users, it still made sense to share things. Local networks usually had ways to share storage and sometimes compute cycles. Thus Carnegie Mellon University built that campus wide shared file system that people would use to share data and applications. If it had had a better user interface we might have called it the WWW. But it didn't, so we didn't.

It was this sort of system that Lamport was talking about in 1987 when he made that quip about distributed systems. At CMU, you could sit down at your personal workstation and command it to do something that it does every day of the week:
>% emacs

only to have it lock up. WTF? You ask yourself. Then in around 45 seconds you get this anonymous message on your screen:
>afs: Lost contact with file server 128.9.209.70

I actually changed the IP address there to protect the innocent. But you get the idea. What machine is this? You have no idea. But it's down and now your machine is toasted.

Of course, eventually local disk drives would get large enough that you would not have to store emacs in a server. You could store it locally. Hell, you could store it on 1/1000th of a $10 USB thumb drive.

But still, we share things. In the 90s local networks like the one at CMU turned into the Internet and the WWW (actually, the Internet had been around long before that, but no one cared before the advent of the Web). But once HTTP and HTML came on the scene network sharing of data on a large scale became so easy that everyone was doing it. Eventually it got to the point where you did not even have to set up the server yourself and we got Facebook and Twitter, the logical endpoint for all of this work.

Meanwhile, the cost of computing resources continued to plummet, to the point where most people who use computers seriously now had not just one or two, but more on the order of seven or eight computers in their lives (PC, laptop, phone, tablet, video game console, machines for both work and home, etc).

In this environment what computational resource is still expensive enough to share? The answer is management. Management of what? Well, it depends.

What users want to manage is their stuff. That is, they want to see the same music, photos, messages, e-mails (for old people) and documents no matter where they are and what computer they happen to be using. It's important, after all, to see the same Twitter or Facebook messages no matter where you are. 

Many web services provide this sort of functionality. Early on they did this by putting the user interface into the web browser and the data model on the server side. So you make your changes, they go into the server and then when you go somewhere else you can see your changes by looking at the web site again. But using web sites all the time is annoying and tedious. So some more modern services provide native UI on your computer and then move data back and forth to the server side transparently and in the background. Examples of services like this would be any IMAP-based mail service, iTunes Match or Spotify for music, and Dropbox for general files and other data.

It turns out that building the large server farms required to run these services is complicated and expensive. So what service providers want to manage is a way to manage this complexity in a way that lets them concentrate on building their service and not on how to structure a data center.

So when I think of "cloud services" what I think is of two things:

1. A user model where your data sticks with you even if you are using multiple machines from multiple places.

2. A set of mechanisms on the server side for managing and maintaining the centralized resources needed to provide the service in (1).

If you have been paying attention you may have noticed that the distributed system problem has snuck back into our discussion. Instead of a nice self-contained personal computer, you now have a box hooked up to the Internet and thus dependent on a lot of external infrastructure to continue working correctly. Say there was some file you wanted to edit, but you listened to some hype about the convenience of "cloud storage", and stored the file in the network rather than on a $10 USB drive in your pocket. The following obstacles may stand between you and your work:

1. A local network.

2. Your ISP.

3. The wide area Internet at large.

4. The server farm for the service that is holding your text messages.

5. The disk on the one anonymous shared machine in said server farm that holds the file that you want. (This is unfair, there are probably a few disks that have the file).

In each one of these layers is a computer that you know nothing about whose failure will thwart you. Instead of happily editing your file, your computer will just stare at you until it finally declares that the server that you didn't even know existed has disappeared. You will look to the sky and the spirit of Leslie Lamport and you will pound your desk and ask why, why, you stupidly expected the network to do this work when you could have just brought a $10 USB drive to work instead.

The lesson is that the hype surrounding cloud services can be very misleading. Rather than a friendly cloud that sits up in heaven instantly providing you with everything you need, I see something more like a bank of fog. You throw things out into the fog and they slowly disappear from sight, and you aren't an entirely sure where they've gone. Like the Fog in <a href="http://www.imdb.com/title/tt0080749/">that movie</a>, you should not trust this Fog. The Fog is not a fluffy friend that is out to help you out, it is a place where numerous potential enemies hide (data corruption! NSA snooping! millions of teenagers running password crackers!) and which you should keep at arm's length. Turn your back and monsters will leap out of it and eat your face, and your data. Always protect and back up what you send into the Fog, because it might not ever come back.

So, if the catch phrase for modern distributed application services is "to the Cloud!", I say bah and replace it in my head with "To the Fog!". I think it makes more sense that way.

