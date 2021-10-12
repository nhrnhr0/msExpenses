source ./env/bin/activate
pip install -r requirments.txt
python3 manage.py migrate
python3 manage.py collectstatic --no-input
sudo service nginx restart
sudo supervisorctl restart gunicornMsExpenses
