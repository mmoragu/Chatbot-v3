from http.client import OK
from time import gmtime, strftime

from fastapi import APIRouter

routerTrain = APIRouter()



@routerTrain.get('/trainBot/',status_code=200)
    #llamada realizada para entrenar el modelo

def TrainBot():
   
    return OK

