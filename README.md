## Plenty of Cats application

'Plenty of Cats' is like Tinder, but for cats. The idea behind this app is that users can create a profile for their kitties so they can meet other cats to play or hang out with.

In this app, users can register for an account if they don't have one and login if they do. Once they've logged in, users can create a profile for their cats with the following information: name, age, breed and bio.

After creating their account, users are able to update it or delete it if they please. Users are also able to 'purr'(or like) other cats' profiles. They can see their likes on the 'Purr' section.

Users can also change their passwords and sign out.

## Link to repositories

[Front end repo](https://github.com/rosydiazl/Plenty-of-Cats-FE)


[Back end repo](https://github.com/rosydiazl/Plenty-of-Cats-BE)

## Link to deployed sites

[Front end deployed](https://rosydiazl.github.io/Plenty-of-Cats-FE/)

[Back end deployed - Heroku](https://uniqueplentyofcats.herokuapp.com/)

## Technologies used

 #### FRONT END:

- JavaScript

- React 

- Bootstrap

- HTML

- CSS


#### BACK END:

- Python

- Django

- SQL

[Schema/Technologies](https://imgur.com/YeeZCCU)

## Link to Entity Relationship Diagram

[ERD link](https://imgur.com/mh5F4Xh)

## User Stories

- As an unregistered user, I would like to sign up with email, password and password confirmation.

- As a registered user, I would like to sign in with email and password.

- As a signed in user, I would like to change my password.

- As a signed in user, I would like to sign out.

- As a signed in user, I would like to create a profile.

- As a signed in user, I would like to be able to edit my profile.

- As a signed in user, I would like to see other’s profiles.

- As a signed in user, I would like to “like” or “dislike” other profiles.

**Stretch Goals**

- As a signed in user, I would like to “match” with profiles that I liked and liked me back.

- As a signed in user, I would like to chat with my “matches”.

## Planning process

My planning process was first thinking about what app I wanted to built. I talked about some ideas I had with my husband and we both ended up cracking up at the idea of a 'Tinder for Cats', so I went ahead with it. 

The first day of Project Week, I created my wireframes, user stories and ERD. I also created a Suggested Schedule for myself that I referenced every day as I worked on new features.

In regards to my problem-solving strategy, I used a rubber duck to explain to it what I was trying to build. I also used it to debug whenever I ran into issues.

[Suggested Scheduled 1](https://imgur.com/fTvG0QX)

[Suggested Schedule 2](https://imgur.com/SWEV6Eo)

[Rubber duck debugging](https://imgur.com/NMfXzT3)

## Screenshot of the app

## Routes that the API expects

VERB -> POST 
URL -> /userprofile/
BODY -> data
HEADERS -> Token
RESPONSE -> 201 Created


VERB -> GET 
URL -> /userprofile/
BODY -> none
HEADERS -> Token
RESPONSE -> 200 OK


VERB -> DELETE 
URL -> /userprofile/ + id
BODY -> none
HEADERS -> Token
RESPONSE -> 204 No Content

VERB -> PATCH 
URL -> /userprofile/ + id + '/'
BODY -> data
HEADERS -> Token
RESPONSE -> 200 OK

VERB -> POST
URL -> /likes/
BODY -> data
HEADERS -> Token
RESPONSE -> 200 OK

VERB -> DELETE
URL -> /likes/
BODY -> none
HEADERS -> Token
RESPONSE -> 204 No Content


- Data
data: {
      profile: {
        name: profile.name,
        age: profile.age,
        breed: profile.breed,
        bio: profile.bio
      }
    }


## Problems to be solved in future iterations

In future iterations, users will be able to:

1. Upload their own pictures when they're creating a profile and see it displayed on the Bootstrap Card.
2. 'Match' with other users when they both 'like' each other. 
3. Chat with their matches (using Socket)


## Installation instructions

1. Fork and clone the repository
2. CD into the project and run 'git init'
3. Empty the README and fill with your own content
4. Create a .env file
5. Add a key ENV with the value 'development'
6. Run 'pipenv shell' to start up the virtual environment
7. Run pipenv install django-rest-auth django-cors-headers python-dotenv dj-database-url in the django-env folder
8. Create a psql database for your app
9. Add the database name to the .env file using the key DB_NAME_DEV
10. Generate a secret key using this tool and add it to the .env file using the key SECRET
