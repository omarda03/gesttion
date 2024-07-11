# deplacement/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
from .models import Chantier, Materiel, Deplacement
from .forms import DeplacementForm

def deplacement_view(request):
    if request.method == 'POST':
        form = DeplacementForm(request.POST)
        if form.is_valid():
            deplacement = form.save(commit=False)

            with transaction.atomic():
                materiel = get_object_or_404(Materiel, id=deplacement.materiel.id)
                chantier_depart = deplacement.chantier_depart
                chantier_destination = deplacement.chantier_destination

                if chantier_depart.quantite < deplacement.quantite:
                    return render(request, 'deplacement_form.html', {
                        'form': form,
                        'error_message': 'Quantité insuffisante dans le chantier de départ.'
                    })

                chantier_depart.quantite -= deplacement.quantite
                chantier_depart.save()

                chantier_destination.quantite += deplacement.quantite
                chantier_destination.save()

                materiel.chantier = chantier_destination
                materiel.save()

                deplacement.save()
                return redirect('deplacement_success')

    else:
        form = DeplacementForm()

    return render(request, 'deplacement_form.html', {'form': form})

def deplacement_success_view(request):
    return render(request, 'deplacement_success.html')

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

def inventaire(request):
    materiel_list = Materiel.objects.all()
    total_ttc = sum(item.prix_total_ttc for item in materiel_list)
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
