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
        all_review_divs = response.xpath('//div[contains(@data-hook, "review"]')

        for reviews in all_review_divs

            review_id = all_review_divs.xpath(
                '//div[contains(@data-hook, "review")]/@id'
            ).extract()
            review_title = all_review_divs.xpath(
                '//a[contains(@data-hook, "review-title")]/span/text()'
            ).extract()
            review_date = all_review_divs.xpath(
                '//span[contains(@data-hook, "review-date")]/text()'
            ).extract()
            review_rating = all_review_divs.xpath(
                '//i[contains(@data-hook, "review-star-rating")]/span/text()'
            ).extract()
            review_text = all_review_divs.xpath(
                '//span[contains(@data-hook, "review-body")]/span/text()'
            ).extract()

        items["review_id"] = review_id
        items["review_title"] = review_title
        items["review_date"] = review_date
        items["review_rating"] = review_rating
        items["review_text"] = review_text
        yield items
