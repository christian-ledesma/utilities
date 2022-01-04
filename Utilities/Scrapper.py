from bs4 import BeautifulSoup
from requests import get

class Scrapper:
    
    def start(url, tag, class_name, headers=None):
        data = list()
        web_page = get(url, timeout=5, headers=headers if headers is not None else None)
        soup = BeautifulSoup(web_page.content, 'html.parser')
        tags = soup.find_all(tag, class_name)
        for item in tags:
            data.append(item.text)
        return list(dict.fromkeys(data)) # Removes duplicates values
