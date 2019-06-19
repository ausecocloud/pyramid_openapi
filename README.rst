No longer maintained use `pyramid_openapi3 <https://github.com/Pylons/pyramid_openapi3>`_ instead


pyramid_openapi
===============


Provides small helpers to handle OpenAPI specs and request validation/parsing.


YAML render
-----------

This package adds an additional renderer to output contents as yaml.


OpenAPI specs
-------------

This package adds some small helper views to download an OpenAPI specification as yaml or json. Additionally, there are two templates which render the OpenAPI specs with Swagger-UI and ReDOC.

It also extends the request object with an attribute ```oas``` to parse and verify requests according to the given OpenAPI spec.

Pyramid route patterns are used to find the correct API path in the OpenAPI spec.

Configuration
=============

All configuration options are prefixed with ```openapi.``` .

.. code:: ini

    # this can either be a pyramid asset specification or an absolute path.
    openapi.spec = mypackage:path/to/openapi.yaml


Usage
=====

Include the package in your configuration

.. code:: python

    config.include('pyramid_openapi')


Use the provided utility in your view code

.. code:: python

    @view_config(....)
    def myview(request):
        # validate and get url parameters
        params = request.oas.validate_params().parameters
        # pull out params from location (query, header, path)
        params = params.get('query')
        # validate and get requestBody
        body = request.oas.validate_params().body

        ...

        return {}
