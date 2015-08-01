Title: The Ultimate Goto
Date: 2010-11-17
Category: Computers
Author: psu

When I was in college I was something of a programming languages hobbyist. I think all young dorks go through this phase. Programming languages are fascinating repositories of different ideas for creating <a href="http://mutable-states.com/the-abstraction-distraction-part-1.html">abstractions</a> for constructs that programmers find themselves building over and over again. Back in the day, one of my favorite papers was the Guy Steele title whose short form is just <a href="http://dspace.mit.edu/bitstream/handle/1721.1/5753/AIM-443.pdf?sequence=2">LAMBDA: The Ultimate GOTO</a>. The title is fantastic because it brings together several disparate trains of thought on how programming languages work and combines them into a single statement. Lambda? Goto? What do these have to do with one another? Therein lies a story.

Computers, <a href="http://mutable-states.com/what-computers-do.html">you will recall</a>, work by  fetching a stream of instructions from some kind of memory and executing these instructions one at a time until they come to the end of the stream or the universe ends, whichever comes first. Computers would not be very interesting if <em>all</em> they could do was follow a single "straight line" of instructions though. If this were the case, all they would be able to do is perform the same computation over and over again. What makes computers interesting is that they can examine their input and make <em>decisions</em> about what to do based on what is presented to them. In programming lingo this is called "flow control."

You need two kinds of instructions to implement flow control. First, you need some way to evaluate boolean expressions. For example, you want to be able to ask "Hey computer, is this number I gave you bigger than 10?". Or maybe "hey computer, did I just touch the iPad screen on top of that button?".  Next, you need a way to jump from wherever you are in the instruction stream to some other location in the instruction stream based on the result of a conditional expression. This jump is what we call a "goto" instruction. You say, "Hey computer, if that value is bigger than 10 GOTO memory location 55 and begin executing whatever instruction is sitting there instead of the one that is right after me."

If you combine memory (that is, a way to save state), conditions and GOTO, you can compute everything that is computable... in the sense that you can emulate any computing machine that man has dreamed up in the past, and will dream up in the future. Alan Turing figured this out back in the day, but that's a different article.

Unfortunately, <em>only</em> having memory, conditions, and GOTO is a tedious way to go through life. Programs built on such a simple infrastructure are hard to organize and difficult to understand. What you'd like to be able to do is organize your program into smaller bits called <em>functions</em> and have these functions be executable from other bits of code. That is, you'd like to be able to have the computer <em>save your spot</em> in whatever code was currently executing and jump somewhere else to do something, and then automatically jump back to where you were in the first place. Why would you want this? Most programs need perform many common tasks, like reading and writing files, or making connections to the Internet. Rather than making every program implement these tasks separately we can just write the code once and stash it away somewhere. Then whenever some program needs to use it we can use this "jump then return" mechanism to jump into the code and then return. This way we can build up a "library" of reusable code snippets for useful things.

Happily, most computers implement just such a instruction. In the venerable 6502 chip, that instruction was called "JSR" which means "jump to subroutine" which is a weird way of saying "jump over there, but save your place so you can return." The 6502 had another instruction called "RTS" which basically just jumped to the last place you saved.

Most programming languages have similar high level mechanisms for building functions or procedures that use these hardware instructions. Typically a function is defined to take a few arguments that the caller provides. These can be used to change the behavior of the function as it executes. So, the function you call to handle the fact that the user just touched a button might take the name of the button that was pushed, so you know what command to run. Once you have hardware instructions like JSR and RTS, it's pretty easy to build up a high level notion of functions. You just need to define conventions for how to manage arguments and results, which is tedious, but not complicated.

Early in the history of computing it was thought that function calls (or procedure calls, as Guy Steele calls them) were relatively expensive. What was actually the case was that they were just implemented badly. This fact is the main subject of the paper referenced above. Steele notes that when you think about procedure calls correctly, all you are really doing is saving some state and then using GOTO to jump to a new place in your program. In 1977, this was a pretty radical idea.

Reading the paper, you might now think, "well, that explains the whole 'Debunking the Expensive Procedure Call Myth' thing, but what about 'The Ultimate GOTO'". Well, that's a longer story.

Functions are so useful that a bunch of clever language designers, including Guy Steele, got to thinking about whether you could define an entire programming language that was completely centered around the idea of function evaluation rather than the more typical "set this value in this memory location and go run that code" programming structure that we are all more used to. To this end, they began to play around with a simple abstract notation called the "lambda calculus" that expresses function evaluation in a way that seems completely different from the operational jump and return dance that I described above.

In the lambda calculus, you write a function in terms of the values that it takes as arguments and the values that it returns as results. The "lambda" in the lambda calculus is an operator that binds names to values. So, you might write a simple function like this:

    (lambda (x) . (x + 1))

