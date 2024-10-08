from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as login_django, authenticate
from django.contrib.auth.hashers import make_password, check_password
from pyexpat.errors import messages

from app_cad_usuario.models import Usuario

# View de cadastro
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        nome = request.POST['username']
        email = request.POST['email']
        cpf = request.POST['cpf']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        ddd = request.POST['ddd']
        telefone = ddd + request.POST['telefone']


        if Usuario.objects.filter(email=email).exists():
            erro = "o email inserido ja foi registrado."
            context = {
                'erro': erro
            }
            return render(request, 'cadastroFalha.html', context)


        if Usuario.objects.filter(cpf=cpf).exists():
            erro = "o cpf inserido ja foi registrado."
            context = {
                'erro': erro
            }
            return render(request, 'cadastroFalha.html', context)

        if Usuario.objects.filter(telefone=telefone).exists():
            erro = "o cpf inserido ja foi registrado."
            context = {
                'erro': erro
            }
            return render(request, 'cadastroFalha.html', context)

        if senha == senha2:
            user = Usuario.objects.create(username=nome, cpf=cpf, email=email, password = senha, telefone=telefone)
            user.set_password(senha)
            user.save()
            return render(request, 'login.html')
        else:
            return HttpResponse(f"senhas não compativéis")


# View de login
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST['email']
        password = request.POST['password']

        user = Usuario.objects.filter(email=email).first()
        try:
            if user.check_password(password):
                login_django(request, user)
                return redirect('home')
            else:
                return render(request, 'login_falha.html')
        except Exception as e:
            return render(request, 'login_falha.html')



# View de home
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return HttpResponse("Não autorizado")