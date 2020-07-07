# Mental wellness Data scraper using Scrapy.

###  Web scraper using scrapy for scraping an agony-aunt website.


Website : http://www.agony-aunt.com/

***

Follow the following steps for running the spider yourself : 

1. Install [pycharm](https://www.jetbrains.com/pycharm/download/#section=windows).

2. Open the project folder 'agony-aunt-scraper' using pycharm.

3. To run the spider  :

```
scrapy crawl advices -o <file_name>.<extension>
``` 

< file_name > :  can be anything

< extension > :  json,cvs,xml.

Note: The file 'data.json' was created using the following command.

```
scrapy crawl advices -o data.json
```

4. To access the scrapy shell : 

 ```
scrapy shell " <url> "
 ```

***

 ### Check the scrapped data at: 

 [Kaggle dataset](https://www.kaggle.com/priya1207/agonyaunts-advice)

