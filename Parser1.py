import requests
from bs4 import BeautifulSoup
import re
import sqlite3
# soup = BeautifulSoup(requests.get('https://www.onliner.by/').text, 'lxml')

def name_news():
    soup = BeautifulSoup(requests.get('https://www.onliner.by/').text, 'lxml')
    # name_news = [i.text for i in soup.find_all('h3', limit=5)]
    # name_news = [line.strip() for line in name_news]
    name_news=list(map(lambda x: x.strip(), [i.text for i in soup.find_all('h3', limit=5)]))
    return (name_news)

def category_news():
    soup = BeautifulSoup(requests.get('https://www.onliner.by/').text, 'lxml')
    return([i.text for i in soup.find_all(class_='b-tile-section', limit=5)])

def link_news():
    soup = BeautifulSoup(requests.get('https://www.onliner.by/').text, 'lxml')
    return ([a['href'] for a in soup.find_all('a', href=True, class_="b-tile-main", limit=5)])

def link_and_load_image():
    import wget
    soup = BeautifulSoup(requests.get('https://www.onliner.by/').text, 'lxml')
    a = ([str(i) for i in soup.find_all( class_='b-tile-bg', limit=5)])
        # filename = wget.download(i, out='D:\Скачал')
    return ([re.search('(?<=\()[^)]+', i).group(0) for i in a])

def main():
    name_news()
    category_news()
    link_news()
    link_and_load_image()

# def create_db():
    db = sqlite3.connect('onliner1.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS top_5 (name_news text, category_news text, link_news text, link_image text)""")
    db.commit()

    common = list(zip(name_news(),category_news(),link_news(), link_and_load_image()))
    sql.execute("SELECT name_news FROM top_5")
    sql.execute("SELECT category_news FROM top_5")
    sql.executemany("INSERT INTO top_5 VALUES (?,?,?,?)", common)
    db.commit()
    def get_posts():
        sql.execute("SELECT * FROM top_5")
        print(sql.fetchall())

    get_posts()
    db.close()

if __name__ == "__main__":
    main()
    # create_db()