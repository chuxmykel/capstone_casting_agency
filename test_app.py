import os
import unittest
import json

from datetime import datetime
from models import setup_db, Movie, Actor
from app import create_app

casting_assistant = ('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIm'
                     'tpZCI6Ik5qQkRNME0yTlVKRU1qWkJRV'
                     'UpEUmpNeFFqSkZSVVJETnpWR0'
                     '5UWkROelZDTXpZM09EazBPQSJ9.eyJp'
                     'c3MiOiJodHRwczovL2F1dGhlbn'
                     'RpcXVlLmF1dGgwLmNvbS8iLCJzdWIiO'
                     'iJnb29nbGUtb2F1dGgyfDEwODQ5M'
                     'zU0MTEwNDgwODk1NzQ5OCIsImF1ZCI6'
                     'WyJodHRwOi8vbG9jYWxob3N0OjUwM'
                     'DAvIiwiaHR0cHM6Ly9hdXRoZW50aXF1'
                     'ZS5hdXRoMC5jb20vdXNlcmluZm8iX'
                     'SwiaWF0IjoxNTc3Mzg1ODI5LCJleHAi'
                     'OjE1Nzc0NzIyMjksImF6cCI6IlN5WE'
                     '41VUZsOWNNOXVvNG96WG40QjdkeFdl'
                     'TWNBanBlIiwic2NvcGUiOiJvcGVuaWQg'
                     'cHJvZmlsZSBlbWFpbCIsInBlcm1pc3N'
                     'pb25zIjpbImdldDphY3RvcnMiLCJnZXQ'
                     '6bW92aWVzIl19.06so2vF8usaYQvCck'
                     'rLeVSxw8VTCwQXfIfVdzc9Jmdn5qTU6Bq'
                     'hDd5B2zqZgvEBoMT_yOlTrDKm2uav2t'
                     '7VEivLbzFChg6TDyVoa6grAadPDW_HfCs'
                     'QXrF-BlECWCxGRI1sVEFFCvvIfinRMa'
                     'YZCw6P0fukxlqTPUoOop6_oAU_jcrDAmjV'
                     'pPTGuJoBnKV8kl3xHsFB1-DA8O3ZW6Z'
                     'tu8VzfH0L54zQHP98t5iiOEYYQtj1zf_Kv'
                     'u9w9OyQrq-AoG4kdAaqoCkNZ2JYmDLp'
                     'SaIaZfaR40QHCjKGHRlo_Gbqp0O'
                     '8CddjsgNL21qlgzNMgqKncx8mFDm_Go'
                     'YZKxq-OtQ'
                     )
casting_director = ('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1N'
                    'iIsImtpZCI6Ik5qQkR'
                    'NME0yTlVKRU1qWkJRVUpEUmpNeFFq'
                    'SkZSVVJETnpWR05UWkROelZDTXpZM09EazBPQS'
                    'J9.eyJpc3MiOiJodHRwczovL2F1dG'
                    'hlbnRpcXVlLmF1dGgwLmNvbS8iLCJzdWIiOiJnb'
                    '29nbGUtb2F1dGgyfDEwNjQyMzg1NT'
                    'Y3MjE0NjQ1MjM3NiIsImF1ZCI6WyJodHRwOi8vb'
                    'G9jYWxob3N0OjUwMDAvIiwiaHR0cH'
                    'M6Ly9hdXRoZW50aXF1ZS5hdXRoMC5jb20vdXNlcm'
                    'luZm8iXSwiaWF0IjoxNTc3Mzg1NzU'
                    '0LCJleHAiOjE1Nzc0NzIxNTQsImF6cCI6IlN5WE41'
                    'VUZsOWNNOXVvNG96WG40QjdkeFdlT'
                    'WNBanBlIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSB'
                    'lbWFpbCIsInBlcm1pc3Npb25zIjpb'
                    'ImNyZWF0ZTphY3RvcnMiLCJkZWxldGU6YWN0b3JzIi'
                    'wiZ2V0OmFjdG9ycyIsImdldDptb3Z'
                    'pZXMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdm'
                    'llcyJdfQ.XTSaMonmIuNkKiAzsuIF'
                    'E_PkdH9GcoYmWuf5Zg9zjc8fVFpgzb-WW8C5QdGKXZKq'
                    '-k1rrOurGaybQDSFmrAfQIl2oEg_8'
                    'msSw--LrE0CZnw38LkqahFGFreOSSmk5wjyaJczRqTvz'
                    '3fBdIDKoIpIqgumizHBwNONn-kj-d'
                    'qRC0yRkAh0IjGSI-vurT6Q0dtwnmp6wd23SDwjkmMHB0'
                    'ozLU_BD_ydCoxwZphsUeqSpRdpUmw'
                    'HoCM5nATrRp2x6f0k6mBle1Aw7bnc8eT92dJC6LJBn'
                    '8tLVXbe8JtUO9kK71uApuENjyWL61'
                    'DdO4aNI9FIJ4GV7CAFC5zwWtzpF1zr7w'
                    )
executive_producer = ('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIs'
                      'ImtpZCI6Ik5qQkRNME0yTlVKRU1qWkJRVUpEUmpNeFFqSkZS'
                      'VVJETnpWR05UWkROelZDTXpZM09EazBPQSJ'
                      '9.eyJpc3MiOiJodHRwczovL2F1dGhlbnRp'
                      'cXVlLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29'
                      'nbGUtb2F1dGgyfDExODIwOTI1OTU4OTM4N'
                      'jIyNjkwMyIsImF1ZCI6WyJodHRwOi8vbG9jY'
                      'Wxob3N0OjUwMDAvIiwiaHR0cHM6Ly9hdXR'
                      'oZW50aXF1ZS5hdXRoMC5jb20vdXNlcmluZm8i'
                      'XSwiaWF0IjoxNTc3Mzg1NjY1LCJleHAiOj'
                      'E1Nzc0NzIwNjUsImF6cCI6IlN5WE41VUZsOWN'
                      'NOXVvNG96WG40QjdkeFdlTWNBanBlIiwic'
                      '2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCI'
                      'sInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY'
                      '3RvcnMiLCJjcmVhdGU6bW92aWVzIiwiZGVsZXR'
                      'lOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiL'
                      'CJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInVw'
                      'ZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aW'
                      'VzIl19.v4SNrguiwD0ISi2Ga3M0fVY1q0nRHwMrx'
                      '8hdDYc0ChkZ9dzso0BMgJe4ERo3Ijq6lHr'
                      'slCRmRvfVC57cRIICePVHg1VJdZ2Ho2cmJ9A0xMeC'
                      'TL1mgKKiz0ERsNIOIvFHc0DrI_ePilC2pm'
                      '7hdbKsY5mj66G0whK79XEFfQQMc2mhtzKQ3HjxE4d'
                      'DPVzFNoWizqXMHIG9jF9pZDhigvf782ure'
                      '7I4vTrCpsfACL1ksw_nT55Ee_pazd72VJbik83voy'
                      'txW92_4YPh4dU0NU7nRHYMYKk3VLj8M1me'
                      '5YaTZmidRwgbL2YSneLaheX5B6iGgXNE0lCnyh2rh'
                      '9S40mC_eQ'
                      )


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
