Title: Useful Libraries
Date: 2009-06-21

There's nothing better than finding a library that does exactly what you're
looking for with a clean and sane API. I'll gradually add to this posting as
it strikes me.

Libraries I Like
----------------

**[flot](http://code.google.com/p/flot/)** A pure canvas/JS plotting library
that is very flexible and generates pretty graphs. It's API is clean and very
javascript-esque. One particularly nice feature that's not present in a lot of
plotting libraries, but I use all the time, is handling times and dates.

Libraries I Haven't Tried--Yet
------------------------------

These libraries look interesting if I ever need them. I haven't tried them
yet, so no endorsements, but they look good.

**[Really Simple History](http://code.google.com/p/reallysimplehistory/)**
"Really Simple History is a lightweight JavaScript library for the management
of bookmarking and browser history in Ajax/DHTML applications."

**[Candygram](http://candygram.sourceforge.net/)** "Candygram is a Python
implementation of Erlang concurrency primitives. Erlang is widely respected
for its elegant built-in facilities for concurrent programming. This package
attempts to emulate those facilities as closely as possible in Python." I
really like Erlang style concurrency so this library immediately appeals. On
the downside, it's [current implementation is rather
heavyweight](http://mail.python.org/pipermail/python-3000/2006-September/003718.html)
and it [hasn't been updated since 2004](http://candygram.sourceforge.net/). I
can't get the repo without CVS... eww.

**[pysage](http://code.google.com/p/pysage/)** "pysage is a lightweight
high-level message passing [Python] library supporting actor based
concurrency." This project is more active than Candygram as well as a bit more
Pythonic. From what I've examined of the API, pysage makes a distinction
between messages that go across the network and those that do not, which irks
me a bit. I need to dig further to substantiate this, however.

**[Pyro](http://pyro.sourceforge.net/)** "Pyro is short for PYthon Remote
Objects." Not as elegant as message passing, but it gets the job done.
