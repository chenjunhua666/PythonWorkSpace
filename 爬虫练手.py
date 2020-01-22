import urllib.request
from bs4 import BeautifulSoup
from lxml import etree
import re


class Spider(object):
    def __init__(self):
        self.begin_page = 'http://search.51job.com/list/010000,000000,0000,00,9,99,%25E8%2590%25A5%25E4%25B8%259A%25E5%2591%2598,2,'
        self.end_page = '.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
        self.start_num = int(input('输入你要爬取的起始页：'))
        self.end_num = int(input('输入你要爬取的结束页:'))

    def load_page(self):
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        headers = {'User-Agent' : user_agent}
        for num in (self.start_num,self.end_num+1):
            url = self.begin_page + str(num) + self.end_page
            request = urllib.request.Request(url,headers=headers)
            response = urllib.request.urlopen(request)
            html = response.read().decode('GBK')
            self.parse_page(html)

    def parse_page(self,html):
        root = etree.HTML(html)
        names = root.xpath('//*[@id="resultList"]/div[@class="el"]/p[1]/span[1]/a[1]/text()')
        links = root.xpath('//*[@id="resultList"]/div[@class="el"]/p[1]/span[1]/a[1]/@href')
        aompanies = root.xpath('//*[@id="resultList"]/div[@class="el"]//span[@class="t2"]/a[1]/text()')
        localtions = root.xapth('//*[@id="resultList"]/div[@class="el"]//span[@class="t3"]/text()')
        selas = root.xpath('//*[@id="resultList"]/div[@class="el"]//span[@class="t4"]/text()')
        times = root.xpath('//*[@id="resultList"]/div[@class="el"]//span[@class="t5"]/text()')
        item = []
        for i in range(0,len(names)):
            items = {}
            items["a:"] = names[i].strip()
            items["b:"] = links[i]
            items["c:"] = aompanies[i]
            items["d:"] = localtions[i]
            items["e:"] = selas[i]
            items["f:"] = times[i]
            item.append(items)
        self.save_file(item)

    def save_file(self,item):
        file = open('55.txt','wb+')
        file.write(str(item).encode())
        file.close()

spider = Spider()
spider.load_page()