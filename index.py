from flask_api import FlaskAPI, status, exceptions
from sqlConnection import getUsersModel


app = FlaskAPI(__name__)


@app.route('/users/', methods=['GET'])
def getUsers():
    return  getUsersModel()

@app.route('/users/update')
def updateUsers():
    return getUsersModel()

@app.route('/users/delete')
def deleteUsers():
    return getUsersModel()

@app.route('/users/create',methods=['POST'])
def createUsers():
    return getUsersModel()


if __name__ == '__main__':
      app.run(debug=True)