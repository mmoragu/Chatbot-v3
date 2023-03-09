from fastapi import FastAPI

from controller.BotController import router
from controller.TrainController import routerTrain

app = FastAPI()

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")

app.include_router(router)
app.include_router(routerTrain)
