import yaml


class YAML(object):
    """ Renderer that returns a YAML-encoded string.
    """

    def __init__(self, **kw):
        """ Any keyword arguments will be passed to the ``serializer``
        function."""
        self.kw = kw

    def __call__(self, info):
        """ Returns a plain JSON-encoded string with content-type
        ``application/yaml``. The content-type may be overridden by
        setting ``request.response.content_type``."""
        def _render(value, system):
            request = system.get('request')
            if request is not None:
                response = request.response
                ct = response.content_type
                if ct == response.default_content_type:
                    response.content_type = 'application/yaml'
            return yaml.dump(value, **self.kw)

        return _render
