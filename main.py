from fastapi import FastAPI, HTTPException
from fastapi. responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import days
import pkgutil
from os import walk, path

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Mount the static files directory
app.mount("/index", StaticFiles(directory="."), name="index")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")

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
    return {"error": "Day not found or 'main' function not available"}

@app.get("/day/{day}", response_class=HTMLResponse)
async def read_day(day: int, request: Request):
    if day == 1:
        results = days.day1.main()
        return templates.TemplateResponse("day1.html", {"request": request, "distance": results["distance"], "result": results["result"]})
    else:
            raise HTTPException(
            status_code=404,
            detail="Day not found"
            )

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
