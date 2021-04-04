Web App to view BSE Bhav Copy data.
Perform search and download

# BSE BhavCopy Viewer
You can check Demo at [https://bhav-copy-viewer.herokuapp.com/home](https://bhav-copy-viewer.herokuapp.com/home) 
## Introduction
BSE publishes a "Bhavcopy" (Equity) ZIP every day.

This Web Application

- Downloads the equity bhavcopy zip from the above page every day at 18:00 IST for the current date.
- Extracts and parses the CSV file in it.
- Writes the records into Redis (Fields: code, name, open, high, low, close).
- Renders a VueJS frontend with a search box that allows the stored entries to be searched by name and renders a 
  table of results and you can download the results as CSV.

## Project Setup

### Frontend folder -
Navigate to frontend folder and run

```
npm install
```
This will download all the requirement.

Configure endpoint axios Enpoint Url at public/constatnt.js
```
apiEndpointUrl = <Your django web-server url>
```

Generate all static files
```
npm run build
```
This will generate static files in backend/static and backend/template folder

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






