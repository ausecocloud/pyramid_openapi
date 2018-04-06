from pyramid.view import view_config
import yaml

from .interfaces import IOASUtility


@view_config(route_name='pyramid_openapi.yaml', renderer='yaml',
             request_method='GET', cors=True)
def openapi_yaml(request):
    utility = request.registry.getUtility(IOASUtility)
    return yaml.load(utility.spec_stream())


@view_config(route_name='pyramid_openapi.json', renderer='json',
             request_method='GET', cors=True)
def openapi_json(request):
    utility = request.registry.getUtility(IOASUtility)
    return yaml.load(utility.spec_stream())
