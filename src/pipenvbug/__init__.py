from pyramid.config import Configurator
from pyramid.view import view_config


@view_config(route_name="example", renderer="json")
def example(request):
    return {"msg": "It works!"}


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route("example", pattern="/")
    return config.make_wsgi_app()
