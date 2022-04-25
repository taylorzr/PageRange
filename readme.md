# PageRange

PageRange is a simple module that provides a PageRange object typically used in printing. Typical usage:

    from pagerange import PageRange

    page_range = PageRange([1,2,3,5,10])
    page_range.range    # -> "1-3, 5, 10"
    page_range.pages    # -> [1, 2, 3, 5, 10]
    page_range.add_page(6)
    page_range.remove_page(5)

	for p in page_range:
		print(i) # or whatever
		
Input strings must correspond to comma or space separated integers, or dashed range (i-j), such as:

	page_range = PageRange('1, 3-5, 8 10')