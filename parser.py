from bs4 import BeautifulSoup


def parse(content):
    return BeautifulSoup(content, 'html.parser')


def get_articles_list(content):
    page = parse(content)

    # Find all article articles on the page
    articles = page.find_all('article')
    result = []

    for article in articles:
        article_type = article.find('span', {'data-test': 'article.type'})
        link = article.find('a', {'data-track-action': 'view article'})

        result.append({"type": article_type.text.strip(), "link": link['href']})

    return result


def parse_article(content):
    page = parse(content)

    title = page.find("title")
    body = page.find("p", {"class": "article__teaser"})

    return {"title": title.text.strip(), "body": body.text.strip()}
