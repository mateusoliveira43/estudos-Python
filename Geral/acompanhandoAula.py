# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:31:18 2020

@author : Mateus
"""
# Arquivo para usar durante uma aula qualquer e acompanhar as instruções do
# professor ao vivo.

# django-admin startproject nome_do_projeto
# python.exe manage.py startapp nome_do_app
# FAZER PASTA templates -> PASTA nome_do_app -> ARQUIVO index.html
# python.exe manage.py runserver

# Criar pasta nome_pasta para salvar home e arquivo base .html
# Em settings, TEMPLATES, DIRS : os.path.join(BASE_DIR, 'nome_pasta')
# {%extends 'nome_arquivo_base.html'%}
# {%block 'titulo'%}Título{%endblock%}
# {%block 'conteudo'%}Conteúdo{%endblock%}

# Criar pasta static -> pasta nome_app -> jogar estáticos ali
# {% load static %}
# Nos locais do código
# {% static 'endereco'%}

# urlpatterns, em path adicionar name='referencia', podemos referenciar na base html da seguinte forma
# {% url 'referencia' %}, na referência do arquivo (href)

# Base de dados
# python.exe manage.py makemigrations
# python.exe manage.py migrate

# Cria um usuário com acesso a tudo
# python.exe manage.py createsuperuser

# https://docs.djangoproject.com/en/2.2/topics/pagination/

# Para edição do site é aconselhável fazer backups do projeto
# Basta salvar as pastas e arquivos dentro de outra pasta (sugestão nome: backup nome_projeto dia/ versão X)
# Caso use virtual env (venv), esta é a única pasta que não deve ser copiada no backup
