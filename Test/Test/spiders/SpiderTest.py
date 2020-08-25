import scrapy


class NewSpider(scrapy.Spider):
    name = "new_spider"

    start_urls = ['https://haikelmp.wixsite.com/website']

    def parse(self, response):
        filename = 'resume.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
