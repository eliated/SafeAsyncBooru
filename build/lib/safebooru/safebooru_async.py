import aiohttp
import asyncio
from bs4 import BeautifulSoup


class SafeAsyncBooru:
    BASE_URL = 'https://safebooru.org/index.php'

    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def fetch(self, endpoint, params=None):
        async with self.session.get(self.BASE_URL, params=params) as response:
            return await response.json()

    async def search_images(self, tags, limit=10):
        params = {
            'page': 'dapi',
            's': 'post',
            'q': 'index',
            'json': 1,
            'tags': tags,
            'limit': limit
        }
        return await self.fetch('', params)

    async def scrape_image_details(self, url):
        page_content = await self.fetch(url)
        soup = BeautifulSoup(page_content, 'html.parser')
        details = {}

        details['id'] = soup.find(text='Id:').find_next().text.strip()
        details['posted'] = soup.find(text='Posted:').find_next().text.strip()
        details['owner'] = soup.find(text='by:').find_next().text.strip()
        details['size'] = soup.find(text='Size:').find_next().text.strip()
        details['source'] = soup.find(text='Source:').find_next().text.strip()
        details['rating'] = soup.find(text='Rating:').find_next().text.strip()
        details['score'] = soup.find(text='Score:').find_next().text.strip()
        return details


# async def search_old(self, tags, limit=10):
#     params = {
#         'page': 'dapi',
#         's': 'post',
#         'q': 'index',
#         'json': 1,
#         'tags': tags,
#         'limit': limit
#     }
#     results = await self.fetch('', params)
#     if results:
#         sorted_results = sorted(results, key=lambda x: x.get('change', 0))
#         return sorted_results[:limit]
#     return []

    async def close(self):
        await self.session.close()
