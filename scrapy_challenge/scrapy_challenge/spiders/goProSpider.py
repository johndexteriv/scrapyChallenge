import scrapy
from scrapy_challenge.items import ScrapyChallengeItem


class goProSpider(scrapy.Spider):
    name = "GoProReviews"
    allowed_domains = ["amazon.com"]

    start_urls = [
        "https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
    ]

    def parse(self, response):
        items = ScrapyChallengeItem()
        review_id = response.xpath(
            '//div[contains(@data-hook, "review")]/@id'
        ).extract()
        review_title = response.xpath(
            '//a[contains(@data-hook, "review-title")]/span/text()'
        ).extract()
