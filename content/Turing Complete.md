Title: Turing Complete
Date: 2015-02-15
Category: Computers
Author: psu

As part of his future dork training, we took the boy to see <a href="http://www.imdb.com/title/tt2084970/">The Imitation Game</a>. This film is essentially a work of fiction loosely based on the life of Alan Turing. Though almost completely conventional in its structure and outlook, the film was enjoyable enough, I guess. It's interesting to observe what movie people think you need to do to the life and character of a relatively reserved British mathematician in order to generate the raw material needed for some end-of-year Oscar bait. Maybe they are really that cynical, but it's hard to tell from just this movie alone. I'm not about to turn around and go see the Stephen Hawking movie to find out though. Still, it's a bit depressing to see one of the fathers of computer science reduced to being just another "tragic male lead in a slightly epic romantic film." I imagine that they did something similar to Hawking. 

Although I finished an advanced degree in computer science, I never really went back and investigated Turing's original work. Of course we are all taught about Turing Machines and their role in proving some of the basic results in theoretical computer science. But theoretical computer science was not really my area, and the courses that you take in it as a student boil down the essentials of his achievement into just enough information for you to move forward and pass the theory qual. But, the movie piqued my curiosity so I went poking around a little and found the paper that originally defined the notion of a Turing Machine. This paper was published in 1936 and is called <a href="href="http://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf">*On Computable Numbers with an Application to the Entscheidungsproblem*</a>. So that's mouthful.

Some background:

The early 20th century was a time of some upheaval in both mathematics and physics. Before, say, the 1920s, people had become reasonably convinced that we had figured it all out. Of course, this did not turn out to be the case. In physics we ran into quantum mechanics, which is still confusing people to this day. And in mathematics there was the whole Gödel thing.

<a hrf="http://en.wikipedia.org/wiki/Kurt_Gödel">Kurt Gödel</a> was an Austrian logician who the lay-geek will mostly know for two things:

1. He's one third of the title of that book Gödel, Escher, Bach.

2. He proved something interesting about formal logic in the 1930s, but I'm not sure quite what. But it had something to do with the book.

What Gödel did was come up with part of an answer for <a href="http://en.wikipedia.org/wiki/Hilbert%27s_second_problem">Hilbert's Second Problem</a>. This problem is concerned with whether you can define a formal system in which you can prove all the things about mathematics. Hilbert was of the opinion that the construction of such a system was possible, and presented the problem to push the people of the time to get to work on finding it.

Gödel showed that you cannot do this. His theorem states, roughly, that any formal system that can model arithmetic can also be used to prove the existence of a theorem within the system that the system itself cannot prove to be true. In particular, Gödel demonstrated that the formal system in <a href="http://en.wikipedia.org/wiki/Principia_Mathematica"</a>Principia Mathematica</a>, which hoped to define a framework in which one could prove every true statement about mathematics, had to be incomplete in this sense.

What Turing was concerned with was the additional question of whether you could automatically compute whether a given statement in a formal system is provable or not. Turing's paper shows that you cannot do this, and so the dream of solving all of mathematics died.

Interestingly, it turns out that a few people independently came to this same conclusion at nearly the same time. In particular, the computer scientists in the audience should have been screaming "What about Church!!???!!!" at me for the last two paragraphs. Church published a similar result at Princeton in 1935, but the formalism that he used was completely different from Turing's, so Turing's work was accepted as independent. What Church used was the &#955;-calculus, which we all know and love as the second major formal model for all of computation and most modern programming languages. When Turing's paper was finally he published he actually added an appendix that contained a proof-let that Turing machines and the &#955;-calculus are in fact equivalent.

I'm not going to go into all of the minutiae of Turing's method. But I encourage anyone who is interested to track down the paper (here is a <a href="http://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf">link</a>). The beginning of the paper sets up a formal system that he will use to prove the larger theoretical results at the end. The model is so simple and elegant that you can describe it to a smart third grader, and yet it turned out to be powerful enough to essentially capture all of the essential aspects of computer programming, which would not be invented for at least another decade.

