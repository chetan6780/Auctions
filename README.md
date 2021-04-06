# Auctions
### How to use it
- **Register** yourself if you are new here.(Please use good username).
- **Login** to your account if not already loged in.
- Select the item which you liked and **bid** on it.
- Make sure that your bid is **high enough**.
- You can comment in **comment section** of the perticular item.
- After owener close the Auction the user with ***highest bid*** will win.
- **Winner** will able to see message in the lising of that perticular item.
- Invite your friend to do bidding and have **fun**!!😃🤟 

### Click <a href="https://auctionscom.herokuapp.com/">here</a> to open the auction.

# How to set up on local machine

## Pre-setup
Create a new folder anywhere on your system
open terminal in this new folder

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/chetan6780/Auctions.git
$ cd Auctions
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ .\env\Scripts\activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
The application should be running on `http://127.0.0.1:8000/`