The second theme is that the enemy of simplicity is scale. In 1981 a single person could build an entire consumer computing system almost from the bare circuits up through all of the code in the base operating system that the user interacted with, and you could describe the whole thing in a 200 page book, complete with a full memory map. Now there might be more people working on your serial connector than built the entire Apple II.

These two aspects of the difference between then and now are both orthogonal and related and I'm going to address the first one directly and the second one only by implication later.

The engine that made that magic possible was dynamics on two levels.

1. Dynamic dispatch in the language runtime. This is the standard and age-old OO mechanism of picking what version of a function to run based on the type of the object that is performing task. This is a big and powerful hammer, though it tends to be overused and too blunt (IMHO).

2. Dynamic meta-programming of various kinds, from querying type information at runtime up to (depending on how evil you are) completely replacing implementations of basic functionality with your own code by nefarious means. These mechanisms are built on top of the basic dispatcher above, but can be used to built more complicated runtime dispatch mechanisms, like the magic connectors in Interface Builder.

So now when people talk about wanting "dynamic" languages they tend to list a spectrum of requirements that must exist before they are happy:

1. Minimal tedious type annotations in the source code.

2. Language-supported dynamic dispatch systems, like the method dispatch mechanisms in Smalltalk and Objective-C. 

3. Dynamic meta-programming.

In practice people tend to be willing to give up (1) first. The evidence for this is that all of the languages that ended up in wide use were "static" enough that they tended to need type annotations, but people were willing to pay that price. Or, at least they found no language that didn't require such annotations to be useful enough to actually use to build a large system.

Most hard-core OO programmers will give up inheritance and dynamic dispatch over their code dead bodies.