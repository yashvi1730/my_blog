from django.http import Http404
from django.shortcuts import render,get_object_or_404
from main import models

# Create your views here.

def index(request):
    latest_articles=models.Article.objects.all()
    context={
        "latest_articles":latest_articles
    }
    return render(request,'main/index.html',context)

def article(request,pk):
    article=get_object_or_404(models.Article,pk=pk)

    context={
        "article":article
    }
    return render(request,'main/article.html',context)

def create_article(request):
    context={}
    if request.method=="POST":
       article_data={
           "title":request.POST['title'],
           "content":request.POST['content']
       }
       article=models.Article.objects.create(**article_data)
       context["success"]=True

   
    return render(request,'main/create_article.html',context)