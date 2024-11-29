#Tests the route to ensure FilmFinder appears in HTML
'''
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Film Finder" in response.data  
'''

#Test Mood to Genre Mapping

from app import GENRE_MAP, MOOD_TO_GENRE

def test_genre_map():
    assert GENRE_MAP["action"] == 28
    assert GENRE_MAP["comedy"] == 35

def test_mood_to_genre():
    assert MOOD_TO_GENRE["happy"] == "comedy"
    assert MOOD_TO_GENRE["spooky"] == "horror"

