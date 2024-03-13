from fastapi import FastAPI

app=FastAPI()

@app.get('/blog')
def index(limit,publish:bool):
    # only get 10 published blogs
    if publish:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit} blogs from the db'}
