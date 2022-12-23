from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='Post title', max_length=100)
    content = forms.CharField(label='Your text', required=False,max_length=500,widget=forms.Textarea(attrs={"rows":"5"}))
    img = forms.ImageField(label='Your image',required=False)


