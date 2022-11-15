# Conversion Notes
## General
* Replace straight single and double quotes with their curved counterparts in all chapters. This includes apostrophes.
* Replaced two hyphens (--) with an en dash (–), also single hyphens spaced between clauses.
* Replaced "Ae", "AE" and "ae" with graphemes. - removing these
* Remove all the [sic] statements from the UESP text. Each book should be corrected.

## Useful regex:
* ^\s+(\w+)(.+?)$
* </p>\n\s+\t\t\t<p> </p>\n\t\t\t<p>
* ' ’
* \s"(.+?)"\s \s“$1”\s
* (\d+)-(\d+) $1–$2

## Chapter specific