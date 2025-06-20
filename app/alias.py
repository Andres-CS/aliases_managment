from dataclasses import dataclass
from datetime import datetime
import os
from pathlib import Path
from .utils import linecount

@dataclass
class aliasObject:
    name:str
    location:str
    description:str
    quantity:int
    # lastModified:datetime

class Alias:
    def __init__(self):
        self.rootPath = os.getenv("APP_MA_ALIASLOCATION")
        self.aliasPrefix = os.getenv('APP_MA_ALIASPREFIX')
        self.aliases = []

        paths = self._iterDir(self.rootPath)
        self._initAliasObjs(paths)
    

    def _iterDir(self,path:str):
        regex = self.aliasPrefix+"*"
        dirPath = Path(path).glob(regex)        
        return dirPath

    def _initAliasObjs(self, filepaths):
        for fp in filepaths:
            name = fp.name
            location = str(fp)
            nlines = linecount(str(fp))
            description = name

            aObj = aliasObject(
                name = name,
                location = location,
                description = description,
                quantity = nlines

            ) 
            self.aliases.append(aObj)
        
    def getAliases(self):
        return self.aliases