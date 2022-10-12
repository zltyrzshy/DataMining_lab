# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:20:40 2021

@author: 66952
"""

import xml.sax
from xml.sax.handler import ContentHandler
from xml.sax import parse
import json
import urllib

doc = open('out2.json', 'w', encoding='utf-8')
json_str = ''
all_json = []


class article(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.author = ""
        self.title = ""
        self.pages = ""
        self.journal = ""
        self.authorIndex = 0
        self.authors = []
        self.authorNum = 0

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        target = ['incollection', "article", 'mastersthesis']
        if tag in target:
            if len(self.authors) != 0:
                all_json.append(self.authors.copy())
                self.authors = []
            mdate = attributes["mdate"]
            key = attributes["key"]
            self.key = key

    # 元素结束事件处理
    def endElement(self, tag):
        if self.CurrentData == "author":
            self.authors.append(self.author)
            if len(self.authors) > self.authorNum:
                self.authorNum = len(self.authors)

        elif self.CurrentData == "title":
            # print("title:", self.title, file=doc)
            pass
        elif self.CurrentData == "journal":
            # print("journal:", self.journal, file=doc)
            pass
        elif self.CurrentData == "article":
            if len(self.authors) > self.authorNum:
                self.authorNum = len(self.authors)
            print('end', len(self.authors), self.authorNum)

    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "author":
            self.author = content
        elif self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "journal":
            self.journal = content

    def addAuthor(self):
        self.authorIndex += 1
        return 'ra' + str(self.authorIndex)


if __name__ == "__main__":
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    parser.setContentHandler(article())
    parser.parse('dblp.xml')
    json_str = json.dumps(all_json)
    print(json_str, file=doc)

doc.close()
