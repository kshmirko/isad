# -*- coding: utf-8 -*-
from pyramid.i18n import TranslationStringFactory
from pyramid.view import view_config

from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )
    
from .models import (
    DBSession,
    NewsPage,
    Page,
    )

_ = TranslationStringFactory('isad')

@view_config(route_name='home', context='isad.models.MyModel', renderer='isad:templates/index.jinja2')
def home(ctx,request):
    return HTTPFound(location = request.route_url('recentnews'))

@view_config(route_name='contacts', context='isad.models.MyModel', renderer='isad:templates/contacts.jinja2')
def contacts(ctx, request):
    return {'project':'ISAD','mainmenulist':ctx.menus}
    

@view_config(route_name='news', context='isad.models.MyModel', renderer='isad:templates/news.jinja2', request_method='GET')
def news(ctx, request):
    category_name = request.matchdict['category']
    pages = DBSession.query(NewsPage).filter_by(category=category_name).order_by('timestamp')
    if pages.first() is None:
	return HTTPNotFound('No such page!')
    return {'project':'ISAD','mainmenulist':ctx.menus,'category':category_name,'pages':pages}
    
@view_config(route_name='recentnews', context='isad.models.MyModel', renderer='isad:templates/recentnews.jinja2', request_method='GET')
def recentnews(ctx, request):    
    pages = DBSession.query(NewsPage).order_by('timestamp')
    if pages.first() is None:
	return HTTPNotFound('No such page!')
    return {'project':'ISAD','mainmenulist':ctx.menus,'pages':pages}
