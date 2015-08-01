Title: What Programming Languages Say
Date: 2014-06-08
Category: Computers
Author: psu

It's probably not surprising that the easiest way to get programmers to talk to you is to ask them about programming languages. Mention your favorite new toy and you will get hours of excitement, invective, or a schizophrenic and bipolar combination of both. Therefore, it is also not surprising that a lot of the dork discussion of Apple this week centered around this new thing that Apple introduced called "Swift". I'll have a little bit to say about Swift, but not much aside from "If you write code for Apple runtimes, Swift is mostly nice". I'm interested in the broader subject.

Computers are stupid machines. This is a fact. At their core they understand a relatively small set of instructions that do very little. Examples:

1. Load this small piece of data from memory into the CPU.

2. Store this small piece of data back memory.

3. Do simple arithmetic.

4. Check this condition. If true, do this, if false, do that.

5. Start running code at this here address.

And so on.

Programming languages, as <a href="http://mutable-states.com/the-ultimate-goto.html">you might recall</a> allow programmers to solve their problems at a <a href="http://mutable-states.com/the-abstraction-distraction-part-1.html">higher level of abstraction</a>. This achieves at least two things:

1. You don't have to break your code down into those stupid tiny bits.

2. You can pretend that you have a machine that understands a more interesting sort of computational model than load/store/goto.

Computational models are a popular subject for academic computer science people to think about. This is because it's their job to think about this sort of thing while the rest of us cavemen toil in the salt mines working with tools that were built at a time when everything was a pointer and explicit memory management seemed like a great idea. But I'm not bitter.

Here are a few of the models that get thrown around in such discussions:

0. Traditional imperative programming. What we know and love. The tradition of Fortran, Algol, and C. These languages present you with something that works much like the computer does, but with the various hardware details abstracted away. You put programs together by combining other smaller programs together. Thus some people also used to call this "procedural" programming.

2. Object-oriented programming. Extends the traditional languages with ways to encapsulate state and behavior into little packets that you talk to with specific interfaces. It is handier than its detractors would have you believe, but nowhere near as powerful as its most ardent evangelists would claim.

	The object languages have traditionally used _inheritance_ and _dynamic dispatch_ as their main mechanisms for creating larger program structures from smaller ones. Again, these are pretty cool, but can also get you into a lot of trouble. But that's a subject for a different rant.

1. Logic programming. Programming based on finding the solution to a set of declarative rules. Most of the logic languages are fairly obscure and forgotten, but the ideas show up in the functional languages below. Also related: constraint languages like the auto-layout engine in the recent Apple user interface toolkits.

3. Functional programming. Programming based on the evaluation of functional expressions. One of the big ideas here (and to a lesser extent in the logic languages) is that purely functional programs are free from explicit side effects. The theory was that effect-free programs are easier to reason about (true), more natural for concurrent runtimes (certainly), and would also allow programmers to automatically take advantage of the coming wave of massively parallel architectures (huh?).

	**Useless Digression**: the late 80s, when I was trying to be an academic computer science type, it was thought that the classic <a href="http://en.wikipedia.org/wiki/Von_Neumann_architecture">"Von Neumann" architecture</a> was not long for this world. The logic went that we would soon end up against the limits of how fast a single core could compute (because of the dreaded <a href="http://en.wikipedia.org/wiki/Von_Neumann_architecture#Von_Neumann_bottleneck">von Neumann bottlebeck</a>), and we would need ways to structure the new generation of parallel processing software that would be needed to get more the performance that we desired. Then what happened was that the hardware kept getting faster for the next 25 years anyway. Computer scientists are cute when they are wrong.

	Yes yes, most new computers are multi-core architectures now. You can <a href="http://store.apple.com/us/buy-mac/mac-pro">buy a cute little machine that is shaped like trashcan</a> with 12 blazing hot cores of death in it. Your phone even has two or maybe four cores in it. But these are the same sorts of machines that we were running in the 80s. They even use the same instruction set. No one is running an Intel <a href="http://en.wikipedia.org/wiki/SECD_machine">graph reduction machine</a> or an <a href="http://en.wikipedia.org/wiki/Warren_Abstract_Machine">ARM WAM logic engine</a> with thousands of processors all dancing in a huge data-flow disco party. All of this is of course forgivable because even if they were never built in hardware, these models have been used as the basis for a lot of interesting language ideas. We are always saved by the fact that models can be just as useful as software than as hardware.

4. The type theory cult. The most modern functional languages also make heavy use of ideas from "type theory", or the theory of <a href="http://en.wikipedia.org/wiki/Type_systems">type systems</a> in languages. It's beyond the scope of this page (and my brain) to talk about this deeply, but we can take a short digression into this now.

