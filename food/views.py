from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView



class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'items' # this is the name of the object that is passed to the template so it's used for variables
    




#replaced by above
# def index(request):
#     item_list = Item.objects.all()
#     template = loader.get_template('food/index.html')
#     context ={
#         'items': item_list,
#     }

    
#     return render(request, 'food/index.html', context)


# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the food index.")

def item(request):
    return HttpResponse("<h1> This is an item view</h1>")


class DetailBasedView(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'
    


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image'] # only the fields in the form
    template_name = 'food/item-form.html'
    #this will get the current user and assign it to the user_name field
    #this is the user that is currently logged in
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    



# def create_item(request):

#     form = ItemForm(request.POST or None)
#     print(f'form is {form}')
#     if form.is_valid():
#         print(f'the form is valid')
#         form.save()
#         return redirect('food:index')
#     print(form.errors)
#     print("form is not valid")
#     #this is used for the default view. the get request. Passes for the form object to the template
#     #context is the dictionary that is passed to the template
#     return render(request, 'food/item-form.html', {'form': form})
    

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

