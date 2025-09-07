from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'Match Attax Store',
        'name': 'Aryandana Pascua Patiung',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)