from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

# Create your views here.


def index(request):
    # contatos = Contato.objects.all()
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 3)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    # try:
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)
    if contato.mostrar:
        return render(request, 'contatos/ver_contato.html', {
            'contato': contato
        })
    else:
        raise Http404()
    # except Contato.DoesNotExist:
    #     raise Http404()


def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'Campo de busca não pode ficar vazio.')
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')
    # contatos = Contato.objects.order_by('-id').filter(
    #     Q(nome__icontains=termo) |
    #     Q(sobrenome__icontains=termo),
    #     mostrar=True,
    # )
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        nome_completo__icontains=termo
    )
    paginator = Paginator(contatos, 3)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
