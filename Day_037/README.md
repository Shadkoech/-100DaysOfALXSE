# Day_037

- #100daysofalxse 
- #DoingHardThings
- #DailyGrowth

I continued on the implementation of session authentication

## Overview
Session authentication is a mechanism used to verify and manage user identity and access within a web application. Unlike traditional authentication methods that require users to provide credentials (such as username and password) with each request, session authentication establishes a temporary session between the user and the server after successful login. This session is typically maintained using a unique identifier stored as a cookie in the user's browser.

## Project description
In this project, Session Authentication is implemented without relying on any additional modules. Session authentication is a common mechanism used to validate and authorize users accessing web applications. While it's typically recommended to utilize established frameworks or modules for authentication, this project aims to provide a deeper understanding of the underlying concepts by implementing it from scratch.

## Key concepts
- The concept of authentication
- Session management (how sessions are created, managed, and terminated in web applications.)
- HTTP cookies are and how they are used to store small pieces of data on the client side (user's browser)
- HTTP requests and responses within a web framework
- Statelessness vs. Statefulness in web applications
- Session expiration and the mechanisms for setting session timeouts.

## Task
Implementation of expiration in session authentication:

File:

    - session_exp_auth.py
Create a class SessionExpAuth that inherits from SessionAuth in the file api/v1/auth/session_exp_auth.py:

- Overload def __init__(self): method:
Assign an instance attribute session_duration:
To the environment variable SESSION_DURATION casts to an integer
If this environment variable doesn’t exist or can’t be parse to an integer, assign to 0

- Overload def create_session(self, user_id=None):
Create a Session ID by calling super() - super() will call the create_session() method of SessionAuth
Return None if super() can’t create a Session ID
Use this Session ID as key of the dictionary user_id_by_session_id - the value for this key must be a dictionary (called “session dictionary”):
The key user_id must be set to the variable user_id
The key created_at must be set to the current datetime - you must use datetime.now()
Return the Session ID created

- Overload def user_id_for_session_id(self, session_id=None):
Return None if session_id is None
Return None if user_id_by_session_id doesn’t contain any key equals to session_id
Return the user_id key from the session dictionary if self.session_duration is equal or under 0
Return None if session dictionary doesn’t contain a key created_at
Return None if the created_at + session_duration seconds are before the current datetime. datetime - timedelta
Otherwise, return user_id from the session dictionary
