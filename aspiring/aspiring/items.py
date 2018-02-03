# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class AspiringItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    years = Field() #年度
    departments = Field() #学科
    recommendation_people = Field() #推薦受験者
    scholastic_people = Field() #学力受験者
    recommendation_people_men = Field() #推薦男
    scholastic_people_umen = Field() #学力女
    recommendation_passed = Field() #推薦合格者
    scholastic_passed = Field() #学力合格者
    recommendation_passed_men = Field() #推薦合格者男
    scholastic_passed_umen = Field() #学力合格者女
    pass
