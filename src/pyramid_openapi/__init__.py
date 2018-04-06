from .interfaces import IOASUtility
from .utility import OpenAPIUtility, OASRequestProperty
from .renderer import YAML


def includeme(config):
    settings = config.get_settings()
    spec_path = settings.get('openapi.spec')

    config.add_renderer('yaml', YAML())

    utility = OpenAPIUtility(config.absolute_asset_spec(spec_path))
    config.registry.registerUtility(utility, IOASUtility)
    config.add_request_method(
        callable=OASRequestProperty,
        name='oas',
        property=True,
        reify=True
    )

    config.add_route('pyramid_openapi.yaml', '/openapi.yaml')
    config.add_route('pyramid_openapi.json', '/openapi.json')
    config.add_route('pyramid_openapi.redoc', '/redoc')
    config.add_route('pyramid_openapi.swagger', '/swagger')
    config.add_view(route_name='pyramid_openapi.redoc', renderer='apidocs.pt')
    config.add_view(route_name='pyramid_openapi.swagger', renderer='swagger.pt')
    config.scan('.views')
