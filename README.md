# Recycling company
Web application "Recycling company" built for my EBC-VWA - Web Applications Development course.

## What I Learned
- Implemented backend using the Flask framework in the Python programming language
- Connected database to store and query data using SQLite
- Designed dynamic web based on different roles and provided authentication process with proper security

## How to run this project on your local machine?
Create virtual environment:
```
$ python -m venv venv
```
Activate your virtual environment:
```
$ source venv/bin/activate
```
Install required librabries from *requirements.txt*:
```
$ pip install -r requirements.txt
```
Start:
```
$ flask run
```

## Repo Structure
```
/
├─ database/         # Database configuration and creating tables
├─ service/          # User class, material class, collections class 
├─ static/           # Static resources
│  ├─ img/ 
|  ├─ css/
│
├─ templates/         # HTML templates
│  ├─ admin/
|     ├─ accounts/ 
|     ├─ materials/
│  ├─ worker/
|     ├─ accounts/ 
|     ├─ collections/
│  ├─ default/  
│  ├─ homepage/    
│  ├─ about_us       
│  ├─ footer  
│  ├─ main
|  ├─ nav
|  ├─ prices
|  ├─ stats
│
├─ views/             # View functions
├─ README.md          # This file
├─ forms.py           # Forms
├─ auth.py            # Authorization and roles control
├─ app.py             # Runner
├─ config.py          # Configuration
└─ requirements.txt   # Required librabries
```

## <p align="center">Entity–relationship model</p>
<p align="center"><img src="https://github.com/bogdanvyzhlov/recycling-company/blob/main/static/img/ERD.png" alt="ER" width="600"/></p>


## <p align="center">Use case diagram</p>
<p align="center"><img src="https://github.com/belekomurzakov/brigadier-agency/blob/master/static/images/UseCase.png" alt="ER" width="600"/></p>
