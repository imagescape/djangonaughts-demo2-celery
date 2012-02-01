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


**Run celery services**  
In separate terminals after activating each of them

    ./manage.py runserver
    ./manage.py celeryd -EB -l info 
    ./manage.py celerycam 
    ./manage.py celeryev 


**Execute a Django Shell to begin experimenting**
    
    ./manage.py shell 
    
    >>> from cel import tasks 
    >>> result = tasks.add.apply_async(args=[1,2])
    
    >>> result.state
    u'SUCCESS'
    
    >>> result.successful()
    True
    
    >>> result.failed()
    False

    >>> result.task_id
    'b35e876a-2fba-4d8e-ab90-3e2aa7796f52'

    

    
    