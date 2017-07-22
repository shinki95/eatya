from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Shop
from .forms import ShopModelForm


def detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    msg = (
        '<p>{pk}번 식당입니다</p>.'.format(pk=shop.pk),
    )
    return HttpResponse(msg)


def create(request):
    if request.method == "POST":
        form = ShopModelForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect('/shop/')
 
    else:
        form = ShopModelForm()
    return render(request, 'shop/edit.html', {
        'form': form,
    })

def home(request):
    shops = Shop.objects.all()
    return render(request, 'shop/homepage.html', {'shops' : shops})

