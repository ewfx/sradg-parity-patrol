from fastapi import FastAPI
from fastapi import UploadFile
from pydantic import BaseModel
from geminiUtil import generate_output2
from geminiUtil import research_csv
import json
import csv

app = FastAPI()

class Data(BaseModel):
    name: str
    quant: int

class Movie(BaseModel):
    movieName: str

@app.get("/ok")
async def ok_endpoint():
    return {"message":"ok"}

@app.post("/data")
async def data_endpoint(name: str, quant: int):
    return {"message": f"Data : {name} with {quant} quantity received"}

""" @app.post("/data_obj")
async def data_endpoint(obj : Data):
    return {"message": f"Data : {obj.name} with {obj.quant} quantity received"}

@app.post("/movieCast")
async def movieCast_endpoint(movie : Movie):
    cast = generate_output2(f"movieName: {movie.movieName}")
    return {"movieCast": cast} """
    
@app.post("/csvRecon")
async def csv_recon_endpoint(file : UploadFile):
    output = research_csv(file.filename)
    print(output)
    return {"Summary": output}