from flask.sessions import SecureCookieSessionInterface
from flask.helpers import total_seconds
from itsdangerous import BadSignature
import logging

old_open_session = SecureCookieSessionInterface.open_session
logger = logging.getLogger(__name__)


def customized_open_session(self, app, request):
    s = self.get_signing_serializer(app)
    if s is None:
        return None

    val = request.args.get('_session', None)
    if not val:
        return old_open_session(self, app, request)

    max_age = total_seconds(app.permanent_session_lifetime)
    try:
        data = s.loads(val, max_age=max_age)
        return self.session_class(data)
    except BadSignature:
        return self.session_class()


SecureCookieSessionInterface.open_session = customized_open_session
