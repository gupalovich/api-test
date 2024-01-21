from ninja import Schema


class Error(Schema):
    message: str


class Error404(Error):
    message: str = "Not found"
