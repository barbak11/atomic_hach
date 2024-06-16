import os
import shutil
from typing import List
from pydantic import BaseModel, Field
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from yolo.model import YoloModel

class ModelRequest(BaseModel):
    image_paths: List[str] = Field(None, description="Paths to images")
    file_name: str = Field(None, description="Filename")


app = FastAPI(root_path="/yolo")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = YoloModel()

@app.post("/predict")
def predict(request : ModelRequest) -> dict:
    
    results = model.predict(request.image_paths)
    image_names = [path.split('/')[-1] for path in request.image_paths]

    classes = {}
    
    if not os.path.isdir(f'.cache/{request.file_name}_results/'):
        os.mkdir(f'.cache/{request.file_name}_results/')
    else:
        shutil.rmtree(f'.cache/{request.file_name}_results/')
        os.mkdir(f'.cache/{request.file_name}_results/')

    for name, res in zip(image_names, results):
        class_mapping = res.names
        cls = [class_mapping[item] for item in res.boxes.cls.numpy()]
        classes[name] = cls
        res.save(filename=f'.cache/{request.file_name}_results/{name}.jpg')

    return classes
