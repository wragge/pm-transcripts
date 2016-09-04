# PM Transcripts repository

The Department of Prime Minister and Cabinet provides transcripts of more than [20,000 speeches, media releases, and interviews](https://pmtranscripts.dpmc.gov.au/about-collection) by Australian Prime Ministers. These transcripts can be [searched online](https://pmtranscripts.dpmc.gov.au/), and the underlying XML files [can be downloaded](https://pmtranscripts.dpmc.gov.au/developers) using a simple API.

This repository contains transcripts harvested from the PM Transcripts web site on 3 September 2016.

The XML files are all saved in the [`transcripts`](transcripts/) folder.

I've also created a simple [index](index.csv) (in CSV format) that contains the metadata from each of the XML files. The fields are:

* transcript id
* release date
* title
* prime minister's name
* type of transcript (speech, interview, media release etc)
* subjects (not used very often)
* url for PDF version

Also included are the scripts I used to [harvest](harvest.py) and [index](index.py) the files. There's some useful bits and pieces in `utilities.py` to extract information about the number of transcripts for each Prime Minister and for each transcript type.

I've combined copies of all the transcripts for each PM and saved them to the [`pms`](pms/) folder -- one file per PM. These files contain only the texts of each transcript, ordered chronologically.

Using `combine_pm()` in `utilities.py` you can generate a file for each Prime Minister and transcript type. So:

``` shell
>>> import utilities
>>> utilities.combine_pm('Gillard, Julia', 'Speech')

```

will create the file `gillard-julia-speech.txt` combining the text of all speeches by Julia Gillard.

Here's the number of transcripts for each Prime Minister:


| Prime Minister | Number of transcripts |
|------|------:|
| Howard, John | 5854 |
| Hawke, Robert | 2310 |
| Fraser, Malcolm | 2072 |
| Gillard, Julia | 2037 |
| Rudd, Kevin | 1726 |
| Keating, Paul | 1572 |
| Abbott, Tony | 1360 |
| Whitlam, Gough | 1227 |
| Menzies, Robert | 1197 |
| Gorton, John | 619 |
| Holt, Harold | 497 |
| McMahon, William | 341 |
| Unknown | 68 |
| McEwen, John | 11 |
| Chifley, Ben | 10 |
| Curtin, John | 3 |

Thanks to the Department of Prime Minister and Cabinet for making these documents available [under a CC-BY licence](https://pmtranscripts.dpmc.gov.au/copyright).

## Attribution

Source: Licensed from the Commonwealth of Australia under a Creative Commons Attribution 3.0 Australia Licence.

The Commonwealth of Australia does not necessarily endorse the content of this publication.