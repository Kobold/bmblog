Type: page
Title: Useful Libraries
Date: 2009-06-30

There's nothing better than finding a library that does exactly what you're
looking for with a clean and sane API. I'll gradually add to this posting as
it strikes me.

Libraries I Like
----------------

**[Fabric](http://fabfile.org/)** "Fabric is a Python library and command-line
tool designed to streamline deploying applications or performing system
administration tasks via the SSH protocol." I wanted to get into Capistrano,
but it's Rails-oriented and I do Python stuff. I could [adapt it to
Django](http://playgroundblues.com/posts/2008/mar/17/capistrano-rules/), but
why leave Python? Especially after the latest refactoring, Fabric does
everything I want it to do and it does it well. I'm not really a shell
scripter, so being able to use Python to slice-'n-dice in Fabric scripts is
doubly nice for me.

**[chain.js](http://wiki.github.com/raid-ox/chain.js/)** This is javascript
templating done right. Rather than the usual templating languages that are a
mishmash of markup and javascript, this is a simple declarative way to splat
data into your HTML.

**[flot](http://code.google.com/p/flot/)** A pure canvas/JS plotting library
that is very flexible and generates pretty graphs. It's API is clean and very
javascript-esque. One particularly nice feature that's not present in a lot of
plotting libraries, but I use all the time, is handling times and dates.

Libraries I Haven't Tried--Yet
------------------------------

These libraries look interesting if I ever need them. I haven't tried them
yet, so no endorsements, but they look good.

**[Synesketch](http://www.synesketch.krcadinac.com/)** OMG, so cool. It's a
text textual emotion recognition and visualization engine. What does that
mean? Have a look at [some of Syneketch's pictures](
http://www.natpryce.com/articles/000748.html). I can't wait to make something
with it!

**[Really Simple History](http://code.google.com/p/reallysimplehistory/)**
"Really Simple History is a lightweight JavaScript library for the management
of bookmarking and browser history in Ajax/DHTML applications."

**[Underscore](http://documentcloud.github.com/underscore/)** "Underscore is a
utility-belt library for Javascript that provides a lot of the functional
programming support that you would expect in Prototype.js (or Ruby), but
without extending any of the built-in Javascript objects."

**[Candygram](http://candygram.sourceforge.net/)** "Candygram is a Python
implementation of Erlang concurrency primitives. Erlang is widely respected
for its elegant built-in facilities for concurrent programming. This package
attempts to emulate those facilities as closely as possible in Python." I
really like Erlang style concurrency so this library immediately appeals. On
the downside, it's [current implementation is rather
heavyweight](http://mail.python.org/pipermail/python-3000/2006-September/003718.html)
and it [hasn't been updated since 2004](http://candygram.sourceforge.net/). I
can't get the repo without CVS... eww.

**[Hashdot](http://hashdot.sourceforge.net/)** "Hashdot elevates Java-platform
script interpreters to first class status on Unix-like operating systems. It
provides a script aware replacement to the stock `java` launcher, and thus
avoids numerous issues in using the `java` launcher to bootstrap a script
interpreter." When experimenting with Clojure I ended up writing my own shell
script launcher to solve exactly this problem. I found this via [technomancy](http://technomancy.us/121).

**[Protovis](http://vis.stanford.edu/protovis/)** "is a visualization toolkit
for JavaScript using SVG. It takes a graphical approach to data visualization,
composing custom views of data with simple graphical primitives like bars and
dots." Pretty. The more ways to do pretty stuff via javascript, the better.


**[Ottoman](http://bitbucket.org/snej/ottoman/wiki/Home)** "Ottoman is
a lightweight, reliable key-value store with multi-version concurrency
control."
