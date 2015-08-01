Title: What Computers Do
Date: 2009-10-22
Category: Computers
Author: psu

Every once in a while someone who I don't know will find out that I work with computers. Often when this happens they get a look on their face like they have just found a great free source of technical support. I try to quickly end any such misconceptions. I just program the things, after all, I don't really know how to <em>use</em> them. At times though I do find myself daydreaming about the true nature of the computer as a device. We know that at the surface the computer is a tool that helps us <em>get things done</em> that we didn't used to be able to do as easily or as efficiently. Things like get directions, or process our photographs, or compose long pieces of text for total strangers around the world to read. That's not the level of inquiry that I'm interested in here.

I'm more interested in the following question: if you had to describe in a single sentence what computers do or how they work, what would you say?<br />
<span id="more-2308"></span>

My answer to this would be: a computer is a machine that stores and manipulates abstract symbols, or languages, that represent real things that you or I are interested in. A second way I might put this is: a computer is a universal recursive name translation machine.

To see how I arrive that this pretentious and esoteric turn of phrase, let's review how computers work. Here's a pretty good picture:

<img src="http://kvdpsu.org/cpu.png"><br />

In its simplest form a computer is a machine that loads instructions from some memory, executes these instructions, and then writes results back into the memory. This immediately brings up the question: what is in the memory? How is it stored? What kinds of objects can we store and retrieve? In most modern computers, the answer is that you store <em>bits</em>. We all know that you can store bits in &#8220;main memory&#8221;, or on the disk, or more recently in other media like DVDs or flash cards. Exactly how a bit is physically manifested varies. Therefore, we software people think about this in a more <a href="http://mutable-states.com/the-abstraction-distraction-part-1.html">abstract way</a> and say that a bit is a place that you can store either a value representing a &#8220;1&#8243; or a value representing a &#8220;0&#8243;. Notice how we have already started to build a language. The memory in a computer does not really contain anything that looks like the digit &#8220;1&#8243;. But we think of it that way. So now we have gone from talking about an entity that probably has a fairly complicated physical construction to something clean and simple. Just ones and zeros.

In order to effectively store and retrieve bits from a memory we need a way to address them. That is, we need a way to talk about where they are in the memory. From this need comes the notion of an <em>address space</em>. Generally computers are built to be able to efficiently work with values made up of some number of bits all packaged together into an aggregate value. When you hear people talk about &#8220;8 bit&#8221; computers vs. &#8220;32 bit&#8221; computers this is generally what they mean. They mean the hardware has been built to be able to push around packets, or &#8220;words&#8221;, that are 8, 16, 32, or 64 bits wide. There have been other oddball sizes too in the past, like the 36 bit DEC machines, or the CDC machine that used 60 bit words. But these days since there is only one architecture that matters (just kidding!) the main values are 32 or 64. In addition to being able to fetch, say, 32 bit values, a 32 bit computer can also be easily programmed to perform arithmetic on these values. That is, the hardware itself supports instructions for doing simple, (and not so simple) math on integers up to 32 bits wide.

With this background, we can talk about address spaces. An address space is simply what you get when you put together all of the possible bit strings that a computer can generate and use each one to name a particular location in memory. So, if your computer deals with 32 bit numbers, you can usually use each one of those numbers to address a unique location in memory. If you write down all the numbers you can represent with 32 bits you get 2^32-1 which is around 4 billion addresses. By convention most modern memory systems lets you store a single 8 bit value at each address in the machine. This is why your laptop maxes out at around 4GB of system memory. Of course, disks and such are much larger than this. But that's another article.

Now we have enough information to go through one step in a computer's life. Assume we have the CPU and the memory hooked up. Assume also that some being of greater intelligence has loaded the memory with a bunch of instructions. Finally assume that the CPU has two pieces of internal memory. One stores the address of the next instruction to be executed. The other stores the result of the last instruction that you executed, if it generated a result. Here's what the computer does:

1. Load the address of the next instruction from the first internal memory slot.

2. Ask the memory system for the instruction at that address.

3. Execute the instruction, storing the result in the second internal memory.

4. Store the result back into memory at a location specified by the instruction that we just executed.

In the old lingo, we used to call the first internal memory slot the &#8220;PC&#8221; or Program Counter. The second internal memory might have been called an accumulator, since it accumulates the results of our arithmetic. These days these things are all just called registers. And typical computers have a few dozen of them instead of just a few.

Now, you  might ask, what kinds of instructions am I talking about here? A typical computer has a few dozen instructions that can do things like

1. Load a value from a location in memory into a register.

2. Store a value from a register to a location in memory.

3. Perform simple arithmetic on loaded values.

4. Jump to a new location in  memory and start executing the instructions stored there.

5. Conditionally jump to a new location in memory based on the value in a register. For example, only jump to location 10 if the value in a register is zero.

