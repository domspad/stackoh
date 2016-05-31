
import stackexchange

so = stackexchange.Site(stackexchange.StackOverflow)

# TODO get fraction of questions unanswered

def get_tag_info(tagname):
	"""
	"""
	tag = so.tag(tagname)
	return tag.count
