Title: TeX Nerd
Date: 2020-11-4
Category: Computers
Author: psu

A long time ago when we used to be able to go out to a special building where dozens of people would sit in a dark room together and watch a high quality projection of movies on to large screens, I read an <a href="https://www.nytimes.com/2012/04/29/magazine/how-samuel-l-jackson-became-his-own-genre.html?_r=1&hp&pagewanted=all">NYT profile of one Samuel L. Jackson</a> that had this thrilling paragraph in it:

> As an only child, he went to movies alone, he said, “to be taken out of my place and transported to another world.” Years later, when people questioned why he appeared in one turkey or another, he would answer, “Because it was a movie I’d seen as a kid.” One such dud, a remake of “Shaft,” was so horrible that Jackson was said to have refused to recite his lines because they were written by a white man. “Not true,” he said, when I asked about the incident. “I changed his lines so they’d sound like a black man,” he said. When the author countered that those were the words he had written, according to Jackson, “I said: ‘Yes, and you got paid for them. Now let me make you sound brilliant.’ ” Jackson had to say “the corniest line I ever heard in my life and make it believable,” he told me, and then laughed before delivering it again: “It’s my duty to please that booty.”

I love that one line:

> “I said: ‘Yes, and you got paid for them. Now let me make you sound brilliant.’ ” 

To be honest, if I were a better and more interesting person I'd be using this quote to introduce a much more interesting article than what is about to follow. But I'm just a nerd in Pittsburgh who remembers a little bit too much about how to use $\rm\LaTeX$ so instead the rest of this article is about how to make $\rm\LaTeX$ look better for reading on your iPad. The tenuous connection being my overly developed ego saying to itself 'Yes, arxiv author, you wrote this, now let me make it look decent instead of like trash.'

So with that incredible disappointment out of the way, here are some tips for how to make papers from <a href="https://arxiv.org">the arxiv</a> look nice on screens.

#### The Big Picture

<a href="https://arxiv.org">The arxiv</a> is a giant database that holds "preprints" of scientific papers. In the past a preprint of a paper would be the manuscript that the researcher typed up to send to the journal publisher. If the paper were important enough they might send copies of this "pre-published" or "pre-print" manuscript around to their friends since it could take months or years for the journal version to show up in its final form.

But, by the 1990s almost everyone was using computers to write papers, so why not store electronic preprints somewhere for convenience? <a href="https://arxiv.org">The arxiv</a> was set up by some physicists (of course) <a href="https://en.wikipedia.org/wiki/ArXiv">almost 30 years ago</a> to do just that and now holds an electronic version of almost every physics paper published since the mid 90s (and also many papers from math, computer science, and other areas).

Since most of the papers in <a href="https://arxiv.org">the arxiv</a> are stored there in their $\rm\TeX$ form ... nerds with too much time can noodle on them to make them look better. So here we go.

#### Page Layout

Most preprint papers use either the standard $\rm\LaTeX$ print paper sizes (letter or a4) or whatever page size is appropriate for a journal pre-print (which is also usually letter or a4 with registration marks). The problem with this for screen use (either laptop or iPad) is that in order to set the text at a reasonably readable width you have to have giant margins. This is OK on paper, where you might want the margins for taking notes or something. But on a screen, and especially on the 11 inch iPad screen what you end up with is a tiny box of text in the middle of a sea of whitespace. Which is not ideal.

Luckily $\rm\LaTeX$ has a package called `geometry` that allows you to fairly easily set up whatever global page layout you want. So I have a setup for that which makes the page size roughly match the display size of my iPad with a much smaller bit of margin on each side, since reading edge to edge is no fun.

#### One Column

One annoying legacy feature of journal paper formats is the use of two column page layout to save on paper when the articles are printed. I suppose this is noble in theory, but then why *print* the papers at all? On screens two column layouts are a disaster because only the largest electronic reading devices are big enough to show a full letter or A4 sized page at once and keep the text at a readable size.

So, the only correct thing to do is reflow the layouts to one column. Luckily most of the major journal formats that use two columns have a one column mode, usually for drafts. So use that, then fix the page size, then fix the fact that the draft modes are inevitably going to be double spaced or worse (why??), and then you are golden.

#### Text Size and Such

Most pre-print formats are set up to use ten point type. This is great on paper, but too small for old eyes on a screen. Use twelve point type if possible, but some facts of life will get in your way.

1. Some formats have no 12 point size. Boo.
2. Many papers, esp. those with complicated calculations in them, will have math in them that is too wide if you use the small page size from above along with bigger type. Usually this is not hard, just very tedious, to fix (see below).
3. Some formats have bugs that make 12 point sizes look strange. The most obvious one is the bug in the `revtex` physics journal style where footnotes are all the wrong size if you the 12pt version of the style.
4. If you want the least amount of hassle from $\rm\TeX$'s line breaking algorithms use `\sloppy` to just make it shut up. Similarly `\raggedbottom` is a good idea for page breaks. Otherwise you will get constant complaints about bad line breaks and/or pages with weirdly giant areas of white space between the paragraphs.

One other thing I do here, if the paper is using one of the default formats in $\rm\LaTeX$, is to use the `titlesec` package to shrink the size of the titles and section headers to something more reasonable. The default $\rm\LaTeX$ formats are much too enthusiastic about their headline fonts. I think my dream would be to make all papers take on the minimal understated look of articles from the AMS journals, but in practice that is much too complicated, so we live with what we can get.

#### Fonts

