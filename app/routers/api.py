import json
from itertools import chain

from fastapi import APIRouter
from starlette.responses import JSONResponse

from configs import project

router = APIRouter()


@router.get('/categories/')
def get_categories(io: str = ''):
    file = project.DATA_DIR / 'categories.json'
    if file.exists():
        data = json.loads(file.read_text(encoding='utf8'))
        if io:
            return data[io]
        else:
            return list(chain.from_iterable([data[key] for key in list(data.keys())]))
    else:
        return JSONResponse(status_code=404, content={'info': 'without category file'})


@router.get('/secondaries')
def get_secondaries(category: str = ''):
    file = project.DATA_DIR / 'secondaries.json'
    info = {'info': ''}
    if file.exists():
        data = json.loads(file.read_text(encoding='utf8'))
        if not category:
            info['info'] = 'must have category in query string'
            return JSONResponse(status_code=400, content=info)
        try:
            return data[category]
        except KeyError:
            info['info'] = 'wrong category'
            return JSONResponse(status_code=400, content=info)
    else:
        info['info'] = 'without secondary file'

        return JSONResponse(status_code=404, content=info)
