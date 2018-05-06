**The Basics**

In physics up until the turn of the century, the world was modeled using and idealized notion of "particles" or "states" that evolved in a a perfectly deterministic way according to differential equations. So you push your point mass around with some force and you get equations like

$$
F = ma
$$

for the relationship between the force and the acceleration. Recall that acceleration is the second time derivative of position, so this is really

$$
 F = m {d^2x \over dt^2}
$$

where $x$ is a real number representing the position of the particle at any given time.

In quantum mechanics things are more complicated. To explain the various and sometimes rather strange experimental results in QM (i.e. the <a href="http://www.feynmanlectures.caltech.edu/III_01.html">two-slit experiment</a>), we use a somewhat different set of mathematical formalisms. 

1. Instead of particles with simple and exact states, you have a set of *quantum states* or *state vectors* that belong to a "Hilbert Space" that we will call $H$. You can think of these states as a list of numbers, perhaps infinitely long, that describe all possible aspects of a system's state.

2. Instead of real numbers, quantum states keep track of complex numbers. We are not going to make use of this fact that much here, but it is worth mentioning because it is a critical and profound piece of structure in the formalism.

3. We write quantum states with a curious bracket notation, like this: $\left| \psi \right>$. We call these "kets" or "vectors" or "ket vectors", depending on how we feel at the time.

4. The other half of the "ket" formalism are objects write like this: $\left < a \right |$. These objects come from  what is called the "dual space" of the Hilbert Space, usually written $H^*$. The dual space is made up of functions that take a vector as an argument and return a complex number. We call these objects dual vectors, or bras, depending on how we feel. When you stick a bra and a ket together, you get a "bra-ket" (get it?) that looks like this: $\langle a\, | \, b \rangle$. This notation denotes bra (which is a function) acting on the ket and returning a complex number. It's also the case that if you have two kets, $\left| a \right>$ and $\left| b \right>$ then you can use the inner product to identify (say) the vector $a$ with the dual vector that maps $b$ to $a \cdot b$. In other words $\langle a\, | \, b \rangle$ = $a \cdot b$. Thus in some sense the Hilbert space $H$ is its own dual.

5. For systems made up of a single particle that moves in the $x$ direction, like the above example, the quantum state is identified with a _wave function_ $\psi (x)$. We define this function like this: $\psi (x) = \langle x \,|\, \psi \rangle$. Exactly how the $x$ ends up as a dual vector is a small detail that I will not explain right now. In this form the function $\psi$ maps $x$ to a complex number called a *probablity amplitude* that is related to the probability that the particle appears at any given position $x$ when you measure it. More on this in a bit.

For more information on what is going on here, you can <a href="https://en.wikipedia.org/wiki/Bra–ket_notation">read this tutorial</a> or <a href="http://ocw.mit.edu/courses/physics/8-05-quantum-physics-ii-fall-2013/lecture-notes/MIT8_05F13_Chap_04.pdf">this one</a> which is mathematically deeper or <a href="http://www.physics.wustl.edu/alford/physics/essentials.pdf">this one</a>, which discusses states and probabilities a bit.

**Digression:** Physics texts tend to play fast and loose with the exact nature of the Hilbert space, implicitly redefining it to suit their purpose. One minute it will be set up to represent position and momentum (continuous values that require that the space be infinite dimensional) and the next we'll be talking about spin spaces that have a finite number of values. This is a running theme them trying to read the math that physicists write: half the battle is figuring out what kind of object they are talking about.

6. Properties that can be measured are modeled using "observables" which are linear mappings on the state vectors. Observables are actually more than just linear mappings, they also have to have some important symmetry properties that I'm not going to go into. You get well-defined values from measurements when you get lucky and find a quantum state that behaves like this when hit with the operator for some observable $O$:
	$$
	O\, |\, \psi \rangle = a\, |\, \psi\rangle
	$$
	where $a$ is some constant. What the formula means is "$O$ applied to the vector $\left| \psi \right>$ is some constant times the vector $\left| \psi \right>$". In math such a vector is called an "eigenvector" of the operator $E$ and the constant $a$ is called an "eigenvalue". In QM measurements that produce well-defined values always involve eigenvectors and eigenvalues.

7. When measuring observable values, the probability amplitudes of the wave function are such that the probability of measuring any given value can be computed by $\langle \psi\, |\, O \rangle^2$. In the case of the position example above, we can interpret this as meaning that the probability that you find the particle at a given location is given by $| \psi(x) |^2$. This is the *Born Rule* which relates the probality amplitudes of the wave function with the probability distribution of the results of measurements.

This lets you explain all the weird Feynman things.