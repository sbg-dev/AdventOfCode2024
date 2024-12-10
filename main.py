from os import walk, path
from fastapi import FastAPI
import pkgutil
import days

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/days")
async def get_days():
    modules = [name for _, name, _ in pkgutil.iter_modules(days.__path__)]
    return modules

@app.get("/days/{day}")
async def call_day(day: str):
    if hasattr(days, day):
        day_module = getattr(days, day)
        if hasattr(day_module, 'main'):
            return day_module.main()
    return {"error": "Day not found or 'main' function not available"}

@app.get("/files")
async def read_file():
    for root, _, files in walk("inputs"):
        file_paths = [path.join(root, file) for file in files]

    return {"file_path": file_paths}

