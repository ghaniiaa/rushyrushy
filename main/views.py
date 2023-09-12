from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Vinyl',
        'amount' : '5',
        'description' : 'You have 5 vinyl',
        'category' : 'those are 90s vinyl',
        'price' : '25'
    }

    return render(request, "main.html", context)