# from exec.executor import executor_service
#
# exe=executor_service()
# exe.run()
from _pyrepl.commands import end
from html import escape

from fastapi import FastAPI, Form
from starlette.responses import PlainTextResponse, HTMLResponse, RedirectResponse

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

#creating table with 2 labels n store values
employees = []

def table():

    rows=''
    for i,emp in enumerate(employees, start=1):
        rows+=f"<tr><td>{i}</td><td>{escape(emp['name'])}</td><td>{emp['salary']}</td></tr>"
    return f"""
    <h2>Add employee</h2>
    <form method ="post" action="/addemployee">
        <input type="text" name="name" placeholder="Employee name" required>
        <input type="number" name="salary" placeholder="employee salary" step="0.01" required>

        <button type="submit">Add</button>
    </form>
    <h2>Employees</h2>
    <table border="1" cellpadding="8" cellspacing="0">
        <tr><th>#</th><th>name</th><th>salary</th></tr>
        {rows}
    </table>
    """
@app.get("/table",response_class=HTMLResponse)
def home():
    return table()
@app.post("/addemployee")
def add_employee(name: str = Form(...),salary: float = Form(...)):
    employees.append({"name":name,"salary":salary})
    return RedirectResponse("/table",status_code=303)










