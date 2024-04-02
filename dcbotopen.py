import asyncio
import aiohttp

async def openbox(token):
    async with aiohttp.ClientSession() as session:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
            'Accept': '*/*',
            'Authorization': token,
            'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEyNC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEyNC4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI0LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vdGV0cmF6ZXJvLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoidGV0cmF6ZXJvLmNvbSIsInJlZmVycmVyX2N1cnJlbnQiOiJodHRwczovL2Rpc2NvcmQuY29tLyIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6ImRpc2NvcmQuY29tIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjgwNDU4LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
        }
        async with session.post("https://discord.com/api/v9/users/@me/lootboxes/open", headers=headers) as response:
            return await response.json()

async def opener():
    token = input("Discord Token: ")
    while True:
        await asyncio.sleep(2.2)
        res = await openbox(token)
        if not res:
            print('Request failed')
            continue

        if 'code' in res and res['code'] == 0:
            print('Invalid Token')
            return

        if 'retry_after' in res:
            print(f"Rate limited for: {res['retry_after']}s")
            await asyncio.sleep(res['retry_after'] - 5)
            continue

        prize = res.get('opened_item')
        if not prize:
            print('unknown error:', res)
            continue

        prize_map = {
            '1214340999644446726': 'Quack!!', 
            '1214340999644446724': '⮕⬆⬇⮕⬆⬇', 
            '1214340999644446722': 'Wump Shell',
            '1214340999644446720': 'Buster Blade', 
            '1214340999644446725': 'Power Helmet', 
            '1214340999644446723': 'Speed Boost',
            '1214340999644446721': 'Cute Plushie', 
            '1214340999644446728': 'Dream Hammer', 
            '1214340999644446727': 'OHHHHH BANANA'
        }
        print('Opened:', prize_map.get(prize))

if __name__ == "__main__":
    asyncio.run(opener())
