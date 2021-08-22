from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import pandas as pd

class FindJobs:

	def __init__(self, keyword, location):
		# Initial Values
		self.keyword = keyword
		self.location = location
		self.wd = webdriver.Chrome('chromedriver.exe')

	def get_url(self):
		# get job search url
		# keyword(s) and location needed
		# post time pre-set to last week
		template = 'https://www.linkedin.com/jobs/search?keywords={}&location={}&geoId=90000031&sortBy=R&f_TPR=r604800&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
		url = template.format(keyword, location)
		self.wd.get(url)

	def autoscroll(self):
		no_of_jobs = self.wd.find_element_by_css_selector('h1>span').get_attribute('innerText')
		no = []
		# keep numbers only
		for i in no_of_jobs:
			try:
				int(i)
				no.append(i)
			except:
				pass
		no_of_jobs = int(''.join(no))
		# fetch all
		j = 2
		while j <= int(no_of_jobs/25)+1:
			self.wd.execute_script("window.scrollTo(0, document.body.scrollHeight)")
			j += 1
			try:
				self.wd.find_element_by_xpath('/html/body/div/div/main/section[2]/button').click()
				time.sleep(5)
			except:
				pass
				time.sleep(5)

	def posts(self):
		job_lists = self.wd.find_element_by_class_name('jobs-search__results-list')
		jobs = job_lists.find_elements_by_tag_name('li')
		print('Number of Jobs Found: ' + str(len(jobs)))

		job_title = []
		company_name = []
		job_location = []
		job_link = []
		job_detail = []

		for job in range(len(jobs)):
			title = jobs[job].find_element_by_class_name('base-search-card__title').text
			company = jobs[job].find_element_by_tag_name('h4').text
			office = jobs[job].find_element_by_class_name('job-search-card__location').text
			link = jobs[job].find_element_by_tag_name('a').get_attribute('href')

			time.sleep(2)
			jobs[job].find_element_by_tag_name('a').click()
			detail = self.wd.find_element_by_xpath("//div[@class='description__text description__text--rich']").text
			# handle description not show
			while len(detail) < 2:
				try:
					jobs[job-1].find_element_by_tag_name('a').click()
					time.sleep(3)
					jobs[job].find_element_by_tag_name('a').click()
					detail = self.wd.find_element_by_xpath("//div[@class='description__text description__text--rich']").text
				except:
					pass
					
			job_title.append(title)
			company_name.append(company)
			job_location.append(office)
			job_link.append(link)
			job_detail.append(detail)

		job_data = pd.DataFrame({'Title': job_title,
			'Company': company_name,
			'Location': job_location,
			'Link': job_link,
			'Detail': job_detail})
		print('Number of Jobs Crawled: ' + str(len(job_data)))
		job_data.to_excel('LinkedIn {} Job {}.xlsx'.format(keyword, location), index = False)

	def run(self):
		self.wd.maximize_window()
		self.get_url()
		time.sleep(2)
		self.autoscroll()
		self.posts()

if __name__ == '__main__':
	keyword = "'business analyst' and 'sql'"
	location = "Dallas-Fort Worth Metroplex"
	FindJobs(keyword, location).run()
	

