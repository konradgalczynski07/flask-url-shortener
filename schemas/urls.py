from ma import ma
from models.urls import UrlModel


class UrlSchema(ma.ModelSchema):
    class Meta:
        model = UrlModel
        load_only = ("actual_url",)
        dump_only = ("id", "shortened_url",)
