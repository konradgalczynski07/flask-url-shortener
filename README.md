# flask-url-shortener

A simple flask rest api that allows urls shortening
- `[POST] localhost:5000/  body: 'actual_url', returns: 'shortened_url'` 
- `[GET] localhost:5000/<string:shortened_url> redirects to actual url`

## Stack
- Python 3.7
- SQLAlchemy
- Flask 
- Marshmallow

## Instalation
```
git clone ...
pipenv install
flask run
```