from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm


def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context ={
        'items': item_list,
    }

    #return render(request, 'food/index.html', {'items': items})
    return render(request, 'food/index.html', context)


# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the food index.")

def item(request):
    return HttpResponse("<h1> This is an item view</h1>")

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)

def create_item(request):

    form = ItemForm(request.POST or None)
    print(f'form is {form}')
    if form.is_valid():
        print(f'the form is valid')
        form.save()
        return redirect('food:index')
    print(form.errors)
    print("form is not valid")
    #this is used for the default view. the get request. Passes for the form object to the template
    #context is the dictionary that is passed to the template
    return render(request, 'food/item-form.html', {'form': form})
    

def update_item(request, item_id):
    print(f"item_id is {item_id}")

    item = Item.objects.get(id=item_id)
    print(f"item is {item}")
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form': form, 'item': item})


def delete_item (request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/confirm-delete.html', {'item': item})

