from flask import Flask

app = Flask(__name__)

@app.route("/")
def root_test():
    msg = '<html><h1>TEST A</h1></html>'
    return msg


if __name__=='__main__':
   app.run(ip='0.0.0.0', debug=True)
