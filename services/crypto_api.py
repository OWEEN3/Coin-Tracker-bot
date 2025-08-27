import aiohttp

async def fetch_prices(context):
    url = "https://api.binance.com/api/v3/ticker/price"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    context.application.bot_data["prices"] = {
                        item["symbol"]: float(item["price"]) for item in data
                    }
                    print("✅ Prices updated")
                else:
                    print(f"⚠️ Failed to fetch prices: {response.status}")
    except Exception as e:
        print(f"⚠️ Exception fetching prices: {e}")
