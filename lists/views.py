from django.shortcuts import render
# second add
from django.http import HttpResponse
# Create your views here.
#home_page=None

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
		return render(request,'home.html',{
			'new_item_text':request.POST.get('item_text',''),
			}
			)

