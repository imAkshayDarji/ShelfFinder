# Scraper for Amazon product pages
import requests
from bs4 import BeautifulSoup

def scrape_amazon(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        title = soup.find(id="productTitle").get_text(strip=True)
    except:
        title = "Title not found"

    # price_selectors = [
    #     ".priceToPay .a-offscreen",     #Latest Structure Amazon use for price
    #     ".a-price .a-offscreen",        #Common Structure Amazon use
    #     "#priceblock_ourprice",         #Older Layout Amazon use
    #     "#priceblock_dealprice",        #Deal Price Amzon use
    #     "#price_inside_buybox",         #Buy Box price
    #     ".a-color-price"                #Fallback
    # ]
    price = "Price not found"
    price_elements = soup.select(".a-price .a-offscreen, .priceToPay .a-offscreen")

    for el in price_elements:
        price_candidate = el.get_text(strip=True)
        if price_candidate:
            price = price_candidate
            break
    
    # for selector in price_selectors:
    #     el = soup.select_one(selector)
    #     if el and el.get_text(strip=True):
    #         price = el.get_text(strip=True)
    #         break
        
    try:
        availability = soup.select_one("#availability").get_text(strip=True)
    except:
        availability = "Availability not found"
    
    try:
        brand = soup.select_one("#bylineInfo").get_text(strip=True)
    except:
        brand = "Brand not found"

    try:
        image = soup.select_one("#imgTagWrapperId img")["src"]
    except:
        image = "Image not found"
    
    return {
        "title": title,
        "price": price,
        "availability": availability,
        "brand": brand,
        "image": image
    }
