import falcon


def require_auth(req, resp, resource, params):
    if not req.user:
        raise falcon.HTTPError(falcon.HTTP_403)


def require_token_auth(req, resp, resource, params):
    auth_type = getattr(req, 'auth_type', None)
    token = getattr(req, 'token', None)
    user = getattr(req, 'user', None)
    if auth_type != 'token' or not token or not user:
        raise falcon.HTTPError(falcon.HTTP_403)


def require_user(req, resp, resource, params):
    if not req.user:
        raise falcon.HTTPError(falcon.HTTP_403)
