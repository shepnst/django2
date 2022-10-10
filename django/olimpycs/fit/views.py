from django.shortcuts import render
from fit.models import Olimp

def olimp_list(request):
    olimps = Olimp.objects.all()
    s=[]
    for olimp in olimps:
        if 'инф' or 'мета' in olimp.tegs:
            s.append(olimp)


    return render(request, 'fit/olimp_list.html', {'s': s})
 
