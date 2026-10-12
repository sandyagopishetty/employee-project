# from exec.executor import executor_service
#
# exe=executor_service()
# exe.run()
from _pyrepl.commands import end

from fastapi import FastAPI
from starlette.responses import PlainTextResponse

app = FastAPI(title="employee Details")

@app.get('/helloworld')
def hello_world():
    return "hello world.."

@app.get('/add/{a}/{b}')
def addition(a, b):
    c=int(a)+int(b)
    return c
@app.get('/pattern/{n}',response_class=PlainTextResponse)
def pattern(n):
    result = ""
    n =int(n)
    for i in range(n+1):
        result += "* " * (i + 1) + "\n"
    return result

@app.get('/sumofnnumbers/{n}')
def sumofnnumbers(n):
    n = int(n)
    result = 0
    for i in range(n+1):
        result +=i
    return result