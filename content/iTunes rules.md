Title: iTunes Rules
Date: 2007-01-11
Category: Things
Author: psu

<p>iTunes told me today that it has 440 albums in its database. That number seemed high to me, but I have been ripping the occasional disk once in a while ever since I got my iMac two years ago. And, every new disk I buy generally goes into the machine. After bootstrapping the <a href="http://mutable-states.com/the-one-true-index.html">one true indexing system</a>, I have been more motivated to actually rip and catalog the disks. While iTunes is not the ideal catalog database, you can muddle through by following some simple workflow rules. The goal is to have the music be easy to browse and search on both the main iTunes machine and in the iPod.<br />
<span id="more-747"></span><a></a></p>
<p>The first rule is that there are only three genres of music:</p>
<p>1. Pop</p>
<p>2. Jazz</p>
<p>3. Classical</p>
<p>I reject the ludicrous and neurotic over-categorization of music. Especially popular music. So, R&#038;B is pop. Blues is pop. Electronic Trance Drool Dance Laser Techno Jerk-Off Ska Vocal Sampling &#8230; is pop.</p>
<p>The reason for this is simple. It makes it easy to construct shuffle playlists, party shuffle lists, autofill lists, and so on. I don&#8217;t have time to sit there and write complicated queries to match against every freak&#8217;s idea of what the correct set of genres is. Having only three makes this easy.</p>
<p>The second rule is: the iTunes data model is fairly simple, so aggressively de-normalize the data. This is especially true for Classical music where the single artist single song model really breaks down. If you are not careful, you&#8217;ll go and browse albums or songs on the iPod and see 50,000 titles called &#8220;String Quartet XYZ in B Major&#8221; and so on. This is useless. The solution is to put the key artist or composer in every field of the database so they will show up in all major views in both iTunes and on the iPod. Of course, you have to do some work to be careful and keep your de-normalized formats as uniform as possible. Life is hard.</p>
<p>Sadly, almost no one who uses the <a href="http://www.tleaves.com/weblog/archives/000296.html">CDDB</a> follows these rules, so for most Classical records, you have to completely rewrite the meta-data.</p>
<p>The third rule is: Multiple disk albums count as one album. Do not put the disk number in the title. This will make iTunes think it&#8217;s a completely different album, which is sort of stupid.  Instead, use the &#8220;Disk N of M&#8221; meta-data fields. I forget about this rule from time to time and have to go fix things.</p>
<p>The final rule is: if you have a filing system for CDs, put the CD into the filing system <em>immediately</em> after you rip it. I never follow this rule, so my disks are all over the house in little piles and I can never find anything. It&#8217;s getting better though. I have about 140 disks filed now. So I guess I have about <strike>400</strike>300 to go to catch up to my iTunes database.</p>