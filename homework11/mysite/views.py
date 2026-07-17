from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse ( "<h1>Gamarjoba, I am Nino </h1>")

def about(request):
    return HttpResponse("""
        <h1> About me </h1>
        <p> My favorite food is khinkali </p>
        <p> My hobby is solving sudoku </p>
        """)

def hello(request, name):
    return HttpResponse(f"<h1>გამარჯობა, {name.title()}</h1>")

def movies (request):
    context = (
        {
            "title": "My favorite movies",
            "movies": ["Interstellar", "Green Book", "La-La-Land", "Harry Potter"]
        }
    )
    return render(request, "movies.html", context)

def table(request, n):
    rows = []
    for i in range (1,11):
        rows.append(f"{n}*{i}={n*i}")
    context = {"n": n, "rows": rows}
    return render(request, "table.html", context)

