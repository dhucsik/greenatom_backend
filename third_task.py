import requests
from bs4 import BeautifulSoup


def count_tags_with_attributes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tags = soup.find_all()

    tag_count = len(tags)
    attr_count = 0
    for tag in tags:
        if tag.attrs:
            attr_count += 1

    return tag_count, attr_count


url = "https://greenatom.ru/"
tag_count, attr_count = count_tags_with_attributes(url)
print("Number of tags:", tag_count)
print("Number of tags with attributes:", attr_count)
