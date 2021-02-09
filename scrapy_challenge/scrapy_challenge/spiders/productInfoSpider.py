import scrapy
from scrapy_challenge.items import ProductInfoItem


class productInfoSpider(scrapy.Spider):
    name = "productinfo"
    allowed_domains = ["amazon.com"]

    start_urls = [
        "https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=sr_1_3?crid=D3C7EDM435E7&keywords=gopro+fusion&qid=1550442454&s=electronics&sprefix=GoPro+Fu%2Celectronics%2C1332&sr=1-3"
    ]

    def parse(self, response):
        items = ProductInfoItem
        all_info_div = response.xpath('//div[contains(@id, "ppd")]')

        for info in all_info_div

            