It turns out that these five things are, essentially, all that is needed to build all of the computing infrastructure in use today. Real hardware is, of course, much more capable than this. But it's reassuring to know that at the bottom of it all, this is all you need. This is because what computers excel at is providing you with a basic set of building blocks and letting you combine and layer the piece into an ever more complicated edifice. Before you know it you are taking a machine that basically only knows arithmetic and using it to render the next Pixar film. It's a miracle.

How does this miracle happen? It happens because you can represent everything using bits. Most importantly, the instructions that the computer executes and the addresses provided to those instructions are also represented using bits. Therefore, the <em>machine itself</em> can process and generate instructions that it will then turn around and execute. This is the fundamental meta-recursion that makes the entire modern computer industry possible. We can write programs that when executed, generate programs.

As one final example of how computers are constantly immersed in self-referential confusion, I would now like to discuss the notion of <em>virtual memory</em>. The original virtual memory systems were motivated by the fact that you wanted to be able to write programs that operated on more data than could be stored in the main memory of the machine at once. Therefore, people built a two level memory. The first level was small and fast. The second level was large and slow. The virtual memory system would then automatically transfer data from the small memory to the large one and back again as the need arose. We do this by taking the addresses that the CPU generates and doing a bit of computation with them before feeding them to the memory system. This second box remembers whether we actually have the data at that address in the fast memory or not and manages the transfer of the data if required. The interesting thing, to me, about virtual memory is the management of the address space.

Recall the main processing loop of every program above. First we generate an address at which to load the next instruction (and/or data). Then we ask the memory system for what is stored at this address. Suppose we put another box between the CPU and the memory system:

<img src="http://kvdpsu.org/vm.png"><br />

Every time the CPU generates an address, it goes first to this other box which then asks the memory system for the data. What this second box does is keep a table of memory addresses that the CPU has generated. Next to each address in this table is another address. When the CPU hands this second box an address, the second box looks it up in the table, finds the second address, and uses it instead to load data from the main memory. We call this <em>address translation</em>. The address that the CPU generates is a <em>virtual address</em> and the address that this mystery box stores is called the <em>physical</em> address. We call this mystery box the address translation unit, or more generically the memory management unit or MMU.

It might be the case that we have not yet mapped the virtual address to any physical address. In this case we pick a spot in the &#8220;real&#8221; memory to put the address and create a new entry in the table. It might also be the case that the smaller physical memory is full, in which case we have to pick some other entry in the table to throw away to make room. When the entry is removed from the table we have to save the data to the slow memory for safe keeping, and reload it if we need it again. The MMU, with the help of the operating system, manages these low level details. From the CPU's point of view, it is looking at a simple linear address space, even though we have really cut it up into little pieces.

While virtual memory was originally developed to deal with address spaces that were much larger than a machine could physically provide, I don't think this is its most interesting application anymore. For most users and most programs physical memories are plently large these days. It's easy to buy a computer with 4GB of system memory.  The real importance of the MMU lies in the fact that it allows the CPU to use addresses do not really exist in our reality. They are a figment of the computer's imagination. It's as if everything in the machine has a forwarding address.

You might ask, why is this important? It's important because it is what allows you to run your Web Browser and Photoshop at the same time without the two programs interfering with one another. Operating systems use address translation to provide the <em>illusion</em> that every program is running on a mystical computer whose memory starts at address zero and ends at address 4 billion (or whatever). It doesn't matter where the data <em>really is</em>, the MMU and the OS are keeping track.

It turns out that this is a facility of remarkable convenience.  Before virtual memory, you had to constantly worry if the memory you wanted to use for your program was already in use and figure out how to move it around so that you could get your work done. With the address translation system around, you just load the program at address &#8220;zero&#8221; and go. Not only does the operating system keep track of where the data really is, it also makes sure that your program can't accidentally end up loading or storing data that it does not own. It can only see what the MMU and the OS let it see. So, in general, when Firefox crashes, it can only destroy things that were in its address space, and therefore Photoshop will keep happily humming along.

Addressing memory is at the core of how computers operate. You can't do anything in a computer without fetching it from or writing it back to memory at some point. Therefore, given how virtual memory works you can now really think of a computer as a machine that spends much of its time translating the name of one thing (the virtual address) into a completely different name for something else (the physical address). Hence, I return to the more pretencious and abstract statment form the beginning of this article:

A computer is a universal recursive name translation machine.

In fact, there is more truth to this than you  might imagine. Even outside the relatively esoteric and abstract land of address translation, almost all software can really be thought of as just a fancy translation engine. But that is a subject for another time.

<b>Note</b>

If you want a more detailed yet more understandable version of how this works, go read <a href="../../../../2006/06/19/the-soul-of-a-new-machine/index.html"><em>The Soul of a New Machine</em></a>. Really. You'll be glad you did.

