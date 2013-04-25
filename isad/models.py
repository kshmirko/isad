# -*- coding: utf-8 -*-
from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    )
                
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )
                            
from zope.sqlalchemy import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

from datetime import datetime
#Определим каким образом будут храниться новости в нашей базе
class NewsPage(Base):
    """
    Класс структуры новостей
    """
    __tablename__ = 'newspages'
    id = Column(Integer, primary_key=True) #Уникальный идентификатор
    timestamp = Column(DateTime)
    category = Column(Text)  #Категория новостей
    title = Column(Text, unique=True)      #заголовок
    data = Column(Text) 
    
    def __init__(self, category, title, data):
	self.timestamp = datetime.now()
        self.category = category
        self.title = title
        self.data = data


class Page(Base):
    """
    Класс для обычных информационных страниц (требует изменений в дальнейшем)
    """
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    data = Column(Text)
    
    def __init__(self, name, data):
        self.name = name
        self.data = data


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
    
    

