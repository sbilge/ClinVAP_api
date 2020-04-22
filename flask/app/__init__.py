from flask import Flask

app = Flask(__name__)

# before running dont forget export FLASK_ENV=development or others
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")


from app import api_calls
