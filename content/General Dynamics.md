Title: General Dynamics
Date: 2016-07-02
Category: Computers
Author: psu

Today another rumination about programming computers. Today's thoughts expand on an earlier piece that I wrote here about <a href="http://mutable-states.com/what-programming-languages-say.html
">programming languages</a>, but it is also related to how programs are <a href="http://mutable-states.com/the-inscrutable-tubes.html">inscrutable tubes of complexity</a>, and who is <a href="http://mutable-states.com/who-are-the-programmers.html"> good at programming computers anyway</a>.

With some trepidation I will wade into that old warhorse topic: "static" vs. "dynamic" languages. This came up a couple of months ago in the context of the evolution of the Swift language, which I have <a href="http://mutable-states.com/what-programming-languages-say.html
">talked about before</a>. But disagreements over this issue go back almost to the time when you could write an article in a <a href="http://dl.acm.org/citation.cfm?id=356640&dl=ACM&coll=DL&CFID=638723219&CFTOKEN=86771664">journal of research computer science</a> about whether using "goto" in your code is a good idea or not. As with gotos, the dynamic vs. static argument hides a high level philosophical discussion about what programming tools should do for you behind a lot of posturing about personal stylistic preferences. 

The first thing to say is that "static" and "dynamic" are bad words. They are too vague and don't necessarily reflect what you really mean to talk about. For me, "compile time" and "runtime" work better. But for conciseness I will use "static" to nominally mean "compile time" and  "dynamic" to mostly mean "runtime."

The shallowest water in which to have this argument is to concentrate on the extent to which a language requires you to annotate your code to declare all the types up front at compile time. Or the extent to which you even have a compile time at all. In the 80s, advocates for Lisp and Smalltalk would rail against "bondage and discipline" languages like Pascal and C for requiring you to make sure all your micro-level type annotations matched up everywhere so the compiler could correctly allocate storage. They sort of had a point. That sucked. In the 2010s, advocates for Javascript and Ruby (say) may try to make similar arguments. However their point is not as sharp now since you can now build languages that do not require you to declare types, but which are still statically checked. There are even versions of Javascript that do this, yet people will still howl at the moon about how you are tying their hands behind their backs if you whisper the phrase "static type checking" on twitter.

This behavior will be somewhat confusing to people who have either bought into the "type theory cult", as I call it, or people who have a lot of experience working on very large systems. These folks will generally trot out a familiar list of things that more advanced static checking can do for you:

1. Tell you the types of the things you are manipulating in your code even without you explicitly annotating it.

2. Make sure you don't make stupid mistakes that make your program crash.

3. Make sure you don't make more complicated mistakes that make your program crash.

4. Provide shallow documentation for the code in the form of various type-related invariants.

5. Use type information to optimize the code.

	and also in more recent times:

6. Provide flexible ways to express polymorphism in code.

All of these things are demonstrably valuable, especially in larger systems built by large teams with a lot of internal interfaces whose expectations and limitations may not be well communicated. Having types around to enforce such constraints even at a shallow level can only help? Right? Yet when such lists get thrown against the Internet the answer that returns is one of two things:

1. "Oh, I don't need that stuff, it just gets in my way."

	or

2. "Yeah, but then I won't be able to patch the runtime to do what I want."

You can see some of these attitudes projected on this <a href="http://mjtsai.com/blog/2016/05/21/dynamic-swift-2/">page that catalogs some of the discussion about the perceived lack of dynamic features in Swift</a>. To their credit, most of the commenters there seem to understand the actual tradeoffs that are in play, and that some level of static checking has value. But I also get the feeling that many don't understand why Swift is so concerned with the fussy complexity of its type system when just hitting the world wth the Smalltalk-style dynamics hammer would be so much simpler.

