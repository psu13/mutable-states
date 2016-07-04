Title: Who are the Programmers
Date: 2015-11-12
Category: Computers
Author: psu

The 2015 Splash/OOPSLA conference was in Pittsburgh this year, so I took advantage of this fact to go see what the academics had to say about some aspects of what I do every day: program computers to do silly things. Even though I haven't been around academics since I got my PhD half a life ago they seem to be about the same. But like everyone else they carry tiny little computers with them everywhere now. Though they don't seem to know how to use them as well as everyone else.

OOPSLA is an old classic among the ACM conferences, having begun when Object Oriented Programming started to capture the imagination of the industry in the 80s. Surprisingly, there are still a lot of people in the world who are deeply interested in looking at the world through the lens of Smalltalk and systems like it. My overly pragmatic view was that surely people were over that by now, and had moved into the modern world of higher order interfaces, type systems and monads. But I guess not.

Under the name SPLASH the OOPSLA conference has expanded its focus into all manner of subjects ranging from the old classics (inheritance or prototypes?, what's a meta-class?) to more prosaic and industrial concerns (deploying Haskell at Facebook!, high level languages for science types!)

Several of the sessions I went to ended in me pondering the question: "who are the programmers anyway? And what do they do?" You would think that after 25 years of doing this work in one form or another I'd have some ideas about this. But the truth is that I never really thought about it. In fact, historically the front of my brain only really had two answers and neither one is all that useful:

1. Programmers are people who program computers.

	or

2. Let me get back to you on that after I write a whole book about it.

Luckily, the back of my brain happened to come up with an answer that I like the other night while I was at dinner with one of the better programmers I know. The summary of the thought is this:

>Programmers are people who can effectively visualize and manipulate the *dynamic* structure of computer programs.

But this is a fairly lofty and abstract way to put it. To make it more concrete I'm going to start with something fairly simple as a running example.

**Step 1: What Computer Programs Look Like**

I'm going to take a bit of a low level turn here, which isn't usually my style, but this has a nice payoff at the end. So let's talk about the 6502 CPU.

The 6502 CPU is a beloved machine from the past. From the late 70s until the introduction of the IBM PC in the early 1980s it powered most of earliest consumer computing products. The most famous of these, of course, were the Apple II and later the Commodore 64. But there were a few others too. Programming the 6502 is pretty easy.

First, there are three special pieces of memory called *registers*. They are called A, X and Y. These are special only because they are fast. You can use A to do simple arithmetic, and you use X and Y as "indexes" to address memory. But you don't have to know about that. Each register can hold a single value between 0 and 255 (or 0 and 0xff in hex).

Here is a simple program for the 6502. First we load the number 8 (also 8 in hex) into the X register:

	LDX #$08

LDX means "load X", #$08 is just a syntax for the literal value 8 in hex. I picked 8 at random. It has no great significance here. Next, we decrement X and then store that value in the memory location 30:

	1: DEX
	STX $30
 
The label "1" will be used later so we can loop back to that instruction. DEX means "decrement X" and "STX" means "Store X" (LD for load, ST for store).

Now we compare the value in X to the constant 1:

	CPX #$01

CPX means "compare X" (you get the idea now). The result of this comparison will be either 0, if X is equal to 1 or non-zero if X is not equal to 1. This result goes into a special place in the machine that stores all such results. Now we can branch based on the value in this special place:
	
	BNE 1
	STX $31
	BRK

This tells the machine to jump back to the memory location that the label 1 represents, but only if the result of the compare was not zero. If we don't branch we store X into memory location 31 (for no reason) and then hit the BRK instruction which tells the computer to stop. So what we have done is instruct the computer to do some simple math over and over again ("in a loop") until we tell it to stop.

The computer, of course, does not understand what these text instructions or labels are. It only understands binary code. What we'll do is use a program called an "assembler" to translate the simple text instructions into binary. So here is the whole program in text form:

	LDX #$08
	1: DEX
	STX $30
	CPX #$01
	BNE 1
	STX $31
	BRK
	
The binary form of these instructions looks like this (again in hex):

	a2 08 ca 8e 30 00 e0 01 d0 f8 8e 31 00 00

Each hex value here is one instruction plus some arguments. Don't worry too much about it.

**Step 2: Review**

We have written a simple program in a simple language. The program doesn't do much but it illustrates every static fact that you need to know about computer programs. There are constructs to load and store values. There are instructions for simple arithmetic. And most importantly you can use looping and conditionals (CPX, BNE) to express decision making and repetition. With these tools you can now write programs to do anything you want (for why, see <a href="http://mutable-states.com/turing-complete.html">this other article</a>).

What is also notable about this program is that it takes a fairly compact *static* form. It's just a few lines of text, and an even smaller amount of binary data. The whole thing can be represented as a fairly small number of bits. But, when you load it into the right kind of machine, you get a cascade of magic which you can capture and actually *see* the machine do just what you told it to.

**Step 3: Runtime**

At this point you might think I'm a bit crazy. How fantastic could a simple program that counts down from 8 be? Well, to see, first click on the link that follows and watch the animation:

> <a href="http://www.visual6502.org/JSSim/expert.html?loglevel=2&a=0000&d=a208ca8e3000e001d0f88e310000&steps=180">http://www.visual6502.org/JSSim/expert.html?loglevel=2&a=0000&d=a208ca8e3000e001d0f88e310000&steps=180</a>

What you are seeing on that page is a visualization of the actual binary code above running on what is effectively an actual 6502 computer. Ok, the 6502 is really the result of some software that some crrraaaazy people wrote in *javascript* that does a gate level simulation of the 6502 hardware. But really this is almost better than the real hardware.

The left side of the page is a micrograph of the actual circuits of the CPU:

> <a href="https://www.flickr.com/photos/79904144@N00/22352317834/in/dateposted-public/" title="chip"><img src="https://farm6.staticflickr.com/5646/22352317834_0bbeed581e.jpg" width="500" height="499" alt="chip"></a>

As the program runs you can watch the gates turn on and off. If you know enough about the hardware you can trace how the all of the data moves through the machine while executing your simple program.

On the top right is the "debugger", which shows you the contents of the machine's memory and provides controls for running the program step by step or all at once:

> <a data-flickr-embed="true"  href="https://www.flickr.com/photos/79904144@N00/22986185741/in/dateposted-public/" title="memory"><img src="https://farm1.staticflickr.com/573/22986185741_4bc5a2d57c.jpg" width="500" height="225" alt="memory"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

For this screen shot I had the machine stopped right after it had stored the value 1 into the memory location $30. You can also see the other 1 right next to it in location $31 from a previous run.

Finally, the lower right of the page is a log of everything that the CPU has done in the current session. That's kind of boring, so I won't bother with an image.

Anyway, I find this web page to be a mesmerizing work of almost-performance art. Truly a tour de force. But what does it have to do with answering my original question?

**Step 4: What's the Point?**

Here is the point. Programs have two forms. I would call them "phases", analogous to phases of matter, but I want to use the word "phase" for something else later in my life so I'm not going to do that. Let's stick with forms.

As we saw above, the simple form of the program is the *static* one. It's usually a piece of text or a large text file. At some point this form is translated into another static representation that the machine can understand. This is the application that you tap on to make your iPhone dance. Once the phone starts dancing, we encounter the second form of the program: the *dynamic* form. Here the small pieces of text that we looked at before can cause all manner of effects and magic to happen. Messages are sent, photos captured, payrolls calculated. In addition, and here is my point, all of those things that happen started as the same kind of idea in the mind of a programmer somewhere. The programmer had a though process like this:

1. Man, I do this task a lot... maybe I can figure out how to describe it to the machine.

2. Some amount of work and conceptual translation ensues.

3. A program is created which, when run, does something like what the programmer had in her head in step 1 which happens to also make people's lives better and more productive by taking a small amount of tedium out of the world.

So the answer to the question "Who are the Programmers" is sort of simple: programmers are the people who can translate things you want done into little pieces of text that do the right things in the machine when the final binary is executed. 

But the answer is sort of complicated too: in order to be good at programming, the key skill you need is to be able to look at a piece of program text and in some sense predict what the dynamic form of that program will do. Obviously our puny brains can't actually do something like the 6502 simulator above. But what programmers do is to build simpler models or simulations in their mind's eye and use these to efficiently structure and reason about their programs. The good ones get pretty good at this and can efficiently create pretty complicated systems that capture most of what they intended. They can also use these mental skills to fix and enhance the code that they have created in an efficient and systematic way. Perhaps more importantly, the better ones can also quickly absorb what *other people's*  code does, and fix and enhance that too, while staying true to its intended structure.

The very best ones can do this on a large scale and create large architectures that can be used by other programmers to make the creation of even more complicated systems possible. These wizards are doing multiple levels of model building and mental visualization. At the static level the programming interfaces they build need to be understandable to their clients and make for code that is pretty and efficient. At the dynamic level they have to be able to predict all the terrible things that people using their code might do, and make the runtime structures hold up under that stress. As you might imagine, this is very hard. I've never been good at it, not very many people are.

But those lofty heights should not concern you. Circling back, anyone who has had the idea to take some process and encapsulate it into a single button that does the right thing every time is already thinking like a programmer. They have captured whatever it is they wanted to do, freeze dried it into static program structures and then made sure to arrange things so that when the code is unleashed into the machine, its dynamic dance does exactly the right thing. Whether you do this in 6502 assembly language, BASIC, R, SQL, Haskell, Objective-C, Javascript, Swift or some special purpose language is at some level immaterial. The task is always the same, and the most interesting part is always the mental leap from the static text to the runtime magic.

**Extra Note:**

The 6502 assembler that I used for the example is here: <a href="http://skilldrick.github.io/easy6502/">http://skilldrick.github.io/easy6502/</a>. You'll also notice a program there that looks similar to the example program. I always liked tweaking other people's code more than writing my own.
