from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader, RequestContext
from DemoDog.models import Article
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from DemoDog.forms import ArticleForm

#def index(request):
#    return HttpResponse('Share')  #None

@csrf_exempt
@login_required
def index(request):
    a = Article.objects.all()
    t = loader.get_template('index.html')
    r = RequestContext(request, {'a': a,})
    return HttpResponse(t.render(r))

@csrf_exempt
def login(request):
    t = loader.get_template('login.html')
    r = RequestContext(request, {})
    return HttpResponse(t.render(r))
    #return HttpResponse('login')

@csrf_exempt
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@csrf_exempt
def authfunc(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/logged_in')
    else:
        return HttpResponseRedirect('/accounts/invalid')

@csrf_exempt
def logged_in(request):
    return HttpResponseRedirect('/')
    #return HttpResponse('logged_in')

@csrf_exempt
def invalid_login(request):
    return HttpResponse('invalid_login')

@csrf_exempt
def enter_article(request):
    if request.method == "GET":
        af = ArticleForm() #instance=obj_article)
        t = loader.get_template('article.html')
        r = RequestContext(request, {'form': af.as_p()})
        return HttpResponse(t.render(r))
    else:
        af = ArticleForm(request.POST)
        if (af.is_valid()):
            new_obj = Article.objects.create(title=af.cleaned_data['title'], body=af.cleaned_data['body'])
        else:
            return HttpResponse('Invalid form')
        return HttpResponseRedirect('/')