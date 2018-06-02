from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()

    word_dict = {}

    for w in word_list:
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1

    sorted_words = sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(word_list),'sorted_words':sorted_words})

def about(request):
    return render(request,'about.html')
