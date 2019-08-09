### :koala: Notes for the flask project

> Create a .flaskenv file to execute the flask app
> FLASK_APP=main.py (Application to run)
> FLASK_ENV=development/production (set to development for debug messages)


### Command lines
> To view the list of routes type the following command 
> flask routes 
 
|Endpoint      | Methods | Rule                   |
|--------------| ------- | -----------------------|
|create_error  | GET     |/error                  |
|greeting      | GET     |/greeting/<name>        |
|index         |  GET    | /index                 |
|index         |  GET    | /home                  |
|index         | GET     |/                       |
|return_message|  GET    | /data                  |
|static        | GET     |/static/<path:filename> |