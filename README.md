# 1)BooksScrapy:
This is a Scrapy project to scrape information about books at http://books.toscrape.com/

## Extracted data

This project extracts all data including book, price, book_url,book_image_url etc...
A sample item:

<pre><code>
{
    'title': 'A Light in the Attic',
    'upc': '£51.77',
    'product_type': 'Books',
    'price': '£51.77',
    'tax': '£0.00',
    'stock': 'In stock (22 available)',
    'reviews': '0',
    'rating': '3'
}
</pre></code>

## Pipelines
This project contains pipelines are meant to show you how to create csv files from the scraped data. You can disable pipelines in settings.py.

## execution

<pre><code>
scrapy crawl books
</pre></code>

# 2)Qoutes:
This is a Scrapy project to scrape information about qoutes at https://quotes.toscrape.com/js/

## Extracted data

This project extracts all data including quote, author, tags etc...
A sample item:


<pre><code>

{'quote': '“There are few people whom I really love, and still fewer of whom I think well. The more I see of the world, the more am I dissatisfied with it; and every day confirms my belief of the inconsistency of all human characters, and of the little dependence that can be placed on the appearance of merit or sense.”', 'author': 'Jane Austen', 'tags': ['Tags: ', 'elizabeth-bennet', ' ', 'jane-austen']}


</pre></code>


## Pipelines
This project contains pipelines are meant to show you how to create csv files from the scraped data. You can disable pipelines in settings.py.

## execution

<pre><code>
scrapy crawl quotes
</pre></code>
