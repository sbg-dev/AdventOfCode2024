from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import days
import pkgutil
from os import walk, path

app = FastAPI()

# Mount the static files directory
app.mount("/index", StaticFiles(directory="."), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}

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
    print(f'{day}')
    return {"error": "Day not found or 'main' function not available"}

@app.get("/files")
async def get_files():
    file_paths = []
    for root, _, files in walk("inputs"):
        file_paths.extend([path.join(root, file) for file in files])
    return {"file_paths": file_paths}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return {"content": content}
