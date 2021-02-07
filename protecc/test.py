from vortex import Vortex
from flask import Flask

app = Flask(__name__)
vtx = Vortex()

@app.route('/')
@vtx.register_endpoint
def does_something():
    print(vtx.endpoints)
    return 'some text'

app.run()