Recall that a Turing Machine is made up of three basic parts:

1. An infinitely long *tape* divided into squares.

2. A read/write head that can read and write symbols on the tape.

3. A finite state machine attached to the head. The state machine is controlled using a table.

In his paper Turing defines the control table as a matrix with four columns. The first column represents the current state of the machine. The second column represents the symbol on the tape. The third column indicates the action that the machine should take given the values in the first two. The last column indicates what *new* state the machine should move to.

The machine can perform the following actions:

1. Erase the symbol on the tape.

2. Write a new symbol on the tape.

3. Move the read/write head one square Left

	or

4. Move the read/write head one square right.

Of course, this is just a simple computer. But Turing did not create this model as an abstraction of some existing stored program digital computer. Such things didn't exist yet. What he did was create an idealized version of what a human "computer" solving some simple math problem might look like. Yet, in this paper he is able to take his simple model and build many of the same artifacts that systems programmers all over the world would spend the next 50 years re-creating. For example:

1. Subroutine "macros" for frequently used functions, and a mechanized way to, essentially, recursively expand these macros until you have reached the base form of the instruction table.

2. A way to represent programs in a machine readable form. This is essentially like machine code, and thus takes the form of a large string of digits. Turing uses this to work out his answer to Hilbert's decidability question.  

3. Given the above representation a way to build a single machine that could emulate any other machine. He doesn't use these words in the paper, but this section really makes you think "virtual machines".

Even though it is in a simplified and abstract form, you can't help but think you are really staring at something that is essentially equivalent to the sort of stack that we use now to write programs, though of course modern tools support programs on a much larger scale and are much much much easier to use. All that is missing is the hardware platform on which to actually run the programs. The software engineer in me finds this much more fascinating than the rest of the paper, even though the rest of the paper essentially lays down the entire theoretical foundations of the entire field.

Turing takes his abstraction and uses it to prove the main theoretical results in the paper:

1. First, that the halting problem is undecidable. That is, you cannot build a general program that can decide whether any other program will halt or not. He does this using the same sort of <a href="http://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument">diagonalization argument</a> that Gödel used. The proof as presented is a bit different in style than the standard proof you see in modern texts. It's interesting to wrap your head around it.

2. Second, he showed that you cannot use one of his machines to solve Hilbert's decidability problem. He does this by reducing the issue to a version of the halting problem.

3. Finally, as I mentioned, he shows that his machines and the &#955;-calculus are equivalent.

While he's at it he also hints at future formalisms that will come into use in complexity theory, like non-deterministic machines. Although he doesn't explore that idea very much.

All of this happens in a relatively compact 35 pages of text, much of which is taken up by example program tables, his standard library of Turing Machine utility functions ("replace all occurrences of the letter X with the letter Y", and so on), and the actual definition of the universal machine. To me this is a tour de force of imagination and insight, especially when you consider that, as I've said now over and over, there *were no actual computers yet*. My primitive primate brain can't comprehend how you create such elegant abstractions without concrete experience. But, after all, that's why they haven't named an <a href="http://amturing.acm.org/byyear.cfm">ACM lifetime achievement award</a> after me.

**Further Reading**: For a more detailed discussion of Turing and his writing, try these books:

1. <a href="http://www.amazon.com/Alan-Turing-Enigma-Inspired-Imitation/dp/069116472X/">Alan Turing: The Enigma</a>. This is the biography that was adapted as fiction for the movie.

2. <a href="http://www.amazon.com/Essential-Turing-Philosophy-Artificial-Intelligence/dp/0198250800/">The Essential Turing</a>. A collection of several of Turing's papers, with notes.

3. <a href="http://www.amazon.com/Annotated-Turing-Through-Historic-Computability/dp/0470229055/">The Annotated Turing</a>. Noted Microsoft Windows programming guru Charles Petzold explains everything in Turing's 1936 paper in a remarkable amount of detail.