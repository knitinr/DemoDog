from django.forms import ModelForm
from DemoDog.models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body'] #'__all__'
        #exclude = []