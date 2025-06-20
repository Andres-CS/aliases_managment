import logging

def linecount(filepath:str):
    try:
        nlines:int = 0
        with open(filepath,'rb') as file:
            nlines = file.read().count(b'\n')
        return nlines

    except FileNotFoundError as e:
        logging.error(f'File, {filepath}, not found.')
        raise
