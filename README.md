Web App to view BSE Bhav Copy data.
Perform search and download

### Project Setup

First install all dependencies -

```
pip install -r requirements.txt
```

Generate static files from frontend
Navigate to frontend folder and run - 

```
npm run build
```
This will generate all static files

Configure Redis Server in projectZero/settings.py file - 
```
REDIS_HOST = <redis-server host>
REDIS_PORT = <redis-server port>
REDIS_PASSWORD = <redis-server password>
```


