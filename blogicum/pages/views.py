from django.shortcuts import render


def about(request):
    """О проекте"""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Правила"""
    template = 'pages/rules.html'
    return render(request, template)
