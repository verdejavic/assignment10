from flask import Flask, render_template
from players import TOP_PLAYERS

app = Flask(__name__)

#get all the ids from the dataset and put into list
def get_ids(source):
    ids = []
    for row in source:
        id = row['id']
        ids.append(id)
    return sorted(ids)

#find the row that matched the name in the URL, retrieve age and birthplace
def get_player(source, id):
    for row in source:
        if id == str( row['id']):
            name = row['name']
            age = row['age']
            birthplace = row['birthplace']
            id = str(id)
            return name, age, birthplace
    return "Unknown", "Unknown", "Unknown"

#Flask routes
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', players=TOP_PLAYERS)


#code
@app.route('/player/<id>')
def player(id):
    name, age, birthplace = get_player(TOP_PLAYERS, id)
    return render_template('player.html', id=id, name=name, age=age, birthplace=birthplace)


#to work offline
app.config['BOOTSTRAP_SERVE_LOCAL'] = True


if __name__ == '__main__':
    app.run(debug=True)
