from django.shortcuts import render


def dashboard(request):
    return render(request, 'cryptopilot/dashboard.html')


def price_history(request):
    return render(request, 'cryptopilot/price_history.html')
