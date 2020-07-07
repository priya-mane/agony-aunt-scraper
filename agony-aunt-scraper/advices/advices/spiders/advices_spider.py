#!/usr/bin/env python3
# -*- coding: cp1252 -*-

import scrapy
from ..items import AdvicesItem
import re


class AdvicesSpider(scrapy.Spider):
    name = 'advices'
    start_urls =[
        'http://www.agony-aunt.com/'
    ]

    def parse(self, response):
        urls = response.css("li#categories-3 li a").xpath("@href").extract()
        urls = urls[2:]

        for url in urls:
            yield scrapy.Request(url, callback=self.parse_titles)

    def parse_titles(self,response):
        '''
        Scrapes urls for each title under the posted category
        '''
        post_obj = response.css("h2.entry-title")
        post_url = post_obj.css("a::attr(href)").extract()

        for url in post_url:
            yield scrapy.Request(url, callback=self.get_problem_and_advice)

        next_page = response.css("div.nav-previous a::attr(href)").extract_first()

        if next_page is not None:
            yield response.follow(next_page,callback=self.parse_titles)


    def get_problem_and_advice(self,response):
        '''
        Scrape categories,title,problem,advice for each problem posted on the website.
        '''
        title  = response.css("h1.entry-title::text").extract()

        problem = response.css("div.entry-content p em::text").extract()

        if len(problem)==0:
            problem = response.css("div.entry-content p em span::text").extract()

        if len(problem)==0 :
            problem = response.css("div.entry-content p i::text").extract()

        advice = response.css("div.entry-content p::text").extract()

        if len(advice)==0:
            lst = response.css("div.entry-content p em::text").extract()
            l = len(lst)
            advice = response.css("div.entry-content p span::text").extract()[l:]

        items = AdvicesItem()

        items['category'] = response.css("div.entry-utility a::text").extract()[:-1]
        items['title'] = title
        items['problem'] = problem
        items['advice'] = advice

        yield items











