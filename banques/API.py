from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
  

app = FastAPI()


@app.get("/get_all_cars")
def get_all_cars():
    f = open('Data/Allcars.json')
    data = json.load(f)
    return data   
@app.get("/get_car_by_name/{name}")
def get_car_bay_name(name):
    f = open('Data/Allcars.json')
    data = json.load(f)
    return data[name]  
@app.get("/get_car_by_name/{name}")
def get_car_bay_name(name):
    f = open('Data/Allcars.json')
    data = json.load(f)
    return data[name]  
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=5000)
   
    