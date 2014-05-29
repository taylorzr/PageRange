

class PageRange(set):
    def __init__(self, pages=[]):
        """
            Args:
                pages: Either a list of integers, or a range string.
        """
        super(PageRange, self).__init__()
        if type(pages) is str:
            pages = self._parse_range(pages)
        for page in pages:
            self.add_page(page)

    def __str__(self):
        return self.range

    def __repr__(self):
        return """PageRange("{0}")""".format(self.range)

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
            page_range = str(pages[0])
            sequential = False
            for current_page, previous_page in zip(pages[1:], pages):
                difference = current_page - previous_page
                if difference > 1:
                    if sequential:
                        page_range = "-".join([page_range, str(previous_page)])
                    page_range = ",".join([page_range, str(current_page)])
                    sequential = False
                if difference == 1:
                    if current_page == pages[-1]:
                        page_range = "-".join([page_range, str(current_page)])
                    sequential = True

            return page_range

    def add_page(self, page):
        if not type(page) == int:
            raise TypeError
        else:
            self.update([page])

    def remove_page(self, page):
        if not type(page) == int:
            raise TypeError
        else:
            self.remove(page)
