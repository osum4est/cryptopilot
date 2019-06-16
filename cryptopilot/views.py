from django.shortcuts import render


def dashboard(request):
    return render(request, 'cryptopilot/dashboard.html')


def simulation(request):
    return render(request, 'cryptopilot/simulation.html')


def data_loader(request):
    return render(request, 'cryptopilot/data_loader.html')
