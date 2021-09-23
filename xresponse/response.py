from rest_framework.response import Response
from .codes import (
    MISSING_HEADERS,
    INVALID_PAYLOAD
)


class XResponse(Response):
    def __init__(self, data=[], code=0, message='success ok'):
        response_data = {
            'code': code,
            'message': message,
            'data': data
        }
        return super().__init__(
            status=200,
            data=response_data
        )


class XError(Response):
    def __init__(self,
                 data=None,
                 code=999,
                 message='unexpected error occured'):
        response_data = {
            'code': code,
            'message': message,
            'data': data
        }
        return super().__init__(
            status=599,
            data=response_data
        )


class InvalidPayloadError(XError):
    def __init__(self, data=[]):
        super().__init__(
            code=INVALID_PAYLOAD,
            message='Invalid payload',
            data=data,
        )


class MissingHeadersError(XError):
    def __init__(self, headers=[]):
        super().__init__(
            code=MISSING_HEADERS,
            message='Invalid or missing headers',
            data=headers,
        )
