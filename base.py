from pyppeteer import launch
import os
import asyncio
from review_scrapper import ReviewScrapper
from dotenv import load_dotenv

load_dotenv()

import asyncio

class BaseScrapping:

    # method to launch browser
    async def get_browser(self):
        print("Launching browser")
        return await launch(
            ignoreHTTPSErrors=True,
            headless=True,
            args=[
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-accelerated-2d-canvas',
            '--no-first-run',
            '--no-zygote',
            '--single-process',
            '--disable-gpu'
        ]
    )


    # method to open page
    async def get_page(self, url):
        browser = await self.get_browser()
        print("Opening page")
        page = await browser.newPage()
        print("Going to url")
        await page.goto(url, timeout=1000000)
        return page

    # extracting data by calling particular scrapper
    async def extract(self, url):
        page = await self.get_page(url)
        data = await ReviewScrapper(page).scrape()
        return data

    
try:
    loop = asyncio.get_event_loop()
    url = os.getenv("AMAZON_URL")
    result = loop.run_until_complete(BaseScrapping().extract(url))
    print({"final_data": result})
except Exception as e:
    print(e)
    print({"Error": e})