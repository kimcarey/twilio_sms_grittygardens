Combating Malnutrition
============

Installing
---------

1. Clone the repo
2. Install [pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today)
3. Make sure you have Python 3.7 installed 
4. Run this command in the root: `pipenv install --dev`

Running
----

### Backend

`pipenv run backend-start`

### Frontend

`pipenv run frontend-start` (or use `npm start` from frontend folder.)


#### Building

From the frontend folder, run `npm run build` to create production 
builds of the frontend which will then be served by Flask

### Jupyter

`pipenv run notebooks`
