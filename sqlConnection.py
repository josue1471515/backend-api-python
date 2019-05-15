from flask_api import FlaskAPI, status, exceptions
from flask_pymongo import PyMongo
from bson import json_util

app = FlaskAPI(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/bear"
mongo = PyMongo(app)


@app.route("/")
def getUsersModel():
    online_users = mongo.db.users.find({"userState":True})
    return json_util.dumps(online_users,default=json_util.default),status.HTTP_200_OK

