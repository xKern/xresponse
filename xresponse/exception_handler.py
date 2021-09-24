from rest_framework.views import exception_handler
from .response import XError


def xkern_exception_handler(exc, context):
    response = exception_handler(exc, context)
    try:
        status_code = response.status_code
    except AttributeError:
        status_code = 999

    return XError(
        code=status_code,
        message=str(exc),
        data=[]
    )
