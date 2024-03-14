# now here in this file we i will code related to POST methods : POST method generally use to create something 

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn
app=FastAPI()

class Blog(BaseModel):
    title: str
    body:str
    published: Optional[bool]


@app.post('/blog')
def new_blog(request:Blog):
    return {'title':f'Blog is created as my {request.title}','body':request.body}


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)

