# CAPSTONE CASTING AGENCY

> An API for a movie/actor database management system. 

Banka is a light-weight core banking application that powers banking operations like account
creation, customer deposit and withdrawals. This app is meant to support a single bank, where
users can signup and create bank accounts online, but must visit the branch to withdraw or
deposit money..

The capstone casting agency API is my final project for the Udacity Fullstack Nanodegree program.
The Casting Agency API models a company that is responsible for creating movies and managing and assigning actors to those movies.

* [Technologies](#technologies)
* [API Endpoints](#api-endpoints)
* [Getting Started](#getting-started)
  * [Installation](#installing)
  * [Licensing](#licensing)


### API url
The API endpoints can be accessed using the base URL [https://capstone-casting-agency.herokuapp.com/](https://capstone-casting-agency.herokuapp.com/)

## Technologies
---
- [Python](https://www.python.org/) - Python is a programming language that lets you work quickly
and integrate systems more effectively.
- [Flask](https://palletsprojects.com/p/flask/) - Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

### Supporting Packages
#### Linter
- [Pycodestyle](https://pypi.org/project/pycodestyle/) - pycodestyle is a tool to check your Python code against some of the style conventions in PEP 8.

#### Test Tools
- [Unittest](https://docs.python.org/3/library/unittest.html) - Python framework for unit testing


## API Endpoints   
#### Documentation
```

Endpoints
# Movies
GET '/movies'
GET '/movies/<movie_id>'
POST '/movies'
PATCH '/movies/<movie_id>'
DELETE '/movies/<movie_id>'

# Actors
GET '/actors'
GET '/actors/<actor_id>'
POST '/actors'
PATCH '/actors/<actor_id>'
DELETE '/actors/<actor_id>'

GET '/movies'
- Fetches all movies on the platform
- Request Arguments: None
- Required permission (get:movies)
- Response
{
  "movies": [
    {
      "id": 3,
      "release_date": "Thu, 23 Jun 2005 00:00:00 GMT",
      "title": "Mortal Kombat"
    },
    {
      "id": 1,
      "release_date": "Thu, 28 Jun 2000 00:00:00 GMT",
      "title": "Jungle Book"
    }
  ],
  "success": true
}

GET '/movies/<movie_id>'
- Fetches a specific movie
- Request Arguments: movie_id (The ID of the movie to fetch)
- Required permission (get:movies)
- Response
{
  "movie": {
    "id": 1,
    "release_date": "Thu, 23 Jun 2005 00:00:00 GMT",
    "title": "Jungle Book"
  },
  "success": true
}

POST '/movies'
- Creates a new movie with the provided parameters
- Request Arguments: None
- Required permission (create:movies)
- Request Body: {
	"title": "Mufasa",
	"release_date": "2/26/1996"
}

- Response
{
  "movie": {
    "id": 4,
    "release_date": "Mon, 26 Feb 1996 00:00:00 GMT",
    "title": "Mufasa"
  },
  "success": true
}


PATCH '/movies/<movie_id>'
- Updates a specific movie with the provided parameters
- Request Arguments: movie_id (The ID of the movie to update)
- Required permission (update:movies)
- Request Body: {
	"release_date": "2/26/2004"
}

- Response
{
  "message": "Movie with id: 4 updated",
  "movie": {
    "id": 4,
    "release_date": "Thu, 26 Feb 2004 00:00:00 GMT",
    "title": "Mufasa"
  },
  "success": true
}

DELETE '/movies/<movie_id>'
- Deletes a specific movie
- Request Arguments: movie_id (The ID of the movie to delete)
- Required permission (delete:movies)
- Response
{
  "message": "Movie with id: 4 deleted",
  "success": true
}

GET '/actors'
- Fetches all actors on the platform
- Request Arguments: None
- Required permission (get:actors)
- Response
{
  "actors": [
    {
      "age": 25,
      "gender": "male",
      "id": 3,
      "name": "James Ibori"
    },
    {
      "age": 20,
      "gender": "female",
      "id": 1,
      "name": "Jennifer Aniston"
    }
  ],
  "success": true
}

GET '/actors/<actor_id>'
- Fetches a specific actor
- Request Arguments: actor_id (The ID of the actor to fetch)
- Required permission (get:actors)
- Response
{
  "actor": {
    "age": 25,
    "gender": "male",
    "id": 3,
    "name": "James Ibori"
  },
  "success": true
}

POST '/movies'
- Creates a new actor with the provided parameters
- Request Arguments: None
- Required permission (create:actors)
- Request Body: {
	"name": "Bolaji Oluyede",
	"age": 20,
	"gender": "female"
}

- Response
{
  "actor": {
    "age": 20,
    "gender": "female",
    "id": 4,
    "name": "Bolaji Oluyede"
  },
  "success": true
}


PATCH '/actors/<actor_id>'
- Updates a specific actor with the provided parameters
- Request Arguments: actor_id (The ID of the actor to update)
- Required permission (update:actors)
- Request Body: {
	"name": "Bolaji Oluyede",
	"age": 20,
}

- Response
{
  "actor": {
    "age": 28,
    "gender": "female",
    "id": 4,
    "name": "Bolaji Oluyede"
  },
  "message": "Actor with id: 4 updated",
  "success": true
}

DELETE '/actors/<actor_id>'
- Deletes a specific actor
- Request Arguments: actor_id (The ID of the actor to delete)
- Required permission (delete:actors)
- Response
{
  "message": "Actor with id: 4 deleted",
  "success": true
}

Errors 
For errors, the server returns a json object with a description of the type of error. Find the description below:

400 (Bad Request)
  {
    "success": False, 
    "error": 400,
    "message": "bad request"
  }

401 (Resource Not Found)
  {
    "success": False, 
    "error": 401,
    "message": "auth error"
  }

403 (Resource Not Found)
  {
    "success": False, 
    "error": 403,
    "message": "forbidden"
  }

404 (Resource Not Found)
  {
    "success": False, 
    "error": 404,
    "message": "resource not found"
  }

405 (Method not allowed)
  {
    "success": False, 
    "error": 405,
    "message": "Method not allowed"
  }

422 (Unprocessable entity)
  {
    "success": False, 
    "error": 422,
    "message": "unprocessable
  }

500 (Internal server error)
  {
    "success": False, 
    "error": 500,
    "message": "Internal server error
  }
```
## Getting Started
---
### Installing

To run this application locally, you need to have Python3, and git(to clone the repo) installed. Then follow the instructions to get
it up and running

- clone the repo using 
```shell
~> git clone https://github.com/chuxmykel/capstone_casting_agency.git
```

- Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

It is recommended to work within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

- create a .env file from the .env.sample file and fill in the necessary environment variables
- run 
```bash
source setup.sh
```
to setup the environment for running the app
- Then start the server by running
```bash
flask run
```
and then access the endpoints on `localhost:5000`

Now the server will go live and listen for requests

#### Authentication

Authentication is implemented in the form of RBAC(Role Based Access Control) and different endpoints require different claims as specified in the documentation section.
For convenience, JWTs are provided for the reviewer of this project to use for testing. NOTE: These tokens will expire after 24 Hours.

`casting_assistant` = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5qQkRNME0yTlVKRU1qWkJRVUpEUmpNeFFqSkZSVVJETnpWR05UWkROelZDTXpZM09EazBPQSJ9.eyJpc3MiOiJodHRwczovL2F1dGhlbnRpcXVlLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwODQ5MzU0MTEwNDgwODk1NzQ5OCIsImF1ZCI6WyJodHRwOi8vbG9jYWxob3N0OjUwMDAvIiwiaHR0cHM6Ly9hdXRoZW50aXF1ZS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTc3MzE2ODYzLCJleHAiOjE1Nzc0MDMyNjMsImF6cCI6IlN5WE41VUZsOWNNOXVvNG96WG40QjdkeFdlTWNBanBlIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.YvK-6CdHabjYaTd-mSvo0N2woW2ZoKL1bSHifDvTcZQc3M4LxVk-pdMLo0V2zWrCUZqFMcnYBoqSVJkXv3-gH3WYY21A5ERajqOxB1ejotamfY6LM9lBFoK0q661huNWHZCmt8NknrQ3LUo3mvpts4FCIZe9nqDTzjvpOaayz4Z4PE53m74unhDXyrYqmH_tjlQu1tJCmKzN8W6vXS8d2Lv7Q4S0wC5pUTeuD6W-i6OH-bJGIQbwzZ62QW9UMI-GDN8wYvqKex-9oi1NIXpYh33jzXcuqlGyFKU14SZH-loHLE2ZTqUv3DAwMKXwk8FU9Ui2cb261eg3PVutcGl4oQ'

`casting_director` = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5qQkRNME0yTlVKRU1qWkJRVUpEUmpNeFFqSkZSVVJETnpWR05UWkROelZDTXpZM09EazBPQSJ9.eyJpc3MiOiJodHRwczovL2F1dGhlbnRpcXVlLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNjQyMzg1NTY3MjE0NjQ1MjM3NiIsImF1ZCI6WyJodHRwOi8vbG9jYWxob3N0OjUwMDAvIiwiaHR0cHM6Ly9hdXRoZW50aXF1ZS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTc3MzE2NTQyLCJleHAiOjE1Nzc0MDI5NDIsImF6cCI6IlN5WE41VUZsOWNNOXVvNG96WG40QjdkeFdlTWNBanBlIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyJdfQ.XZ9SX3Ose7FpVBQQV7JY05jwMJdAiMJRXclCAnbJ4GYc70mAuYD-03JOY4kUIYNoczMWhNs2cNQRAwlvNLHKv_kdhp65y-OY__ffFP7WQDEzzehGJ8DyHHftLuEVbXNV73gRTf1PUc7i6TsUIhG-YWk-QlxtMWu8nBAa0Br3jdkRVJNcJQMhMAtoi5NbD4yxU-U9Jk2EQV4W3YYO--6KhAKlrIndkzufv_E1-znElWLkJ1w5W99R6Cym44UP4UBZHDahZS7GhsZDZJQiN6vOcpiX4sEAayYlg7a0jX_pJbZ66WshJk1JVJxl5ysVtD0Y3sA6qcdGVo1hQ0MGQBI2wA'

`executive_producer` = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5qQkRNME0yTlVKRU1qWkJRVUpEUmpNeFFqSkZSVVJETnpWR05UWkROelZDTXpZM09EazBPQSJ9.eyJpc3MiOiJodHRwczovL2F1dGhlbnRpcXVlLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExODIwOTI1OTU4OTM4NjIyNjkwMyIsImF1ZCI6WyJodHRwOi8vbG9jYWxob3N0OjUwMDAvIiwiaHR0cHM6Ly9hdXRoZW50aXF1ZS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTc3MzE0NDk5LCJleHAiOjE1Nzc0MDA4OTksImF6cCI6IlN5WE41VUZsOWNNOXVvNG96WG40QjdkeFdlTWNBanBlIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJjcmVhdGU6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.BBfxUDKcwDdD6pWhvPktf0fdfY-XdxWMQTJw6URFUQkv8LlobCZwOHWZ0fu25ViqmT_RF8Es-dthwTsmng6-9YtWXOMdp2feW_XsW_a_9imsaG5yhMj_MpFD8nRkXM8KJgLqWojlhsJ9AOnX5gzFTWbRRzfutPk7HkW2miPrk6iP-AHl6x4HGZ0_4H8rVZA_nie_PWbAudloGcsRsug8K5FHZcHfV_gWddGiZBf-atrcTCD7LhVqhUi5eEiH23IdGV_on7v08QSlN5PgLFl8OUCSgV2qDbdTgfPdk_Y1mGOHhLLLs1nz-UjLnWc7Hu3m5JKUbLMIcRRjZb3bI2iwIw'


## Licensing

Copyright &copy; 2019, Ngwobia, Chukwudi M.
The code in this project is licensed under [ISC LICENSE](https://github.com/chuxmykel/capstone_casting_agency/blob/develop/LICENSE)
