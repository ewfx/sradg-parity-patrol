from fastapi import FastAPI
from fastapi import UploadFile
from pydantic import BaseModel
from geminiUtil import generate_output2
from geminiUtil import research_csv
from geminiUtil import reconcile_csv_usecase1
import json
import csv

app = FastAPI()

class Data(BaseModel):
    name: str
    quant: int

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

@app.post("/csvRecon/usecase1")
async def usecase1_csv_recon_endpoint(file : UploadFile):
    output = reconcile_csv_usecase1(file.filename)
    print(output)
    return {"Summary": output}

@app.post("/csvRecon/usecase2")
async def usecase2_csv_recon_endpoint(file: UploadFile):
    # Process the uploaded file
    output = reconcile_csv_usecase1(file.filename)
    print(output)

    # Clean the output to remove unwanted markers like "```csv" and "```"
    if isinstance(output, str):
        output = output.replace("```csv", "").replace("```", "").strip()

    # Write the cleaned output to a CSV file
    output_csv_path = "usecase2_output.csv"
    with open(output_csv_path, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        # Split the cleaned output into rows and write each row
        for line in output.splitlines():
            # Split each line by commas to create individual fields
            row = line.split(",")
            writer.writerow(row)

    return {"Summary": "CSV created successfully", "Output CSV": output_csv_path}