from django import forms
from .models import stock
from .models import stockPFDates

class stocksForm(forms.ModelForm):

    class Meta:
        model = stock
        fields = ('stockName', 'issuer', 'NYSEexchCode', 'NASDAQexchCode', 'otherExchCode', 'sType', 'nominalAndCurrency',
                  'issuedPr', 'cuponsCount', 'cuponPr', 'accruedInterest')
        labels = {
            'stockName': ('Stock:'),
            'issuer': ('Issuer:'),
            'NYSEexchCode': ('NYSE:'),
            'NASDAQexchCode': ('NASDAQ:'),
            'otherExchCode': ('Other:'),
            'sType': ('Stock type:'),
            'nominalAndCurrency': ('Nominal and currency'),
            'issuedPr': ('Percent'),
            'cuponsCount': ('cupons count:'),
            'cuponPr': ('Cupon percent:'),
            'accruedInterest': ('Accrued interest:')
        }

class stocksPFForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        sId = kwargs.pop('sId', None)
        stk = stock.objects.filter(id=sId)
        super(stocksPFForm, self).__init__(*args, **kwargs)
        self.fields['stockId'].choices = [(st.id, st.stockName) for st in stk]

    class Meta:
        model = stockPFDates
        fields = ('stockId', 'pfDate')