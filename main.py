# Importing required libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests

# Taking user input for search query
search_query = input("What you wanna Search : ")
# Replacing spaces with '+' to format for URL
search_query = search_query.replace(" ","+")

# Constructing the Flipkart search URL
url = f"https://www.flipkart.com/search?q={search_query}"

# Setting a user-agent to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# Sending an HTTP GET request to Flipkart
response = requests.get(url, headers=headers)

# Parsing the page content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Classes from Flipkart used to extract product info
# class for titles: "KzDlHZ"
# class for prices: "Nx9bqj"
# class for ratings: "XQDdHH"

# Empty lists to store scraped data
ti_tle = []
pr_ice = []
ra_ting = []

# Extracting all titles
title = soup.find_all("div", class_="KzDlHZ")
for titles in title:
    t = titles.text.strip()  # Removing extra spaces
    ti_tle.append(t)

# Extracting all prices
price = soup.find_all("div", class_="Nx9bqj")
for prices in price:
    p = prices.text.strip()
    pr_ice.append(p)

# Extracting all ratings
ratings = soup.find_all("div", class_="XQDdHH")
for rating in ratings:
    r = rating.text.strip()
    ra_ting.append(r)

# Ensuring all lists have the same length to avoid mismatch
min_len = min(len(ti_tle), len(pr_ice), len(ra_ting))

# Creating a dictionary of scraped data
data = {
    "Title": ti_tle[:min_len],
    "Price": pr_ice[:min_len],
    "Rating": ra_ting[:min_len]
}

# Converting dictionary to a DataFrame
df = pd.DataFrame(data)

# Asking user for a file name to save data
SaveAs = input("Saves Your File Name as : ")

# Saving the data as Excel or CSV depending on the extension
if SaveAs.endswith(".xlsx"):
    df.to_excel(SaveAs, index=False)
    print(f"{SaveAs} saved")

elif SaveAs.endswith(".csv"):
    df.to_csv(SaveAs, index=False)
    print(f"{SaveAs} saved")

else:
    print("Cannot Save. Please use .xlsx or .csv extensions")

# Printing total number of products scraped
print(f"Scraped items: {len(df)}")

# Example searches you can try:
# laptop, gaming laptop, mobile, smartphone, headphones,
# smartwatch, tablet, monitor, keyboard, printer, bluetooth speaker,
# power bank, external hard disk, ssd, router, graphics card,
# webcam, mic, usb hub
