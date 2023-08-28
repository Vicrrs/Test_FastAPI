from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request

app = FastAPI(docs_url=None, redoc_url=None)
templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount('/media', StaticFiles(directory='media'), name='static')


@app.get('/')
async def index(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse('home/index.html', context=context)


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(app="main:app", host="localhost", port=8000, log_level="info", reload=True)
