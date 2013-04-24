from pyramid.i18n import TranslationStringFactory
from pyramid.view import view_config


_ = TranslationStringFactory('isad')

@view_config(route_name='home', context='isad.models.MyModel', renderer='isad:templates/index.jinja2')
def home(ctx,request):
    
    return {'project':_('Hello!', default='${name}', mapping={'name':'1'}),'mainmenulist':ctx.menus}
    
    
@view_config(route_name='contacts', context='isad.models.MyModel', renderer='isad:templates/contacts.jinja2')
def contacts(ctx, request):
    return {'project':'ISAD','mainmenulist':ctx.menus}
    

@view_config(route_name='news', context='isad.models.MyModel', renderer='isad:templates/news.jinja2', request_method='GET')
def news(ctx, request):
    return {'project':'ISAD','mainmenulist':ctx.menus}