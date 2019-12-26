from flask_script import Manager
from sqlalchemy import Column, String, Integer
from flask_migrate import Migrate, MigrateCommand
from datetime import datetime

from app import create_app
from models import db, Movie, Actor

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def seed():
    Movie(title='Random movie 1', release_date=datetime(2005, 6, 23)).insert()
    Movie(title='Random movie 2', release_date=datetime(2000, 1, 1)).insert()
    Actor(name='Actor 1', age=20, gender='male').insert()
    Actor(name='Actor 2', age=30, gender='female').insert()


if __name__ == '__main__':
    manager.run()
