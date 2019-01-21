from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
from . forms import PostModelForm
from . forms import PostDefinitionForm
from django.utils import timezone

# Create your views here.

def index(request):
    context = {}
    posts = Post.objects.all()
    context['Posts'] = posts
    return render(request, 'index.html', context)

def help(request):
        return render('TABANG')


def detail(request, post_id):
    context = {}
    context['post'] = Post.objects.get(id=post_id)
    return render(request, 'detail.html', context)

def update(request,post_id):
    if request.method == 'POST':
         pass
    else:
        post = Post.objects.get(id=post_id)
        context = {}
        context['form'] = PostModelForm(instance=post)
        context['p_id'] = post_id
        return render(request, 'update.html', context)


def create(request):
    context = {}
    form = PostDefinitionForm(initial={"pub_date":timezone.now()})

    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:index')

    return render(request, "create.html", {'form':form})

def comment(request):
    context = {}
    

# Create your views here.
