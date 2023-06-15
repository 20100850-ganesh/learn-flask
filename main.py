from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '''
      <h1>Hello, Flask!</h1>
      <p>This is a Simple Flask Application built using Python</p>
  '''


if __name__ == "__main__":
    app.run(host='localhost', debug=True)
