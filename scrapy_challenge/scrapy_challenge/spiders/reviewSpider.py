import scrapy
from scrapy_challenge.items import ProductReviewItem


class reviewSpider(scrapy.Spider):
    name = "reviews"
    allowed_domains = ["amazon.com"]

    start_urls = [
        "https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
    ]

    def parse(self, response):
        items = ProductReviewItem()
        all_review_divs = response.xpath('//div[@id="cm_cr-review_list"]')

        for reviews in all_review_divs:

            review_id = reviews.xpath(
                '//div[contains(@data-hook, "review")]/@id'
            ).extract()
            review_title = reviews.xpath(
                '//a[contains(@data-hook, "review-title")]/span/text()'
            ).extract()
            review_date = reviews.xpath(
                '//span[contains(@data-hook, "review-date")]/text()'
            ).extract()
            review_rating = reviews.xpath(
                '//i[contains(@data-hook, "review-star-rating")]/span/text()'
            ).extract()
            review_text = reviews.xpath(
                '//span[contains(@data-hook, "review-body")]/span/text()'
            ).extract()

            items["review_id"] = review_id
            items["review_title"] = review_title
            items["review_date"] = review_date
            items["review_rating"] = review_rating
            items["review_text"] = review_text

            yield items

        # next_page = response.css("li.a-last a::attr(href)").get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)