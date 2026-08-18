# Lao Tzu's Tao Te Ching
An English Version by Ursula K. Le Guin
ISBN: 978-1-59030-744-1

Read it at [nrrb.github.io/tao-te-ching](https://nrrb.github.io/tao-te-ching/).

## What is here

Ursula K. Le Guin's English version of the Tao Te Ching, all eighty-one chapters,
set in Markdown and built into a small static website. Her notes are kept with the
chapters they belong to.

She called it a rendition, not a translation. She did not read Chinese. She worked
from Paul Carus's 1898 edition, which printed the Chinese text with each character
followed by a transliteration and a translation.

## The texts

`Ursula K Le Guin.md` is the whole of it: eighty-one chapters and her notes.
Everything else in the book is made from this one file.

`Jane English and Gia-fu Feng.md` is a second English version, from 1972,
transcribed as far as chapter 3. It is kept for comparison and is not built into
the site.

## The chapters

Each chapter has a folder named for its number and its title, holding one file:

    1_taoing/README.md
    2_soul_food/README.md
    ...
    81_telling_it_true/README.md

The folders are made, not written. `split_tao_te_ching_md.py` reads
`Ursula K Le Guin.md`, splits it on the chapter headings, writes a folder for each
chapter, and writes `SUMMARY.md`, the table of contents the site is built from.

So a fix to the words belongs in `Ursula K Le Guin.md`, followed by:

    python3 split_tao_te_ching_md.py

Anything typed straight into a chapter folder is lost the next time that runs.

## Building the site

The site is built with [HonKit](https://github.com/honkit/honkit), which reads
`book.json`, `SUMMARY.md`, and `styles/website.css`.

    npm install
    npm run build

The build writes to `docs/`. GitHub Pages serves `docs/` from `master`, so the
built site is committed alongside the source, and a change to the text is not
published until the site is built again and the result committed.

To read it locally instead, with live reloading:

    npm run serve

That one builds to `_book/`, which git ignores.

## On the text

Le Guin's version is under copyright, Shambhala Publications, 1997. What is here
is a personal copy, kept for reading and for working on the Markdown. It is not a
license to republish.
