import os
import unittest
import json

from datetime import datetime
from models import setup_db, Movie, Actor
from app import create_app


class CapstoneTestCase(unittest.TestCase):
    '''
        This class represents the test cases for the capstone project
    '''

    def setUp(self):
        '''Define test variables and initialize app.'''
        self.app = create_app()
        self.client = self.app.test_client
        self.new_movie = {
            'title': 'Mortal Kombat',
            'release_date': datetime(2005, 6, 23),
        }
        self.incomplete_movie = {
            'title': 'Jungle Book',
        }
        self.new_actor = {
            'name': 'James Ibori',
            'age': 25,
            'gender': 'male'
        }
        self.incomplete_actor = {
            'name': 'Jennifer Aniston',
            'gender': 'female'
        }
        setup_db(self.app)

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
        Movie tests
    """
    def test_create_movie(self):
        response = self.client().post(
            '/movies',
            json=self.new_movie,
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie']['title'], 'Mortal Kombat')

    def test_bad_request_for_create_movie(self):
        response = self.client().post(
            '/movies',
            json=self.incomplete_movie,
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'bad request')

    def test_get_all_movies(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_get_movie_by_id(self):
        response = self.client().get('/movies/1')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])
        self.assertEqual(data['movie']['title'], 'Random movie 1')

    def test_404_for_get_movie_by_id(self):
        response = self.client().get('/movies/100')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'resource not found')

    def test_update_movie(self):
        id = 1
        response = self.client().patch(
            f'/movies/{id}',
            json=self.incomplete_movie,
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], f'Movie with id: {id} updated')
        self.assertEqual(data['movie']['title'], 'Jungle Book')

    def test_404_for_update_movie(self):
        response = self.client().patch(
            '/movies/100',
            json=self.incomplete_movie,
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_movie(self):
        id = 2
        response = self.client().delete(
            f'/movies/{id}',
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], f'Movie with id: {id} deleted')

    def test_404_for_delete_movie(self):
        response = self.client().delete(
            '/movies/100',
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    """
        Actor Tests
    """
    def test_create_actor(self):
        response = self.client().post(
            '/actors',
            json=self.new_actor,
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor']['name'], 'James Ibori')
        self.assertEqual(data['actor']['age'], 25)
        self.assertEqual(data['actor']['gender'], 'male')

    def test_bad_request_for_create_actor(self):
        response = self.client().post(
            '/actors',
            json=self.incomplete_actor,
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'bad request')

    def test_get_all_actors(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_get_actor_by_id(self):
        response = self.client().get('/actors/1')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])
        self.assertEqual(data['actor']['name'], 'Actor 1')
        self.assertEqual(data['actor']['age'], 20)
        self.assertEqual(data['actor']['gender'], 'male')

    def test_404_for_get_actor_by_id(self):
        response = self.client().get('/actors/100')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'resource not found')

    def test_update_actor(self):
        id = 1
        response = self.client().patch(
            f'/actors/{id}',
            json=self.incomplete_actor,
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], f'Actor with id: {id} updated')
        self.assertEqual(data['actor']['name'], 'Jennifer Aniston')
        self.assertEqual(data['actor']['gender'], 'female')

    def test_404_for_update_actor(self):
        response = self.client().patch(
            '/actors/100',
            json=self.incomplete_actor,
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_actor(self):
        id = 2
        response = self.client().delete(
            f'/actors/{id}',
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], f'Actor with id: {id} deleted')

    def test_404_for_delete_actor(self):
        response = self.client().delete(
            '/actors/100',
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
