# Django stuff

## Installing python
* Make python 3.6 the default ==
```python
sudo alternatives --set python /usr/bin/python3.6
```
## Initialize and update python env
```python
python -m pip install --upgrade-pip --user
python -m pip install virtualenv --user
```

## Setup virtualenv
* create virtual env called pydev
```python
python -m virtualenv pydev
```
* activate venv
```python 
source pydev/bin/activate
```

# Install project-specific stuff
```python
pip install django
pip install django-bootstrap4
pip install import-export
```

# Creating django app == 
```python
django-admin startproject xmas
python manage.py startapp gifts
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser ## rfox/H0ust0n33
```

# Other stuff
* add people via admin
* add exceptions via admin
* add gifts via import/export
```python
python manage.py loaddata data.json ## only contains the gifts.gift entries
```

