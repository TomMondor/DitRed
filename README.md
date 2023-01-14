# DitRed

__DitRed__ is a pastiche of the famous __Reddit__ application, produced as part of an introductory course to SQL databases. 

This project includes a frontend made with `Vue.js`, a backend in Python using `Flask` and `pymysql` and a SQL database.

See the [wiki](https://github.com/TomMondor/DitRed/wiki) for some screenshots of the app!

## Features
Without being connected, a user can :
- see subs, posts, comments and user pages

After creating an account and logging in, a user can :
- see subs, posts, comments and user pages
- create subs, posts and comments
- upvote or downvote posts and comments
- subscribe to subs
- see recent posts from subscribed subs
- visit their own user page and add wallposts
- chat with other users (real-time chat)

Features, as seen by a developper :
- responsive web app (for desktop browsers only)
- real-time chat implemented with websockets
- persistence to a SQL database
- signup and login using session token

## Collaborators
This project was made by myself, [Alexandre Mathieu](https://github.com/alexmathieu22) and [Gabriel Gosselin-Roberge](https://github.com/gabgosrob)

## To use locally :

- Clone the repository.
  ```
    git clone https://github.com/TomMondor/DitRed.git
  ```

- Create a .env file to store your mySQL username and password.
  ```
    USER=myUserNameNoQuotesAround
    PASSWORD=myPasswordNoQuotesAround
  ```
  
- Create a conda environment using the environment.yml file.
  ```
    conda env create --file environment.yml
  ```
  
- Activate the conda environment.
  ```
    conda activate DitRed
  ```

- Run the `DB_populate_script.py` in the environment to create and populate the database with fake, random data.
