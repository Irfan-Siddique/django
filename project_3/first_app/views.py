from django.shortcuts import render

# Create your views here.
def home(request):
    d={"author": "irfan", "age": 5, "list":[2,4,5], 'courses': [
        {
            'id': 1,
            'name': 'django'
        },
        {
            'id': 2,
            'name': 'SDT'
        },
        {
            'id': 3,
            'name': 'web'
        }
    ]}
    return render(request,'first_app/home.html',context=d)