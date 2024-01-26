from django.utils.module_loading import autodiscover_modules

from .documents import Document  # noqa


def autodiscover():
    autodiscover_modules("documents")
