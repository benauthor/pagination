import paginate
import nose
from nose.tools import raises

class TestPagination:
    def test_long_page_gets_paginated(self):
        pages, contents = paginate.paginate('<p>Hello</p><p>world</p>', 1, 5)
        assert pages > 1 
    def test_pagination_gets_right_text(self):
        pages, contents = paginate.paginate('<p>Hello</p><p>world</p>', 2, 5)
        assert contents == 'llo</'
    def test_short_pages_pass_right_through(self):
        pages, contents = paginate.paginate('<p>Hello</p><p>world</p>', 1, 1000)
        assert contents == '<p>Hello</p><p>world</p>'
    def test_short_pages_total_one_page(self):
        pages, contents = paginate.paginate('<p>Hello</p><p>world</p>', 1, 1000)
        assert pages == 1
    @raises(paginate.OutOfRange)
    def test_out_of_range_raises(self):
        pages, contents = paginate.paginate('<p>Hello</p><p>world</p>', 2, 1000)

class TestWordPagination:
    def test_wordpagination_gets_paginated(self):
        pages, contents = paginate.wordpaginate('Avast ye landlubbers!', 2, 6)
        assert pages > 1
    def test_wordpagination_splits_on_words(self):
        pages, contents = paginate.wordpaginate('Avast ye landlubbers!', 2, 6)
        assert contents == 'landlubbers!'
    def test_short_pages_pass_right_through(self):
        pages, contents = paginate.wordpaginate('Avast ye landlubbers!', 1, 1000)
        assert contents == 'Avast ye landlubbers!'
    def test_short_pages_total_one_page(self):
        pages, contents = paginate.wordpaginate('Avast ye landlubbers!', 1, 1000)
        assert pages == 1
    @raises(paginate.OutOfRange)
    def test_out_of_range_raises(self):
        pages, contents = paginate.wordpaginate('Avast ye landlubbers!', 2, 1000)

if __name__ == "__main__":
    nose.main()
