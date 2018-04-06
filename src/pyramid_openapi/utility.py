from urllib.parse import urljoin

from openapi_core import create_spec
from openapi_core.validators import RequestValidator  # , ResponseValidator
from pyramid.path import AssetResolver
import yaml

from .interfaces import IOASUtility


class OpenAPIUtility(object):

    def __init__(self, spec_path):
        self.spec_path = spec_path
        self.spec = create_spec(yaml.load(self.spec_stream()))
        self.request_validator = RequestValidator(self.spec)

    def spec_stream(self):
        return AssetResolver().resolve(self.spec_path).stream()


class OASRequestProperty(object):

    def __init__(self, request):
        self.request = request

    @property
    def utility(self):
        return self.request.registry.getUtility(IOASUtility)

    def validate_params(self, raise_errors=True):
        result = self.utility.request_validator.validate(
            PyramidRequest(self.request)
        )
        if raise_errors:
            result.raise_for_errors()
        return result


class PyramidRequest(object):
    # wrap pyramid request, to work with, openapi-core
    #

    def __init__(self, request):
        self.request = request

    @property
    def full_url_pattern(self):
        return urljoin(
            self.request.host_url,
            self.request.matched_route.pattern
        )

    @property
    def host_url(self):
        return self.request.host_url

    @property
    def method(self):
        return self.request.method.lower()

    @property
    def parameters(self):
        # return parameters based on location
        return {
            'path': self.request.matchdict,
            'query': self.request.params,
            'headers': self.request.headers,
            'cookies': self.request.cookies,
        }

    @property
    def mimetype(self):
        return self.request.content_type

    @property
    def body(self):
        if self.request.content_type == 'multipart/form-data':
            return self.request.params
        return self.request.body

    @property
    def path(self):
        return self.request.path_info

    @property
    def path_pattern(self):
        return self.request.matched_route.pattern


class PyramidResponse(object):
    # wrap pyramid response, to work with openapi-core

    def __init__(self, response):
        self.response = response

    body = NotImplemented
    status_code = NotImplemented

    mimetype = NotImplemented
