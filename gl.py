# -*- coding: utf-8 -*-

import sys
import json

def locadJson(jsonStr):
    return json.loads(jsonStr)

def loadJsonFile(fileName):
    return json.load(open(fileName, 'r', encoding='UTF-8'))

def dumpJson(pyObj):
    return json.dumps(pyObj, sort_keys=True, indent=4, ensure_ascii=False)

def dumpJsonFile(pyObj, fileName):
    json.dump(pyObj, open(fileName, 'w', encoding='UTF-8'), sort_keys=True, indent=4, ensure_ascii=False)

