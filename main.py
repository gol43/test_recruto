from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    name = request.query_params.get("name", "").strip()
    message = request.query_params.get("message", "").strip()
    
    if name and message:
        return templates.TemplateResponse("result.html", {"request": request, "name": name, "message": message})
    else:
        return templates.TemplateResponse("form.html", {"request": request})
