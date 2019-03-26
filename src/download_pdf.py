# coding: utf-8
# author: JamesYi
# created on Mar 26th, 2019

import os
import json
import re

def download_pdf():
    paper_list = json.loads(open('../data/arxivData.json', 'r').read())
    save_dir = '../data/pdf/'
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    with open('../data/pdf_links.txt', 'w') as f:
        for index, paper in enumerate(paper_list):
            _link = re.findall(r'http://arxiv\.org/pdf/.*v\d', paper['link'])[0].replace('arxiv', 'cn.arxiv')
            f.write('{}\n'.format(_link))

if __name__ == '__main__':
    download_pdf()
