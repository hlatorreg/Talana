import os

from talana_kombat import create_app

app = create_app(os.getenv("FLASK_ENV", "development"))
