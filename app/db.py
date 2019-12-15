from databases import Database
import sqlalchemy

from configs import project

DATABASE_URL = f'{project.DB_DRIVER}://{project.DB_USER}:{project.DB_PASSWORD}' \
               f'@{project.DB_HOST}/{project.DB_NAME}'
database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)
