Title: This is Your Brain on Software
Date: 2013-12-27
Category: Computers
Author: psu

In his new book, <a href="https://itun.es/us/I7YDH.l">How Music Works</a>, David Byrne has a lot to say on the effects of digital technologies on how music is created, recorded, distributed and sold. One of the keener insights he has is this one, about software that supports musical composition:

>Though software is promoted as being an unbiased tool that helps us do anything we want, all software has inherent biases that make working one way easier than another.

This sentence made me very happy because it illustrates an understanding of what software does to your brain. The biases that he is talking about here have a very specific origin and unavoidable effects on what software does or does not allow you to do with the "things" that you use it to manipulate. As I have discussed previously, it's all about <a href="http://mutable-states.com/software-models-and-hello-world.html">models</a>.

Recall that models are the structures that we software engineers use to organize the otherwise formless memory of the computer. The goal is to match the model to the task that the software is intended to perform. Some examples:

1. Music composition and editing software tends to represent your project as a series of _tracks_ that are connected together in time. 

2. Text editing software represents the text of the document, usually, as a long stream of characters, perhaps broken up into sections.

3. Image editing software represents the image as a stack of layers each made up of RGBA pixels. Each layer some piece of the final image, and the layers are then combined in various pre-defined ways to form the final image which you can see on the screen or print.

I am of course leaving out a lot of detail here, but even at this high level these models have already injected assumptions about the way you work with the software. I don't know much about music production, so I'll leave that example alone. But consider the other two. The simple text editor assumes that it will primarily be working with relatively small amounts of linear text. If the user would like to edit huge texts (maybe millions of characters long) or maybe text that has some structure (like an outline) the simple linear representation will have problems.

Similarly, our image editor is tied down by its pixel-based representation. This means that while it will work well for pixel-based images, documents that require resolution-indepedence, or path-based structures, or perhaps text that you don't want to pre-rasterize will be annoying to represent and might require strange gyrations to fit into the layers of pixels model.

These simple examples illustrate a classic conundrum in software design:

> On the one hand, the model is what you must implement first. On the other hand, the model can greatly constrain _what_ features and user interface you can implement later, so it's risky to implement it first.

Software idealists and/or utopians will object that only an idiot would make the user interface be tightly constrained by the model and that one should be using a loosely coupled application architecture based on the gold standard that is "MVC" (<a href="http://en.wikipedia.org/wiki/Model–view–controller">look it up</a>). Do not to be fooled by these people. They probably never shipped anything. The model is everything and if you get it wrong you will be fighting that mistake for your entire life.

When software becomes widely used the models that the software implements also have a profound effect on how _users_ end up thinking about the tasks that they perform with the software. This tends to run in stages. Early software for a task will probably ape some pre-existing non-automated workflow. Then, as users and engineers gain experience there might be some radical rethinking of how to break down a task that would seem completely confusing and bizarre to users just starting out. There are lots of example of this:

1. Video (or music) editing software that lets you splice anywhere you want in a track without needing to "play the tape" to that spot. This was so new and wacky that they gave it a completely non-sensical name when the idea was first implemented: non-linear editing. What they meant was random access editing, but what do you expect from a bunch of artists.

2. I tried to come up with an example related to text editors, but there aren't any. Text editors have not materially evolved in any way since 1984. One long stream of text. Perhaps a rumination for another time.

3. <a href="http://tleaves.com/wp-archive/2005/10/17/adjustment-layers/index.html">Adjustment layers</a> in Photoshop define a new kind of layer that contains no pixels. Rather, it just contains instructions about how to take the pixels underneath them and transform them in some way to make a new set of pixels. This transform is editable, so you can make non-destructive adjustments to your images. Here Photoshop takes a wild leap out of its darkroom-like image manipulation model and into the realm of "almost programming". To the uninitiated adjustments layers can seem magic and spooky.

So what we see is this: on the one hand, the model the software uses defines its feature set. On the other hand, after years of using your software users build some understanding of your models in their brains, and this drives both their use of the tools and their expectations for how the tools will evolve. Changing these things too severely causes a lot of confusion and anger.

This can even happen to software developers themselves. To see how, we'll take a ludicrous digression into one of my favorite toolsets as a software guy: the file system and version control.

Recall that the file system is how the operating system (and the user with it) organize the disk of the computer so that you can do two things:

1. Find a place to store the bits that you just created.

2. Organize all these places so you can find them later.

File systems achieve this goal by layering a hierarchical storage system on to the disk. So you can make two kinds of named entities in a file system:

1. Files: these store bits directly. Actually that's a lie. The bits are really stored through a bunch of indirections through various indexes before you get to the actual blocks that have just the raw bits. But that's another article.

