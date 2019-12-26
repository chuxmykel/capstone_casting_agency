import os
import unittest
import json

from datetime import datetime
from models import setup_db, Movie, Actor
from app import create_app

casting_assistant = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5qQkRNME0yTlVKRU1qWkJRVUpEUmpNeFFqSkZSVVJETnpWR05UWkROelZDTXpZM09EazBPQSJ9.eyJpc3MiOiJodHRwczovL2F1dGhlbnRpcXVlLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwODQ5MzU0MTEwNDgwODk1NzQ5OCIsImF1ZCI6WyJodHRwOi8vbG9jYWxob3N0OjUwMDAvIiwiaHR0cHM6Ly9hdXRoZW50aXF1ZS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTc3MzE2ODYzLCJleHAiOjE1Nzc0MDMyNjMsImF6cCI6IlN5WE41VUZsOWNNOXVvNG96WG40QjdkeFdlTWNBanBlIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.YvK-6CdHabjYaTd-mSvo0N2woW2ZoKL1bSHifDvTcZQc3M4LxVk-pdMLo0V2zWrCUZqFMcnYBoqSVJkXv3-gH3WYY21A5ERajqOxB1ejotamfY6LM9lBFoK0q661huNWHZCmt8NknrQ3LUo3mvpts4FCIZe9nqDTzjvpOaayz4Z4PE53m74unhDXyrYqmH_tjlQu1tJCmKzN8W6vXS8d2Lv7Q4S0wC5pUTeuD6W-i6OH-bJGIQbwzZ62QW9UMI-GDN8wYvqKex-9oi1NIXpYh33jzXcuqlGyFKU14SZH-loHLE2ZTqUv3DAwMKXwk8FU9Ui2cb261eg3PVutcGl4oQ'
casting_director = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5qQkRNME0yTlVKRU1qWkJRVUpEUmpNeFFqSkZSVVJETnpWR05UWkROelZDTXpZM09EazBPQSJ9.eyJpc3MiOiJodHRwczovL2F1dGhlbnRpcXVlLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNjQyMzg1NTY3MjE0NjQ1MjM3NiIsImF1ZCI6WyJodHRwOi8vbG9jYWxob3N0OjUwMDAvIiwiaHR0cHM6Ly9hdXRoZW50aXF1ZS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTc3MzE2NTQyLCJleHAiOjE1Nzc0MDI5NDIsImF6cCI6IlN5WE41VUZsOWNNOXVvNG96WG40QjdkeFdlTWNBanBlIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyJdfQ.XZ9SX3Ose7FpVBQQV7JY05jwMJdAiMJRXclCAnbJ4GYc70mAuYD-03JOY4kUIYNoczMWhNs2cNQRAwlvNLHKv_kdhp65y-OY__ffFP7WQDEzzehGJ8DyHHftLuEVbXNV73gRTf1PUc7i6TsUIhG-YWk-QlxtMWu8nBAa0Br3jdkRVJNcJQMhMAtoi5NbD4yxU-U9Jk2EQV4W3YYO--6KhAKlrIndkzufv_E1-znElWLkJ1w5W99R6Cym44UP4UBZHDahZS7GhsZDZJQiN6vOcpiX4sEAayYlg7a0jX_pJbZ66WshJk1JVJxl5ysVtD0Y3sA6qcdGVo1hQ0MGQBI2wA'
executive_producer = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5qQkRNME0yTlVKRU1qWkJRVUpEUmpNeFFqSkZSVVJETnpWR05UWkROelZDTXpZM09EazBPQSJ9.eyJpc3MiOiJodHRwczovL2F1dGhlbnRpcXVlLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExODIwOTI1OTU4OTM4NjIyNjkwMyIsImF1ZCI6WyJodHRwOi8vbG9jYWxob3N0OjUwMDAvIiwiaHR0cHM6Ly9hdXRoZW50aXF1ZS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTc3MzE0NDk5LCJleHAiOjE1Nzc0MDA4OTksImF6cCI6IlN5WE41VUZsOWNNOXVvNG96WG40QjdkeFdlTWNBanBlIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJjcmVhdGU6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.BBfxUDKcwDdD6pWhvPktf0fdfY-XdxWMQTJw6URFUQkv8LlobCZwOHWZ0fu25ViqmT_RF8Es-dthwTsmng6-9YtWXOMdp2feW_XsW_a_9imsaG5yhMj_MpFD8nRkXM8KJgLqWojlhsJ9AOnX5gzFTWbRRzfutPk7HkW2miPrk6iP-AHl6x4HGZ0_4H8rVZA_nie_PWbAudloGcsRsug8K5FHZcHfV_gWddGiZBf-atrcTCD7LhVqhUi5eEiH23IdGV_on7v08QSlN5PgLFl8OUCSgV2qDbdTgfPdk_Y1mGOHhLLLs1nz-UjLnWc7Hu3m5JKUbLMIcRRjZb3bI2iwIw'


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
            headers={'Authorization': f'Bearer {executive_producer}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie']['title'], 'Mortal Kombat')

    # RBAC Casting assistant
    def test_403_for_create_movie_casting_assistant(self):
        response = self.client().post(
            '/movies',
            json=self.new_movie,
            headers={'Authorization': f'Bearer {casting_assistant}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'forbidden')

    # RBAC Casting director
    def test_403_for_create_movie_casting_director(self):
        response = self.client().post(
            '/movies',
            json=self.new_movie,
            headers={'Authorization': f'Bearer {casting_director}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'forbidden')

    def test_bad_request_for_create_movie(self):
        response = self.client().post(
            '/movies',
            json=self.incomplete_movie,
            headers={'Authorization': f'Bearer {executive_producer}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'bad request')

    def test_get_all_movies(self):
        response = self.client().get(
            '/movies',
            headers={'Authorization': f'Bearer {casting_assistant}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_401_for_get_all_movies(self):
        response = self.client().get(
            '/movies',
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'auth error')

    def test_get_movie_by_id(self):
        response = self.client().get(
            '/movies/1',
            headers={'Authorization': f'Bearer {casting_assistant}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])
        self.assertEqual(data['movie']['title'], 'Random movie 1')

    def test_404_for_get_movie_by_id(self):
        response = self.client().get(
            '/movies/100',
            headers={'Authorization': f'Bearer {casting_assistant}'}
        )
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
            headers={'Authorization': f'Bearer {casting_director}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], f'Movie with id: {id} updated')
        self.assertEqual(data['movie']['title'], 'Jungle Book')

    # RBAC Casting assistant
    def test_403_for_update_movie_casting_assistant(self):
        id = 1
        response = self.client().patch(
            f'/movies/{id}',
            json=self.incomplete_movie,
            headers={'Authorization': f'Bearer {casting_assistant}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'forbidden')

    def test_404_for_update_movie(self):
        response = self.client().patch(
            '/movies/100',
            json=self.incomplete_movie,
            headers={'Authorization': f'Bearer {casting_director}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_movie(self):
        id = 2
        response = self.client().delete(
            f'/movies/{id}',
            headers={'Authorization': f'Bearer {executive_producer}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], f'Movie with id: {id} deleted')

    # RBAC Casting director
    def test_403_for_delete_movie_casting_director(self):
        id = 2
        response = self.client().delete(
            f'/movies/{id}',
            headers={'Authorization': f'Bearer {casting_director}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'forbidden')

    def test_404_for_delete_movie(self):
        response = self.client().delete(
            '/movies/100',
            headers={'Authorization': f'Bearer {executive_producer}'}
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
            headers={'Authorization': f'Bearer {casting_director}'}
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
            headers={'Authorization': f'Bearer {casting_director}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'bad request')

    def test_get_all_actors(self):
        response = self.client().get(
            '/actors',
            headers={'Authorization': f'Bearer {casting_assistant}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_get_actor_by_id(self):
        response = self.client().get(
            '/actors/1',
            headers={'Authorization': f'Bearer {casting_assistant}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])
        self.assertEqual(data['actor']['name'], 'Actor 1')
        self.assertEqual(data['actor']['age'], 20)
        self.assertEqual(data['actor']['gender'], 'male')

    def test_404_for_get_actor_by_id(self):
        response = self.client().get(
            '/actors/100',
            headers={'Authorization': f'Bearer {casting_assistant}'}
        )
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
            headers={'Authorization': f'Bearer {casting_director}'}
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
            headers={'Authorization': f'Bearer {casting_director}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_actor(self):
        id = 2
        response = self.client().delete(
            f'/actors/{id}',
            headers={'Authorization': f'Bearer {casting_director}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], f'Actor with id: {id} deleted')

    def test_404_for_delete_actor(self):
        response = self.client().delete(
            '/actors/100',
            headers={'Authorization': f'Bearer {casting_director}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