I have to admit that I'll never understand this objection at all. I find it confusing that anyone would object to *more* compile-time checking. I only have anecdotal evidence to offer, but in my lifetime working on the very large piece of Objective-C code that I work on I have fixed or diagnosed dozens (maybe hundreds?) of bugs that required me to go and figure something out at *runtime* that a modern compiler could have told me about at compile time. In every case the seeing and fixing compiler error would have taken an order of magnitude less time than some poor q/a person (or unit tester) happening upon just the right code path with which to trigger the runtime error. 

This seems to me to be a slam-dunk win. I suppose how you feel about this depends a lot on scale but really programs don't have to get that big before this sort of thing becomes valuable. If you have more than five or ten people working on any given thing, you will want all the compile-time checking you can buy.

As for the second sort of answer, in the context of this discussion I think that the the advocates for dynamics really want various kinds of runtime meta-programming.

This is summed up by <a href="http://inessential.com/2016/05/26/a_definition_of_dynamic_programming_in_t">Brent Simmons' list</a> of three things that dynamic languages ought to be able to do:

	When I talk about dynamic programming on iOS and Mac, I mean this:

	1. An app can learn about its structure at runtime.

	2. An app can do things based on what it knows about its structure.

	3. An app can make changes to its structure.

There is a lot of history behind the desire to have these kinds of features in a language runtime.

Anyone who ever built UI in older Mac and Windows systems in the late 80s and early 90s will have dark memories of a lot of boiler-plate Object Pascal (!) and C++ code setting up tedious plumbing. They might look with envy at what was possible in Smalltalk and LISP systems where you could just hook everything up dynamically in the programming environment and have it "just work". Later, NeXT and by extension MacOS X brought some of these features to the Objective-C tools that so many people are still in love with now. You just drew a connecting line and the UI was would do the right thing by magic! 

The general perception is that the dynamic features of Smalltalk, LISP, and Objective-C made the transparency of these tools possible. There was no need for generated code, no lookup tables, and so on. It was all in the "native language". This desire for this sort of runtime meta-recursiveness is a dominant trait in software developers.

The apotheosis of this philosophy was the Common Lisp Object System where everything was so meta you could, in principle, replace the entire runtime system if you wanted and just keep right on swimming, assuming your new code worked the first time. I recall going to a MacWorld in 1988 or 1989 (70MB SCSI hard drives at a special show price of only $700!) where some dudes from MIT were demoing a Common Lisp implementation on the Mac where you could edit the UI of the Lisp IDE while the Lisp IDE was running. This, they told you (and at the time you believed it) was the coolest shit ever. I imagine that these days the dream of the user being able to change a running application at runtime would cause most developers to run screaming into the night. Think of the cool bug reports.

At a lower level, developers have always felt a perceived need to to be table to patch the platform code to add custom behaviors that their applications require or to work around platform bugs. In the bad days of the original MacOS you apparently could not ship a commercial application that did not patch the operating system itself at runtime. Similarly, in the older Windows days there were entire books written about how to extract and reverse-engineer Windows kernel data structures so you could tweak things.

In the modern world, we have learned how to move on from such shenanigans, and yet advocates for "dynamic Swift" still bring up their desire to keep the  Objective-C features that allow this ethos to live on. Many will fight to the death to be able to hook to behaviors via subclass overrides, perform runtime introspection, add methods to platform classes at runtime, or even replace platform code with their own stuff at runtime. Objective-C, they argue, has "native" features that allow these things and Swift must as well.

First, I would argue that the meta-programming facilities in Obj-C are actually provided by the standard library, not really the language per se. Second, people who get all high and mighty about not needing to use lookup tables for things don't seem to realize that in Obj-C many "native" language features like -respondsToSelector: or -performSelector: or the target/action things are just lookup tables implemented by the standard library. There is nothing particularly special about them, and you could probably implement the same thing in Swift with a comparable level of convenience in use. So my feeling is that anyone who is super worried about this stuff disappearing if the bridge from Swift to Obj-C goes away are a bit confused. You could bring it all back, and it's a small amount of work compared to what you would need to do to, say, rebuild all of Foundation and AppKit.

But these are all small points. The larger point is that you don't want to do any of these things at all if you can help it. They are bad. Here is why.

