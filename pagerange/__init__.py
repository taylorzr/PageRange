# TODO:
#   Raise errors on bad input, i.e. non-integers

class PageRange(set):
    def __init__(self, pages=[]):
        """
            Args:
                pages: Either a list of intergers, or a range string.
        """
        if type(pages) is str:
            pages = self._parse_range(pages)
        self.update(pages)
        super(PageRange, self).__init__(pages)

    def __str__(self):
        return self.range

    def __repr__(self):
        return "{0}(\"{1}\")".format(self.__class__, self.range)

    def _parse_range(self, page_range):
        pages = []
        if "," in page_range:
            page_range = page_range.split(",")
            for part in page_range:
                if "-" in part:
                    start, end = part.split("-")
                    for page in range(int(start), int(end)+1):
                        pages.append(page)
                else:
                    pages.append(int(part))
            return pages

        elif "-" in page_range and "," not in page_range:
            start, end = page_range.split("-")
            for page in range(int(start), int(end)+1):
                pages.append(page)
            return pages

        elif not "," in page_range and not "-" in page_range:
            return [int(page_range)]

        return pages

    @property
    def pages(self):
            return list(self)

    @property
    def range(self):
        if 0 == len(self):
            return ""

        elif 1 == len(self):
            return str(list(self)[0])

        else:
            pages = list(self)
            range_ = str(pages[0])
            sequential = False
            for current_page, previous_page in zip(pages[1:], pages):
                difference = current_page - previous_page
                if difference > 1:
                    if sequential:
                        range_ = "-".join([range_, str(previous_page)])
                    range_ = ",".join([range_, str(current_page)])
                    sequential = False
                if difference == 1:
                    if current_page == pages[-1]:
                        range_ = "-".join([range_, str(current_page)])
                    sequential = True

            # Return the range
            return range_

    def add_page(self, page):
        self.update([page])

    def remove_page(self, page):
        self.remove(page)


if __name__ == "__main__":
    pr = PageRange([1,2,3,5,10])
    pr.add_page(6)
    pr.remove_page(5)
    print pr, "->", pr.pages

    pr = PageRange("1-3,5,10")
    pr.add_page(6)
    pr.remove_page(5)
    print pr, "->", pr.pages

