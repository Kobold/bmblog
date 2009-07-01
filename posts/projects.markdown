Type: page
Title: My Projects

**[sha1.us](http://sha1.us)** A `git`-like url shortening service that
I implemented the bulk of in one night of feverish hacking. Why yet
another URL shortening service?  Because `git` makes an awesome URL
shortener:

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
