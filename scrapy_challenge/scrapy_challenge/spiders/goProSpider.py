import scrapy
from scrapy_challenge.items import ScrapyChallengeItem


class goProSpider(scrapy.Spider):
    name = "GoProReviews"
    allowed_domains = ["amazon.com"]