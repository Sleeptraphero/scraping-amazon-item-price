# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv
import datetime
import time
import smtplib

# Function to check the price of a product on Amazon and save it to a CSV file
def check_price():
    # URL of the Amazon product page to scrape
    URL = "https://www.amazon.de/Got-Data-MIS-Business-Analyst/dp/B09F32Q8J8"

    # Headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "accept-language": "de,en-US;q=0.7,en;q=0.3"
    }

    # Send a GET request to the URL with headers
    page = requests.get(URL, headers=headers)

    # Parse the HTML content of the page using BeautifulSoup
    Soup1 = BeautifulSoup(page.content, "html.parser")

    # Create a new BeautifulSoup object from the prettified HTML content
    Soup2 = BeautifulSoup(Soup1.prettify(), "html.parser")

    # Extract title of the product from the page
    title = Soup2.find(id="productTitle").get_text().strip()

    # Extract price details of the product from the page
    price_whole = Soup2.find(class_="a-price-whole").get_text().replace(",", "").strip()
    price_fraction = Soup2.find(class_="a-price-fraction").get_text().strip()
    price_currency = Soup2.find(class_="a-price-symbol").get_text().strip()
    price = price_whole + "," + price_fraction  # Combine whole and fractional parts of the price

    # Get today's date
    today = datetime.date.today()

    # Define header and data to be written to the CSV file
    header = ['Title', 'Price', "Date"]
    data = [title, price, today]

    # with open("AmazonWebScraperDataset.csv", "w", newline="", encoding="UTF8") as file:
    # writer = csv.writer(file, delimiter=";")
    # writer.writerow(header)
    # writer.writerow(data)

    # Open the CSV file in append mode and write the data
    with open("AmazonWebScraperDataset.csv", "a+", newline="", encoding="UTF8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(data)

    #if(price < 15):
        #send_mail()

# def send_mail():
    # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    # server.ehlo()
    # server.starttls()
    # server.ehlo()
    # server.login("bastian.radlmaier@code.berlin", "xxxxx")

    # subject = "The shirt you want is now below 15€"
    # body = "Boot up your pc and buy that shirt you wanted"

    # msg = f"Subject: {subject}\n\n{body}"

    # server.sendmail("bastian.radlmaier@code.berlin", msg)

# Infinite loop to repeatedly check the price every 5 seconds
while True:
    check_price() 
    time.sleep(5)

    

