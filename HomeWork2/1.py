__author__ = "kehao"
import shelve
with shelve.open('database') as DB:
    DB['a'] = 123
    print(fb)