from rest_framework.views import (
    exception_handler,
    set_rollback
)
from django.core.exceptions import PermissionDenied
from rest_framework import exceptions
from django.http import Http404
from . import XResponse
from .response import XError


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
        data = exc.detail

        set_rollback()
        return XResponse(data=data, code=exc.status_code)
        # return XResponse(data, status=exc.status_code, headers=headers)

    return None
