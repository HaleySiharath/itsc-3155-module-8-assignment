# TODO: Feature 3
#from src.repositories.movie_repository import MovieRepository
from src.repositories.movie_repository import movie_repository_singleton
from src.models.movie import Movie

def test_search_by_title():
    create = movie_repository_singleton.create_movie('Star War', 'Georg Lucas', 5)
    search = movie_repository_singleton.get_movie_by_title('Star War')

    assert create.title == search.title
    assert create.director == search.director
    assert create.rating == search.rating


