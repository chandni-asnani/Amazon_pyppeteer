import re
import asyncio
from datetime import datetime

def extract_country_and_date(review_text):
    country_date_pattern = r"Reviewed in the (.+) on (.+)"
    match = re.search(country_date_pattern, review_text)
    if match:
        country = match.group(1)
        date_str = match.group(2)
        # Parse the date string into a datetime object
        try:
            date = datetime.strptime(date_str, "%B %d, %Y")
            return country, date.strftime('%Y-%m-%d')
        except ValueError as e:
            print(f"Date parsing error: {e}")
            return country, None
    else:
        return None, None

def extract_rating(rating_text):
    rating_pattern = r"(\d+(\.\d+)?) out of 5 stars"
    match = re.search(rating_pattern, rating_text)
    if match:
        rating = match.group(1)
        return rating
    else:
        return None

async def check_or_click(page):
    # Check if the element with class '.a-last.a-disable' exists
    disabled_elements = await page.querySelectorAll('.a-last.a-disable')
    if disabled_elements:
        print("Element with .a-last.a-disable exists. Doing nothing.")
        return False
    else:
        # If not disabled, find the element with class '.a-last' and click it
        next_page_elements = await page.querySelectorAll('.a-last')
        if next_page_elements:
            # Assuming there's only one such element or you want the first one
            await asyncio.gather(
            *[
                page.click(".a-last"),
                page.waitForSelector('#cm_cr-review_list .a-profile-name'),
            ],
            return_exceptions=False
        )
        else:
            print("No clickable .a-last element found.")
        return True