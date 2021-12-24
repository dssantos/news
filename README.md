
# News API
API for a news portal for registering, searching and viewing news

## 1. Run the project
To run this project you can use one of the following methods:

    * Linux script
    * Windows script

### Linux script (copy and paste)
```bash
git clone https://github.com/dssantos/news.git news
cd news
python -m venv .news
source .news/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
cp contrib/.env-sample .env
sed -i "/^SECRET_KEY=/c\SECRET_KEY=$(python contrib/secret_gen.py)" .env
python manage.py migrate
python manage.py test
python manage.py runserver
```

### Windows script
```bash
git clone https://github.com/dssantos/news.git news
cd news
python -m venv .news
Set-ExecutionPolicy Unrestricted -Scope Process -force
./.news/Scripts/activate
python -m pip install -U pip
pip install -r requirements.txt
cp contrib/.env-sample .env
python contrib/secret_gen.py
# Change SECRET_KEY in .env file
python manage.py migrate
python manage.py test
python manage.py runserver
```

## 2. Populate database
Run this script to populate with user. address and demands sample data

```bash
cat contrib/sample-data.py | python manage.py shell

```

## 3. Have fun!!
Have fun with the API. Now use the postman collection to test the endponis of this API.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/4817709/UVRDHmQJ)

**WARNING:** Remember, some operations need authentication, so get a new token in /api/login/ and REPLACE authorization token on postmand requests headers.
