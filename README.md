# Scrapy Challenge

## Overview

- Study the structure of GoPro Camera Fusion Amazon Review Page
- Use Scrapy framework to develop a spider that scrapes information from page elements. Information to be included: Unique Review ID, Review Title, Review Date, Review Star Rating and Review Text.
- Setup local instance of MongoDB to store review data.
- Insert reviews one by one into MongoDB instance.
- Now extend the exercise ot retrieve product level information from GoPro Page. Information to be included: Product Name, Brand, Source, List Price, Sale Price, Description Paragraph, Overall Star Rating and Total Number of Reviews.
- Insert data collected for the product into a different MonogDB associated with products.
- Modify review collection to associate with the product, allowing you to query tht review collection with product_id key.

## Steps to setup

1. Download Python and check version
2. Install VS code Python Extenions
3. Install Anaconda to handle python packages
4. Configure Conda for use in Git Bash Terminal
5. Create Conda virtual environment to house project specific packages

## Spider Development Steps

1. Create new Scrapy project "scrapy startproject projectname"
2. Create new Scrapy spider "-scrapy genspider spidername http://spiderurl.com"
3. CD into spider file
4. Import Scrapy
5. Create item variables for data fields you want to extract in items.py - import items
6. Create a spider class name that inherits scrapy.Spider
7. Create spider name and start_url variables
8. Create parse method taking arugments self & response.
9. Define parent component of information you'd like to extract
10. Create for loop for div components to be extracted within parent.
11. Set extracted data variables to items keys
12. Yield Keys
13. Create next page variable to be set to next button href - use .get() method
14. If next_page is not None - yield response passing next_page & self.parse

## Pipeline Devlopment Steps

1. Activate pipeline in settings.py
2. Create initialization function
3. Create connection variable with pymongo and mongoclient
4. Define database name and collection
5. Create collection insertion statement
