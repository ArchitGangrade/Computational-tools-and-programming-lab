import requests
from bs4 import BeautifulSoup
import csv

# Website URL
url = "https://books.toscrape.com/"

# Send request to website
response = requests.get(url)

if response.status_code == 200:

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all books
    books = soup.find_all("article", class_="product_pod")

    # Create CSV file
    with open("books.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        # Write headings
        writer.writerow([
            "Title",
            "Price",
            "Availability",
            "Rating",
            "Product URL"
        ])

        # Extract and save data
        for book in books:

            title = book.h3.a["title"]

            price = book.find(
                "p", class_="price_color"
            ).get_text(strip=True)

            availability = book.find(
                "p", class_="instock availability"
            ).get_text(strip=True)

            rating = book.find(
                "p", class_="star-rating"
            )["class"][1]

            product_url = book.h3.a["href"]

            writer.writerow([
                title,
                price,
                availability,
                rating,
                product_url
            ])

    print("Data saved to books.csv successfully.")

else:
    print("Failed to access the website.")

