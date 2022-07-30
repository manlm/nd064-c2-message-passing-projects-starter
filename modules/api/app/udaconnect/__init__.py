import os

from app.udaconnect.models import Connection, Location, Person  # noqa
from app.udaconnect.schemas import ConnectionSchema, LocationSchema, PersonSchema  # noqa


def register_routes(api, app, root="api"):
    if "APP" in os.environ and os.environ["APP"] == "connection":
        from app.udaconnect.connection_controller import api as udaconnect_connection_api
        api.add_namespace(udaconnect_connection_api, path=f"/{root}")
    else:
        from app.udaconnect.person_controller import api as udaconnect_person_api
        api.add_namespace(udaconnect_person_api, path=f"/{root}")
