from fastapi import FastAPI
from typing import Optional

app=FastAPI()

@app.get('/blog')
def index(limit=10,publish:bool=True,sort:Optional[str]=None):
    # only get 10 published blogs
    if publish:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit} blogs from the db'}
    

