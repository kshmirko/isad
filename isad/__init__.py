from pyramid.config import Configurator
from pyramid_jinja2 import renderer_factory
from isad.models import get_root

def main(global_config, **settings):
    """ This function returns a WSGI application.
    
    It is usually called by the PasteDeploy framework during 
    ``paster serve``.
    """
    settings = dict(settings)
    settings.setdefault('jinja2.i18n.domain', 'isad')

    config = Configurator(root_factory=get_root, settings=settings)
    config.add_translation_dirs('locale/')
    config.include('pyramid_jinja2')
    config.add_route('home','/')
    config.add_route('contacts','/contacts')
    config.add_route('news','/news')
    config.add_static_view('static', 'static', cache_max_age=3600)
    
    config.scan()
#    config.add_view('isad.views.my_view',
#                    context='isad.models.MyModel', 
#                    renderer="index.jinja2")

    return config.make_wsgi_app()