The hardest thing about programming is reasoning about a program's runtime behavior. Recall that <a href="http://mutable-states.com/who-are-the-programmers.html">the best programmers</a> are the ones who are really good at this and it's even hard for them. When you are staring at a piece of code in the debugger because your program just crashed what you want is for the *local* context to tell you as much about what the code will do as possible. You want to minimize the extent to which *non-local* and *state dependent* factors change the behavior of your code. You want your tools to be able to easily tell you everything that you might need to know about which tube went wrong and where, so you can reach in and fix it. The smarter the static analysis tools are in your programming environment the better this will be.

And so here is the point: the catalog of "dynamic" features that we have built above all *increase non-local and runtime-dependent effects*. Therefore the compiler goes from having a small but definite chance of telling you what went wrong to zero chance of telling you what went wrong. All you can do is run the code over and over again to isolate the piece of the runtime state that is incorrect by catching it in the debugger. Therefore your code is harder to reason about locally. Therefore your code is harder to fix. So if you want your code to be easier to understand and easier to fix, you should use dynamics as little as possible. There are few obvious places where you really need to work with and respond to things in the type system at runtime, but you should try to avoid them at all costs.

A great example of a dynamic runtime feature that makes my life miserable, but which you have to implement in every user interface toolkit, is the responder chain mechanism in AppKit. It's part of what makes those magic connecting lines in Interface Builder work. When you dispatch user interface actions in AppKit you essentially send a string signature into the responder chain and the responder chain finds the first piece of UI in its list that declares that it can service your request (by doing string matching against the name of the operation).

For smaller applications with simple goals, this is a great and flexible system that allows you to write very little code and still dispatch all your stuff to just the right place. For larger applications it can be a nightmare because it makes it impossible for you to figure out what code will service a given request without exercising the entire user interface at runtime. It also makes it really hard to ask the debugger to track down how you ended up servicing a request in the wrong place, because you have to step through all of the changes to the responder chain's state to see why (say) the object you thought should take have taken over was not there. Responder chain problems are really hard to debug because there is no static model of how they should be behaving. You can only try to observe things at runtime, and that's bad. So remember: overusing dynamics makes everything into a responder chain problem. You don't want that.

A lot of people in the Swift dynamics discussion brought up exactly this sort of feature as one that is "hard" to implement in "static" languages. But this is of course not true. Here is a simple implementation in Swift: <a href="https://gist.github.com/anandabits/ec26f67f682093cf18b170c21bcf433e">https://gist.github.com/anandabits/ec26f67f682093cf18b170c21bcf433e</a>. The only difference between this and what's in AppKit is that does not handle all of the real world edge cases that AppKit must and that it is not using "built-in" runtime mechanisms to represent messages and actions. But this is no big deal, it's not like the Obj-C compiler was giving you a lot of help with those types anyway. They were essentially just strings.

In addition to illustrating that implementing dynamic features in Swift is not all that hard the other thing this code shows you is the potential to go beyond what AppKit gave you in 1987. For example, in the target/action mechanism the signature of an action can only be the relatively simple

	-(void)action:(id)sender
	
Why can't you pass in more parameters? Why can't you return values? What about error checking? Swift's type system and higher order functional features open up many more design possibilities here. Perhaps you could even build something like the responder chain that lends itself to more static analysis, so you do would not have to grovel around in the debugger to figure out that the reason some operation does not hit you is that you spelled its name wrong.

I think that we will eventually find that the majority of dynamic features in the current Obj-C runtime that are truly useful will be translated to Swift and in fact will usually be made richer in the process. We're already seeing some of this in the new more Swifty Foundation and CF libraries described at WWDC. Of course, you will probably never be able to do method swizzling, per se. But you didn't want to do that anyway. Really you didn't.

Meanwhile, the real value of this transition will be to make people really consider whether their favorite runtime constructs actually need to be dynamic and therefore only checkable at runtime. For me, the more stuff that can be folded into the comfortable embrace of the compiler the better.

May you never need to actually debug responder chain problems at runtime.
