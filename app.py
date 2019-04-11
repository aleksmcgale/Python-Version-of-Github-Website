from flask import Flask, render_template, request
from flask_mail import Message, Mail
import githubwebscrape


app = Flask(__name__)
mail = Mail(app)


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        url = 'https://github.com/aleksmcgale?tab=repositories'
        projects = githubwebscrape.create_project(url)


        return render_template('index.html', result=projects)



if __name__ == '__main__':
    app.run()
