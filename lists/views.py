from django.shortcuts import render

# 10th
from django.shortcuts import redirect

# second add
#from django.http import HttpResponse
# Create your views here.
#home_page=None


#9th
from lists.models import Item

def home_page(request):
	#pass
	#second add
#	return HttpResponse()
	# third add
	#return HttpResponse('<html>')
	#4th 
	#return HttpResponse('<html><title>To-Do lists</title>')
	# 5th
#	return HttpResponse('<html><title>To-Do lists</title></html>')
	# 6th
	#return render(request,'home.html')
	# 7th
	#if request.method == 'POST':
	#	return HttpResponse(request.POST['item_text'])
	# 8th
	#return render(request,'home.html')
#	return render(request,'home.html',{
#		'new_item_text':request.POST.get('item_text',''),
#		}
#		)
	# 9th
#	item = Item()
#	item.text = request.POST.get('item_text','')
#	item.save()
#	
#	return render(request,'home.html',{
#
#			'new_item_text':request.POST.get('item_text','')
#			}
#
#		)
#	
	#10
	if request.method == 'POST':
		new_item_text = request.POST['item_text']
		Item.objects.create(text=new_item_text)
		# 10th redirect url.
		return redirect('/')
	#else:
		#new_item_text = ''
	items = Item.objects.all()
	return render(request,'home.html',{
		#'new_item_text':new_item_text,
		# 11th
		'items':items,
		}
		)
