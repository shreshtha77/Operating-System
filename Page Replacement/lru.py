# Python implementation of Least Recently Used (lru)
def pageFaults(pages, n, capacity):

	# To represent set of current pages. We use an unordered_set so that we quickly checkif a page is present in set or not
	s = set()

	# To store least recently used indexes of pages.
	indexes = {}

	# Start from initial page
	page_faults = 0
	for i in range(n):

		# Check if the set can hold more pages
		if len(s) < capacity:

			# Insert it into set if not present already which represents page fault
			if pages[i] not in s:
				s.add(pages[i])

				# increment page fault
				page_faults += 1

			# Store the recently used index of each page
			indexes[pages[i]] = i

		# If the set is full then need to perform lru i.e. remove the least recently used pageand insert the current page
		else:

			# Check if current page is not already present in the set
			if pages[i] not in s:

				# Find the least recently used pagesthat is present in the set
				lru = float('inf')
				for page in s:
					if indexes[page] < lru:
						lru = indexes[page]
						val = page

				# Remove the indexes page
				s.remove(val)

				# insert the current page
				s.add(pages[i])

				# increment page fault
				page_faults += 1

			# Update the current page index
			indexes[pages[i]] = i

	return page_faults


# Driver code
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
n = len(pages)
capacity = 4
print(pageFaults(pages, n, capacity))
