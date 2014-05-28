=========
pagerange
=========

Pagerange is a simple module that provides a PageRange object typically used in printing.

Usage::
    page_range = PageRange([1,2,3,5,10])
    page_range.range    # -> "1-3, 5, 10"
    page_range.pages    # -> [1, 2, 3, 5, 10]
    page_range.add_page(6)
    page_range.remove_page(5)

