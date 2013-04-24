## Пока определяем меню тупым способом
##
##
class MyModel(object):

    def __init__(self):
	self.menus={}
	self.menus['Home']='/'
	self.menus['Contacts']='/contacts'
	self.menus['News']='/news'
    pass

root = MyModel()


def get_root(request):
    return root
