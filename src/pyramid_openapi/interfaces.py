from zope.interface import Interface, Attribute


class IOASUtility(Interface):

    spec_path = Attribute('Pyramid asset specification to find spec file')

    spec = Attribute('OAS spec object')

    request_validator = Attribute('OAS request validator')

    def spec_stream():
        """Return a file like object to read the openapi spec from spec_path"""
