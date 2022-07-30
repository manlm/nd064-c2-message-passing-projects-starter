import os

from app.udaconnect.models import Connection, Location, Person  # noqa
from app.udaconnect.schemas import ConnectionSchema, LocationSchema, PersonSchema  # noqa


def register_routes(api, app, root="api"):
    from app.udaconnect.connection_controller import api as udaconnect_connection_api
    api.add_namespace(udaconnect_connection_api, path=f"/{root}")

