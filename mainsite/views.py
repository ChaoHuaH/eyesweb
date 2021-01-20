from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime
from .models import Post, Product
import random

# Create your views here.
def homepage(request):
    posts=Post.objects.all()
    now=datetime.now()
    return render(request, 'index.html', locals())

def showpost(request, slug):
    try:
        post=Post.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')

# def about(request):
#     html = '''
# <!DOCTYPE html>
# <html>
# <head><title>About Myself</title></head>
# <body>
# <h2>C.H Huang</h2>
# <hr>
# <p>
# Hi, I am C.H. Huang.
# </p>
# </body>
# </html>
# '''
#     return HttpResponse(html)

def about(request):
    quotes = ['S1',
                'S2',
                'S3',
                'S4']
    quote = random.choices(quotes)
    return render(request, 'about.html', locals())



def listing(request):
    html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>List</title>
</head>
<body>
<h2>Folowing is the list of saling phone</h2>
<hr>
<table width=400 border=1 bgcolor='#ccffcc'>
{}
</table>
</body>
</html>
'''
    products = Product.objects.all()
    tags = '<tr><td>Name</td><td>Price</td></tr>'
    for p in products:
        tags = tags + '<tr><td>{}</td>'.format(p.name)
        tags = tags + '<td>{}</td>'.format(p.price)

    return HttpResponse(html.format(tags))

def disp_detail(request, sku):
    html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset = 'utf-8'>
<title>{}</title>
</head>
<body>
<h2>{}</h2>
<hr>
<table width=400 border=1 bgcolor='#ccffcc'>
{}
</table>
<a href='/list'>Go back to List</a>
</body>
</html>
'''
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404("Can't find the item number")
    tags = '<tr><td>Item number</td><td>{}</td></tr>'.format(p.sku)
    tags = tags + '<tr><td>Item name</td><td>{}</td><tr>'.format(p.name)
    tags = tags + '<tr><td>Price</td><td>{}</td></tr>'.format(p.price)
    return HttpResponse(html.format(p.name, p.name, tags))

# def disp_detail(request, sku):
#     try:
#         p = Product.objects.all(sku=sku)
#     except Product.DoesNotExist:
#         raise Http404("Can't find the item")
#     return render(request, 'disp.html', locals())