from pathlib import Path
import shelve

# script demonstrates saving app state with shelve module

with shelve.open('mydata') as shelve_file:
    shelve_file['cats'] = ['can', 'zoo', 'moo']
    shelve_file['car'] = 'toyota'

with shelve.open('mydata') as shelve_file:
    for key in shelve_file.values():
        print(key)