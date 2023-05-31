from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount('/secao02/static', StaticFiles(directory='static'), name='static')


@app.get('/')
async def index(request: Request, usuario: str = 'Victor Roza'):
    context = {
        "request": request,
        "usuario": usuario
    }

    return templates.TemplateResponse('index.html', context=context)

# Nome do template com o mesmo nome da funcao


@app.get('/servicos')
async def servicos(request: Request):
    context = {
        "request": request,
    }

    return templates.TemplateResponse('servicos.html', context=context)


@app.post('/servicos')
async def card_servicos(request: Request):
    form = await request.form()

    servico: str = form.get('servico')
    print(f"Servico: {servico}")

    context = {
        "request": request,
    }

    return templates.TemplateResponse('servicos.html', context=context)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app='main:app', host="127.0.0.1",
                port=8000, log_level='info', reload=True)
