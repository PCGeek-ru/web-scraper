import string
import os

from file import write_file
from cache import get_from_cache_or_load
from parser import get_articles_list, parse_article


def get_filename(title):
    # Remove punctuation
    title = ''.join(char for char in title if char not in string.punctuation)

    # Replace whitespaces with underscores
    title = title.replace(" ", "_")

    return f'{title}.txt'


def filter_articles_by_type(articles, type):
    return [article for article in articles if article["type"] == type]


if __name__ == '__main__':
    site = "https://nature.com"
    
    page_count = int(input())
    article_type = input()
    # page_count = 2
    # article_type = "News Feature"

    for i in range(page_count):
        page_number = i + 1
        url = f"{site}/nature/articles?sort=PubDate&year=2020&page={page_number}"
    
        page_content = get_from_cache_or_load(f'page_{page_number}.html', url)
    
        articles = get_articles_list(page_content)
        filtered_articles = filter_articles_by_type(articles, article_type)

        folder_name = f"Page_{page_number}"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        for index, article in enumerate(filtered_articles, start=1):
            page_content = get_from_cache_or_load(f'{folder_name}/{article_type + str(index)}.html', site + article["link"])

            data = parse_article(page_content)

            file_name= get_filename(data["title"])
            file_path = f"{folder_name}/{file_name}"

            write_file(file_path, data["body"].strip(), "w")
