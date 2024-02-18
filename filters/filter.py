from django.http import HttpRequest

from .mappings import DEFAULT_CARS_FILTER_CONFIG


class CarFilter:
    config = DEFAULT_CARS_FILTER_CONFIG

    def __init__(self, request: HttpRequest):
        self.request = request

    def _build_qs_response(self) -> dict:
        return {
            "data": {
                "count": None,
                "count_visible": None,
                "group_name": "",
                "id": None,
                "page": None,
                "url": "",
                "values": [],
            },
            "type": "cars",
        }

    def _build_filters_response(self) -> list:
        return []

    def _build_head_filters_response(self) -> list:
        return []

    def _build_sorting_response(self) -> list:
        return []

    def _build_info_response(self) -> dict:
        return {
            "breadcrumbs": [],
            "description": "",
            "h1": "",
            "isNoindex": "",
            "keywords": [],
            "title": "",
            "url": "",
            "cars_count": "",
            "page_next": "",
            "watchedItems": "",
        }

    def get_response(self) -> dict:
        qs_response = self._build_qs_response()
        filters_response = self._build_filters_response()
        head_filters_response = self._build_head_filters_response()
        info_response = self._build_info_response()
        sorting_response = self._build_sorting_response()

        return {
            "cars": qs_response,
            "filters": filters_response,
            "head_filters": head_filters_response,
            "info": info_response,
            "sorting": sorting_response,
        }
