Title: Marginal Added Value
Date: 2008-04-14
Category: Computers
Author: psu

There are two universal rules about people who work in software:

1. Inexperience breeds an unrealistic optimism towards the power of new tools.

2. To offset (1), experience breeds an unrealistic hatred of all tools.

We have seen this cycle play out over and over again in the design, implementation and adoption of instruction sets (remember when those still mattered?), programming languages, operating systems, and end user applications. Back when I was younger and more optimistic about the power of new tools, I used to tinker a lot with scripting languages of various kinds. Over about ten years or so what this experience taught me was very valuable in my later career. The main lesson was this: pick one, learn it, and then stop paying attention. The one I picked to use most at the time was perl. Since then, perl has become a popular punching bag for newer and shinier scripting tools, but I have stuck to my guns. I know perl, therefore there is no reason to learn another scripting language.

Most of the languages that I am concerned with come from the tradition of batch systems on time sharing computers. These allow users to create simple scripts of tasks that they may want to run over and over again and submit them as a whole unit, saving a lot of typing and waiting in front of the terminal. The UNIX shell languages and the scripting tools that evolved from them certainly have this heritage.

Perl, in particular, is nothing if not a utility that combines the functionality of what were historically separate tools (sh, awk, sed, grep) in the UNIX world into a single more efficient and easy to use package if what you needed was a tool to scan and process huge amounts of text in various forms in order to transform it into text in some other form. Perl follows a few simple rules:

1. Don’t get in my way with a lot of extraneous glue that I don’t care about. Perl is very direct. No compilers, no linkers, no type checking.

2. Process text well. This is my “equal twiddle” rule, referring to the operator in perl (=~) that triggers regular expression matching and replacement of text. In my mind, a script language must have a concise way to do this. I don’t want to have to type out regularExpression.matchThisStringPlease() when I mean =~.

3. Handle iteration and files well. Most tasks that perl is well suited for involve processing large areas of the file system. Make sure this is streamlined.

4. Simple general purpose data structures. In other words, hash tables.

5. Make every feature useful. I’m not going to learn how to use all of them, but if I do there should be a good reason for it.

At their core, scripting languages are all designed around one idea: making writing quick programs easier. A high level of utility is prioritized over cleaner syntax, rich type systems with rigorous type checking, and features that are needed to scale the size of programs or the teams working on them. In my opinion, the designer of perl understood these tradeoffs almost intuitively and usually made the right choices in the core of the language itself. Yes there are warts, but find me any system without them.

With this background, it is clear why I stopped paying attention to scripting languages. They are all designed with these tradeoffs in mind. Therefore, they all make weird compromises to increase the utility to code density. Therefore, you are guaranteed to have to learn some idiosyncratic way of thinking or working in order to deal with these tradeoffs. Therefore, you should only do it once.

There are certainly many other scripting languages. Some, like tcl, are not worth mentioning except to spit in the face of anyone who ever worked to propagate that particular demon seed. Others, like python and ruby claim to be “like perl only cleaner”. And yet these claims never hold up. Once the rubber hits the road, every one of these newer tools has some brain damage of its own, and each of them falls backwards on the utility scale by breaking one of the rules above. In particular, most fail the equal twiddle rule, but there are other examples. Python has its psychotic use of white space to determine lexical scope. Ruby has a lot of useless tinkering with modern language features like closures and continuations, except that it does not get them right. So why bother?

But, don’t let me make your decisions for you. I picked up perl because at the time I did there was nothing else that did as much as easily. You young people have a wider variety of choices to make, so go out and pick something that appeals to your sense of aesthetics and design. Just make sure you remember two things:

1. When push comes to shove, not having =~ will piss you off.

2. Whatever you do, only learn one. It’s just not worth the time and the brain space to do more.