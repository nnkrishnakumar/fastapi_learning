# query parameter: this blog is all about query parameter
#this is the url: http://127.0.0.1:8000/blog?limit=10&publish=True


from fastapi import FastAPI

app=FastAPI()

@app.get('/blog')
def index(limit=10,publish:bool=True):
    # only get 10 published blogs
    if publish:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit} blogs from the db'}
    

