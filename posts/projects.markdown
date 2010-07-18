Type: page
Title: My Projects

## 2010

**[Real Time Farms](http://realtimefarms.com)** It's my job to make this site
awesome.

**[SICP](github.com/Kobold/sicp)** Working through [Structure and 
Interpretation of Computer Programs](http://mitpress.mit.edu/sicp/)--one of
the best damn books on programming out there. I'm solving the exercises in
Haskell as well as Scheme.

## 2009

**[MichMusic](http://github.com/Kobold/michmusic)** A music management server
using the functional language Clojure integrating a Java ID3 tag library, the
Last.fm API, and an interactive interface using jQuery and the SoundManager2
Flash MP3 player.

**[clj-doc-test](http://github.com/Kobold/clj-doc-test)** A doodle implementing
[Python like doctests](http://docs.python.org/library/doctest.html) for
Clojure. Your tests end up looking something like this:

    (defn adder
        "A simple function to test the doctest macro with.
    
        => ((adder 1) 2)
        4 ; incorrect!
        => ((adder 4) 5)
        9"
        [n1]
        (fn [n2] (+ n1 n2)))

**[sha1.us](http://github.com/Kobold/shaurl)** A `git`-like url shortening
service that I implemented the bulk of in one night of feverish hacking. Why yet
another URL shortening service?  Because `git` makes an awesome URL shortener:

1. One potential issue with url shortening services is the potential
   for fraud. That is, what if some service turns out to be malicious
   and changes the location that shortened URL links to? Git provides
   reasonably strong cryptographic verification of a repository's
   contents via the SHA-1 hash that it uses to tag a commit. The
   shortened URL that sha1.us provides is a hash of the original URL
   so you can verify that you are being redirected to the right
   location.

2. When you use a `git` hash to refer to a commit, you only have to
   use whatever portion is necessary to uniquely identify the
   commit. sha1.us allows the same, making it actually pretty decent
   at shortening URLs.

3. I saw a giant list of URL shortening services and I wondered why
   I didn't have one for myself.
