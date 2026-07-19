import requests
from bs4 import BeautifulSoup
import csv

# رابط الموقع المستهدف (موقع تجريبي للممارسة)
url = "https://quotes.toscrape.com"

def run_scraper():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    # فتح ملف CSV للكتابة
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Quote', 'Author']) # العناوين الأساسية

        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            writer.writerow([text, author])
            print(f"تم سحب: {author}")

    print("✅ تم الانتهاء! البيانات محفوظة في scraped_data.csv")

if __name__ == "__main__":
    run_scraper()


  
