# template drf and fbv



## Getting started

Firstly, run server to ensure all dependencies are fulfilled. 

python manage.py runserver

if any libraries are missing, install using:

pip install packagename


## Populate your DB

Although not entirely necessary, it is best to populate your server with some dummy data, to do this, either through the app interface, the REST template or through admin page.


## API Endpoints

To navigate through the project API, please use belows url endpoints:

1. To view all posts in lists:

http://127.0.0.1:8000/pl/

by title:

http://127.0.0.1:8000/pl/title=<title>

example:

http://127.0.0.1:8000/pl/title=Study

by content:

http://127.0.0.1:8000/pl/content=<content>

example:

http://127.0.0.1:8000/pl/content=not%20converge%20but%20diverge

by category:

http://127.0.0.1:8000/pl/category=<category>

example

http://127.0.0.1:8000/pl/category=Work

2. To view and update details of post:

http://127.0.0.1:8000/pd/<postid>

example

http://127.0.0.1:8000/pd/1

3. to view categories

http://127.0.0.1:8000/categories/





Others

The above were created with rest API, but https endpoints are also available through FBV.
