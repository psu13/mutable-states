Title: The Abstraction Distraction, Part 1.
Date: 2008-07-28
Category: Computers
Author: psu

<em>Abstraction</em> is the activity that lies at the core of much of computer science, and computer hardware and software engineering. Understanding what the word means is thus at the core of understanding both how and why computing systems are are put together and evolve the way they do. It is also a large part of the key to understanding the mind of the engineer, because more than anything an enthusiasm for clever and aesthetically pleasing abstractions is what drives people to become engineers in the first place.

So what is abstraction anyway? In my mind the you can boil it down to the following overly simple definition: Abstraction is the act of giving a short and easy to remember name to something that is long and complicated. By doing this, you absolve yourself of needing to remember the long and complicated stuff.

The Internet provides a convenient example. Suppose you want to explain to people what "Abstraction" is. You could do a lot of research and thinking and then write several hundred words down on a piece of paper. Then, when anyone asks you could read the paper to them. But this can get long and tedious. So, instead, what you could do is post your several hundred words on the Internet in a special place and then just hand out this:

<a href="http://en.wikipedia.org/wiki/Abstraction">http://en.wikipedia.org/wiki/Abstraction</a>

or maybe

<a href="../../../../index2735.html?p=1081">http://tleaves.com/?p=1081</a>

Then people can just keep the link around and read the words by themselves. This, I claim, is abstraction at its core. We have taken something long and complicated and turned it into a single easy to remember name so we don't have to think about the other stuff anymore.

If you spend any time around computers, you see abstraction everywhere. Building a circuit to perform arithmetic on 32 bit fixed point numbers is complicated and hard. So we build the circuit and then hide it behind a few dozen bit patterns that represent instructions for load, store, add, multiply, and so on. Bit patterns are hard for humans to remember, so we further encode them as assembly language mnemonics. You will soon find yourself writing the same sequences of assembly language over and over again, so we package these up as a set of libraries and functions that all applications can use and call that an "operating system".

Operating systems further abstract the physical hardware that might be connected to a computer so as to make it more easily shareable by multiple applications. The most obvious example here is virtual memory. Most people think of virtual memory as "paging", but it is really something deeper. All physical hardware defines a fixed set of names at which we can store program data. These are "physical addresses". If application programs were forced to always use physical addresses they would constantly have to argue with each other over where they could be loaded and which areas of memory were free for use or not. This is tedious and error prone.

Virtual memory allows every program to pretend that it has some fixed set of addresses that start at zero and go up to whatever. Further, they can pretend that they have this whole address space <em>to themselves</em>. The operating system then takes care of making sure that programs don't end up using the same physical memory or otherwise destroying each other. Again, we simplify high level code by introducing an abstraction layer that essentially does name translation.

The higher levels of software applications also have their own collections of abstractions. Some are important enough to have special names. I work primarily in desktop software with a fancy graphical interface. These applications tend to be constructed out of three abstractions that like to think of each other as black boxes, although it never works out.

1. Model: how the application stores the basic units of the user's data. In a text editor, this would be text and layout. In a video game, this would be the models and assets that the engine uses to represent the state of the game. You get the idea.

2. View: how the application displays data for the user. This is the visible part of the user interface.

3. Controller: how the application responds to user commands. This is the less visible part of the user interface. It determines which sequences of actions are legal in a user interface and thus what workflows it can support. A good rule of thumb would be to say that the view side draws the button and the controller defines what the button <em>does</em> to the model.

Thinking about applications in this way allows software engineers to not have to consider every single possible detail whenever they sit down to solve some problem or fix some bug. First, you can isolate it to the black box you need to work in. Then you can work on only the concerns that are relevant to that box.

Of course, abstraction boundaries are not perfect, and the details of the boxes tend to leak out, which is what makes fixing software complicated. Still, it is amazing the extent to which people that work on different parts of the system can be completely isolated from each other. The model guy might understand hundreds of details about how the application encodes the various data on disk, but know nothing about how it is later rendered on the screen for the shiny demos. Similarly, the graphics guy just knows how to write code to draw. The stuff he needs to draw is always just there, because the model guy has taken care of it for him. This isolation can be strong enough that people can work for years on applications and not even know what the basic feature set is. I've seen it.

The essential service that abstractions provide is that they allow you to be <em>lazy</em>. Rather than remember how physical memory is managed in a machine you just ask the operating system to take care of you. Similarly, instead of knowing how you write the blue and red widgets to disk, you just call into some API defined by someone else on your team and then go scream at them when the code does not work and starts to show up on crashlogs in the bugs you have been given to fix.

This capacity for increasing laziness is a wondrous thing. But, it can also get us into trouble. We can be blinded by the power of our wonderful abstractions and lose track of the problems we had set out to solve in the first place. Worse, we can surround ourselves with abstractions and, assuming they will solve all our problems, not really think about the problems at all and thus never really solve them. As incredible as it may seem, I am writing here that it is possible to be <em>too lazy</em>.

But, we'll leave those thoughts for the second part of this long winded pontification, which will explain the <em>Distraction</em> part of the Abstraction Distraction.

