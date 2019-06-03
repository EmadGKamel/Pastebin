# Pastebin

A Web project help you share
codes and notes with your friends 
## Made with ❤ by Python with Django
![language](https://img.shields.io/badge/language-Python-lightgrey.svg)
![Platform](https://img.shields.io/badge/platform-DJANGO-lightgrey.svg)

## Table of Contents
* [Summary](#summary)
* [Installation](#Installation)
* [Example](#Example)


<a name="summary"></a>
## Summary
Pastebin is a clone of the original [Pastebin](https://pastebin.com/) that include the following features:

- A hosted web version on IBM CLoud at [pastbin](https://pastebin.eu-gb.mybluemix.net/) 
- An API to CRUD the snippets, users and groups


<a name="Installation"></a>
## Installation
This project tested with [Python 3.7](https://www.python.org/downloads/release/python-373/), [Django 2.2](https://www.djangoproject.com/download/), and [Pipenv](https://docs.pipenv.org/en/latest/#install-pipenv-today) and it's highly recommend to use Pipenv over pip
### Steps
1. Open the terminal or CMD and paste the following commands:
    ```bash
    git clone https://github.com/
    cd Pastebin
    ```
2. After checking Python version, use one of the following methods to install the depends:
    1. For Pipenv use the following command
        ```bash
        pipenv install
        pipenv shell   # to run the virual environment
        ```    
    2. For pip use the following command
        ```bash
        pip install -r requirements.txt
        ```
3. Now run these two commands to make a sqlite db instanse
    ```bash
    python manage.py makemigrations --settings=Pastebin.settings.development
    python manage.py migrate --settings=Pastebin.settings.development
    ```
4. You're ready to bring up your local server
    ```bash
    python manage.py runserver --settings=Pastebin.settings.development
    ```
    Your application is running at: `http://localhost:8000/` in your browser.
<a name="Example"></a>
## Example
