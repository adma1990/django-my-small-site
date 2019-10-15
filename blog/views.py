from django.shortcuts import render
from django.shortcuts import redirect
from .forms import PostForm
from .models import *



# Create your views here.
def index(request):
    images = CaruselImage.objects.all()
    context = {'images': images}
    return render (request, 'blog/index.html', context)



def product(request, slug):
    product = Mag.objects.get(slug__iexact=slug)
    context = {'product': product}
    return render (request, 'blog/product.html', context)

def katalog(request):
    mags = Mag.objects.all()
    context = {'mags': mags}
    return render (request, 'blog/katalog.html', context)

def contacts(request):

    return render (request, 'blog/contacts.html')


def form(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form')
    else:
        form = PostForm()

    posts = Post.objects.all()
    context = {
    'form': form,
    'posts': posts
     }
    return render (request, 'blog/form.html', context)


def delivery(request):
    return render (request, 'blog/delivery.html')
