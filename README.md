# Python Weather Forecast Scraper

This is a portfolio project demonstrating web scraping using Python. This script asks a user for a 5-digit US zip code, finds the correct forecast page on the National Weather Service (weather.gov), and scrapes the 7-day forecast.

All the extracted data is saved to a structured CSV file named `weather_forecast.csv`.

## Features

* **User Input:** Asks for a 5-digit zip code to find a specific forecast.
* **Dynamic URL Handling:** Uses the `requests` library to handle the site's zip code search and follow the redirect to the correct forecast URL.
* **Data Scraping:** Parses the HTML with `BeautifulSoup` to find and extract the 7-day forecast data.
* **Data Export:** Saves the 7-day forecast (Period, Forecast, Temperature) to a clean `weather_forecast.csv` file using Python's built-in `csv` module.

## Technologies Used

* **Python**
* **Requests:** For fetching the webpage and handling HTTP redirects.
* **BeautifulSoup (bs4):** For parsing the HTML and extracting all target data.
* **CSV:** A built-in Python module for writing the data to a .csv file.

## How to Use

1.  Clone the repository or download `weather_scraper.py`.
2.  Make sure you have Python installed, along with the required libraries:
    ```sh
    pip install requests beautifulsoup4
    ```
3.  Run the script from your terminal:
    ```sh
    python weather_scraper.py
    ```
4.  You will be prompted to enter a 5-digit zip code (e.g., `90210`).
5.  The script will create a `weather_forecast.csv` file in the same directory.
