from django.shortcuts import render, redirect
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import BookData
from .forms import BookDataForm
def index(request):
    latest_bookdata_list = BookData.objects.order_by('bookname')[:10]
    template = loader.get_template('bookkanri/index.html')
    context = {
        'latest_bookdata_list': latest_bookdata_list
    }
    
    return HttpResponse(template.render(context, request))
def bookNew(request):
    f = BookDataForm()
    return render(request, 'bookkanri/bookNew.html', {'form1': f})
    
def bookNewSave(request):
    f = BookDataForm(request.POST or None)
    if f.is_valid():
        bookdata = BookData()
        bookdata.jyanru = f.cleaned_data['jyanru']
        bookdata.bookname = f.cleaned_data['bookname']
        bookdata.author = f.cleaned_data['author']
        bookdata.publisher = f.cleaned_data['publisher']
        bookdata.purchase_date = f.cleaned_data['purchase_date']
        bookdata.price = f.cleaned_data['price']
        bookdata.memo = f.cleaned_data['memo']
        bookdata.save()
        
        return redirect('index')
    #return 'valid error'
    return render(request, 'bookkanri/bookNew.html', {'form1': f})
def bookUpdate(request, bookdata_id):
    updateMSG = '変更します。'
    bookdata = BookData.objects.get(id=bookdata_id)
    if request.method == 'POST':
        f = BookDataForm(request.POST)
        if f.is_valid():
            
            bookdata.bookname = f.cleaned_data['bookname']
            bookdata.author = f.cleaned_data['author']
            bookdata.publisher = f.cleaned_data['publisher']
            bookdata.purchase_date = f.cleaned_data['purchase_date']
            bookdata.price = f.cleaned_data['price']
            bookdata.memo = f.cleaned_data['memo']
            bookdata.save()
            return redirect('index')
        else:
            return render(request, 'bookUpdate.html', {'form1': f, 'updateMSG': updateMSG})

    else:
        f = BookDataForm({
            'jyanru': bookdata.jyanru,
            'bookname': bookdata.bookname,
            'author': bookdata.author,
            'publisher': bookdata.publisher,
            'purchase_date': bookdata.purchase_date,
            'price': bookdata.price,
            'memo': bookdata.memo


        })
    
    
    
    return render(request, 'bookkanri/bookUpdate.html', {'form1': f, 'updateMSG': updateMSG })

def bookDelete(request, bookdata_id):
    updateMSG = '削除します。'
    bookdata = BookData.objects.get(id=bookdata_id)
    if request.method == 'POST':
        f = BookDataForm(request.POST)
        bookdata.delete()
        return redirect('index')
    
    else:
        f = BookDataForm({
            'jyanru': bookdata.jyanru,
            'bookname': bookdata.bookname,
            'author': bookdata.author,
            'publisher': bookdata.publisher,
            'purchase_date': bookdata.purchase_date,
            'price': bookdata.price,
            'memo': bookdata.memo


        })
    
    
    
    return render(request, 'bookkanri/bookUpdate.html', {'form1': f, 'updateMSG': updateMSG })

    