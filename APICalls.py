from PyQt5.QtCore import pyqtSignal, QThread
import asyncio
import aiohttp
import datetime

class UpdatePriceThread(QThread):
    ApiReceive = pyqtSignal(str, int)
    NetworkActivityData = pyqtSignal(list, list)
    OnlineData = pyqtSignal(list, list, list, list, list)

    async def update_price(self):
        urls = [
        {'url': "https://api.stats.golem.network/v1/network/provider/average/earnings", 'value': 'average_earnings'},
        {'url': "https://api.stats.golem.network/v1/network/earnings/6", 'value': 'total_earnings'},
        {'url': "https://api.stats.golem.network/v1/network/earnings/24", 'value': 'total_earnings'},
        {'url': "https://api.stats.golem.network/v1/network/earnings/90d", 'value': 'total_earnings'},
    ]

        while True:
            async with aiohttp.ClientSession() as session:
                for i, url_data in enumerate(urls, start=1):
                    url = url_data['url']
                    value_key = url_data['value']
                    async with session.get(url, ssl=False) as resp:
                        data = await resp.json()
                        Value = round(data[value_key], 3)
                        CallID = i
                        self.ApiReceive.emit(str(Value) + " GLM", CallID)
                """async with aiohttp.ClientSession() as session:
                async with session.get("https://api.coingecko.com/api/v3/coins/golem?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false", ssl=False) as resp:
                    data = await resp.json()
                    data = data["market_data"]
                    data = data["current_price"]
                    price = round(data["usd"], 3)
                    self.GolemTokenPrice.emit("$" + str(price)) """
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.stats.golem.network/v1/network/utilization", ssl=False) as resp:
                    data = await resp.json()
                    if data['status'] == 'success':
                        values = data["data"]["result"][0]["values"]
                        timestamps = [value[0] for value in values]
                        provider_amount = [value[1] for value in values]
                        self.NetworkActivityData.emit(timestamps, provider_amount)
                        #print(timestamps)
                        #print(provider_amount)
                    else:
                        raise Exception("API request was not successful")
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.stats.golem.network/v1/network/historical/stats/30m", ssl=False) as resp:
                    data = await resp.json()
                    if resp.status == 200:
                        timestamps = []
                        cores = []
                        online = []
                        memory = []
                        disk = []

                        for item in data:
                            date = (item["date"])
                            dt = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f%z')
                            unix_timestamp = dt.timestamp()
                            timestamps.append(unix_timestamp)
                            cores.append(item["cores"])
                            online.append(item["online"])
                            memory.append(item["memory"])
                            disk.append(item["disk"])

                        self.OnlineData.emit(timestamps, cores, online, memory, disk)
                    else:
                        raise Exception("API request was not successful")
            self.sleep(10)

    def run(self):
        while True:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.update_price())

def ApiThreadConnection(ApiCallLoop, Window):
    ApiCallLoop.ApiReceive.connect(lambda Value, CallID: Window.ApiReceive(Value, CallID))
    ApiCallLoop.NetworkActivityData.connect(lambda timestamps, provider_amount: Window.NetworkActivityUpdate(timestamps, provider_amount))
    ApiCallLoop.OnlineData.connect(
        lambda timestamps, cores, online, memory, disk: 
        (
            Window.OnlineDiskUpdate(timestamps, disk), 
            Window.OnlineCoresUpdate(timestamps, cores), 
            Window.OnlineMemoryUpdate(timestamps, memory), 
            Window.OnlineProvidersUpdate(timestamps, online)
        )
    )

    ApiCallLoop.start()