# coding: utf-8
# author: JamesYi
# created on Mar 26th, 2019

from urllib.request import urlretrieve
import os
import json
from progressbar import *

def download_pdf():
    paper_list = json.loads(open('../data/arxivData.json', 'r').read())
    total = len(paper_list)
    save_dir = '../data/pdf/'
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    p_bar = ProgressBar().start()
    for index, paper in enumerate(paper_list):
        _id = paper['id']
        _link = paper['link'][1]['href'].replace('//', '//cn.')
        urlretrieve(_link, save_dir + _id + '.pdf')
        p_bar.update(int((index + 1)/ total * 100))
    p_bar.finish()

if __name__ == '__main__':
    download_pdf()
