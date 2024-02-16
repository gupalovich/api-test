from django.core.exceptions import PermissionDenied
from django.core.exceptions import ValidationError as DjangoValidationError
from django.http import Http404
from rest_framework import exceptions
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.serializers import as_serializer_error
from rest_framework.views import exception_handler


def drf_default_with_modifications_exception_handler(exc, ctx):
    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(as_serializer_error(exc))

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()

    if isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    response = exception_handler(exc, ctx)

    # If unexpected error occurs (server error, etc.)
    if response is None:
        return response

    if isinstance(exc, DRFValidationError):
        if isinstance(exc.detail, dict):
            formatted_errors = flatten_nested_errors(exc.detail)
            response.data = {"validations": formatted_errors}
        else:
            response.data = {"validations": exc.detail}
    else:
        response.data = {"message": str(exc)}

    return response


def flatten_nested_errors(nested_errors):
    flat_errors = {}

    if isinstance(nested_errors, list):
        flat_errors = {"__all__": nested_errors}
    elif isinstance(nested_errors, dict):
        for field, errors in nested_errors.items():
            if isinstance(errors, list):
                flat_errors[field] = errors
            elif isinstance(errors, dict):
                nested_flat_errors = flatten_nested_errors(errors)
                for nested_field, error_list in nested_flat_errors.items():
                    flat_errors[f"{field}.{nested_field}"] = error_list

    return flat_errors
