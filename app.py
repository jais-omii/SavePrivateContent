form flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world( ):

  return 'OGMaster'

if __name___ == "__main__":

  app.run()
