from flask import Flask
# creating an instance

app = Flask(__name__)
# routing about me.
@app.route('/')
def home():
    return '<h2> Welcome to my Aweasome home page <h2>'

@app.route('/about.html')
def about():
    return '<h2> I Love football.<h2>'


@app.route('/contact,submission.html')
def submission():
    return '<h2> You can contact me on 0763461020.OR you can submite ur resume,thank you.<h2>'

@app.route('/user/<username>')
def username(Esther):
    return f'user, {Esther}! This is my user name.'

if __name__ == '__main__':
    app.run(debug=True)