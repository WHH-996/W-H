from django.shortcuts import render, reverse, redirect
from .models import Vote, Option


# Create your views here.
def index(resquest):
    q1 = Vote.objects.all()
    return render(resquest, 'index.html', {"q1": q1})


def detail(resquest, voteid):
    answer = Vote.objects.get(id=voteid)
    return render(resquest, 'detail.html', {'answer': answer})


def result(request, voteid):
    vote = Vote.objects.get(id=voteid)
    if request.method == 'POST':
        optionid = request.POST.get("content")
        option = Option.objects.get(id=optionid)
        option.num = option.num + 1
        option.save()
        url = reverse('vote:result', args=(voteid,))
        return redirect(to=url)
    elif request.method == 'GET':
        return render(request, 'result.html', {'vote': vote})
