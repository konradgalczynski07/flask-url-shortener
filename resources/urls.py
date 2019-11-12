import validators
from flask import request, redirect
from flask_restful import Resource

from models.urls import UrlModel
from schemas.urls import UrlSchema

url_schema = UrlSchema()
BASE_URL = 'http://localhost:5000'
URL_NOT_EXISTS = "Given URL does not exist."
INVALID_URL = "Please provide valid url."


class RedirectUrlResource(Resource):
    @classmethod
    def get(cls, shortened_url: str):
        '''
        eg. http://localhost:5000/icvsuoea redirects to facebook.com
        :param shortened_url:
        :return redirection to actual site:
        '''
        url = UrlModel.find_by_shortened_url(shortened_url)
        print(url.actual_url)
        if not url.actual_url:
            return {"error": URL_NOT_EXISTS}, 404

        return redirect(url.actual_url, code=302)


class ShortenUrlResource(Resource):
    @classmethod
    def post(cls):
        '''
        :param: 'actual_url' in body
        :return: 'shortened_url'
        '''
        url_json = request.get_json()
        url = url_schema.load(url_json)
        if not validators.url(url.actual_url):
            return {"error": INVALID_URL}

        shortened_url = url.save_to_db()

        return {"shortened_url": f'{BASE_URL}/{shortened_url}'}, 201
