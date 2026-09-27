import asyncio
from aiohttp import web

class MCPServer:
    def __init__(self, app):
        self.app = app
        self.clients = set()

    async def handle_client(self, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        self.clients.add(ws)
        try:
            async for msg in ws:
                if msg.type == web.WSMsgType.TEXT:
                    for client in self.clients:
                        if client is not ws:
                            await client.send_str(msg.data)
                elif msg.type == web.WSMsgType.ERROR:
                    print('WebSocket connection closed with exception %s' %
                          ws.exception())
        finally:
            self.clients.remove(ws)
            await ws.close()

    async def start(self):
        app = self.app
        app.router.add_get('/ws', self.handle_client)
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, 'localhost', 8080)
        await site.start()

async def main():
    app = web.Application()
    mcp_server = MCPServer(app)
    await mcp_server.start()
    await app.shutdown()

if __name__ == "__main__":
    asyncio.run(main())