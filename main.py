from newspaper import Article
url = 'https://www.bbc.com/indonesia/articles/cpr1pnl1gqxo'

my_article = Article(url, language="id")
my_article.download()
#print(my_article.html)
my_article.parse()
print('Title:', my_article.title)
print('Author:', my_article.authors)
print('Publishing date:', my_article.publish_date)
my_article.nlp()
print('Summary: ', my_article.summary)
print('Keywords: ', my_article.keywords)