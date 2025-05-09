# Scraper for Flipkart product pages
import requests
from bs4 import BeautifulSoup
import re

def search_flipkart(query):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }

    # Let's convert the query to Flipkart search URL
    query = query.strip().replace(" ", "+")
    url = f"https://www.flipkart.com/search?q={query}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    products = []

    product_cards = soup.select("div[class*-".1AtVbE"]") #Each card for the product

    for card in product_cards:
        try:
            title = card.select_one("div._4rR01T") or card.select_one("a.s1Q9rs")
            price = card.select_one("div._30jeq3")
            link = card.select_one("a")

            if title and price and link:
                product = {
                    "title": title.get_text(strip=True),
                    "price": price.get_text(strip=True),
                    "link": "https://www.flipkart.com" + link["href"]
                }
                products.append(product)
        except Exception as e:
            continue
    
    return products

        
