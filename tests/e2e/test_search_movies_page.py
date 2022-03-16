# TODO: Feature 3
from urllib import response
from flask.testing import FlaskClient
import pytest
from app import app

def test_search_page(test_app: FlaskClient):
    response = test_app.get('/movies/search')
    response_data = response.data
    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in response_data
