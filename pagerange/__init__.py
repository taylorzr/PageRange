import re

class PageRange(set):
	def __init__(self, pages=[]):
		"""
			Args:
				pages: Either a comma or space separated list of integers,
				or a range string (formed by a dash separated pair of integers.
		"""
		super(PageRange, self).__init__()
		if type(pages) is str:
			self._parse_range(pages)
		elif type(pages) is list:
			for p in pages:
				self.add_page(p)
		else:
			e = TypeError()
			e.args += ('Argument must be a well formed string or list of integers',)
			raise e

	def __str__(self):
		return self.range

	def __repr__(self):
		return """PageRange("{0}")""".format(self.range)

	def _parse_range(self, page_range):
		# extract dashed sub-patterns
		dash_pattern = '(?P<start>\d+)\s*-\s*(?P<end>\d+)'
		prog = re.compile(dash_pattern)
		result = prog.search(page_range)
		while result != None:
			start = result.group('start')
			end = result.group('end')
			left, right = result.span()

			# raise exception if start > end
			if start > end:
				e = ValueError()
				e.args += ("Wrong interval boundaries '{}', lower bound {} is greater than upper bound {}".format(page_range[left:right], start, end),)
				raise e

			self.add_pages(list(range(int(start), int(end)+1)))

			# discard from page_range expression that's just been processed
			page_range = page_range[:left] + page_range[right:]

			result = prog.search(page_range)

		# then extract all remaining integers, comma or space separated
		page_range = list(filter(lambda x: x!= '', page_range.replace(',', '').split(' ')))
		for page in page_range:
			self.add_page(page)

	@property
	def pages(self):
		return sorted(list(self))

	@property
	def range(self):
		if 0 == len(self):
			return ""

		elif 1 == len(self):
			return str(list(self)[0])

		else:
			pages = sorted(list(self))
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
		try:
			p = int(page)
			self.add(p)
		# could not convert page to int
		except ValueError as e:
			e.args += ('Argument must be a well formed string or list of integers',)
			raise

	def remove_page(self, page):
		if type(page) is not int:
			e = ValueError()
			e.args += ('Argument must be a well formed string or list of integers',)
			raise e
		else:
			self.remove(page)

	def add_pages(self, pages):
		for page in pages:
			self.add_page(page)

	def remove_pages(self, pages):
		for page in pages:
			self.remove_page(page)

	def add_range(self, page_range):
		pages = self._parse_range(page_range)
		self.add_pages(pages)

	def remove_range(self, page_range):
		pages = self._parse_range(page_range)
		self.remove_pages(pages)

if __name__ == '__main__':
	pr = PageRange(" 12, 14, 30  -32, 31-33 45")
	print(pr)
	for i in pr:
		print(i)