Title: This is What I Do
Date: 2007-01-03
Category: Computers
Author: psu

Once in a while, in the midst of casual conversation, someone will ask me what I do. When I was a graduate student, I would mutter something about computer science research, algorithms analysis and by the time the word “geometry” came out of my mouth after “computational” their eyes would glaze over and they would back away slowly. When you work in research, you can scare people away with the power of your abstraction.

I don’t work in research anymore. I work in software production and once in a while I will spend some time trying to figure out how to boil the essence of the job down to a simple sound bite. With a few release cycles behind me, I finally came up with the right catch phrase. If you work in software engineering, and you are actually shipping something, you spend most of your time doing one thing: fixing bugs.

This insight is not surprising. After all, software is complicated and notoriously difficult to specify and design. The number of flows through the state machine that represents your average application with a GUI is staggering, and you can’t really account for all of them ahead of time. The reality is that even though we try to do a lot of up front design and specification work ahead of the implementation, we can’t escape the inevitable fix then test then fix then test some more cycle between when we think we have implemented all the features and when we can actually ship the final product.

I’ve been debugging code for more than 20 years now, and it’s always been basically the same process:

1. Find a sequence of operations that fails or produces the wrong answer or the wrong behavior.

2. Make sure said operations produce exactly the same failure every time.

3. Watch the application fail over and over again performing this sequence of operations.

4. Isolate the failure to a particular piece of logic going haywire.

At this point, you generally know why the bug is happening. The critical activity here is between steps 3 and 4. If you think of the application under test as a gigantic state machine, what we are trying to do here is tease out the small subset of the application state that becomes incorrect in the particular case we are testing. Then we need to figure out how the state has become incorrect. The dance you do is generally the same.

1. You run the test case right up to where the application is about to fail.

2. You query the application about its state.

3. You run a a bit more.

4. You look query the application about its state.

And so on until that magic moment when between two program steps you see the state transition from being correct to being wrong. At this point you have essentially recorded the failure for posterity, and you are ready to fix the bug.

In all the time I’ve fixed code, the basic tool that you use to perform the above task has remained basically the same. You run the code in a debugger, which allows you to control the program’s execution so that you can pause it at any time and look at the state you are interested in.

I have never liked debuggers. I don’t like them because it’s hard to get them to tell you what you want to know at the exact time you need to know it. I always end up in one of two scenarios: either it takes too long to single step all the way to the failure or I have to play whack-a-mole with breakpoints until I get lucky and manage to break at just the right point. Interactive applications also present some special problems because sometimes it can be hard or impossible to set breakpoints at certain places in code, because doing so lands you in the debugger after every event loop and the application can never make forward progress.

One alternative to debuggers is to put a lot of tracing code into the application itself, so the application essentially records its state to some external file over and over again while it runs. Then you slog through all of this trace to find the proof you need. This can work some of the time, but without some systematic way to format and analyze the trace, it’s hard to glean any information from it. It is also notoriously difficult to effectively instrument the program to spit exactly the state you need and nothing more. The result is that rather than sitting in front of the debugger going step step step you sit in front of your trace, reading all the text to find the bits that tell you what went wrong. It’s not necessarily any easier.

It always seemed to me that the ideal tool would be a debugger that let you run the failing test case once and recorded everything that the program did into a single place. You could then load this trace into a debugger and play it backwards and forwards, up and down, left and right, stopping and starting however you please. The debugger could also let you query and display any piece of state that draws your fancy as it plays the trace back. Since the trace captures absolutely everything that the program did, you can imagine an arbitrary level of introspection. In other words, such a debugger would combine the incremental step step watch watch aspect of a traditional debugger with the convenience of having tracing, but without the disadvantages of either. You don’t need to actually run the test over and over again, you just play back the trace. You don’t need to strategically instrument the code by hand, you just need to query the state of the application for the pieces you need to know about.

In other words, it would be the perfect tool for what software engineers do most. This tool would take pictures of programs failing, and allow us to discover those pictures in a way that is much less tedious than before. Happily, a friend of mine has been working on a system which does exactly this. Robert O’Callahan’s Amber system promises to provide most of what I outline above. You can capture full trace and then play around and query that trace for the proof that you need. Of course, the capture part is pretty slow, but this is offset by the fact that you only need to do it once rather than dozens of times like we do now.

Rob deserves great fame and glory showing us that this can be done. Here’s hoping that people figure out how enormously cool this tool could be. Maybe sometime before I retire we’ll finally build a debugger that doesn’t suck.