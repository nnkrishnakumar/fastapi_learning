from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def hello():
    return {"name":"Krishna"}

@app.get("/about")
def about():
    return {"about":"this is about us page"}

@app.get("/blog")
def blog():
    return {"blog":"this is the first blog"}

@app.get("/blog_id/{id}")         #it is a dynamic route
def blog_id(id):
    return {'data':id}

@app.get("/blog_id/{id}/comments")
def comments(id):
    return {'data':{'1','2'}}

