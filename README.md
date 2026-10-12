# unofficial-skyrim-library-ebook

**This project is part of the `ebookbuild` collection of sample books.**

An unofficial e-book for the vast amount of texts contained within *The Elder Scrolls V: Skyrim*. 

I have attention deficit disorder (ADD) so I would rather be exploring, questing or killing things in Skyrim than reading the impressive amount of literature. It would be convenient to have a professional-quality e-book to take with me on the go that  

This project’s goal is to provide a complete and beautiful reading experience for Skyrim’s impressive selection of books in one anthology. I am using the Unofficial Elder Scrolls Pages (UESP)’s articles called [*Skyrim:Books by Subject*](https://en.uesp.net/wiki/Skyrim:Books_by_Subject), [*Skyrim:Unobtainable_Items*][https://en.uesp.net/wiki/Skyrim:Unobtainable_Items#Unobtainable_Books_.26_Notes], and [*Skyrim:Creation Club Books*][https://en.uesp.net/wiki/Skyrim:Creation_Club_Books].

The books are not presented verbatim as we have wikis for that. Instead, the aim is to reformat the books, correcting any typos and using standardised punctuation to provide an enjoyable reading experience on any EPUB3-compatible device (or a Kindle by converting it). Ideally, Bethesda could adapt the content into a full 5×8 inch paperback as the official Skyrim Library are large collectible books that are not portable in any way.

In addition, this will be my chance to try making a fully standards-compliant EPUB 3.2 book!

<p align="center">
  <img src="https://github.com/inferno986return/unofficial-skyrim-library-ebook/blob/main/unoffical_library.png" alt="Unofficial Skyrim Library logo" />
</p>

Oh and lastly, a happy soon-to-be 15<sup>th</sup> anniversary to Skyrim!

## Current progress

This is a large book project because Skyrim has over 200 books and notes to be found and read by the player.

* ✅ **Biographies** - all 11 books are content complete and pending a final check, especially to check the headings are consistent and to separate the en and em dashes
* ✅ **Esoteric Texts** - content complete, only 1 text which was written in pseudo-Esperanto
* ✅ **Faction Books** - content complete, pending a final check
* ❌ **Fiction** - incomplete with only 2 of 44, though 2 *Kolb and the Dragon* is functional and *The Cake and the Diamond* is content complete
* ❌ **History & Lore**
* ❌ **Instruction & Research**
* ✅ **Notes & Letters** - all 7 notes and letters are content complete, pending a final check
* ❌ **Plays, Poetry, & Riddles**
* ❌ **Politics & Law**
* ❌ **Religion & Prophecy**
* ✅ **Travel** - all 11 books are content complete and pending a final check
* ❔ **Unobtainable Books** - possibly incomplete. However, 3 are content complete including a decrypted copy of *Gallus’s Journal*. I will review the remaining unavailable texts to determine if they are worthy of inclusion
* ❌ **Creation Club** - incomplete. I started *The Crimson Dirks* and need to review the remaining texts

## Select improvements made to the text

A non-exhautive list of improvements to the text:

* All [sic] annotations from the UESP have been corrected
* Hyperlinks (including a fully 'playable' *Kolb and the Dragon* CYOA book)
* Text figures for body text (i.e. numbers which are the same height as the lowercase letters)
* Curly apostrophes and quote marks
* En dashes and em dashes (I'll need to recheck the source text for these)
* Superscripted ordinals for 1st, 2nd, 3rd, 4th, etc.
* Asterisms (⁂) instead of 3 horizontal asterisks (***) as the solidus for scene breaks 

## Setting up `ebookbuild` for compilation
The following components are required:

* Python 3
* Bash (zsh may be just fine on macOS)
* OpenJDK
* Windows Subsystem for Linux (WSL) (on Microsoft Windows)

The new `ebookbuild` has 2 dependencies which can be installed using in the Bash terminal:

* lxml - the popular XML Python library via `pip install lxml`
* orjson - the Rust JSON library via `pip install lxml`

## Building an EPUB 3.3 file

New build command that outputs everything into an .md. Neat!

`python3 ebookbuild-3.3.py && java -jar epubcheck.jar SkyrimLibraryUnofficial.epub 2>&1 | tee epublog.md`

Old command that doesn’t output to the terminal screen:

`python3 ebookbuild-3.3.py && java -jar epubcheck.jar SkyrimLibraryUnofficial.epub > epublog.md 2>&1`


## Licencing
* Each of the book’s text and images is copyrighted to ZeniMax Media and Bethesda Softworks. The content is re-used in a transformative manner with no profit incentive similar to a Skyrim mod.

* `ebookbuild`’s Python source code is licenced under the GNU General Public License v3 (GPLv3).

* The EPUB’s XHTML, CSS and JSON source code are licenced under Creative Commons Zero 1.0 (CC0).

* The Oblivion font is by Steve Deffeyes (aka dongle) who has released it under the terms of a freeware licence.

* Epubcheck 4.26 is licenced under the Apache License 2.0. Other related licences are in the "licenses" folder in the e-book directory.