import csv
from operator import itemgetter, attrgetter
from bs4 import BeautifulSoup
import os
import re

INDEX = "index.csv"


def summarise_pms():
    pms = {}
    with open(INDEX, 'rb') as index_file:
        reader = csv.DictReader(index_file)
        for row in reader:
            if not row['pm']:
                row['pm'] = 'Unknown'
            try:
                pms[row['pm']][row['type']] += 1
                pms[row['pm']]['total'] += 1
            except KeyError:
                try:
                    pms[row['pm']][row['type']] = 1
                except KeyError:
                    pms[row['pm']] = {}
                    pms[row['pm']]['pm'] = row['pm']
                    pms[row['pm']]['total'] = 1
    pm_totals = sorted(pms.values(), key=itemgetter('total'), reverse=True)
    for pm in pm_totals:
        print '{}: {}'.format(pm['pm'], pm['total'])
    return pms


def summarise_types():
    types = {}
    with open(INDEX, 'rb') as index_file:
        reader = csv.DictReader(index_file)
        for row in reader:
            try:
                types[row['type']] += 1
            except KeyError:
                types[row['type']] = 1
    types = sorted(types.items(), key=itemgetter(1), reverse=True)
    for type in types:
        print '{}: {}'.format(type[0], type[1])
    return types


def combine_pm(pm, type=None):
    transcripts = []
    with open(INDEX, 'rb') as index_file:
        reader = csv.DictReader(index_file)
        for row in reader:
            if row['pm'] == pm:
                if not type:
                    transcripts.append(row)
                elif row['type'] == type:
                    transcripts.append(row)
    transcripts = sorted(transcripts, key=itemgetter('date'))
    filename = pm.lower().replace(', ', '-')
    if type:
        filename = '{}-{}'.format(filename, type.lower())
    with open(os.path.join('pms', filename + '.txt'), 'wb') as pm_file:
        for transcript in transcripts:
            if transcript['id']:
                with open(os.path.join('transcripts', 'transcript-{}.xml'.format(transcript['id'])), 'rb') as xml_file:
                    soup = BeautifulSoup(xml_file, 'xml')
                    content = soup.find('content').string.replace('<![CDATA[', '').replace(']]>', '').encode('utf-8')
                    clean_content = re.sub('<[^<]+?>', '', content)
                    pm_file.write(clean_content + '\n\n')


def combine_all_pms(type=None):
    pms = summarise_pms()
    for pm in pms:
        if pm != 'Unknown':
            combine_pm(pm, type)

