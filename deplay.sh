source env/scripts/activate
pip install -r requirements.txt
python manage.py migrate
sudo service nginx restart
sudo supervisorctl restart gunicornMsExpenses