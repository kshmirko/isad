# -*- coding: utf-8 -*-
from pyramid.config import Configurator
from pyramid_jinja2 import renderer_factory
from isad.models import get_root
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a WSGI application.
    
    It is usually called by the PasteDeploy framework during 
    ``paster serve``.
    """
#    settings = dict(settings)
    #Подгружаем драйвер используемой бады данных из файла конфигурации
    engine = engine_from_config(settings,'sqlalchemy.')
    #устанавливаем соединение
    DBSession.configure(bind=engine)
    

    # добавляем поддержку шаблонов jinja2 для нашего проекта
    settings.setdefault('jinja2.i18n.domain', 'isad')

    #настройка WSGI сервера
    config = Configurator(root_factory=get_root, settings=settings)
    #добавляем директорию с переводами (пока я не разобрался, с чем их едят)
    config.add_translation_dirs('locale/')
    #добавляем генератор шаблонов
    config.include('pyramid_jinja2')
    
    #прописываем маршруты
    config.add_route('home','/')
    config.add_route('contacts','/contacts')
    config.add_route('recentnews','/news')    
    config.add_route('news','/news/{category}')

    config.add_route('login','/login')
    config.add_route('logiout','/logout')
    config.add_static_view('static', 'static', cache_max_age=3600)
    
    config.scan()

    return config.make_wsgi_app()
