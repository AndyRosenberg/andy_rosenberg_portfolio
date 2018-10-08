from app import *
from urllib.parse import urlparse

if 'HEROKU' in os.environ:
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    pg_db = PostgresqlDatabase(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
else:
    pg_db = PostgresqlDatabase('portfolio_dev', user=os.environ['PG_USER'], password=os.environ['PG_PW'],
                               host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = pg_db

class Blog(BaseModel):
    title = TextField()
    body = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    image = TextField()
