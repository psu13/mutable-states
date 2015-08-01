Title: The Inscrutable Tubes
Date: 2014-11-26
Category: Computers
Author: psu

Here is what a wise man once said about software:

> The complexity of software is an essential property, not an accidental one. Hence, descriptions of a software entity that abstract away its complexity often abstract away its essence. For three centuries, mathematics and the physical sciences made great strides by constructing simplified models of complex phenomena, deriving properties from the models, and verifying those properties by experiment. This paradigm worked because the complexities ignored in the models were not the essential properties of the phenomena. It does not work when the complexities are the essence. 

This man was Fred Brooks and he said this in the now classic article about the nature of software construction: <a href="http://worrydream.com/refs/Brooks-NoSilverBullet.pdf">*No Silver Bullet*</a>. You should stop reading this page now and go read that article. It is probably more useful than anything I could possibly write here.

Another not quite so wise man <a href="http://en.wikipedia.org/wiki/Series_of_tubes">once said this about the Internet</a>.

> And again, the Internet is not something that you just dump something on. It's not a big truck. It's a series of tubes. 

That was the late Senator Ted Stevens. At the time he was widely mocked for this statement. The Internet, all the dorks cried, is a fantastically complicated and interconnected system of hardware and software that moves terabytes of data from place to place on a daily basis. 

But here's the thing: it sort of *is* made of tubes. You put data in your tubes and sometime later your data falls out of someone else's tubes. In the middle there are a lot of tubes owned by various middlemen. The picture is not that far off.

If you break down the ways we structure large systems to fight their inherent complexity, you also end up with a picture that is not all that different from the one above of the Internet. Every long-time software person that I know of has a similar of way of thinking about or internally visualizing complicated systems, and it would not be entirely inaccurate to say this: it's all made of tubes. Where does this picture come from? Let us review.

Large software systems are put together by <a href="http://mutable-states.com/the-abstraction-distraction-part-1.html">combining small software systems</a>. Programming languages have long given us ways to build the small structures, usually as data types or higher level modules. In most systems that you would work with these days, any given module typically has three components that you need to keep track of:

1. A well-defined public programming interface, or API. 

2. The externally visible state of the module.

3. The internal representation of the sub-system the module implements, to the extent that its state may affect behavior.

When looked at this way, each module in a larger system is like its own little computer. A machine whose instruction set is defined by the high level API of the module.

If you wanted you could push this idea all the way up and down the various levels of our computing stack. And people have. Many  Internet servers these days are conceptually nothing more than software layers running on other software layers running on still more software layers that just *look* like hardware to the software above them. Everything is virtualized. But that's a subject for another time.

Ideally the behavior of the module would be very predictable. If the system implements some function called *foo* that takes (say) three blocks of data (x, y, z) as arguments what you would like is for all calls to foo(x, y, z) to act the same way if x, y and z are the same. What makes computers different from mathematics is that this is usually not the case. The problem, as Neo learned in the *Matrix*, has to do with state.

In a computer, state is any given configuration of the computer's memory. Computers are interesting to people specifically because they can store state. Here are states that you like to store in your computer:

1. That term paper you were writing.

2. Those songs that you bought off the Intertubes.

3. Whether or not your phone should remind you to do something at precisely 1:00pm tomorrow afternoon.

And so on.

The problem is that while computers would be useless without these kinds of states, the existence and overuse of state to implement the building blocks of computer systems inevitably leads to trouble. If you use state in the implementation of the function "foo" above, that means that when I call foo(x, y, z) *now* it may not do the same thing as when I call foo(x, y, z) *one microsecond from now*. This is why some large percentage of horrible bugs happen in the software systems that you use every day.

The eminent computer scientist John Backus figured this out in 1977 and made it the subject of his <a href="http://web.stanford.edu/class/cs242/readings/backus.pdf">Turing Award</a> lecture. That means it's a pretty important idea. So go read that paper. Here is a smart thing he said about the nature of state in large programs:

> The second world of conventional programming languages is the world of statements. The primary statement in that world is the assignment statement itself. All the other statements of the language exist in order to make it possible to perform a computation that must be based on this primitive construct: the assignment statement. 

Almost forty years after that paper was published, most working programmers are still in this second world. We both live in fear of, and in service to, the assignment statement. What we try to do is *encapsulate* the state into little caves, hiding in the lower level parts of our APIs, hoping that no one can sneak in and steal it while we are not looking. Thus, if you stare at a high level diagram of some big piece of software you'll see the same sort of picture.

1. A lot of hierarchy.

2. A lot of little components, all with their own state.

3. A lot of communication channels between components and between the various layers of hierarchy.

Does this seem familiar? Large software systems are like a ... I don't know ... *network* (?) of virtual machines all talking to each other via a complicated system of interconnects.

A huge amount of time in software development turns out to be spent in building complicated strategies to do the following sort of thing:

Component A puts data into a tube to pass it through a complicated set of component-to-component tubes and layer-to-layer tubes so that it can travel up and down and around eventually fall out of a tube into Component B. Then Component B paints the data with its marker, and sends back again.

Backus also made this observation, but at a level of thought that was closer to the machine. In addition, he noted that much of what we pass back and forth is not actually the data we want to work on, the *name* of the data we want to work on:

> Ironically, a large part of the traffic in the bottleneck is not useful data but merely names of data, as well as operations and data used only to compute such names. Before a word can be sent through the tube its address must be in the CPU; hence it must either be sent through the tube from the store or be generated by some CPU operation. If the address is sent from the store, then its address must either have been sent from the store or generated in the CPU, and so on. If, on the other hand, the address is generated in the CPU, it must be generated either by a fixed rule (e.g., "add 1 to the program counter") or by an instruction that was sent through the tube, in which case its address must have been sent ... and so on. 

