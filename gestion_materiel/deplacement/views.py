from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Chantier, Materiel, Deplacement
from .forms import DeplacementForm

# def deplacement_view(request):
#     if request.method == 'POST':
#         form = DeplacementForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('deplacement_success')
#     else:
#         form = DeplacementForm()
#     return render(request, 'deplacement_form.html', {'form': form})

# def deplacement_success_view(request):
#     return render(request, 'deplacement_success.html')

def accueil(request):
    chantier_list = Chantier.objects.all()
    paginator = Paginator(chantier_list, 10)  

    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'accueil.html', {'page_obj': page_obj})

def deplacement(request):
    deplacement_list = Deplacement.objects.all()
    paginator = Paginator(deplacement_list, 10)  

    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'deplacement.html', {'page_obj': page_obj})

def inventaire(request):
    materiel_list = Materiel.objects.all()
    total_ttc = sum(materiel.prix_total_ttc for materiel in materiel_list)
    return render(request, 'inventaire.html', {'materiel_list': materiel_list, 'total_ttc': total_ttc})


def materiel(request):
    materiel_list = Materiel.objects.all()
    paginator = Paginator(materiel_list, 10)  

    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'materiel.html', {'page_obj': page_obj})

def entree(request):
    return render(request, 'materiel.html')
