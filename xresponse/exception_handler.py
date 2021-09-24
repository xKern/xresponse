from rest_framework.views import exception_handler
from .response import XError


def xkern_exception_handler(exc, context):
    response = exception_handler(exc, context)

    status_code = response.status_code or 900
    return XError(
        code=status_code,
        message=str(exc),
        data=[]
    )
