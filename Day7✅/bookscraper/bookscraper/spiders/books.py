import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ["http://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            yield {
                "title": book.css("h3 a::attr(title)").get(),
                "price": book.css(".price_color::text").get()
            }

        # follow pagination
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
