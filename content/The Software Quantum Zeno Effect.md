Title: The Software Quantum Zeno Effect
Date: 2020-05-27
Category: Computers
Author: psu

Long time readers will remember that while I am a computer geek professionally in recent years I have become the <a href=http://mutable-states.com/reading-physics.html">tiniest bit of an amateur dilettante physics nerd</a>, to make up for having dropped out of the physics major in college. Suffice to say that if in 1986 I had realized that theoretical computer science and theoretical physics (quantum mechanics) were going to get together the way that they have recent years, I might have stuck with it at the time. In particular, I might have figured out more about quantum mechanics.

As we all know, the weird thing about quantum mechanics is that while you are allowed to imagine that some quantum system somewhere is in some state, you are not really allowed to know or talk about what that state *is* unless you actually *look* at it and find out. This is called the *measurement problem* although in some sense *measurement dilemma* might be a better way to put it.

In the traditional way of talking about this, if you have some quantum wave function $ | \psi \rangle$ (shout out to the Dirac notation), it can just float around in Hilbert space doing anything it wants until you hit it with some measurement operator to see where it really is. At this point the measurement will return some value $a$ and from then on the wave function is thought to be in the state that returns the value $a$ when measured.

This strange behavior is known, in the lingo, as the "*collapse of the wave function*"... the idea being that before you looked at it the quantum state was indeterminate and could be made up of a superposition of any number of wave-like components, but after you look it collapses down into just one thing that always gives just one answer.

In the 70s, some physicists had a funny thought about this. In <a href="https://doi.org/10.1063%2F1.523304">this paper</a> they proposed the following thought experiment:

1. Suppose we have a quantum system that has a stable state and an unstable state.
 
1. Normally, if the system is prepared in the unstable state it will tend to decay back to the stable state in some amount of time if left alone.

1. But, what if instead of just allowing the system to sit there we keep measuring it to see if it has decayed?

The conclusion of the paper was that if you ran the measurements in just the right way you could *keep the system from decaying* just by *measuring to see if it has decayed*. This idea has come to be known as the <a href="https://en.wikipedia.org/wiki/Quantum_Zeno_effect">Quantum Zeno Effect</a>, a reference to one of the most famous of <a href="https://en.wikipedia.org/wiki/Zeno%27s_paradoxes">Zeno's paradoxes</a>. If you know your quantum mechanics, you can look at <a href="https://arxiv.org/abs/quant-ph/0612187v1">this review paper at arxiv.org</a> for a fairly clear explanation of what's going on here without dealing with academic paywalls.

My interest is in what this idea has to do with software.

As we all know, <a href="http://mutable-states.com/the-inscrutable-tubes.html">large software systems are complicated</a>. They are complicated to design. They are complicated to implement. And they are complicated to work on. One daily complication in working on such systems is what we call "building" the code. In this usage "building" does not mean the actual construction of the code itself, but rather organizing it so that it is executable in a way that allows for testing and debugging.

Some background on this.

Hardly any software is written either directly to the hardware or directly to a language that is understandable at the hardware level. This is because machine level instructions are <a href="http://mutable-states.com/what-computers-do.html">very simple and primitive</a> (I'm lying here, they are not) and you have string a lot of them together to get useful work done. So instead we take the various things we need to do a lot and package them into various sorts of tools, <a href="http://mutable-states.com/what-programming-languages-say.html">programming languages and libraries</a> being the most obvious.

*Building* an application is the process of doing three main things:

1. Collecting all the high level code that is required together in one place.

2. Translating that code into machine language so the computer can understand it.

3. Collecting all the resulting machine code and packaging it into a container that the computer can run as an "application".

With web applications all of these words get fuzzier meanings, but the basic idea is the same so bear with me.

All of these things are pretty easy to do for small systems. But for large systems each one gets exponentially more complicated. So complicated that you need a computer to help you do it. So complicated that you have to write and test special software to tell the computer how to build and test the actual software that you are writing. 

What, you may ask, does all this have to do with quantum mechanics?

Software that is under development is an inherently unstable thing. Because of all the complexity in it, it tends to break a lot. You can think of being somehow broken as the natural low energy state of a software system, and being in a good working form as a higher energy but more unstable state.

The same can be said of complicated build and test processes. Whether or not builds work can depend on a large web of dependencies like

1. Are you running the right tools?
2. Are you building the right version of the code?
2. Are you running the right version of the source platform?
3. Are you running the right version of the target platform?
4. Is your Internet working?

Every day your intrepid programmer sits down at their workstation and needs to do work. The first thing they do is to get the latest copy of the source code to work on. The second thing they need to do is build the code and set things up for testing. It has long been my experience that these things only go smoothly if you stick to the following rules:

1. Build every day.
2. Build the same way every day.
2. Build everything you might ever need to test every day.
4. Build it all from scratch every day.

The problem is that you can't actually build everything all the time. The product that I work on is made up of (say) nine different top level artifacts for three different platforms with a lot of support code running in the background. It's actually not possible to verify that everything is always working for me in every possible way I might need it to work every single day. It would take my whole day and I'd never do any work.

So inevitably there are things I don't build and don't test. And those things inevitably decay so that the next time I *do* need to work on them, it takes a day or two to get them working again.

Meanwhile, the things that I actually exercise and practice with every day are rock solid and always in a good state. Just recently I was working on a feature in a particular area of our system that takes a lot of complicated setup to test. For months, even through some complicated transitions in my working environment, this setup worked fairly smoothly. Later, I took a two week break from working on this stuff, and did not do the setup during this time period. The next time I tried, nothing worked at all and I had to go back to it the next day and spend a whole morning making it work again.

So to summarize: If you *build and use* (i.e. "measure") the code and support tools constantly, they stay stable and in a good and testable form. But if you stop looking at some piece of it, that piece decays into a "lower energy" state where nothing works.

This, my friends, is the "Software Quantum Zeno Effect".

I have worked on various versions of the same relatively large software system for about twenty years now (wow!). A lot of things have changed about how I do this work. But this rule has stayed constant.

So I will repeat it: If you build it, then it stays good. If you stop building it, it decays to shit.

Ponder the truth of this, and now go do a clean build for me.

**Note**

I should note here that it's critical that these builds happen in the local working environment of the programmer. Some people reading this are no doubt rolling their eyes right now and muttering "continuous integration" under their breaths. And they would be partially right. But continuous build and deploy systems do not always solve the particular problem that I am talking about. 

If you can prove that your builders are always building in and deploying to exactly the same platform and runtime environment as every programmer's workstation or target device, then congratulations you are very lucky and you win a prize. Sadly this is not always the case. So while CI gives you a useful backstop it is not a guarantee that when I sit down at my work computer in the morning I'll end up with something that I can actually work on.
