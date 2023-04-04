from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/')
async def index():
    conteudo = """
        <center>
            <h1>Testando <u>FastAPI</u> mais uma vez</h1>
            <span>Testando</span>
        </center>
    """
    return HTMLResponse(content=conteudo)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0",
                port=8000, log_level="info", reload=True)
