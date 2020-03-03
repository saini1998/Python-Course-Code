# INTRODUCTION
# 1. Excel spreadsheets
# 2. PDFs
# 3. Sending texts
# 4. Browser Automation
# 5. Web scrapping

# WHAT ARE APIs?

# Application Programming Interfaces
# yelp business search api


# YELP API

# yelp fusion
# create an app
# NOTE SIGN IN PROBLEMS


#  SEARCHING FOR BUSINESSES

import requests
import config
url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer" + config.api_key
}
params = {
    "term": "barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
print(response.text)
businesses = response.json()["businesses"]
print(businesses)
# for business in businesses:
#     print(business["name"])

names = [business["name"]
         for business in businesses if business["rating"] > 4.5]
print(names)
# 401 unathorization
# 400 bad requests


# HIDING API KEYS


# SENDING TEXTS


# WEB SCRAPPING

# pipenv install beautifulsoup4


# BROWSER AUTOMATION


# WORKING WITH PDFs


# WORKING WITH EXCEL SPREADSHEETS


# COMMAND QUERY SEPERATION PRINCIPLE

# sheet.cell(row,1) will create new cells in iteration. So be aware of that


# NUMPY
