from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from django.template import context
# from django.template import defaulttags
from Fouraso.form import ProductForm, StockForm, PersonForm, CommandForm
from Fouraso.models import Product, Stock, Person, Command
    # Zone, ZoneForm,


def thanks(request):
    return HttpResponse('Thanks, your form has been processed')

def products(request):
    if request.method == 'POST':
            na = request.POST.get("name")
            ref = request.POST.get("reference")
            pr = request.POST.get("price")
            data = Product(name=na, reference=ref, price=pr)
            data.save()
            return HttpResponseRedirect(reverse('thanks'))
    else:
       form = ProductForm()
    return render(request, 'Fouraso/products.html', {'form': form})


def products_detail(request, product_id):
    products = Product.objects.all()

    context = {

        'products': products
    }
    return render(request, 'Fouraso/products_list.html', context)


def about(request):
    # products = Product.objects.all()

    # context = {
    #
    #     'products': products
    # }
    return render(request, 'Fouraso/homepage.html',)


def stock(request,):
    Stocks = Stock.objects.all()
    form = StockForm()
    # context = {
    #     # 'stock': stock
    #
    # }
    return render(request, 'Fouraso/stock.html', {'form': form})

    # else:
    #    form = ProductForm()


def command(request,):
    if request.method == 'POST':
            locat = request.POST.get("localite")
            qteC = request.POST.get("qteCommande")
            subm = request.POST.get("submontant")
            rm = request.POST.get("remise")
            tv = request.POST.get("tva")
            dat = request.POST.get("created_at")
            mont = request.POST.get("montant")
            data = Command(localite=locat, qteCommande=qteC, submontant=subm,
                             remise=rm, tva=tv, created_at=dat, montant=mont,)
            data.save()
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = CommandForm()
    return render(request, 'Fouraso/command.html', {'form': form})

def person(request):
    if request.method == 'POST':
            stat = request.POST.get("status")
            f_name = request.POST.get("first_name")
            l_name = request.POST.get("last_name")
            cont = request.POST.get("contact")
            ema = request.POST.get("email")
            dat = request.POST.get("created_at")
            data = Person(status=stat, first_name=f_name,
                          last_name=l_name, contact=cont, email=ema, created_at=dat,)
            data.save()
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = PersonForm()
    return render(request, 'Fouraso/person.html', {'form': form})

# def zone(request,):
#     Zone = Zone.objects.all()
#     form = ZoneForm()
#     return render (request, 'Fouraso/zone.html', {'form':form})


def persons_detail(request):
    form = PersonForm()
    return render (request, 'Fouraso/person_detail.html', {'form':form})