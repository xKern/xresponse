from rest_framework.exceptions import (
    PermissionDenied as PermDenied
)


class PermissionDenied(PermDenied):
    error_code = 810
