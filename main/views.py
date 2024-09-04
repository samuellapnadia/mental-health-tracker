from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306170446',
        'name': 'Samuella Putri Nadia Pauntu',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)