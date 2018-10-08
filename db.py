from app import *

if 'HEROKU' in os.environ:
    pg_db = PostgresqlDatabase(os.environ['PG_DBNAME'], user=os.environ['PG_DBUSER'], password=os.environ['PG_DBPW'],
                               host=os.environ['PG_DBHOST'], port=5432)
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
