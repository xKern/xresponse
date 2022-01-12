from django.http import (
    JsonResponse,
)


def server_error(request, template_name=None):
    return JsonResponse({
        'code': 999,
        'message': 'An unexpected error occured(server 500)',
        'data': None
        }, status=500)


def page_not_found(request, exception, template_name=None):
    try:
        path = exception.args[0].get('path', 'requested resource')
        message = f'{path} could not be found'
    except (AttributeError, IndexError):
        message = 'requested resource could not be found'
    return JsonResponse({
        'code': 104,
        'message': message,
        'data': None
    }, status=404)


def bad_request(request, exception, template_name=None):
    return JsonResponse({
        'code': 104,
        'message': 'Foobar',
        'data': None
    }, status=404)
