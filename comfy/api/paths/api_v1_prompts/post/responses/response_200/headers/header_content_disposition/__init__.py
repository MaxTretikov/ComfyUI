# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from comfy.api.shared_imports.header_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from . import schema


class ContentDisposition(api_client.HeaderParameterWithoutName):
    style = api_client.ParameterStyle.SIMPLE
    schema: typing_extensions.TypeAlias = schema.Schema
