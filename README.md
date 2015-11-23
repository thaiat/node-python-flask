## Destruction
```bash
heroku destroy node-python-flask --confirm node-python-flask
```

## Installation
### WORKING WITH PYTHON 2.7.10 and OPENCV 2.4.11
```bash
heroku create node-python-flask  --buildpack https://github.com/heroku/heroku-buildpack-nodejs.git
heroku buildpacks:add --index 2   https://github.com/diogojc/heroku-buildpack-python-opencv-scipy.git#cedar14
```


## Procfile
```
gunicorn --log-file=- app:app
```