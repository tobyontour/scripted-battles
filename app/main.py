from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/css", StaticFiles(directory="static/css"), name="css")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/map/{map_id}", response_class=HTMLResponse)
async def map(request: Request, map_id: str):
    map_data = []
    for x in range(40):
        map_data.append([])
        for y in range(40):
            map_data[x].append({
                "x": x,
                "y": y,
                "type": "grass",
                "background_color": "lightgreen",
                "foreground_color": "black",
                "symbol": " ",
                "outline_color": "inherit",
            })
    map_data[20][20]["symbol"] = "🥷"
    map_data[20][20]["outline_color"] = "red"
    map_data[20][38]["symbol"] = "👑"
    map_data[20][38]["outline_color"] = "red"
    return templates.TemplateResponse(
        request=request,
        name="map.html",
        context={"request": request, "map_id": map_id, "map_data": map_data},
    )
