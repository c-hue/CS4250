#-------------------------------------------------------------------------
# AUTHOR: Caitlyn Hue
# FILENAME: scraper.py
# SPECIFICATION: crawls Circular Links of a seed URL
# FOR: CS 4250 - Assignment #2
# TIME SPENT: 25min
#-------------------------------------------------------------------------

# Importing Python libraries
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"
baseURL = "https://testingurl.dev"

# Creating the frontier and seen collections
# --> add your Python code here
frontier = [seed]
seen = [seed]


# Crawling until the frontier is empty
while frontier:

    # Removing the first URL from the frontier
    # --> add your Python code here
    url = frontier.pop(0)

    # Retrieving and parsing the Web page
    # --> add your Python code here
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")


    # Printing the text contained in the <h1> element
    # --> add your Python code here
    print(soup.h1.text)


    # Extracting and processing hyperlinks
    # --> add your Python code here
    links = soup.find_all("a", href=True)
    for link in links:
        absoluteURL = urljoin(url, link["href"])
        if absoluteURL.startswith(seed) and absoluteURL not in seen:
            seen.append(absoluteURL)
            frontier.append(absoluteURL)

# Printing all URLs in seen
# --> add your Python code here
for url in seen:
    print(url)