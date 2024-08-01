from __future__ import annotations
import sys
import requests
from tqdm import tqdm
def sizeof_fmt(num: int | float) -> str:
    for x in ['bytes', 'KB', 'MB', 'GB']:
        if num < 1024.0:
            return "%.1f %s" % (num, x)

        num /= 1024.0

    return "%.1f %s" % (num, 'TB')
def load(filename):
    url = "https://reedflystorage.blob.core.windows.net/vocalizations/wolves/" + filename
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    print('From content-length:', sizeof_fmt(total_size))

    chunk_size = 1024
    num_bars = int(total_size / chunk_size)
    with open(filename, 'wb') as f:
        for data in tqdm(response.iter_content(chunk_size), total=num_bars, unit='KB', file=sys.stdout):
            f.write(data)
        print("upload ", filename)

filename = "./wolves.txt"
with open(filename, 'r') as f:
    for line in f.readlines():
        name = line
        name = name[:-1]
        load(name)
