from folium import GeoJSON
from graphene import ObjectType, String

class Query(ObjectType):
    polygon = GeoJSON(required=True, name=GeoJSON())
    hello = String(required=True, name=String())

    def resolve_hello(parent, info, **kwargs):
        name = kwargs.get('name', 'World')
        return f'Hello, {name}!'