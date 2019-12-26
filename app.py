import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from models import setup_db, Movie, Actor, db
from auth import requires_auth, AuthError

environment = os.getenv('ENV')


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type,Authorization,true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS'
        )
        return response

    '''
        Actors
    '''
    @app.route('/')
    def home():
        return jsonify({
            'message': 'capstone casting agency API'
        })

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        actors = Actor.query.all()
        return jsonify({
            'success': True,
            'actors': [actor.format for actor in actors],
        }), 200

    @app.route('/actors/<int:id>', methods=['GET'])
    @requires_auth('get:actors')
    def get_actor_by_id(payload, id):
        actor = Actor.query.get(id)

        if actor is None:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'actor': actor.format
            })

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        actor = Actor.query.get(id)

        if actor is None:
            abort(404)
        try:
            actor.delete()
            return jsonify({
                'success': True,
                'message': f'Actor with id: {actor.id} deleted',
            })
        except Exception as e:
            if environment == 'development':
                print(e)
            db.session.rollback()
            abort(500)

    @app.route('/actors', methods=['POST'])
    @requires_auth('create:actors')
    def create_actor(payload):
        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
        gender = data.get('gender')

        if name is None or age is None or gender is None:
            abort(400)
        try:
            actor = Actor(name=name, age=age, gender=gender)
            actor.insert()
            return jsonify({
                'success': True,
                'actor': actor.format
            }), 201

        except Exception as e:
            if environment == 'development':
                print(e)
            abort(500)

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('update:actors')
    def edit_actor(payload, id):
        actor = Actor.query.get(id)

        if actor is None:
            abort(404)

        data = request.get_json()

        actor.name = data.get('name', actor.name)
        actor.age = data.get('age', actor.age)
        actor.gender = data.get('gender', actor.gender)

        try:
            actor.update()
            return jsonify({
                'success': True,
                'message': f'Actor with id: {id} updated',
                'actor': actor.format
            }), 200

        except Exception as e:
            if environment == 'development':
                print(e)
            db.session.rollback()
            abort(500)

    '''
        Movies
    '''
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        movies = Movie.query.all()
        return jsonify({
            'success': True,
            'movies': [movie.format for movie in movies],
        }), 200

    @app.route('/movies/<int:id>', methods=['GET'])
    @requires_auth('get:movies')
    def get_movie_by_id(payload, id):
        movie = Movie.query.get(id)

        if movie is None:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'movie': movie.format
            })

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        movie = Movie.query.get(id)

        if movie is None:
            abort(404)
        try:
            movie.delete()
            return jsonify({
                'success': True,
                'message': f'Movie with id: {movie.id} deleted',
            })
        except Exception as e:
            if environment == 'development':
                print(e)
            db.session.rollback()
            abort(500)

    @app.route('/movies', methods=['POST'])
    @requires_auth('create:movies')
    def create_movie(payload):
        data = request.get_json()
        title = data.get('title')
        release_date = data.get('release_date')

        if title is None or release_date is None:
            abort(400)
        try:
            movie = Movie(title=title, release_date=release_date)
            movie.insert()
            return jsonify({
                'success': True,
                'movie': movie.format
            }), 201

        except Exception as e:
            if environment == 'development':
                print(e)
            abort(500)

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('update:movies')
    def edit_movie(payload, id):
        movie = Movie.query.get(id)

        if movie is None:
            abort(404)

        data = request.get_json()

        movie.title = data.get('title', movie.title)
        movie.release_date = data.get('release_date', movie.release_date)

        try:
            movie.update()
            return jsonify({
                'success': True,
                'message': f'Movie with id: {id} updated',
                'movie': movie.format
            }), 200

        except Exception as e:
            if environment == 'development':
                print(e)
            db.session.rollback()
            abort(500)
    '''
        Error handlers
    '''
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(401)
    def unathorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "auth error",
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "forbidden",
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal server error"
        }), 500

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
