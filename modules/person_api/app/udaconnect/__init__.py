import os

from app.udaconnect.models import Connection, Location, Person  # noqa
from app.udaconnect.schemas import ConnectionSchema, LocationSchema, PersonSchema  # noqa


def register_routes(api, app, root="api"):
    from app.udaconnect.person_controller import api as udaconnect_person_api
    api.add_namespace(udaconnect_person_api, path=f"/{root}")
