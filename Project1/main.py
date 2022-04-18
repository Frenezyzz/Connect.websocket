
import asyncio
import websockets
import time
import ast
from summary import *
from cleanScreen import CleanScreen

class App:
    url = ''
    def __init__(self,url):
        self.url = url
    async def getData(self):
        async with websockets.connect(self.url,ping_interval=None) as websocket:
            currentTime = 0 
            interval = 0.200
            execution = True
            bValue = 0
            blockSummaries = []
            
            while execution:
                summary = Summary()
                while currentTime < interval:
                    
                    start = time.time()

                    msg = await websocket.recv()
                    msg_dic = ast.literal_eval(msg)
                    bValue = msg_dic['b']

                    fillSummary = summary.setSummary(bValue)
                    
                    final = time.time()
                    currentTime += final-start             
                blockSummaries.append(fillSummary)
                print(fillSummary)
                currentTime = 0
                if len(blockSummaries) > 100:
                    CleanScreen()
                    blockSummaries.clear()

            

def main():
    a = App('ws://209.126.82.146:8080')
    asyncio.get_event_loop().run_until_complete(a.getData())

if __name__ == '__main__':
    main()

            


