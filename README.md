# PM Transcripts repository

The Department of Prime Minister and Cabinet provide transcripts of more than [20,000 speeches, media releases, and interviews](https://pmtranscripts.dpmc.gov.au/about-collection) by Australian Prime Ministers. These transcripts can be [searched online](https://pmtranscripts.dpmc.gov.au/), and the underlying XML files [can be downloaded](https://pmtranscripts.dpmc.gov.au/developers) using a simple API.

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

Also included are the scripts I used to [harvest](harvest.py) and [index](index.py) the files.

Thanks to the Department of Prime Minister and Cabinet for making these documents available [under a CC-BY licence](https://pmtranscripts.dpmc.gov.au/copyright).

## Attribution

Source: Licensed from the Commonwealth of Australia under a Creative Commons Attribution 3.0 Australia Licence.

The Commonwealth of Australia does not necessarily endorse the content of this publication.