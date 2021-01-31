
import urllib
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#All I need to do is pass this into a text file
def load_jobs(job_title, location, start):
    getVars = {'q' : job_title, 'l' : location, 'radius': 25, 'start': start}
    url = ('https://au.indeed.com/jobs?' + urllib.parse.urlencode(getVars))
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    job_soup = soup.find(id="resultsCol")
    return job_soup
start = 0
open('Results.txt', 'w').close()
f = open("Results.txt", "a")

while start < 110:
    jobs = load_jobs("Retail Assistant", "Sydney NSW", start)

    job_cards = jobs.find_all("div", {"class": 'jobsearch-SerpJobCard'})


    job_detail = jobs.find_all("div", {"class": 'sjcl'})


    job_links = jobs.find_all("h2", {"class": 'title'})

    links_list = []

    for link in job_links:
        for actual_link in link.findAll('a'):
            links_list.append(actual_link.get('href'))





    job_titles = []

    for job in job_detail:
        stuff = job.find_all("span", {"class":'company'})
        job_titles.append(stuff[0])



    #Finds the dates at which they were found

    job_dates = []


    for job_card in job_cards:
        stuff = job_card.find_all("span", {"class": 'date'})
        job_dates.append(stuff[0])



    count = 0
    for i in range(len(job_dates)):
        text = job_dates[i].get_text()
        text_split = text.split(" ")

        try:
            if(text_split[0] == '30+' or int(text_split[0]) > 15):
                count += 1
                pass
            else:
                f.write(job_titles[i].get_text() + "\n")
                f.write(job_dates[i].get_text() + "\n")
                f.write("\n")
        except:
            f.write(job_titles[i].get_text() + "\n")
            f.write(job_dates[i].get_text() + "\n")
            f.write("\n")
    start += 10






