import os
basedir = os.path.abspath(os.path.dirname(__file__))


CSRF_ENABLED = True
SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
DB_USER = os.environ.get('POSTGRES_USER') or 'admin'
DB_NAME = 'otus_db'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, '{}.db'.format(DB_NAME))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
