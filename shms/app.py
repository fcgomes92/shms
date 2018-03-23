from flask import Flask

from flask_cors import CORS

from shms.routes import ROUTES

app = None


# def route_version(version, route):
#     return '/' + version + route


# def set_routes(api):
#     from shms.resources import auth
#
#     _versions = ['v1', ]
#     api.add_route(route_version(_versions[0], ROUTES.users_auth), auth.UserAuthenticationResource())


# def register_middleware():
#     from shms.middleware import NonBlockingAuthentication, LoggerMiddleware
#
#     cors = CORS(allow_all_origins=True,
#                 allow_all_headers=True,
#                 allow_credentials_all_origins=True,
#                 allow_all_methods=True)
#
#     return [
#         cors.middleware,
#         NonBlockingAuthentication(),
#         LoggerMiddleware(logging.getLogger(__name__)),
#     ]


def create_app():
    # create the app

    api = Flask(__name__)

    CORS(api)

    api.config.from_object('shms.settings')

    return api


def get_app():
    return create_app()
