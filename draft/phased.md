Most large applications have a phased nature. For example, many interactive editing applications like Word, or Keynote run in a loop that's something like this:

1. Take input from the user (mouse, touch, keyboard, etc)

2. Translate input into a command to update the document.

3. Update the document.

4. Inform everyone that the document has been updated.

5. Let the user see what the new version of the document looks like.

This is the classic <a href="">MVC</a> event loop.

So here's a thing that happens a lot. Say you have some piece of user interface displays a simple value computed from the aggregate state of the entire document (i.e. number of words, number of slides, or whatever). Every time the document changes,  you want to recompute this value. So maybe you sign up to be one of the people told in step (4) above that things have changed. When you get the signal, you go and compute your value so that you can display it later in step (5).

But what if this 