This takes a single argument "x" and returns the value that you get by evaluating the expression "x+1&#8243;. In other words, it adds 1 to the argument. You might write something like

    (lambda (x) . (x + 1)) 10

which will evaluate the function we wrote with the argument "10". First, the value "10" is bound to the argument "x". Then we evaluate the expression in the function itself, and we get 11.

Surprisingly, it turns out that if all you have is some rules for binding and evaluation and a few primitive functions, you can take any program at all and translate it into the lambda calculus. But that's a subject for a course in theoretical computer science.  Not so surprisingly, actually writing programs in lambda calculus gets tedious quickly. As with the primitive machine language, you need some higher level languages that let you organize programs into smaller bits that are more easily understood. One such language is called Scheme and happens to be the one that Guy Steele was interested in at the time he wrote his paper.

Scheme programs look a lot like lambda calculus. The function above might be written like this

    (define add-one (lambda (x) (+ x 1)))

Then when you evaluate the expression 

    (add-one 10)

you'd get back the value 11. Easy. Scheme defines various rules for binding values to arguments, and you can think of the evaluation engine as just a fancy and more featureful version of the simple lambda calculus.

One of the more novel ideas implemented in Scheme was the notion that functions themselves would be manipulated as primitive values in the language. This is a natural outgrowth of the language's basis in the lambda calculus. Consider the code above. What we are really doing there is taking the name <em>add-one</em> and binding it to a value which is the function defined by the lambda expression. There are some tricky mechanical issues involved in implementing a mechanism like this. The main issue is that you need a way to capture bindings for all names that appear in the body of the function, even those that are not defined as arguments to the function. I'm not going to get into the details of where such bindings come from, or exactly how you implement this capture scheme. Let's just assume that we have a magic box that does the right thing, and let's call that box a "closure".

In other words, an expression like <em>(lambda (x) (&#8230;))</em> constructs a special object which first captures bindings for all the names in the body of the function and then transfers control of the program to the function itself. But wait. That sounds a lot like the simple procedure call mechanism that we defined on our simple memory and GOTO machine. In the context of this paper, the phrase "The Ultimate GOTO" is used to illustrate that while procedure calls and GOTOs seem very different, in fact they are not.

But there is more to it that this. 

Recall how our simple abstract machine implements function calls:

1. Save values for arguments.

2. Save location to return to.

3. GOTO the code for the function

4. At the end of the function, save the return value of the function and then GOTO the location you saved in step 2.

Suppose we think about this process slightly differently:

1. Save values for arguments

2. Save a function value that represents a function to call with the result

3. GOTO the code for the function

4. At the end of the function, call the function value you saved in (2) with the result of your computation as an argument.

The new forms of steps (2) and (4) seem on the surface to be different than before. But really they are not. As we have already seen, function calls and GOTOs are really the same thing. This is a pretty old idea, and the theorists call the  function that we create in step (2) a <em>continuation</em>.

In later papers on Scheme, Steele and others observed that you could create very efficient implementations of Scheme by structuring the runtime to transform procedures and procedure calls into what they called "continuation passing style". All this means is that all of the functions are transformed into something like the second form above. In other words, all of the code in a Scheme program is twisted around so that all the function calls have an extra argument that is a function value  that represents "where to go next."

But, Scheme programs are nothing but function calls, so this means that the "where to go next" function is always available to the runtime. It's sitting right there, since we created it to implement the function call in the first place. Therefore, Scheme also defined a special construct called "call with current continuation" (or call/cc) that allowed the programmer to explicitly capture the "where to go next" function and pass it wherever you wanted. When called, this captured function would restore the state of the program to be exactly the same as it was when the function was captured.  This is a fantastically powerful and psychotic mechanism. Having access to the current continuation lets you capture and manipulate the control state of your programs <em>any way you want</em>. Iteration, recursion, exception handling, multiple threads of control and any other control construct that you can imagine can be implemented using this mechanism. In other words, lambda really is the ultimate GOTO.

<h4>Extra Notes</h4>
Scheme is not the only language that has call/cc. ML is another famous one.

Closures have made their way into more mainstream languages: Java, C#, and Objective  C among others all have constructs that are similar to closures. As far as I know, there isn't really anything like continuations outside of the functional languages, although setjmp/longmp in C is similar, but not as "clean". This is probably for the best, since esoteric mechanisms for creating odd flows of control tend to be used only for evil.

I had always assumed that the idea of the continuation had originated with the work on Lisp and Scheme, but I was wrong. It's actually a much older idea, <a href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.135.4705&amp;rep=rep1&amp;type=pdf">as discussed in this paper by John Reynolds</a>, the notable programming languages researcher at CMU. The use of continuations in implementing Scheme is discussed in <a href="http://dspace.mit.edu/bitstream/handle/1721.1/5794/AIM-349.pdf?sequence=2">this paper by Sussman and Steele</a>.

Who said weblogs aren't educational?

