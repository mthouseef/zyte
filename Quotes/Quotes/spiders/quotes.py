from gc import callbacks
import scrapy
from scrapy_splash import SplashRequest


class QuotesJs1Spider(scrapy.Spider):

    name = 'quotes'

    def start_requests(self):
        yield SplashRequest('http://quotes.toscrape.com/js',callback=self.parse)

    def parse(self, response):
        for quote in response.xpath("//div[contains(@class,'quote')]"):
            yield {
                'quote': quote.xpath(".//span[contains(@class,'text')]/text()").extract_first(),
                'author': quote.xpath(".//small[@class='author']/text()").extract_first(),
                'tags': quote.xpath(".//div[@class='tags']//text()").extract(),
            }

        next_page = response.css('li.next > a::attr(href)').extract_first()
        if next_page:
            yield SplashRequest(response.urljoin(next_page))
