from unittest import TestCase, main
from pagerange import PageRange


class PageRangeTestCase(TestCase):
    def setUp(self):
        self.page_range_1 = PageRange([1, 2, 3, 4, 5, 10, 42])
        self.page_range_2 = PageRange("1-5, 10, 42")

    def test_add_page(self):
        self.assertNotIn(6, self.page_range_1)
        self.assertTrue(7 == len(self.page_range_1))
        self.page_range_1.add_page(6)
        self.assertIn(6, self.page_range_1)
        self.assertTrue(8 == len(self.page_range_1.pages))

    def test_remove_page(self):
        self.assertIn(42, self.page_range_1)
        self.assertTrue(7 == len(self.page_range_1))
        self.page_range_1.remove_page(42)
        self.assertNotIn(42, self.page_range_1)
        self.assertTrue(6 == len(self.page_range_1))

    def test_equality(self):
        self.assertEquals(self.page_range_1, self.page_range_2)

    def test_unique(self):
        self.page_range_2.add_page(1)
        self.assertEquals(self.page_range_1, self.page_range_2)

    def test_noninteger(self):
        self.assertRaises(TypeError, self.page_range_1.add_page, "x")
        self.assertRaises(TypeError, self.page_range_1.remove_page, "x")


if __name__ == "__main__":
    main()