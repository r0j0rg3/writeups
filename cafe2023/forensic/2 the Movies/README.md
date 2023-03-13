# 2 the Movies
## Description
Solves: 28  Easy

Here is a file for you to play with...I think there was something in it, but I haven't played with it in such a long time I forgot!

You might need Linux or Mac for solving this.

Flag: RUSH{ALL_CAPS_MESSAGE}
## Hint:
"**CIINEMA...hmmm..."
## Files
1. 2 the movies

## Solve
If we do "$ file 2\ the\ Movies" we get that this is a "Unicode text, UTF-8 text, with very long lines (1734)". I opened it with vim and quickly I realised it was like a log of a terminal where someone has opened a file called Flag with vim on the directoy /**CIINEMA. But there was a lot of noise and I wasn't able to obtain more info in this way.

After looking at the hint I realised with CIINEMA has 2 i instead of one, it is becouse the 2 * means that two letters are missing, those are A and S. 

**ASCIINEMA** is a tool that let us record a terminal session, dump it to a file and later be able to see it like a video, but with a Terminal User Interface (TUI). I downloaded the tool and read de Docs, now all you have to do is to run 
```bash
$ asciinema play 2\ the\ Movies
```
Now, while we eat some popcorn, we can see how the creator opens a new file with vim, and writes the flag with a lot of noise to obfuscate it. If we transcribe the flag, we get it:

RUSH{T3RM1N4L_MOOOV135_4R3_COOOL}

## Conclusion
That was a very cool challenge, I have to ask for more hints but the only told me that I had to realise why CIINEMA has 2 i, that's when i saw it. Also I learnt about this cool tool, asciinema.
