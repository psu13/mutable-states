Title: Dynamics Appendix
Date: 2016-07-05
Category: Computers
Author: psu

Just in case you thought that <a href="http://mutable-states.com/general-dynamics.html">almost 3000 words on dynamic runtimes wasn't enough</a>, I had a few more thoughts that did not fit into how the final piece flowed together. In addition I thought of an obscure but relevant piece of Ancient Lisp Lore that I am contractually obligated to share (hi Patrick!). So here we go.

**Part 1: Dynamic Dispatch**

The place to start is with the aspect of dynamics that I glossed over on my way to the shiny dumpster-fire of meta-programming. The most popular single dynamic mechanism in the programming languages of the last 40 years has been "dynamic dispatch". This mechanism goes by many names: message passing, virtual methods,  generic functions, and so on. Most "object-oriented" languages implement this in one form or another as follows:

When you want to call a function *foo* with some set of arguments *(a,b,c,d)* the language will allow you to define multiple implementations of the function for various combinations of argument type. Then the some implementation of the method is chosen at runtime based on the manifest types of the arguments when you make the call. Generally this is done by walking up and/or down the inheritance hierarchy that the programmer has defined to find an object or type that implements the function. For 40 years this has put the "object" in "object oriented".

Usually the dispatch scheme depends only on the first argument to the function, and usually the syntax for the function call is turned around like this:

* a.foo(b, c, d) 

* or a->foo(b,c,d)

* or [a foo:b c:c d:d]

or whatever.

The idea here is that you are invoking the function *via* the object that makes up the first argument. Some people find it very important to their lives to describe this sort of syntax as "sending the message *foo* to the object *a* with the various arguments", as if this slightly more abstract picture will be easier to grasp than "oh that's a function call". At this point in my life I have no time to indulge this sort of pedantic nonsense.

Besides, attaching the method too closely to the object just encourages the language designer to commit the first of two major sins that all of the object languages have committed since the beginning of time, to wit: equating *classes* with *interfaces*. They should have realized that this was a bad idea in 1983. *I* should have realized that this was a bad idea in 1983, but at least I have the excuse that I was only 18 and really stupid.

Anyway, the last thing to say about dynamic dispatch is to point out, once again, that the Common Lisp Object System had the most general, most psychotic, and most reprogrammable dispatch system that the world ever saw and will ever see. Hopefully that doesn't happen again. The tip of that iceberg is the fact that CLOS could function dispatch based on the types of *all* the arguments to a function, not just the first one. I think it also had multiple inheritance. Try to fold your head around that and start reading again after you patch up your exploded brain.

I mentioned some of this in passing in the original piece but didn't discuss it in detail for a few reasons:

1. The meta-programming issues were more the core of the discussion.

2. Dynamic dispatch is fairly well understood and is even widely implemented in languages that have basically static type systems. Swift certainly supports this sort of thing. Even as long ago as Object Pascal we had integrated a static type system with dynamic dispatch. In addition the compiler and linker would work together to optimize away calls that they could prove were actually statically resolvable at link time. My point is that making this conceptually dynamic feature work in a more static context is a fairly well understood problem. The only people who gripe about this are the ones who really want the meta-programming stuff or the ones who still insist on using the term "message passing." 

In the context of the dynamic Swift discussion there are a couple of dispatch-related mechanisms in Objective-C that people will claim to miss when moving towards a more pure Swift style.

1. Method forwarding via "forwardInvocation:".

2. Stringy-type dispatch mechanisms like Key-Value coding (and its related evil cousin KVO: Key-Value Observing)

I dislike both of these things because they are different ways of making it impossible to figure out what code is going to run with you call some method in some context. Method forwarding means that the dispatch engine will not necessarily be following the class hierarchy to figure out what to do, so you have to search all over your code to work it out. And I hate that. 

