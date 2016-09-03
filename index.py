import os
from bs4 import BeautifulSoup
import csv
import arrow


def get_tag(soup, tag):
    try:
        value = soup.find(tag).string.strip().encode('utf-8')
    except AttributeError:
        value = ''
    return value

files = [f for f in os.listdir('transcripts') if f[-4:] == '.xml']
with open('index.csv', 'wb') as index_file:
    writer = csv.writer(index_file)
    writer.writerow(['id', 'date', 'title', 'pm', 'type', 'subjects', 'pdf'])
    for filename in files:
        with open(os.path.join('transcripts', filename), 'rb') as xml_file:
            soup = BeautifulSoup(xml_file.read())
            id = get_tag(soup, 'transcript-id')
            title = get_tag(soup, 'title')
            pm = get_tag(soup, 'prime-minister')
            release_date = get_tag(soup, 'release-date')
            try:
                parsed_date = arrow.get(release_date, 'DD/MM/YYYY')
                iso_date = parsed_date.format('YYYY-MM-DD')
            except:
                iso_date = ''
            release_type = get_tag(soup, 'release-type')
            subjects = get_tag(soup, 'subjects')
            pdf = get_tag(soup, 'document')
            writer.writerow([id, iso_date, title, pm, release_type, subjects, pdf])

