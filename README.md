<h1 align = 'center'>
    LinkedIn Jobs Scraping Without Login
    </h1>

## About

## Prerequisite
Download [Chrome WebDriver](https://chromedriver.chromium.org/downloads)
```python
from selenium import webdriver
```

## Usage
+ Keyword: 
  + Keyword can be title, company name or keywords included in a job post
  + For mutiple keywords, use 'singla quote mark' for every keyword along with AND/OR operator in between
  + Example: 'Data Scientist' AND 'Github' AND 'Bachelor's degree'
+ Location:
  + Location can be City, State, Counrty or Area
  + Default distance from location is 25mi, LinkedIn will alter to the closest location if not readable
  + Date Posted is set to 'Past Week'. Locate ```sortBy=``` in [Line18](https://github.com/pandasTong/LinkedIn-Jobs-Scraping/blob/e61b3f4d436ca368af9cb14ac82b5269aaf28e0a/crawler.py#L18To) to change this criteria. <br> Past 24 Hours = ```f_TPR=r86400```; Past Week = ```f_TPR=r604800```; Past Month = ```f_TPR=r2592000```, Remove for 'Any Time'

## Sample
```Python
if __name__ == '__main__':
	keyword = "'data analyst' and 'machine learning'"
	location = "Dallas-Fort Worth Metroplex"
	FindJobs(keyword, location).run()
```

![Result](https://raw.githubusercontent.com/pandasTong/LinkedIn-Jobs-Scraping/main/Sample.PNG)

### Simple App
Visit [TBAnalytic-LinkedIn](https://tbanalytic.com/linkedin)
