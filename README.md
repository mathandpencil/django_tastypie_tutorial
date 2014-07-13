This is a simple example of how to setup a REST API using Django Tastypie
This tutorial assumes that you are running a Postgres backend. I KNOW this does
not work with sqlite3 because of the south migration to seed the database.

To get started, first create a new postgers database:

```
createdb example
```

Next, sync your database:

```
python manage.py syncdb
```

Then, run the the south migrations:

```
python manage.py migrate
```

Finally, run the server and go to the following URL:

```
python manage.py runserver 8001
http://127.0.0.1:8001/api/v1/user/?format=json
```

You should see the following output:

```
{"meta": {"limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 3}, "objects": [{"date_joined": "2014-07-12T20:45:16.823123", "email": "joe@example.com", "first_name": "", "id": 1, "is_active": true, "is_staff": false, "is_superuser": false, "last_login": "2014-07-12T20:45:16.823077", "last_name": "", "password": "", "resource_uri": "/api/v1/user/1/", "username": "joe@example.com"}, {"date_joined": "2014-07-12T20:45:16.825555", "email": "tim@example.com", "first_name": "", "id": 2, "is_active": true, "is_staff": false, "is_superuser": false, "last_login": "2014-07-12T20:45:16.825510", "last_name": "", "password": "", "resource_uri": "/api/v1/user/2/", "username": "tim@example.com"}, {"date_joined": "2014-07-12T20:45:16.827626", "email": "sam@example.com", "first_name": "", "id": 3, "is_active": true, "is_staff": false, "is_superuser": false, "last_login": "2014-07-12T20:45:16.827584", "last_name": "", "password": "", "resource_uri": "/api/v1/user/3/", "username": "sam@example.com"}]}
```


The blog post for this code can be found [here](http://blog.mathandpencil.com/using-django-tastypie-to-create-RESTful-APIs/)


Have Fun and Good Luck!