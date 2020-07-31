# PM Transcripts repository

The Department of Prime Minister and Cabinet provides transcripts of more than [20,000 speeches, media releases, and interviews](https://pmtranscripts.pmc.gov.au/about-collection) by Australian Prime Ministers. These transcripts can be [searched online](https://pmtranscripts.pmc.gov.au/), and the underlying XML files [can be downloaded](https://pmtranscripts.pmc.gov.au/developers) using a simple API.

This repository contains transcripts harvested from the PM Transcripts web site on 11 July 2019.

The XML files are all saved in the [`transcripts`](transcripts/) folder.

I've also created a simple [index](index.csv) (in CSV format) that contains the metadata from each of the XML files. The fields are:

* `id` – transcript id
* `date` – release date
* `title`
* `pm` – prime minister's name
* `release_type` – type of transcript (speech, interview, media release etc)
* `subjects` – subjects (not used very often)
* `pdf` – url for PDF version (if there is one)

I've combined copies of all the transcripts for each PM and saved them to the [`pms`](pms/) folder -- one file per PM. These files contain only the texts of each transcript, ordered chronologically.

I've also created a zip file for each PM and saved them to the [`pms`](pms/) folder.

The code for harvesting, indexing, analysing, and aggregating the transcripts is [in the GLAM Workbench](https://github.com/GLAM-Workbench/pm-transcripts).

Here's the number of transcripts for each Prime Minister:

```
Howard, John         5865
Hawke, Robert        2321
Fraser, Malcolm      2081
Gillard, Julia       2072
Turnbull, Malcolm    1751
Rudd, Kevin          1735
Keating, Paul        1582
Abbott, Tony         1371
Whitlam, Gough       1238
Menzies, Robert      1212
Gorton, John          625
Holt, Harold          507
McMahon, William      349
McEwen, John           16
Chifley, Ben           11
Curtin, John            4
```

Thanks to the Department of Prime Minister and Cabinet for making these documents available [under a CC-BY licence](https://pmtranscripts.pmc.gov.au/copyright).

## Attribution

Source: Licensed from the Commonwealth of Australia under a Creative Commons Attribution 3.0 Australia Licence.

The Commonwealth of Australia does not necessarily endorse the content of this publication.
