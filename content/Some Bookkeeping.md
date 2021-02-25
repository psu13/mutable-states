Title: Some Bookkeeping
Date: 2021-02-25
Category: Computers
Author: psu

It's hard to believe but this "new" site is now halfway into its 8th year of existence. Back then I somewhat arbitrarily chose <a href="https://blog.getpelican.com">Pelican</a> as the tool to generate these pages because it was easy to set up and had a web site template that I liked. I tried it out on some test content and it fit well with my main goals for running this site which were that to put up a page what I wanted to do was:

1. Write some words in a text file on my laptop.
2. Run the generator once.
3. Run `rsync` to push the new stuff up.

I don't care about remote editing, automatically pushing from a github repo, having multiple authors, or anything that makes the site more complicated than the above. Overall Pelican has been fine.

At some point I added a module to do $\TeX$ markup for math. At some point I made a backup copy of the repository on github. I fought with the shitty CSS a bit over the years ("shitty CSS" is of course redundant, what a cursed system). But mostly I did not think about how the site works.

Of course in my relative ignorance I did not realize that I had made one perhaps crucial mistake in my initial setup... the code was running in Python *2* which I guess people have been trying to kill for the better part of a decade. So at some point I would have to figure out how to update that. Updating software is, of course, horrible but inevitable.

The number one rule for updating software is this: Update your software as little as possible and if everything is working find then wait until you _have no other choice_ before doing anything. Even then do it in small steps so you know it will work.

I've been thinking about the python3 issue for about the last three or four years, but I knew I'd have to do it around now because they will soon be removing Python 2 form macOS installs.

My git history says that in 2016 I did a dry run of this by setting up the software for the site in a python virtual environment. This is a neat hack that installs all the binaries and libraries for a project in a single local place rather than in the system install. You can then mess around with how things are set up without destroying your machine. It also makes it easy to set up multiple trial installs to see how things will work. After doing this I was fairly confident that to move to Python 3 all I would have to do is

1. Make a new `virtualenv` with python3
2. Install `pelican` in it.
3. Install `render_math` in it for $\TeX$ via MathJax.
4. Copy everything else over.
5. Generate the site and make sure it looks right.

So this week I finally did that. But with one tweak

1. Make a new `virtualenv` with python3
2. Install `pelican` in it.
3. Install `pelican_jsmath` in it for $\TeX$ via <a href="https://katex.org>$\KaTeX$</a>.
4. Copy everything else over.
5. Generate the site and make sure it looks right.

And sure enough it worked. Kudos to all involved.

Anyway, this page is here just so I can remember how to set things up again if I need to. Really I could have just posted those five lines above. But since this is a blog we have to pad things out a bit.

**Note**: It's amazing to me that we live in a world where there are *multiple* ways to embed $\TeX$ markup inside HTML content. For my purposes the main reasons to use $\KaTeX$ over MathJax are that it's a lot faster, it has nicer fonts, and it's easier to serve up your own local copy of the code rather than fetching it from the Internet all the time. I have not set up that last part yet ... maybe some day.

**Second Note**: While I dithered about this I considered moving to a different tool for reading markdown and burping out HTML. The main reason I never moved to anything else was that I would have to somehow interact with the shitty CSS to make the site look right again. The only way I would even consider doing that is if the new tool were three orders of magnitude better than Pelican. But if that were true then it would be able to read my current site and set itself up completely automatically, making the whole question moot. So I apologize to Jekyll, hugo, pandoc and the rest. But you are not there yet.
