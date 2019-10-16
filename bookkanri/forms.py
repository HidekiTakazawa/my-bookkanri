from django import forms
class BookDataForm(forms.Form):

    jyanru = forms.CharField(
        label='ジャンル',
        max_length=20,
        required=True
    )
    bookname = forms.CharField(
        label='タイトル',
        max_length=100,
        widget=forms.TextInput(attrs={'size':'40'}),
        required=True
    )
    
    author = forms.CharField(
        label='著者',
        max_length=100,
        widget=forms.TextInput(attrs={'size':'40'}),
        required=True
    )
    publisher = forms.CharField(
        label='出版社',
        max_length=200,
        widget=forms.TextInput(attrs={'size':'40'}),
        required=True
    )
    purchase_date = forms.DateField(
        label='購入日',
        widget=forms.DateInput(attrs={"type":"date"}),
        required=False
    )
    price = forms.IntegerField(
        label='購入価格',
        min_value=0,
        max_value=999999,
        
        required=True
    )
    memo = forms.CharField(
        label='メモ',
        max_length=200,
        widget=forms.TextInput(attrs={'size':'100'}),
        required=False
    )
