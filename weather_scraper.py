import requests
import csv
from bs4 import BeautifulSoup
# We no longer need 're'

def get_forecast_url_from_zip(zip_code, headers):
    """
    Takes a 5-digit zip code and returns the full weather.gov
    forecast URL by handling the website's redirect.
    """
    search_url = f"https://forecast.weather.gov/zipcity.php?inputstring={zip_code}"
    try:
        response = requests.get(search_url, headers=headers, allow_redirects=True)
        response.raise_for_status()

        if "MapClick.php" in response.url:
            return response.url
        else:
            print(f"Could not find a forecast for zip code: {zip_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error finding forecast URL: {e}")
        return None


def scrape_weather_data(forecast_url, headers):
    """
    Scrapes a weather.gov forecast page for the 7-day forecast
    and saves it to 'weather_forecast.csv'.
    """
    try:
        page = requests.get(forecast_url, headers=headers)
        page.raise_for_status()
        soup = BeautifulSoup(page.content, 'html.parser')

        # --- --- ---
        # Task: Scrape 7-Day Forecast and Save to CSV
        # --- --- ---
        forecast_container = soup.find(id='seven-day-forecast-list')
        if not forecast_container:
            print("Could not find the 7-day forecast container.")
            return

        periods = forecast_container.find_all('div', class_='tombstone-container')
        forecast_data = []

        for period in periods:
            period_name = period.find('p', class_='period-name').get_text(strip=True)
            short_desc = period.find('p', class_='short-desc').get_text(strip=True)
            temp = period.find('p', class_='temp').get_text(strip=True)

            forecast_data.append([period_name, short_desc, temp])

        if not forecast_data:
            print("No forecast data was extracted.")
            return

        # Write the 7-day forecast to the CSV file
        filename = 'weather_forecast.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Period', 'Forecast', 'Temperature'])
            csv_writer.writerows(forecast_data)

        print("-" * 30)
        print(f"Success! Scraped {len(forecast_data)} forecast periods.")
        print(f"7-day forecast saved to {filename}")
        print("-" * 30)

    except requests.exceptions.RequestException as e:
        print(f"Error scraping data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# --- --- ---
# Main part of the script
# --- --- ---
if __name__ == "__main__":
    browser_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }

    zip_code = input("Please enter a 5-digit US zip code: ")

    if len(zip_code) == 5 and zip_code.isdigit():
        forecast_url = get_forecast_url_from_zip(zip_code, browser_headers)

        if forecast_url:
            print(f"Found forecast URL: {forecast_url}")
            scrape_weather_data(forecast_url, browser_headers)
    else:
        print("Invalid zip code. Please enter a 5-digit number.")
