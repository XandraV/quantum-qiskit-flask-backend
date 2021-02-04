# Quantum Circuit Simulator - Backend code

![python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![qiskit](https://img.shields.io/badge/-Qiskit-3776AB?style=flat-square&logo=python&logoColor=white)
![flask](https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=Flask&logoColor=white)

This is the backend code for a web application that allows the user to graphically build quantum circuits and view the results on a dashboard. This project combines **React(TypeScript)** frontend with a **Flask(Python)** backend using **Qiskit** library to perform quantum operations. This project is automated with continuous deployment on [Heroku](https://www.heroku.com/).

You can visit the deployed, fully functional app [here](https://master.d3vhvy7iyx12n.amplifyapp.com/).

![quantum](https://general-gif-bucket.s3.eu-west-2.amazonaws.com/quantum.gif)

Frontend source code can be found [here](https://github.com/XandraV/quantum-circuit-simulator) :octocat: and is automated with continuous deployment on [AWS Amplify](https://aws.amazon.com/amplify/).

## Installation

You will need to have the latest version of [Python 3](https://www.python.org/downloads/), [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/) installed on your machine. To install Qiskit follow the guide [here](https://qiskit.org/documentation/install.html).

Clone the master branch and then run the following scripts in the project directory to install the relevant dependencies:
- `pip install Flask` - to install Flask

- `pip install flask-cors` - to install a Flask extension for handling Cross Origin Resource Sharing

- `python ./main/app.py` - to start the Flask server


## Resources

| Description                                                        | Link                                                                      |
| :----------------------------------------------------------------- | :------------------------------------------------------------------------ |
| Qiskit - SDK for working with quantum computers| [Qiskit](https://qiskit.org) |
| Flask           | [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/)|
|Heroku |  [Heroku](https://www.heroku.com/)
