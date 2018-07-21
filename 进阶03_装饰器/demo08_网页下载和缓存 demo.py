# _Author: zc-cris

import os
from urllib.request import urlopen


def cache(func):
    def inner(*args, **kwargs):
        # 缓存文件存在并且有内容
        if os.path.exists('cache') and os.path.getsize('cache'):
            with open('cache', 'rb') as file:
                return file.read()

        else:
            # 如果文件不存在，则创建文件并且写入网页的二进制内容
            with open('cache', 'wb') as file:
                result = func(*args, **kwargs)
                print("------------")
                file.write(result)
                return result

    return inner


@cache
def get_url_content(url):
    content = urlopen(url).read()
    return content


result = get_url_content('http://www.baidu.com')
print(result)
