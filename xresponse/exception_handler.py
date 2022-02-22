from rest_framework.views import (
    set_rollback
)
from django.core.exceptions import PermissionDenied
from rest_framework import exceptions
from django.http import Http404
from . import XResponse


def xkern_exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.
    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.
    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        # if isinstance(exc.detail, (list, dict)):
        #     data = exc.detail
        # else:
        #     data = {'detail': exc.detail}
        message = exc.detail
        try:
            error_code = exc.detail.code
            """
            DRF Permissions default code set to a string.
            However we explicitly need an integer to be returned in the
            response.
            """
            if isinstance(error_code, str):
                error_code = 999
        except AttributeError:
            error_code = 999

        set_rollback()
        return XResponse(message=message, code=error_code)

    return None
