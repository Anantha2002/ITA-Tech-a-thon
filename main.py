from app import create_app, db
from flask_migrate import Migrate

app = create_app()

# Setup Flask-Migrate for handling database migrations
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
