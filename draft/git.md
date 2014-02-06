So that was a bit of a leap. But try and stick with me. Recall that the file system is how the operating system (and the user with it) organize the disk of your computer so that you can do two things:

1. Find a place to store the bits that you just created.

2. Organize all these places so you can find them later.

File systems achieve this goal by layering a hierarchical storage system on to the disk. So you can make two kinds of named entities in a file system:

1. Files: these store bits directly. Actually that's a lie. The bits are really stored through a bunch of indirections through various indexes before you get to the actual blocks that have just the raw bits. But that's another article.

2. Directories: these store a table that maps names to either files or directories. This is also sort of a lie like the other item is a lie. But again, that's another article.

Back in the dark ages of computing, files were a pretty mysterious thing to new users. On the one hand, they promise something concrete: this is the _file_, like maybe a file folder file, that contains your address book list, or your grades, or your term paper. On the other hand, they are nothing more than a short name (8.3 anyone?) that is only meaningful if you feed it to the right program.

They claim to exist as a real thing, yet they are invisible, colorless, odorless, and they can disappear in two stray keystrokes without even feeling remorse.

But, as computing system evolved, we learned to give the file system a friendlier face. User interface evolved that allowed users to visualize and manipulate the tree structure. We started calling files things like "documents" or "projects" to better connect them with what users were using them for. Finally, users got used to them. Most users picking up computers these days already have some vague notion of what a file is and how to keep from destroying them. So, through decades of trial and error, users came to understand and feel more comfortable with this strange abstract idea.

If groups of people have to share files, this whole system gets more complicated. Say you open create a file A and then save it to the shared spot. Then your friend opens up file A and makes some changes. Then you open the file and make your own changes. Then you both save to the shared spot at the same time. Whose changes win?

Teams that develop software have long used various engines to deal with conflicts like this. They generally involve a central repository server that stores both the shared files and their edit histories. At any given point you can _checkout_ a snapshot of the world that makes a copy of the most recent version of every file in your local file system. You then make changes and try to check them in. If the there are conflicting changes you need to resolve these automatically or by hand and then try again.

Version control systems add another layer of indirection on to the idea of the file system. Now the file system you _see_ is just a snapshot in time of the real shared artifact. You have to keep it in your head that you are working on a copy and you have to remember to send the changes back to the central server in order for everyone else to see it.

So, just as we got comfortable with the spooky idea of files, in come systems where the _file_ is now just a standin for something more complicated.

But, even this has annoying limitations. Versioning systems that use a snapshot checkout model limit you in various ways. It's hard to work on multiple lines of development at the same time (you need one snapshot per line). They also make it hard to make local snapshots of your work since if you checkin from your sandbox the changes go back to the central repository. The model in use here is

1. Checkout

2. Make local changes.

3. Checkin, making a new history snapshot

The only tools you get in step 2 are whatever is in your file system. The communication between the server and the client is all in terms of textual changes to some set of files. This is important.

These issues have lead to a new class of versioning systems called "distributed" version control systems. This is an odd name since all shared repositories are in some sense "distributed" but in this context what it means is that rather than checkout a snapshot into your sandbox what you get instead is a copy of the entire central repo. You can then work in your own repository as you wish: make checkouts, checkin intermediate changes, work on multiple lines of code at once, and so on. When your changes are done you package them up and send them back to be merged into the central repo.

DVC systems, as exemplified by the psychotically useful tool called <a href="http://git-scm.com">"git"</a> tend to work with a subtly different model than traditional systems. You tend to think of them as tools for manipulating the actual history graph of the repository rather than just the changes to the individual files themselves. This is a natural extension of the model since rather than working on a local snapshot you are working on a local *repository* with its own unique history. The goal is then to figure out how this local history and the history in the server should be related.

So here is what you do:

1. Copy the repository.

2. Checkout files from your local repo to do work.

3. Checkin changes locally until you are happy.

4. Merge local history with remote history in some way to clean up your changes.

5. Push the merged changes to the server.

6. Copy history from the server.

What's happened here is that we've added yet another abstraction layer (the local repository) into the system. So now instead of two levels of thinking you have to keep track of three. But for the 20 years before git most developers had been programmed by their tools to think in the two level model. This means that introducing new tools, even to a  technically sophisticated audience, can be really hard. Rather than using the new tools in the new models, they will first try and use it in away that mirrors the *old* model. But this tends to just lead to more confusion because the tools just don't match.

Worse, you might try to use some version control GUI to interact with git. But this will be a disaster unless the GUI is set up to match git's model, which I bet it won't be.
