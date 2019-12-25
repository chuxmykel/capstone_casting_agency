export ENV='test'
python ./src/manage.py db downgrade
python ./src/manage.py db upgrade
python ./src/manage.py seed
python ./src/test_app.py
