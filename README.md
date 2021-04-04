Web App to view BSE Bhav Copy data.
Perform search and download

# BSE BhavCopy Viewer

## Introduction


## Project Setup


### Backend folder - 
First install all dependencies -

```
pip install -r requirements.txt
```

Configure Redis Server in projectZero/settings.py file - 
```
REDIS_HOST = <redis-server host>
REDIS_PORT = <redis-server port>
REDIS_PASSWORD = <redis-server password>
```


### Frontend folder -
Generate static files from frontend
Navigate to frontend folder and run - 

```
npm run build
```
This will generate all static files



