# Login - Logout Api
This api is made in flask (Python web framework).

## Required libraries
Flask
Flask-Restful (for Restful Api)
Flask-JWT-Extended (for authorization purpose)
Flask-SQLAlchemy (To work with database using ORM)
passlib (To make password more secure)

# Api Endpoints

#### 1. /register (Post)
  - send username and password as json data

#### 2. /login (Post)
  - send username and password as json data

#### 3. /allusers (get)
  - returns all the user in db

#### 4. /ATlogout (post)
  - revokes the access_token
  - add Authorization (Bearer access_token) in request header

#### 5. /RTlogout (post)
  - revokes the refresh_token
  - add Authorization (Bearer refresh_token) in request header

#### 6. /refreshToken (post)
  - returns new access token
  - it is used when access_token is expired after 15 min
  - add Authorization (Bearer refresh_token) in request header

#### 7. /SecretResource (get)
  - To test login - logout functionality
  - add Authorization (Bearer access_token) in request header
