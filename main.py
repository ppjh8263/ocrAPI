import time
from typing import Optional
from fastapi import FastAPI, UploadFile, File
from typing import List
from starlette.middleware.cors import CORSMiddleware
# from db_config import session
# from model import UserTable, User, CityTable, City
import uvicorn
from classification import predict, read_imagefile, inference

app = FastAPI()

@app.get("/")
def read_root():
    return "Boost Camp AI tech CV7's API"


@app.post("/classification/image")
async def predict_api(file: UploadFile = File(...)):
    time_start = time.monotonic()
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    # prediction = predict(image)
    prediction = inference(image)
    running_time = time.monotonic() - time_start
    print(f'inference time : {running_time:.2f}s')

    return prediction


if __name__ == '__main__':
    uvicorn.run(app, port=6006, host='0.0.0.0')