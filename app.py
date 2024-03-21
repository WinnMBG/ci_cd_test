from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
   ip = request.host.split(':')[0] 
   return f"<p><h2>Hello, World!</h2><h3>L'adresse IP est la suivante : {ip}</p>"

if __name__== "__main__":

   app.run('0.0.0.0',port=5000)