**Second Digression**: The first thing to say is that even primitive cave-men used types in a basic way. In pre-historic languages like Fortran, C and Pascal, you had a set of basic value types that corresponded to the primitives that the machine understood (integers, floating point, characters, etc) There were also ways to combine these primitives into more complicated compound values to represent more complex data structures (pointers, records/structs, enums, etc). These systems work OK, but require that you explicitly tag every value that you use with a type so that the compiler can check your work. This is tedious, but the extra checking is usually deemed worth it.

The second thing to say is that the most well known early functional languages (Lisp and Scheme) were based on untyped or weakly typed foundations. The idea was to keep the tedious type checking out of the way of the programmer, and do checking at runtime to make things safe.

The third thing to say is that advanced type systems and modern functional languages provide a souped up combination of static checking, much more powerful compositional abilities _and_ the convenience of avoiding mostly useless type annotations. Thus they combine the static checking of some traditional languages (only better) and the relatively flexible programming style of languages like Lisp (only better). Consider that you get features like:

1. Clean generics. That is, types (and functions) that take some unknown type as a parameter, but which are still statically type checked. STL is a weak version of this.

2. Types for functions.

7. Types for describing complex recursive values (abstract data types) and operations on them (pattern matching).

4. Types for higher order program constructs like module systems.

5. Types for describing explicit flow control and state in languages that are otherwise state-free (Haskell! Monads!).

6. Finally, type inference. Type inference allows you to write your code with a minimal number of type annotations. For the most part the compiler _infers_ the types you need to make things work. How does this magic happen? It turns out that you can use a core aspect of any logic programming language (<a href="http://en.wikipedia.org/wiki/Unification_(computer_science)">unification</a>) to build complex type checking engines. The first version of the <a href="http://en.wikipedia.org/wiki/ML_programming_language">ML</a> language got its start in this way. Since then basically all of the interesting modern languages have used a similar engine to build advanced features into their type systems.

**Summary**: Modern functional languages combine the functional evaluation model with rich type systems. The combination creates languages where you can write very little code, and yet make your entire brain explode anyway.

This short catalog of programming models is obviously incomplete. I've left out the scripting languages (you only need to know one anyway), languages associated with specific applications (emacs lisp! that gene sequencing perl thing, Mathematica), some esoterics like database languages and spreadsheets, macro languages, various other things that I'd rather just forget about (php, tcl), and who knows what else.

Luckily, completeness is not my goal and is not needed to illustrate my main point. What you want out of a language ultimately says more about you and the problems you are trying to solve than the language itself. It also tells me how you like to think about problem solving. Each of the models that I've discussed implies a certain way of looking at the world, so what you like to use tells me how you see things. While there are some languages that are literally bad at everything (I'm not naming names, but one of them starts with a P and ends with a P and has an H in the middle), most are good at _something_ and if you need that something then you'll be happy. Thus, if I know what programming language you like then I know what makes you happy.

Beyond that though, programming languages really are not that important in the grand scheme. In general what is more important is the tool and runtime ecosystem that the language is connected to.

Want to write soulless corporate enterprise workflow-ware for the drone army of Windows users? Then .NET and C# is your game (or these days, maybe Javascript and Java). Want to write the next mindlessly addictive mobile tapping simulator? Then (until recently) Objective-C and iOS are for you (or Java and that other thing, whatever). Want to study how to write compilers for advanced languages? Then go to Computer Science School and learn ML, Haskell, or something similar because all those languages are really used for is writing compilers for advanced languages (troll).

The problem is that people tend to confuse "good at the thing that I want to do" with "objectively the best thing for everything", and they become emotionally attached to their own pet issues and litmus tests. Then they evaluate every new tool based on those false standards. Thus you will get complaints that some language is not "purely functional" or "truly object based." Or maybe it has "too much mutability" or suffers from not being "cross platform enough." The problem with these complaints is that it makes no sense to hold them up as universal standards. They only matter if they actually matter.

Which brings me to the one paragraph I wanted to write about Swift. Swift is a reasonably modern, yet pleasingly pragmatic language that you can use to access the Apple runtime for applications. It fixes a lot of things and solves a lot of problems, but mostly it addresses pain that you have only experienced if you have written MacOS or iOS applications in the last ten to fifteen years or so. To me it's also a fairly pretty solution to these problems, assuming they  make it work well. I used to joke that Perl5 was the _only_ way that you could imagine adding objects to Perl4. Swift is a compelling candidate for being _the_ reference design for how to put a modern language on top of Cocoa or UIKit.

So if what you want to do is use language with a lot of interesting modern features (parametric polymorphism, algebraic types and pattern matching, higher order functions, monads) and is also built from the start to work with the current Apple runtimes, then you should be happy with Swift. Otherwise, maybe not. But it really doesn't matter. You'll get by without it, and it will get by without you.