This is currently the most fertile ground for nerding out with $\rm\TeX$. Long gone are the days when the only choice you had was to use the 300dpi pre-generated Metafont bitmaps of the Almost Computer Modern glyphs, or, god forbid, use Postscript text fonts with Computer Modern math fonts (ugh). Now there are a plethora of choices for different font combinations that work in most modern documents. For older files you still have some choices, but it can sometimes be hard to make things work out at the edges. Here are some favorite combinations:

1. Palatino. Here the classic but mostly out of date choice is `mathpazo`, and the newer more modern choice is to use the `newpxtext` and `newpxmath` package. `newpx` depends on things being set up to use the AMS $\rm\LaTeX$ setup for symbols and whatnot, so if that fails for some reason you are out of luck. The newer package also fixes the most egregious problem with `mathpazo` which is that the symbol it uses for `\sum` is horrible. You can hack around this by hand if you are deranged but it's nice not to have to do it.

1. Charter. Charter is another great choice IMHO. You use the `XCharter` package. There are a few choices of math macros that fit well with this font set, just google for how to use it.

1. Lucida. I talked about Lucida <a href="http://mutable-states.com/yak-shaving-and-typography.html">in my previous missive on this topic</a>.

1. Other fonts by Michael Sharpe. <a href="http://math.ucsd.edu/~msharpe/RcntFnts.pdf">Look at this page</a>. That document covers how to use some particularly classic looking fonts like Garamond and Baskerville, for when you want to use $\rm\LaTeX$ to write some treatise with deep 19th century classical thoughts in it.

1. Any of the above with `eulervm` for math. The <a href="https://en.wikipedia.org/wiki/AMS_Euler">Euler math fonts</a> are pretty cool. They were originally designed by Zapf on commission from the AMS and first used by Knuth and Ronald Graham for the book <a href="https://en.wikipedia.org/wiki/Concrete_Mathematics">Concrete Math</a>, which covered various mathematical topics in computer science. I like the upright but swooshy style of it, esp. for papers on category theory for some reason. It fits particularly well with Palatino ... but Charter and Lucida work well too.

OK that's it for fonts.

#### Hyperlinks

The `hyperref` package is great. Among other things it makes citations (references), various sorts of cross references (sections, equations, figure numbers, etc) into PDF hyperlinks so you can easily follow them around the document. Unfortunately its default setup formats these links as little red boxes around the text, which is horrible. So do this instead
	
	\usepackage[colorlinks=true
	,breaklinks=true
	,urlcolor=blue
	,anchorcolor=blue
	,citecolor=blue
	,filecolor=blue
	,linkcolor=blue
	,menucolor=blue
	,linktocpage=true]{hyperref}
	\hypersetup{
		bookmarksopen=true,
		bookmarksnumbered=true,
		bookmarksopenlevel=10
	}

The setup at the end is to populate the TOC of the final pdf with a nice outline for even easier navigation.


#### Other Nonsense

As unbelievable as it sounds, there are dozens of other little details on which you can expend all your excess mental energy if you wish. Here are just a few:

1. Unicode trouble. A lot of files in the arxiv, especially from Europe are stored in some random not ASCII but also not standard Unicode format. As yet I have not come up with an automatic way to fix this shit. It's really annoying.

1. Long Equations. Long equations are annoying, but not hard, to fix. Learn how to use the `align` and `multline` macros from the AMS math setup and you will have a fairly easy time of it. The hardest part of this is actually finding the overflows in the source code and then parsing the math to find a good breakpoint.

1. Graphics. Including graphics has always been a headache in $\rm\TeX$ in general and $\rm\LaTeX$ in particular. There are macro packages for drawing pictures if writing what amounts to raw Postscript (or similar) programs for drawing things is what you like to do in your spare time. What most people do is generate the pictures in some other program and then import them into the final output using the special mechanism in the $\rm\TeX$ engine for these things. In the olden days you would do this with EPSF. These days you suck in PDF. Usually this is not too bad and the modern system does the file conversion for you. But dealing with older documents that use external postscript files can be a hassle if the postscript is not marked up with the right meta-data (e.g. bounding boxes).

1. Again, Use `\sloppy` and `\raggedbottom` to avoid stupid line breaking problems and page layouts that have horribly stretched out whitespace in them.

1. Given the nice automatic navigation features of pdf files, most uses of headers/footers as cookies for where you are in the document are kind of pointless. So I like to use `\pagestyle{plain}` to just remove them and leave a small page number at the bottom of the page instead (which you also don't really need, but is nice).

1. Oh oh oh. Single spacing is always right. I am here to tell you that the time for killing double spacing is now. But, for most fonts you want to tell $\rm\LaTeX$ to use a slightly wider spacing than the default. The easiest thing to do to kill both of these birds at once is to say `\linespread{1.x}` where `x` is some small number like .1 or .05.

1. Dealing with Plain $\rm\TeX$. The oldest papers in the arxiv sometimes still use plain $\rm\TeX$ with the `harvmac` macros. Fixing all of the above things without $\rm\LaTeX$ to help you is hard ... but you can at least fix the double spacing and font size issues if you have a hearty nerd soul. Then save your work in a special copy of `harvmac` so you don't have to think about it again.

1. Finally, store it all in github so you can undo your work if you completely fuck it up.

I think that's all I can think of right now. And surely that is for the best. On the one hand reading this was a total waste of your time. On the other hand, given its day of publication maybe you needed exactly that sort of tedious distraction.

