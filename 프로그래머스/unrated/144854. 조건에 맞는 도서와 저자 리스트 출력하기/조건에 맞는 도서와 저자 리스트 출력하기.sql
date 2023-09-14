select book_id, author_name, date_format(published_date, '%Y-%m-%d')
from book,author
where book.author_id = author.author_id and book.category = '경제'
order by published_date;