funny-words
===========

A Python script that generates a list of pairs of funny words for naming things such as app releases, internal projects, servers and children.

## Installation

```sh
pip install funny-words
```

## Command-line Usage
```sh
funny-words [-n] [-w] [-d]

-n, --number     how many lines of funny words to generate
-w, --words      how many funny words to generate per line
-d, --delimiter  what to put between the funny words
```

## Command-line Examples

In its purest form funny-words will return a single pair of randomly selected funny words separated by a space.

```sh
$ funny-words
birthday magic
```

If you feel like being vertically loquacious you can increase the number of pairs returned with `-n, --number` 

```sh
$ funny-words --number 5
laughter asphalt
odour dimple
oboe rotate
thinkable flash
fungus fizzy
```

If you feel like being horizontally loquacious you can increase the number of words generated per line with `-w, --words`

```sh
$ funny-words --words 4
chart squiggle camera spiral
```

If spaces are not your cup of tea you can change the delimiter between words with `-d, --delimiter`

```sh
$ funny-words --delimiter -
croissant-nostril
```

And, as always, you can mix and match to suit your specific need

```sh
$ funny-words --delimiter , --number 6 --words 3
fuse,bangles,fuzzy
amazing,magic,burst
smooch,butter,statistics
angle,magic,smash
pasta,amazing,flock
smash,haberdashery,angle
```

## Python Usage

If you feel the need to use this in a scripted fashion within Python, you most certainly can. The funny_word library that comes with funny-word gives you everything you need to generate funny words on-the-fly.

```python
>>> from funny_words import build_n_gram
>>> build_n_gram()
u'chesterfield'
```
