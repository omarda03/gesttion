from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Chantier, Materiel, Deplacement
from .forms import DeplacementForm

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

    if request.method == 'POST':
        form = DeplacementForm(request.POST)
        if form.is_valid():
            try:
                print('Tentative de sauvegarde du déplacement')
                form.save()
                messages.success(request, 'Le déplacement a été effectué avec succès.')
            except ValidationError as e:
                messages.error(request, str(e))
            except ValueError as e:
                messages.error(request, str(e))
        else:
            messages.error(request, 'Erreur lors de la validation du formulaire.')
    else:
        form = DeplacementForm()

    return render(request, 'accueil.html', {'page_obj': page_obj, 'form': form})

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

def materiaux_par_chantier(request, chantier_id):
    chantier = get_object_or_404(Chantier, id=chantier_id)
    materiaux = Materiel.objects.filter(chantier=chantier)
    deplacements = Deplacement.objects.filter(chantier_destination=chantier)
    return render(request, 'materiaux_par_chantier.html', {
        'chantier': chantier,
        'materiaux': materiaux,
        'deplacements': deplacements
    })