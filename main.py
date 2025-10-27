from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def hello(request: Request):
    # забираем параметры как есть, включая возможные пробелы
    name = request.query_params.get("name", "").strip()
    message = request.query_params.get("message", "").strip()
    return f"Hello {name}! {message}!"
