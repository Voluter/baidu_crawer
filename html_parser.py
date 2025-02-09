# -*- coding: utf-8 -*-
import re
import urllib.parse
from bs4 import BeautifulSoup


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls=set()
        links =soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url=link['href']
            new_full_url=urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls



    def _get_new_data(self, page_url, soup):
        res_data={}
        res_data['url']=page_url
    #<dd class="lemmaWgt-lemmaTitle-title">
    #<h1>Python</h1>
        title_node=soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title']=title_node.get_text()

        #<div class="para" label-module="para">ABC是由Guido参加设计的一种教学语言。就Guido本人看来，ABC 这种语言非常优美和强大，是专门为非专业程序员设计的。但是ABC语言并没有成功，究其原因，Guido 认为是非开<div class="lemma-picture text-pic layout-right" style="width:220px; float: right;">
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node=soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url, soup)
        new_data=self._get_new_data(page_url, soup)
        return new_urls, new_data



