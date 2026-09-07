import requests
from bs4 import BeautifulSoup
# Hacker News URL
url = "https://news.ycombinator.com/"

# Send request to the website
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:

    # Parse HTML using Beautiful Soup
    soup = BeautifulSoup(response.text, "html.parser")

    print("=" * 80)
    print("             HACKER NEWS HEADLINES")
    print("=" * 80)

    # Find all story links
    stories = soup.select("span.titleline > a")

    # Display headlines and hyperlinks
    for number, story in enumerate(stories, start=1):

        headline = story.get_text(strip=True)
        link = story.get("href")

        print(f"\n{number}. {headline}")
        print(f"   Link: {link}")

else:
    print("Failed to access the website.")
    print("Status Code:", response.status_code)

