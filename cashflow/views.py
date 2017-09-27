from django.shortcuts import render
from .models import cashFlow
from .models import portfolioManager
from .forms import cfForm
from django.shortcuts import redirect
from .forms import PMSelectForm
# Create your views here.

def cflist(request):
    cf = cashFlow.objects.all()
    return render(request, 'cashflow/cflist.html', {'cflist':cf})

def showPMList(request):
    pmList = portfolioManager.objects.all()
    return render(request, 'cashflow/pmlist.html', {'pmList': pmList})

def cfInput(request, pmId):
    if request.method == "POST":
        form = cfForm(request.POST,pm=pmId)
        if form.is_valid():
            pcf = form.save(commit=False)
            pcf.save()
            return redirect('cflist')
        else:
            return render(request, 'cashflow/errorpage.html', {'errT': "error saving cashflow"})
    else:
        cf = cfForm(pm = pmId)
        return render(request, 'cashflow/cfinput.html', {'cfForm':cf})