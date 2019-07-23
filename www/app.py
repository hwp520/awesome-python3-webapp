import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

async def index(request):  # 参考aiohttp的文档
    return web.Response(body='<h1>Awesome</h1>'.encode('utf-8'), content_type='text/html')

def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])  # 多看看官方文档，aiohttp和asyncio都要看
    logging.info('Server started at http://127.0.0.1:9000')
    web.run_app(app, host='127.0.0.1', port=9000)

init()