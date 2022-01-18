from flask import Flask, jsonify

users = [
    {"ID": 1, "FirstName": "Valeria", "LastName": "Lammerding",
     "Email": "vlammerding0@flickr.com", "JobTitle": "Geologist III",
     "Username": "vlammerding0", "Active": False},
    {"ID": 2, "FirstName": "Bond", "LastName": "Tomczynski",
     "Email": "btomczynski1@ehow.com", "JobTitle": "Environmental Specialist",
     "Username": "btomczynski1", "Active": True},
    {"ID": 3, "FirstName": "Nowell", "LastName": "Triplet",
     "Email": "ntriplet2@sciencedirect.com", "JobTitle": "Business Analyst",
     "Username": "ntriplet2", "Active": False},
    {"ID": 4, "FirstName": "Patience", "LastName": "Boulds",
     "Email": "pboulds3@reverbnation.com", "JobTitle": "Assistant Manager",
     "Username": "pboulds3", "Active": True},
    {"ID": 5, "FirstName": "Darelle", "LastName": "Lemonby",
     "Email": "dlemonby4@prweb.com", "JobTitle": "Staff Accountant I",
     "Username": "dlemonby4", "Active": True}
]

STATIC_DIR = './dist/dev'

app = Flask(__name__, static_folder=STATIC_DIR, static_url_path='/')

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/api/user/<userid>')
def get_user(userid):
    person = next((user for user in users if str(user['ID']) == userid), {})
    return jsonify(person)

@app.route('/api/users')
def get_userlist():
    user_list = []
    for user in users:
        user_name = ', '.join([user['LastName'], user['FirstName']])
        user_list.append([user['ID'], user_name])
    return jsonify(user_list)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)

