import requests, zipfile, io, csv, redis
from django.conf import settings
from datetime import datetime, timedelta
from .constants import Constants

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, 
                                    password=settings.REDIS_PASSWORD, charset="utf-8", decode_responses=True, db=0)

def getUpdateBhavCopyZip():
    bhavDataDate = datetime.strftime(datetime.now() - timedelta(1), '%d%m%y')
    print(bhavDataDate)
    r = requests.get(Constants.FILE_URL.format(bhavDataDate), allow_redirects=True, headers=Constants.HEADERS)
    if(r.status_code==200):
        z = zipfile.ZipFile(io.BytesIO(r.content))
        fileOpen = z.open(z.namelist()[0])
        reader = csv.reader(io.TextIOWrapper(fileOpen, 'utf-8'))
        iteratorCSV = iter(reader)
        next(iteratorCSV)
        populateRedis(iteratorCSV)

def populateRedis(iteratorCSV):
    for row in iteratorCSV:
        rValue = {
            'CODE': row[0],
            'NAME': row[1].strip(),
            'OPEN': ' '.join([Constants.IND_CURR_SYMBOL, row[4]]),
            'HIGH': ' '.join([Constants.IND_CURR_SYMBOL, row[5]]),
            'LOW': ' '.join([Constants.IND_CURR_SYMBOL, row[6]]),
            'CLOSE': ' '.join([Constants.IND_CURR_SYMBOL, row[7]])
        }
        redis_instance.hmset(Constants.KEY_PATTERN.format(row[0], row[1].strip()), rValue)



    