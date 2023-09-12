from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Ghania Larasati Nurjayadi Putri',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)