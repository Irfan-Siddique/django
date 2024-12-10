from django.shortcuts import render, redirect
from .forms import addCategory
# Create your views here.
def addCategoryForm(request):
    if request.method=='POST':
        category_form= addCategory(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
    else:
        category_form=addCategory()
    return render(request,'add_category.html',{'form':category_form})