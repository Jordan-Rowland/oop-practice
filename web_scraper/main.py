"""Used for webscraping, needs work."""

from requests import get

from bs4 import BeautifulSoup as BS


class WebPage:
    def __init__(self, url):
        self.url = url
        self.soup = BS(get(url).text, 'html.parser')

    def get_elements(self, element, error=True):
        elems = self.soup.select(element)
        if elems:
            return elems
        else:
            if error:
                print(f'Error: {error}')
            else:
                pass

    def get_images(self, elems):
        imgs = []
        for i in elems:
            try:
                element = i['href']
                if element.lower().endswith('.jpg') or element.lower().endswith('.jpeg') \
                  or element.lower().endswith('.gif') or element.lower().endswith('.png') \
                  or element.lower().endswith('.webm') or element.lower().endswith('.gifv') \
                  or element.lower().endswith('.giphy') or element.lower().endswith('.webp') \
                  or element.lower().endswith('.mp4') or element.lower().endswith('.mpeg'):
                    imgs.append('http:' + element)
            except Exception:
                pass
        return set(imgs)

    def download_images(self, folder, elements):
        makedirs(folder + '/',exist_ok=True)
        cache = listdir('./' + folder + '/')
        for element in elements:
            filename = element.split('/')[-1]
            if filename in cache:
                print('Image exists')
                continue
            else:
                cache.append(filename)
                imgUrl = element
                print(imgUrl)
                res = get(imgUrl)
                with open(folder + '/' + filename, 'wb') as f:
                    f.write(res.content)
                    print(element.split('/')[-1] + ' DOWNLOADED')


w = WebPage("https://www.google.com/search?q=easy+web+scraping+page")
a = w.get_elements('a')
