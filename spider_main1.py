# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import url_manager
import html_downloader
import html_parser
import html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls= url_manager.UrlManager()
        self.downloader= html_downloader.HtmlDownloader()
        self.parser= html_parser.HtmlParser()
        self.outputer= html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url(root_url):
            try:
                new_url=self.urls.get_new_url()
                print('craw %d: %s'%(count,new_url))

                html_cont=self.downloader.download(new_url)
                new_urls, new_data=self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collecter_data(new_data)
                if count==10:
                    break
                count=count+1
            except:
                print('craw fail')
        self.outputer.output_html()

if __name__=="__main__":
    root_url="http://baike.baidu.com/link?url=RTiSx-ti7HT8ecRY5cetsiv7ektR-LqbixRh-nylDdY5itVkp3SwWRAhx7zNrZ4FjZS8I56MmSYI6jLyWZRiSq"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)