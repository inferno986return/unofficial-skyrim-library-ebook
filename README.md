# unofficial-skyrim-library-ebook
An unofficial e-book for Skyrim's vast array of texts. Happy 11<sup>th</sup> anniversary to Skyrim!

I have attention deficit disorder (ADD) so I would rather be exploring, questing or killing things in Skyrim than reading the impressive amount of literature. It would be convenient to have a professional-quality e-book to take with me on the go that  

This project's goal is to provide a complete and beautiful reading experience for Skyrim's impressive selection of books in one anthology. I am using the Unofficial Elder Scrolls Pages (UESP)'s article called [*Skyrim:Books by Subject*](https://en.uesp.net/wiki/Skyrim:Books_by_Subject).

The books are not presented verbatim as we have wikis for that. Instead, the aim is to reformat the books, correcting any typos and using standardised punctuation to provide an enjoyable reading experience on any EPUB3-compatible device (or a Kindle by converting it). Ideally, Bethesda could adapt the content into a full 5×8 inch paperback as the official Skyrim Library are large collectible books that are not portable in any way.

In addition, this will be my chance to try making a fully standards-compliant EPUB 3.2 book!

## Compiling
The following components are required:

* Python 3
* Bash (zsh may be just fine on macOS)
* OpenJDK
* Windows Subsystem for Linux (WSL) (on Microsoft Windows)

The new `ebookbuild` uses the popular lxml Python library which can be installed using `pip install lxml` in the Bash terminal.

I am working on the new `content.opf` and figuring out how to make it compliant with the EPUB3.2 / EPUB3.3 standard.

## Licencing
* Each of the book's text and images is copyrighted to ZeniMax Media and Bethesda Softworks. The content is re-used in a transformative manner with no profit incentive similar to a Skyrim mod.

* `ebookbuild`'s Python source code is licenced under the GNU General Public License v3 (GPLv3).

* The EPUB's XHTML, CSS and JSON source code are licenced under Creative Commons Zero 1.0 (CC0).

* The Oblivion font is by Steve Deffeyes (aka dongle) who has released it under the terms of a freeware licence.

* Epubcheck 4.26 is licenced under the Apache License 2.0. Other related licences are in the "licenses" folder in the e-book directory.