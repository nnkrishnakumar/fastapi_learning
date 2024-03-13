# fastapi_learning


problem: 
--------

this route:
@app.get("/route_int/{id}")
def route_int(id:int):
    return {"data":id}

this is the url: http://127.0.0.1:8000/route_int/mohan

error getting on the screen :

{
"detail": [
{
"type": "int_parsing",
"loc": [
"path",
"id"
],
"msg": "Input should be a valid integer, unable to parse string as an integer",
"input": "mohan",
"url": "https://errors.pydantic.dev/2.6/v/int_parsing"
}
]
}


Solution:
---------
@app.get("/route_int/{id}")
def route_int(id:int):            # remove int datatype infront of id to solve
    return {"data":id}


===============================================================================

Query parameter
---------------

this is the code :

@app.get('/blog')
def index(limit,publish:bool):
    # only get 10 published blogs
    if publish:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit} blogs from the db'}
    

output:
-------
this is the url: http://127.0.0.1:8000/blog?limit=10&publish=True

{
"data": "10 published blogs from the db"
}