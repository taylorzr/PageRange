from unittest import TestCase, main
from pagerange import PageRange

pr = PageRange([1,2,3,5,10])
pr.add_page(6)
pr.remove_page(5)
print pr, "->", pr.pages

pr = PageRange("1-3,5,10")
pr.add_page(6)
pr.remove_page(5)
print pr, "->", pr.pages

class PageRangeTestCase(TestCase):
    pass
