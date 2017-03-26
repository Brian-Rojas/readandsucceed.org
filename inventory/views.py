from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from inventory.models import Item
from django.contrib.auth.decorators import login_required


def index(request):
	items = Item.objects.order_by("title")

	#Search by barcode:
	query = request.GET.get("q")
	if query:
		items = items.filter(barcode__icontains=query)


	# items = Item.objects.exclude(amount=0)
	context = {
		'items': items,
	}
	return render(request, 'index.html', context)

######################################################
###Decrement amount of selected book, then redirect
######################################################
@login_required(login_url='/login/')
def checkOut(request, book_id):
    try:
        item = Item.objects.get(id=book_id)
    except Item.DoesNotExist:
        raise Http404("This item does not exist")
    
    if(item.amount > 0):
        item.amount = item.amount - 1;
        item.save()
    return redirect("/")

######################################################
###Increment amount of selected book, then redirect
######################################################
@login_required(login_url='/login/')
def checkIn(request, book_id):
    try:
        item = Item.objects.get(id=book_id)
    except Item.DoesNotExist:
        raise Http404("This item does not exist")
    
    if(item.amount < 1000):
        item.amount = item.amount + 1;
        item.save()
    return redirect("/")

@login_required(login_url='/login/')
def item_detail(request, id):
	try:
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404("This item does not exist")

	context = {
		'item': item,
	}
	return render(request, 'item_detail.html', context)

@login_required(login_url='/login/')
def addBooks(request):
	try:
		if(request.method == 'POST'):
			title = request.POST['title']
			amount = request.POST['amount']
			barcode = request.POST['barcode']
			description = request.POST['description']

			item = Item(title=title, amount=amount, barcode=barcode, description=description)
			item.save()
	except:
		raise Http404("All fields are requiered")

		return redirect("/")
	else:
		return render(request, 'addBooks.html')


def lowBookList(request):
	items = Item.objects.filter(amount__lte=10)
	context = {
		'items': items,
	}
	return render(request, 'index.html', context)
