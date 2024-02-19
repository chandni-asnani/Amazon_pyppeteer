import pandas as pd
import asyncio
from utils import extract_country_and_date, extract_rating, check_or_click


class ReviewScrapper:

    def __init__(self, page):
        self.page = page
        self.data = pd.DataFrame()
        self.status = True
        self.iteration = 0

    async def get_reviews(self):
        while self.status:
            self.iteration += 1
            review = await self.page.querySelectorAll('#cm_cr-review_list .a-section.celwidget')
            rows = []
            for r in review:
                reviewer = await r.Jeval('.a-profile-name', "(element) => element.textContent")
                review = await r.Jeval('.review-text-content', "(element) => element.textContent")
                review_date = await r.Jeval('.review-date', "(element) => element.textContent")
                rating = await r.Jeval('.review-rating .a-icon-alt', "(element) => element.textContent")
                review_country, review_date = extract_country_and_date(review_date)
                rating = extract_rating(rating)
                rows.append({"reviewer": reviewer, "review": review.strip(), "review_date": review_date, "rating": rating, "review_country": review_country})
            data = pd.DataFrame(rows)
            self.data = pd.concat([self.data, data], ignore_index=True)
            self.status = await check_or_click(self.page)
            await asyncio.sleep(2)
    
    async def scrape_all_reviews(self):
        await asyncio.gather(
            *[
                self.page.click("#reviews-medley-footer .a-text-bold"),
                self.page.waitForSelector('#cm_cr-review_list .a-profile-name'),
            ],
            return_exceptions=False
        )
        print("Clicked on 'See all reviews' and waiting for the reviews to load.")
    
    def upload_data(self):
        self.data.to_csv("reviews2.csv", index=False)
    
    async def scrape(self):
        try:
            await self.scrape_all_reviews()
            await self.get_reviews()
        except Exception as e:
            print(e, self.iteration)
        self.upload_data()
        return {
            "data": self.data
        }