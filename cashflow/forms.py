from django import forms
from .models import cashFlow
from .models import portfolioManager
from .models import bankAccount

class PMSelectForm(forms.ModelForm):

    class Meta:
        model = portfolioManager
        fields = ('pmName', 'pmAutorPerson',)

class cfForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        pm = kwargs.pop('pm', None)
        super(cfForm, self).__init__(*args, **kwargs)
        pms = portfolioManager.objects.filter(id=pm)
        self.fields['pmId'].choices = [(spm.id, spm.pmName) for spm in pms]
        bacnts = bankAccount.objects.filter(pmId=pms)
        self.fields['baId'].choices = [(ba.id, ba.baName) for ba in bacnts]


    class Meta:
        model = cashFlow
        fields = ('transType', 'cfDate', 'currency', 'pmId', 'baId',)