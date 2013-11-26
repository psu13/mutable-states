Title: Software Models and Hello World
Date: 2013-11-25
Category: Computers
Author: psu

I was at home for Christmas one year reading the New York Times on my laptop as we do, when my brother asked a random and off-hand question. He said "If all a computer can do is store zeros and ones, how does it end up drawing text and pictures on that screen?" This turns out to be a question that is impossible to answer in a short sentence.

Computers are strange machines. They take electrical signals that have an actual reality to them and use magic to turn them into what amounts to an elaborate fiction. Then they use similar magic to turn that fiction back into something your brain thinks is real ("text" on a "page").

What is this magic that they do? Well, the magic is software. But that's not an answer. That's just another question. What does the software do? Lacking a better word to describe it, I will call it making "models", because when we write the software that's the word we use.

Computers store information in little packets of bits. Each bit represents either the number 0 or the number 1. These packets vary in length, but it has become generally standard to break them up into groups of 8. 8 bits make a byte, and bytes have stuck with us even though we are almost always dealing with many more than one at a time these days. Thus we had 8 bit computers, 16 bit computers, 32 bit computers, and 64 bit computers. 8 bits also form a "byte" which is the informal base unit for measuring all forms of computer storage.

**Digression**: This is a good time to indicate my deep and utter hatred for the <a href="http://en.wikipedia.org/wiki/Mebibyte">insane unit reform assholes</a>. These people seem to think that a relatively minor imprecision in the wording used to indicate various powers of 10 (or 2) of computer storage capacities is the _end of the god damned world_ and must be stopped at the cost of making people use completely asinine terminology for something that everyone really understands anyway.

Anyway, back to bits.

Computers interpret these groups of bits in different ways. Sometimes they are just literal values. Therefore (depending on the actual representation) the bit string "1000 0100" might mean the decimal number 132.

On the other hand, the bit strings can also be used _indirectly_ to compute other values. Say we have the following group of bytes: [4 65 66 66 65]. We could program the computer with the following rules:

1. The first byte is a length (call it L), which tells you how many of the next few bytes to interpret as a group.

2. For each of the next L bytes, take the value and look it up in this <a href="http://en.wikipedia.org/wiki/ASCII">table of ASCII letters</a>.

3. The result is the string "ABBA"

We have done two important things here. First, we have laid out specific rules for how the computer should interpret particular areas of memory. Programming languages take this idea and generalize it into constructs we call _types_ that specify not only how software objects should be organized in memory, but also what mechanisms are available to the programmer for accessing and manipulating that representation. While we are taking a fairly low level view of types here, rest assured that there is an almost infinite library of literature on what types should be and how they should be used in programming languages.

The second important thing we have done it to use _indirection_ to compute an answer. We used the indexes in that short buffer to reference a table to tell use that for our purposes, if you see a "65" in memory somewhere, what that really means is the letter A.

Types and indirection are at the heart of how we construct software. Types allow programmers to build higher level abstractions out of the memory buffers that the machines provide them (or lambda expressions, if you prefer to be stateless, Patrick). Indirection allows types to express their relationship to other types. Software people use these two tools to build _models_ for their software. Behind everything you do with a computer is a model. Your presentation program has a model for representing graphical objects, outlines of text, and sequences of fancy slide animations. Your text editor has a simple model for storing the buffer of text that you are editing. The model is how software keeps track of what you are doing. And the part of the model that gets written to disk is what allows the computer to save your place, your game, or your term paper so that you can get back to it later.

Anyway, these models are everywhere, and in particular they are at the heart of the stack of things that ends up putting text on your screen. So how does that work, anyway?

First, let's start with a simpler example. Back in the 70s and 80s a lot of people used computers via <a href="http://www.vt100.net">"TTY Terminals"</a>. This was a simple keyboard and screen. The screen could show you as much text as you wanted as long as it was 24 lines of 80 characters. Sometimes the text was white. Sometimes it was green.

Terminals would take text as input over a serial line as a sequence of ASCII (or sometimes older encodings) bytes. The terminal would take each byte and store it in some memory for the whole screen (80x24 bytes). Then each time the screen needed to refresh, it would run through this buffer and generate the fixed pattern of dots that it should display for each character on the screen. This probably worked via a relatively simple piece of firmware running on a super primitive CPU. The terminal used what is essentially a really simple font. But you only get one. So when the value 65 came over, you'd see "A", and so on. Later advanced terminals let you put any letter you wanted at *any* screen coordinate you wanted. That was bitchin' in those days.

So the simple answer is: some simple hardware and firmware has a lookup table (a model!) that translates ASCII into signals to display the right bit pattern in the right place.

Now what about your web browser? Well, things have evolved, but it works basically in the same way. Just with more intermediate steps.

It goes like this. Let's say that you have fetched a web page that contains the text "Hello World". Your web browser has asked the server for the contents of some page and the server has fed it a string of characters that it knows is in a format called "HTML". It might look like this:

    <p>Hello World</p>

Your web browser interprets this as

"First, make a new paragraph. Then show the string 'Hello World'. Then end the paragraph".

Somewhere in its memory, it will have a buffer with the string "Hello World" in it. Somewhere else in its memory, it has a model for what paragraphs are supposed to look like. Among other things, this model will tell the machine that font to use, how big the font should be, how much space to leave at the top and bottom of the text, whether we should draw the text left to right or right to left, and so on.

The web browser software will now feed this string and all of this other information into some code that does typesetting. The typesetters builds a completely different representation of the text. First, it makes up a box to put the text in. The top/left of this box is where the string starts. It takes the text and all the font information and for each letter of text it creates a vector of information that indicates where in the box the letter belongs. The result is a high level specification for how to draw the text in the box.

This representation is sent to the rendering system whose job it is to create a rasterized representation of the text. Given yet more information in the font, the resolution of the output device *and* the typesetting information we created above, each character is now turned into rows of RGB values representing what each pixel on the screen should show for this particular letter.

Now what we have in memory is a block of RGB values. This block is a large enough to be a box on the screen that fits the text "Hello World". We call this sort of object a "frame buffer", or a "bitmap". The word "bitmap" is interestingly archaic, since it harkens back to the days of black and white screens when each dot really was just one bit. But these days each dot is 24 or 48 bits deep (8 or 16 bits per color channel).

Anyway, all that's left to do now is feed this bitmap to the graphics system. The graphics system takes the one bitmap and integrates it into the frame buffer representing what the whole screen should be showing. Remember, the screen is probably being used by multiple programs at once, each of which is allowed to only draw in the parts of the whole that they own. All of these different drawing requests all converge in a single place, and at just the right time a single aggregate bitmap is created in some piece of memory in the graphics card. This is then pushed over the display cable and on to the screen. Or it's pushed out the analog output and to your TV. Or it's pushed over the network into your iPad (because you are using screen sharing) and drawn over *there*...

This all might seem complicated. And it is. There are a ton of layers here, and new ones are being dreamed up every day. But I've actually left a lot of things out because I don't actually know how they work. So I'd guess that at least half, but more like 3/4ths of the whole story is missing. 

My only goal in typing all this nonsense out is for you to think about one thing. Each of these layers has its own *model* for representing its core task and the data that it needs to perform that task. The browser has a high level model of the text on the page. The typesetter has a model for lines of text. The graphics system has a model for what a frame buffer looks like. And on and on. The great game of software is how to combine these disparate representations into a single system which, in the end, is working best when it is completely invisible. All you see is the text

Hello World

Oh, and when you put your two fingers on the screen and spread them out, the text is magically zoomed. Just imagine how *that* works.
