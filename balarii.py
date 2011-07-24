from elementtree import ElementTree
def parse_it(source):
	root = ElementTree.fromstring(source.encode('utf-8')).getroot()
	return root
