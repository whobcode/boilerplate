from playwright.async_api import async_playwright, Browser, Page, Playwright
from typing import Optional

class WebAgent:
    """
    An agent to interact with web pages using Playwright.
    """

    def __init__(self):
        self.playwright: Optional[Playwright] = None
        self.browser: Optional[Browser] = None
        self.page: Optional[Page] = None

    async def start(self):
        """
        Starts the playwright browser.
        """
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch()
        self.page = await self.browser.new_page()

    async def stop(self):
        """
        Stops the playwright browser.
        """
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

    async def navigate(self, url: str):
        """
        Navigates to a URL.
        """
        if not self.page:
            raise Exception("Agent not started. Call start() first.")
        await self.page.goto(url)

    async def fill_field(self, selector: str, value: str):
        """
        Fills a form field.
        """
        if not self.page:
            raise Exception("Agent not started. Call start() first.")
        await self.page.locator(selector).fill(value)

    async def take_screenshot(self, path: str):
        """
        Takes a screenshot of the page.
        """
        if not self.page:
            raise Exception("Agent not started. Call start() first.")
        await self.page.screenshot(path=path)
