# Login - Logout Api
This api is made in flask (Python web framework).

## Required libraries
Flask
Flask-Restful (for Restful Api)
Flask-JWT-Extended (for authorization purpose)
Flask-SQLAlchemy (To work with database using ORM)
passlib (To make password more secure)

# Api Endpoints

#### 1. / (get)
  - payment gateway page

#### 2. /register (Post)
  - send username and password as json data

#### 3. /login (Post)
  - send username and password as json data

#### 4. /allusers (get)
  - returns all the user in db

#### 5. /ATlogout (post)
  - revokes the access_token
  - add Authorization (Bearer access_token) in request header

#### 6. /RTlogout (post)
  - revokes the refresh_token
  - add Authorization (Bearer refresh_token) in request header

#### 7. /refreshToken (post)
  - returns new access token
  - it is used when access_token is expired after 15 min
  - add Authorization (Bearer refresh_token) in request header

#### 8. /employee/<string:id>
  - add Authorization (Bearer access_token) in request header for all below 4 operations
  - emp_id is given endpoint itself
  -  **get**: gives employee detail
  -  **post**: send emp_name and city to add
  -  **push**: send emp_name and city to update
  -  **delete**: delete given employee

#### 9. /allEmployee
  - returns all employees