2. Directories: these store a table that maps names to either files or directories. This is also sort of a lie like the other item is a lie. But again, that's another article.

Back in the dark ages of computing, files were a pretty mysterious thing to new users. On the one hand, they promise something concrete: this is the _file_, like maybe a file folder file, that contains your address book list, or your grades, or your term paper. On the other hand, they are nothing more than a short name (8.3 anyone?) that is only meaningful if you feed it to the right program. They claim to exist as a real thing, yet they are invisible, colorless, odorless, and they can disappear in two stray keystrokes without even feeling remorse.

As computing systems evolved, they tried to give the file system a friendlier face. User interfaces allowed users to visualize and manipulate the tree structure. We started calling files things like "documents" or "projects" to better connect them with what users were using them for. Finally, users got used to them. Most users picking up computers these days already have some vague notion of what a file is and how to keep from destroying them. So, through decades of trial and error, users came to understand and feel more comfortable with this strange abstract idea.

If groups of people have to share files, this gets more complicated. Say you open create a file A and then save it to the shared spot. Then your friend opens up file A and makes some changes. Then you open the file and make your own changes. Then you both save to the shared spot at the same time. Whose changes win?

Teams that develop software have long used various tools to deal with conflicts like this. They generally involve a central repository server that stores both the shared files and their edit histories. At any given point you can _checkout_ a snapshot of the world that makes a copy of the most recent version of every file in your local file system. You then make changes and try to check them in. If the there are conflicting changes you need to resolve these automatically or by hand and then try again.

Version control systems add another layer of indirection on to the idea of the file system. Now the file system you _see_ is just a snapshot in time of the real shared artifact. You have to keep it in your head that you are working on a copy and you have to remember to send the changes back to the central server in order for everyone else to see it.

So, just as we got comfortable with the spooky idea of files, in some systems where the _file_ is now just a proxy for something more complicated.

But, even this has annoying limitations. Versioning systems that use a simple checkout model limit you in various ways. It's hard to work on multiple lines of development at the same time (you need one checkout per line). They also make it hard to make local snapshots of your work since if you checkin from your sandbox the changes go back to the central repository. The model in use here is this:

1. Checkout

2. Make local changes.

3. Checkin, making a new history snapshot

The only tools you get in step 2 are whatever is in your file system. The communication between the server and the client is all in terms of textual changes to some set of files. This is important.

These issues have lead to a new class of versioning systems called "distributed" version control systems. This is an odd name since all shared repositories are in some sense "distributed" but in this context what it means is that rather than checkout a snapshot into your sandbox what you get instead is a copy of the entire central repo. You can then work in your own repository as you wish: make checkouts, checkin intermediate changes, work on multiple lines of code at once, and so on. When your changes are done you package them up and send them back to be merged into the central repo.

DVC systems, as exemplified by a psychotically useful tool called <a href="http://git-scm.com">"git"</a> tend to work with a slightly different model than traditional systems. You tend to think of them as tools for manipulating the actual history graph of the repository rather than just the changes to the individual files themselves. This is a natural extension of the snapshot model since rather than working on a local snapshot you are working on a local *repository* with its own unique history. The goal is then to figure out how this local history and the history in the server should be related.

So here is what you do:

1. Copy the repository.

2. Checkout files from your local repo to do work.

3. Checkin changes locally until you are happy.

4. Merge local history with remote history in some way to clean up your changes.

5. Push the merged changes to the server.

6. Copy history from the server.

What's happened here is that we've added yet another abstraction layer (the local repository) into the system. So now instead of two levels of thinking you have to keep track of three. But for the 20 years before git most developers had been programmed by their tools to think in the two level model. So what you observe is that even though the third level is there, people don't use it. They go on using the DVC as if it's a more traditional tool. In the best case they gain nothing for their trouble. In the worst case they get confused and angry when the models don't match up.

Thus, introducing new tools, even to a  technically sophisticated audience, can be really hard. Their brains, programmed by years of experience with the old models, resist change and get grumpy. Developers had just gotten used to managing files when they had to come to grips with sharing and versioning. Then just when they were used to centralized versioning, a new tool comes down the pike that throws another layer of confusion in their way.

In the end, this is how I imagine what your brain looks like on software: I see a blank canvas on to which a picture of the software's model slowly materializes, like a black and white picture in a tray of developer (I wonder how many people will understand that reference). Then, just as the picture solidifies, the software changes and you are a blank slate again.

You can take comfort from this story. The next time you are pissed that some piece of software that you used has changed in some inscrutable way, don't feel too bad. It's probably happening every day to the very same people who wrote the software that just made you angry. So they are suffering too.

