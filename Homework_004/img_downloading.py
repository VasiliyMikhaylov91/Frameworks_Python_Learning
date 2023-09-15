import os
from threading import Thread
from multiprocessing import Process
from sys import argv
from os import chdir, path
import time
import asyncio
import aiohttp
import aiofiles
import requests


def download(url: str):
    start_time = time.time()
    response = requests.get(url).content
    filename = url[url.rfind('/') + 1:]
    with open(filename, 'wb') as img:
        img.write(response)
    print(f"Downloading {filename} {time.time() - start_time:.2f}seconds")


def download_all(urls: list[str], method_name: str = 'multiprocessing'):
    start_time = time.time()
    items = []

    for url in urls:
        if method_name == 'threading':
            item = Thread(target=download, args=[url])
        else:
            item = Process(target=download, args=(url,))
        items.append(item)
        item.start()

    for item in items:
        item.join()

    print(f"{method_name} downloading {time.time() - start_time}seconds")


async def async_download(url):
    start_time = time.time()
    filename = url[url.rfind('/') + 1:]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            f = await aiofiles.open(filename, mode='wb')
            await f.write(await response.read())
            await f.close()

    print(f"Async downloading {filename} {time.time() - start_time}seconds")


async def async_download_all(urls: list[str]):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(async_download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


def async_main(urls: list[str]):
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_download_all(urls))
    print(f"Async downloading {time.time() - start_time}seconds")


if __name__ == '__main__':
    images = ['https://www.sunhome.ru/i/wallpapers/57/raiskoe-ozero.orig.jpg',
              'https://gas-kvas.com/uploads/posts/2023-02/1675484251_gas-kvas-com-p-kartinki-dlya-fonovogo-risunka'
              '-raboch-stol-43.jpg']
    images_list = images
    if len(argv) > 1:
        images_list = argv[1:]
    if not path.isdir('threading_download'):
        os.mkdir('threading_download')
    chdir('./threading_download')
    download_all(images_list, 'threading')
    chdir('../')
    if not path.isdir('multiprocessing_download'):
        os.mkdir('multiprocessing_download')
    chdir('./multiprocessing_download')
    download_all(images_list)
    chdir('../')
    if not path.isdir('asynch_download'):
        os.mkdir('asynch_download')
    chdir('./asynch_download')
    async_main(images_list)
    chdir('../')
