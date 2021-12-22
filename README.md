
# News API
API for a news portal for registering, searching and viewing news

## How to dev

### Linux
```bash
git clone https://github.com/dssantos/news.git news
cd news
python -m venv .news
source .news/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
cp contrib/.env-sample .env
sed -i "/^SECRET_KEY=/c\SECRET_KEY=$(python contrib/secret_gen.py)" .env
```

### Windows
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
```
