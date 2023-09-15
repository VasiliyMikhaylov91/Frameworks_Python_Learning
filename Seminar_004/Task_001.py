from threading import Thread
import requests

urls = ['https://www.google.com/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://bootstrap-4.ru',
        'https://www.wikipedia.org',
        'http://web.archive.org',
        'https://online.sberbank.ru/CSAFront/index.do',
        'https://www.tinkoff.ru'
        ]


def download(url):
    response = requests.get(url)
    filename = 'processing_' + url.replace('https://', '') \
        .replace('http://', '') \
        .replace('.', '_') \
        .replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloading {filename} complete")


def main_thr():
    threads = []

    for url in urls:
        thread = Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main_thr()
