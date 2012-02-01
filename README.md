**Install and Configure RabbitMQ**

    sudo aptitude install rabbitmq-server
    sudo rabbitmqctl add_user my_rabbit_user 1234
    sudo rabbitmqctl add_vhost /my_vhost
    sudo rabbitmqctl set_permissions -p /my_vhost my_rabbit_user ".*" ".*" ".*"


mkdir testcelery; cd testcelery
virtualenv --no-site-packages .
. ./bin/activate 
pip install django celery django-celery
mkdir proj/; cd proj/
django-admin startproject testcelery 
cd testcelery
./manage.py syncdb 


**Run celery services:**  
in separate terminals after activating each of them

    ./manage.py runserver
    ./manage.py celeryd -EB -l info 
    ./manage.py celerycam 
    ./manage.py celeryev 