Note how Backus already realized that computers were made of tubes in 1977.

Anyway, for these data trips to work out, everything along the way has to be *just right*. As a programmer, you have to make sure that each segment of the journey will:

1. Correctly pass the data to the next segment.

2. Not somehow corrupt the data along the way because of some bug.

The number of ways that one of these two simple things can go wrong in a large system is simply staggering. This is because like the two components on either end of the trip, everything in the middle has state too, and every little bit of state has the potential to make your trip go wrong.

So here's something that happens a lot. Most large applications have a phased nature. For example, many interactive editing applications like Pages, or Keynote run in a loop that's something like this:

1. Take input from the user (mouse, touch, keyboard, etc)

2. Translate input into a command to update the document.

3. Update the document.

4. Inform everyone (that is, all the other software pieces that care) how the document has been updated.

5. Let the user see what the new version of the document looks like.

This is the classic <a href="http://mutable-states.com/the-abstraction-distraction-part-1.html">MVC</a> application loop.

What makes this structure work is that it is understood that no part of the system moves to the next phase of the loop until *everyone* is ready. If you have some components in phase (4) and some already running ahead in phase (5), you will be sad because step (4) has not yet correctly computed what you should display. The question that comes up is: how do you enforce this lock step nature on the world?

In general the answer is you don't. For smaller systems the invariants you need tend to hold by themselves. For larger systems we tend to do the following dodgy thing: you make the various pieces of the system register their interest in the other pieces of the system that they depend on, and you depend on the programmer to correctly reason out which pieces need to depend on which other ones. You can imagine how well this works. This is why when you use your favorite software you will often need to beat it like a stupid child until shows the edit that you know you just made. Some programmer forgot to declare the correct set of interests.

In the above view of the world, your software becomes a tangled nest of little boxes stacked on top of each other and connected together with various tubes. The poor programmer is always stuck trying to find pathways through the nest of layers and boxes and tubes so that the she can push the right state from one part of the world to another. Making this even harder is that often the boxes and layers and tubes are not permanent structures, but come and go dynamically as the user does different things. I don't know how many times I've pushed something into the tubes only to find out that the final tube/box that I wanted to get to had already disappeared by the time my message got there, thus destroying my world.

So, what is to be done about this? If I had the answer I'd probably be sharing my brilliance in a Turing Award lecture. I don't think that's going to happen, but in my experience there are a few things you can try to do to mitigate the pain.

1. When possible, avoid state, even hidden state. Since no one has figured out how to make stateless documents, you clearly need *some* state. But most systems have too much. The best example of bad state is the useless cache built to solve a performance problem that doesn't exist. Every cache is an invalidation bug waiting to happen.

2. When possible, avoid object (1) references. Document objects holding pointers to other document objects is a sure way to lose. Every time. Obviously you need *some* way for objects to refer to each other. I'm just saying that a programming language level reference is usually the wrong thing (although the more new fangled languages may fix this).

3. When possible, avoid hierarchy. The relational database people had this right: hierarchy that you do not need tends to saddle you with a lot of useless invariants that you must maintain for no reason. A lot of hierarchy makes your tube trips longer, because you need to pass through a tube every time to change levels.
	
	Examples of hierarchy that I don't like: deep inheritance trees, long chains of programmer-induced containers, anything involving unmanaged weak back-pointers to something, deep file system hierarchies in code repositories, mail folders. One of the things Google mail really got right was not using folders.

4. Whenever possible, enforce strict phasing. See above.

What I imagine is that over time we'll be able to add a management layer to the standard application architecture (2) that sits somewhere between the model and the controller. Let's call this manager the TubeConnectorManagerTransactionTubeController. What this manager would do is mediate all relationships between objects in the model and objects in the other layers. No model object would ever be explicitly accessible. In addition it would manage and keep track of which operations are allowed to run in which phases of the application execution loop. If requests come in that are out of phase then depending on the situation you could imagine the system just crashing immediately or perhaps queueing the operation until it's safe to run.

Generally I favor crashing immediately, because that forces someone to fix the bug. Trying to be friendly and carry on tends to result in someone being forced to backtrack to the original bug via some other anomaly that is reported as a bug. This is usually hellish and painful. It's always better to crash on the first thing you find that's wrong, if you can get away with it.

The TubeManager replaces at least part of the pile of tubes above with a single black box that is responsible for holding the tubes so you don't have to see them. Even if I knew how to build it, I don't think that it would be a complete solution (3). But I think it would help, assuming that it wasn't a buggy mess like all software is. 

The complete solution would probably be some giant magic transformational box that takes the existing document and somehow transforms it into the "document plus one edit" along with an updated display for the user while not engaging in any stateful activity in between *and* performing better than all of the stacks of code we have now. I'm not sure how you do this, but I bet it involves  <a href="http://homepages.inf.ed.ac.uk/wadler/topics/monads.html">monads</a>.

**Notes**:

1. When I say object here I mean object in a more generic sense. I will not make you suffer through all of that standard OO-design bullshit. That stuff is dumb.

2. My idea of the standard application architecture is the one defined by the AppKit "document oriented application" idea. Not all apps fall under this umbrella. But most of the interesting ones do.

3. Someone is sure to tell me that the web application people, with their enforced separation between server-side model and client-side view have somehow already implemented this idea. But I'm skeptical. I mean, a lot of those people are still using PHP.


