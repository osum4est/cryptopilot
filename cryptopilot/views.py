from django.shortcuts import render


def dashboard(request):
    return render(request, 'cryptopilot/dashboard.html')


def simulation(request):
    return render(request, 'cryptopilot/simulation.html')


def simulate(request, trader_id):
    return render(request, 'cryptopilot/simulate.html')


def data_loader(request):
    return render(request, 'cryptopilot/data_loader.html')
