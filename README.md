# Auctions
### How to use it
- **Register** yourself if you are new here.(Please use good username).
- **Login** to your account if not already loged in.
- Select the item which you liked and **bid** on it.
- Make sure that your bid is **high enough**.
- You can comment in **comment section** of the perticular item.
- After owener close the Auction the user with ***highest bid*** will win.
- **Winner** will able to see message in the lising of that perticular item.
- Have **fun** bidding!😃🤟 

### Click <a href="https://auctionscom.herokuapp.com/">here</a> to open the auctions.

# How to set up on local machine

## Pre-setup
Create a new folder anywhere on your system
open terminal in this new folder.

## Setup

1. The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/chetan6780/Auctions.git
$ cd Auctions
```

2. Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ .\env\Scripts\activate
```
**OR**<br/>
```sh
$ pip install pipenv
$ pipenv shell
```

3. install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
*Note: `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.
For pipenv you will not see any `(env)` in front of the propt.*

4. Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
The application should be running on `http://127.0.0.1:8000/`
