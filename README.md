# Clery_Django_Demonization

# Two important things don't make mistake
1.Setting the CHDIR  in celeryd file which is located in init.d folder .Make sure that it should be project name
2.Setting the CHDIR_PATH in celryd file which is located in init.d folder . Make sure that place your project path

# Run celery in demon
sudo /etc/init.d/celeryd start
# run the flower
run the flower from the django project folder
 flower -A reflection run
you will see like below status info log
[I 181009 17:37:26 command:139] Visit me at http://localhost:5555
[I 181009 17:37:26 command:144] Broker: amqp://guest:**@localhost:5672//
[I 181009 17:37:26 command:147] Registered tasks:
    ['api.tasks.addition',
     'celery.accumulate',
     'celery.backend_cleanup',
     'celery.chain',
     'celery.chord',
     'celery.chord_unlock',
     'celery.chunks',
     'celery.group',
     'celery.map',
     'celery.starmap']
[I 181009 17:37:26 mixins:224] Connected to amqp://guest:**@127.0.0.1:5672//