KVC and KVO use arbitrary strings to synthesize method calls, which means that in principle you have no idea what will happen since you have a whole Turing Complete string generator at your disposal. Used poorly these mechanisms are also vectors for the injection of arbitrary code  into your frameworks or for allowing the nefarious among us to access code that the interfaces say should be private. Want to read a private ivar that no one has told you about but which you saw in a trace somewhere? Just do '[object valueForKey:@"_myPrivateParts"]' and poof you are in.

These things need to die or to be reimplemented in a rational way with some damned type checking. 

**Part 2: Dynamic Scope**

I was in the shower the day after I posted the original article when I remembered this obscure piece of ancient LISP lore. I realized that it would make a good second example of a dynamic language mechanism that a *lot* of people liked because it bears some similarities to dynamic dispatch above and the various bits of meta-programming that I talked about. But then I was sad because I had already posted my article. And so here we are.

Now I will tell you about "dynamic scope" or "shallow binding" in a LISP runtime.

The idea is simple. Any Lisp interpreter needs to keep around a store that keeps track of the *values* that *names* are bound to. So when you write come code like

	(let ((a 1) (b 2)) (+ a b))
	
the Lisp system will have some record of how to look up the value for "a" and "b" in the final body of the statement.

Now in all modern languages use a scheme called "lexical scope" (or in times past "static scope" ... there's that word again) to figure these things out. That is, the values that a variable can take on can only come from two places:

1. The immediate syntactic block of the code that uses it.

2. Some outer block that the in which immediate block is nested

Usually these will be either local variables, instance variables in object languages, and arguments to functions.

But, in LISP you don't have to declare names. So you could write code like

	(defun foo (a b c) (+ a b c d))
	
And the system will happily accept it. So the question then becomes, what happens when the interpreter tries to evaluate the value of "d" above?

In lexically scoped Lisp you will get an error if the name is not bound locally or in the global environment. So if had done something like

	(define d 4)
	(defun foo (a b c) (+ a b c d))
	
Then you'd be OK. Or if you had stuck it in a let:

	(let ((d 4))
		(defun foo (a b c) (+ a b c d))
		(foo 1 2 3))
		
You'd also get an OK answer. Here all of the local values get pushed into stack frames at runtime just like you expect, but any given block of code can only look at its local stack frame.

In *dynamically* scoped Lisp what the interpreter did was just keep all the bindings on the stack but when it went looking for a value it would walk the whole stack to find the binding closest to the current call site, no matter what frame it was in.

So code like this:

	(defun bar (x) (+ a x))
	(defun foo ()
		(let ((a 1)) 
			(bar 1)))
	(foo)

Would return the value "2" rather than an error like you'd expect. The reason is that the let statement inside "foo" binds "a" to a value which is then used in the body of "bar" since it's sitting on the stack.

If for some reason you changed the body of "foo" like this:

	(defun foo ()
		(let ((a 1)) 
			(let ((a 2))
				(bar 1))))
			
then the answer would be "3" instead because the inner binding of "a" wins. 

People actually thought this was a good idea! The usual rationale was that it allowed programs to twiddle state that could change the behavior of various bits of code without needing to either reach in and change the code itself or tediously figure out how to build an explicit interface to provide the knob that you wanted to turn. Sound familiar? These arguments are very similar to some of the typical arguments given in favor of the various dispatch and meta-programming mechanisms that we have already discussed at length. They are also wrong.

But, the Lisp people saw the light early. In the late 70s and early 80s the first versions of scheme had lexical scope and it was seen to be good. Why was it good? Because it makes it easier to decode the behavior of the code based on *local* information. Remember? Dynamic scope essentially died off with Common Lisp (although even Common Lisp still had a dynamically scoped version of let called fluid-let) and the only place you ever saw it was in Emacs. But even modern Emacs has lexical scope now if you want it.

There are two lessons here:

1. Making it easer to debug based on the lexical structure of code is good.

2. I will do *anything* to come up with an example from Lisp.

OK we are really done now.
