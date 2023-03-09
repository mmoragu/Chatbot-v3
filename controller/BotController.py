from time import gmtime, strftime

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from services.ChatBot import ChatBot

router = APIRouter()



@router.get('/getReponse/{request}',status_code=200)
    #si es posible usar un modelo de objetos para las respuestas tambien
    #el modelo de repsuesta debe ser unica independientemente de si la llamada es buena o mala

def GetReponse(request):
    msg = request
    res = ChatBot.getBot().response(msg)
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return JSONResponse({
        "desc": "Success",
        "ques": msg,
        "res": res,
        "time": time})
   
       # return JSONResponse({"desc": "Bad request"},status_code=404)

# app.include_router(router)