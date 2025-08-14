## Flipkart Product Scraper
A simple Python web scraping script that allows you to search for any product on Flipkart.com and extract details like product title, price, and rating. The scraped data can be saved in either .xlsx or .csv format using Pandas.

🚀 Features
Search any product (e.g., laptop, smartphone, router, mic, keyboard)
Scrape the first page of Flipkart search results

Extract-->
📌 Product Title
💸 Price
⭐ Rating

Save to Excel or CSV

Easy to use and beginner-friendly code

## Technologies Used
--requests – for sending HTTP requests
--BeautifulSoup (bs4) – for parsing HTML content
--pandas – for creating and exporting DataFrames

## Example Output
Title	Price	Rating
Realme Narzo 60X	₹11,999	4.3⭐
HP 15s Laptop	₹39,999	4.1⭐
boAt Rockerz Bluetooth	₹1,499	4.2⭐

## How to Use
Install dependencies
Make sure you have the following libraries installed:

-->pip install requests beautifulsoup4 pandas

Enter a product to search

What you wanna Search : laptop
Choose a file name and format

Saves Your File Name as : laptop_data.xlsx
✅ File is saved successfully!

Available Searches-->
laptop
gaming laptop
smartphone
headphones
smartwatch
monitor
printer
bluetooth speaker
router
webcam
graphics card

This scraper currently works for the first page only
Flipkart changes its HTML structure often; class names might need updates

This is for educational purposes only. Respect website terms of use.

## To-Do / Future Improvements
-->Scrape multiple pages
-->Add product links
-->Include seller or availability info

## Installation
bash
git clone https://github.com/bhaskaraya3/Flipkart_Product_Scrapper
cd Flipkart_Product_Scrapper
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt

This project is open source and free to use under the MIT License.

