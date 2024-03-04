# Amazon Web Scraper

This Python script scrapes the Amazon product page to monitor the price of a specific product and saves the data to a CSV file. It utilizes web scraping techniques using the Requests and BeautifulSoup libraries.

## Dependencies

- `requests`: Used to send HTTP requests to the Amazon product page.
- `beautifulsoup4`: A library for pulling data out of HTML and XML files.
- `csv`: Used to read from and write to CSV files.
- `datetime`: Provides classes for manipulating dates and times.
- `time`: Provides various time-related functions.
- `smtplib` (commented out): Module for sending emails via Simple Mail Transfer Protocol (SMTP).

## Functionality

The script contains a function `check_price()` which performs the following tasks:

1. Sends a GET request to the Amazon product page and retrieves the HTML content.
2. Parses the HTML content using BeautifulSoup to extract the product title and price.
3. Combines the whole and fractional parts of the price into a single string.
4. Retrieves today's date.
5. Writes the product title, price, and date to a CSV file named `AmazonWebScraperDataset.csv`.

The main loop of the script continuously calls the `check_price()` function every 5 seconds to monitor the price changes.

## Usage

To use this script:

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:
   ```
   pip install requests beautifulsoup4
   ```
3. Copy the script into your Python environment.
4. Uncomment the `send_mail()` function and configure it to send email notifications if desired.
5. Run the script.
6. The script will continuously monitor the price of the specified product on Amazon and save the data to the CSV file. Adjust the URL and other parameters as needed.

## Note

- Make sure to comply with Amazon's terms of service when scraping their website.
- Be cautious with frequent scraping as it may result in IP bans or other restrictions.