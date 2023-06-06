from app_config import app
from models import db
if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
