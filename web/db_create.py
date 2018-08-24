from project import db
from project.models import Paper

# drop all of the existing database tables
db.drop_all()

# create the database and the database table
db.create_all()

# insert recipe data
#paper1 = Paper('db_create', 'init db')
#db.session.add(paper1)

# commit the changes
db.session.commit()
