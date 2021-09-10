from rest_framework.views import exception_handler
from .response import XResponse


def xkern_exception_handler(exc, context):
    response = exception_handler(exc, context)

    status_code = response.status_code or 900
    return XResponse(
        code=status_code,
        message=str(exc),
        data=[]
    )
