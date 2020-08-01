I've been working on the project with docker for a majority of the time so I was using docker-compose up to run 
and develop the website. For some reason though due to something I'm not understanding using docker-compose up
doesn't allow django channels to work correctly(I'm assuming it's an ip issue with the docker container). I'm not 
sure if you were already going to use python3 manage.py runserver to test the project but if you are that should 
allow the real time chat to work.

References:
I've adapted code for user authentication, username changes, uploading images, and follower relationships
from django tutorials by the following youtuber:
image uploading:
https://www.youtube.com/watch?v=tT2JOpfelSg

friend or follower relationships:
https://www.youtube.com/watch?v=_DqmVMlJzqA

allow user to change username:
https://www.youtube.com/watch?v=D9Xd6jribFU

I also found a tutorial for using a django password change form to
allow user to change password here:
https://simpleisbetterthancomplex.com/tips/2016/08/04/django-tip-9-password-change-form.html

