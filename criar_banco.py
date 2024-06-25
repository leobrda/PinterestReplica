from sitefakepinterest import database, app
from sitefakepinterest.models import Usuario, Foto

with app.app_context():
    database.create_all()
