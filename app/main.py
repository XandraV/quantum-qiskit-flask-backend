from flask import Flask
import qiskit
from qiskit import Aer
from result import get_result

app= Flask(__name__)
@app.route('/')
def index():
  q = [{"idx":0, "gates": [{"name":"CX", "param": 1}]}, {"idx":1, "gates": [{"name":"H", "param":""}]}]
  res = get_result(q)
  # return "<h1>Welcome to CodingX</h1>"
  return res