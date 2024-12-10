from django.shortcuts import render

# Create your views here.
def index(request):
    data = [
        {"id": 1, "first_name": "John", "last_name": "Doe", "handle": "@johndoe"},
        {"id": 2, "first_name": "Jane", "last_name": "Smith", "handle": "@janesmith"},
        {"id": 3, "first_name": "Alice", "last_name": "Johnson", "handle": "@alicej"},
        {"id": 4, "first_name": "Bob", "last_name": "Brown", "handle": "@bobbyb"},
    ]
    return render(request, 'first_app/index.html', {'data': data})


# def about(request,id):
def about(request):
    # return render(request, 'first_app/index.html',{'id': id})
    print(request.GET)
    return render(request, 'first_app/index.html',{'id': request.GET})