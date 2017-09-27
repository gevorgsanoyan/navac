from django.shortcuts import render
from .models import stock
from .models import stockPFDates
from .forms import stocksForm
from .forms import stocksPFForm
from django.shortcuts import redirect
#from django.shortcuts import get_object_or_404

# Create your views here.

def stocklist(request):
    s = stock.objects.all()
    return render(request, 'stock/stocklist.html', {'stock':s})

def stocknew(request):
    if request.method == "POST":
        form = stocksForm(request.POST)
        if form.is_valid():
            s = form.save(commit=False)
            s.imUser = request.user
            s.save()
            return redirect('stlist')
        else:
            return render(request, 'cashflow/errorpage.html', {'errT': "error saving stock"})
    else:
        s = stocksForm()
        return render(request, 'stock/stockinput.html', {'stockform': s})



def stockedit(request, sId):
    s = stock.objects.get(id=sId)
    sform = stocksForm(request.POST or None, instance=s)
    if sform.is_valid():
        s = sform.save(commit=False)
        s.imUser = request.user
        s.save()
        return redirect('stlist')

    return render(request, 'stock/stockinput.html', {'stockform': sform})

def stockPFList(request, sId):
    s = stock.objects.get(id=sId)
    spf = stockPFDates.objects.filter(stockId=s)
    return render(request, 'stock/stockspflist.html', {'sPF': spf})


def stockPFDatesInput(request, sId):
    if request.method == "POST":
        form = stocksPFForm(request.POST, sId=sId)
        if form.is_valid():
            s = form.save(commit=False)
            s.imUser = request.user
            s.save()
            return redirect('spflist', sId=sId)
        else:
            return render(request, 'cashflow/errorpage.html', {'errT': "error saving stock pf dates"})
    else:
        spfForm = stocksPFForm(sId=sId)
        return render(request, 'stock/stockpfinput.html', {'pfform': spfForm})

def stockPFDatesEdit(request, spfId):
    spf = stockPFDates.objects.get(id=spfId)
    pfForm = stocksPFForm(request.POST or None, instance=spf, sId=spf.stockId.id)
    if pfForm.is_valid():
        spf = pfForm.save(commit=False)
        spf.save()
        return redirect('spflist', sId=spf.stockId.id)

    return render(request, 'stock/stockpfinput.html', {'pfform': pfForm})