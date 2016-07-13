# -*- coding: utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    def collecter_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout=open('html_output.html','w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<head>")
        fout.write("<style>")
        fout.write(".Aclass{color: red;font-size: 30;}	")
        fout.write("</style>")
        fout.write('<meta charset="utf-8">')
        fout.write("<title>百度百科相关词条页面</title>")
        fout.write("</head>")
        fout.write("<body>")

        for data in self.datas:
            fout.write("<a class='Aclass' href='%s' >%s</a> " % (data['url'],data['title']))
            fout.write("<p>%s</p>" % data['summary'])


        fout.write("</body>")
        fout.write("</html>")
        fout.close()
