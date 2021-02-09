# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyChallengeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    review_id = scrapy.Field()
    review_title = scrapy.Field()
    review_date = scrapy.Field()
    review_rating = scrapy.Field()
    review_text = scrapy.Field()


class ProductReviewItem(scrapy.Item):

    product_name = scrapy.Field()
    product_brand = scrapy.Field()
    product_source = scrapy.Field()
    product_list_price = scrapy.Field()
    product_sale_price = scrapy.Field()
    product_description = scrapy.Field()
    product_rating = scrapy.Field()
    product_review_count = scrapy.Field()