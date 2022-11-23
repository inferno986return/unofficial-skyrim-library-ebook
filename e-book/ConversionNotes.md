# Conversion Notes
## General
* Replace straight single and double quotes with their curved counterparts in all chapters. This includes apostrophes.
* Replaced two hyphens (--) with an en dash (–), also single hyphens spaced between clauses.
* Added superscript for ordinals (such as 1<sup>st</sup>, 2<sup>nd</sup>, 3<sup>rd</sup> and 4<sup>th</sup>).
* Remove all the [sic] statements from the UESP text. Each book should be corrected.
* Replaced "Ae", "AE" and "ae" with graphemes. - removing these

## Useful regex:
* ^(\w+)(.+?)$ \t\t<p>$1$2</p> - copied raw text from UESP and make into paragrpah tags.
* ^\s+(\w+)(.+?)$
* </p>\n\s+\t\t\t<p> </p>\n\t\t\t<p>
* ' ’
* \.\.\. …
* \s"(.+?)"\s \s“$1”\s
* (\d+)-(\d+) $1–$2

## Chapter specific