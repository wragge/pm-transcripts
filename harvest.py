import requests
from bs4 import BeautifulSoup
from os.path import basename, join, exists
from urlparse import urlparse
import re

TRANSCRIPTS_URL = 'http://pmtranscripts.dpmc.gov.au/transcripts.xml'

r = requests.get(TRANSCRIPTS_URL)
soup = BeautifulSoup(r.text)
for uri in soup.find_all('uri'):
    uri = unicode(uri.string)
    uri_bits = urlparse(uri)
    filename = basename(uri_bits.path)
    filepath = join('transcripts', '{}.xml'.format(filename))
    if not exists(filepath):
        try:
                id = re.search('transcript-(\d+)', filename).group(1)
                xml_url = 'https://pmtranscripts.dpmc.gov.au/query?transcript=' + id
                transcript = requests.get(xml_url)
                transcript.encoding = 'utf-8'
                with open(join('transcripts', '{}.xml'.format(filename)), 'wb') as xml_file:
                    xml_file.write(transcript.text.encode('utf-8'))
        except AttributeError:
            pass

