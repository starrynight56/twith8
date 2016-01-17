from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('twitter.html')

if __name__ == '__main__':
    app.run()

#find a way to present twitter .thml file in ay.py. and then
