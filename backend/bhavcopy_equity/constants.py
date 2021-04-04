from currency_symbols import CurrencySymbols

class Constants():
    FILE_URL = 'https://www.bseindia.com/download/BhavCopy/Equity/EQ{0}_CSV.ZIP'
    HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
    KEY_PATTERN = 'bhav:{0}:{1}'
    IND_CURR_SYMBOL = CurrencySymbols.get_symbol('INR')
    ASTERISK = '*'