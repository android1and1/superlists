from django.shortcuts import render
from django.shortcuts import redirect
from lists.models import Item,List

def home_page(request):
	return render(request,'home.html')

def view_list(request):
	items = Item.objects.all()
	return render(request,'list.html',{'items':items,})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(list=list_,text=request.POST['item_text'])
	return redirect('/lists/the-only-list-in-the-world/')
