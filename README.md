# Web-Scrapping



## Overview

This project is a Python-based web scraper designed to extract mobile phone listings from eBay. It utilizes the requests library for making HTTP requests, BeautifulSoup for parsing HTML content, and pandas for data manipulation and storage.

## Features

- **Scraping Capabilities:** Extracts product names, prices, and shipping details from eBay mobile phone listings.
- **Data Storage:** Saves scraped data to a CSV file (`Mobiles_Data.csv`) for easy access and analysis.
- **Customizable:** Easily adjustable to scrape more pages by modifying the range in the script.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repository.git
2. **Navigate to the project directory:**
cd ebay-mobile-phone-scraper
3. **Install dependencies:**
pip install -r requirements.txt
## Usage
1. **Run the script:**
python ebay_scraper.py

2. **Adjust scraping parameters (optional):** 
Modify the range in ebay_scraper.py to scrape more pages if needed:

for j in range(1, 10):  # Adjust the range as per your requirement


4. **Output:**
The script will scrape eBay for mobile phone listings and store the data in Mobiles_Data.csv.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
