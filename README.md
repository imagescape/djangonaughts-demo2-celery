**Install and Configure RabbitMQ**

    sudo aptitude install rabbitmq-server
    sudo rabbitmqctl add_user my_rabbit_user 1234
    sudo rabbitmqctl add_vhost /my_vhost
    sudo rabbitmqctl set_permissions -p /my_vhost my_rabbit_user ".*" ".*" ".*"


    mkdir testcelery; cd testcelery
    virtualenv --no-site-packages .
    . ./bin/activate 
    pip install django celery django-celery
    git clone git://github.com/imagescape/djangonaughts-demo2-celery.git proj/
    cd proj/
    cd testcelery
    ./manage.py syncdb 


**Run celery services**  
In separate terminals after activating each of them, execute the following: 

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

    >>> result.task_name
    'cel.tasks.add'
    
    >>> result.result
    3
    
    >>> from datetime import datetime, timedelta
    >>> result = tasks.add.apply_async(args=[1,2], eta=datetime.now() + timedelta(seconds=5))
    >>> result.result
    3
    
    >>> result = tasks.add.apply_async(args=[1,2],countdown=10) 
    >>> result.ready()
    False
    >>> result.wait()
    3


    

    
    