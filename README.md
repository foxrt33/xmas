=Django stuff=

== make python 3.6 the default ==
sudo alternatives --set python /usr/bin/python3.6

== initial installs & updates
python -m pip install --upgrade-pip --user
python -m pip install virtualenv --user

== install virtualenv == 
# create virtual env called pydev
python -m virtualenv pydev
# activate venv
source pydev/bin/activate

== install project-specific stuff ==
pip install django
pip install django-bootstrap4
pip install import-export

== creating django app == 
django-admin startproject xmas
python manage.py startapp gifts
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser ## rfox/H0ust0n33

-- add people via admin
-- add exceptions via admin
-- add gifts via import/export
python manage.py loaddata data.json ## only contains the gifts.gift entries
