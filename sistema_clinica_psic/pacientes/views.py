from django.shortcuts import render, redirect
from .models import Pacientes, Tarefas, Consultas, Visualizacoes
from django.contrib import messages
from django.contrib.messages import constants
from django.http import Http404

def pacientes(request):
    if request.method == 'GET':
        pacientes = Pacientes.objects.all()
        queixas = Pacientes.queixa_choices
        return render(request,'pacientes.html', {'queixas': queixas,'pacientes':pacientes})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        queixa = request.POST.get('queixa')
        foto = request.FILES.get('foto')

        if len(nome.strip()) == 0 or not foto:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('pacientes')

        paciente = Pacientes(
            nome=nome,
            email=email,
            telefone=telefone,
            queixa=queixa,
            foto=foto
        )

        paciente.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!')
        return redirect('pacientes') 
    
def paciente_view(request, id):
    paciente = Pacientes.objects.get(id=id)
    if request.method == 'GET':
        tarefas = Tarefas.objects.all()
        consultas = Consultas.objects.filter(paciente=paciente)
        tuple_grafico = ([str(i.data) for i in consultas], [str(i.humor) for i in consultas]) #forma resumida
        
        """consultas_list = []
         for i in consultas:
            consultas_list.append(str(i.data))
        humor_list = []
        for i in consultas:
            humor_list.append(i)

        tuple_grafico = (consultas_list, humor_list) """

        return render(request,'paciente.html', {'paciente':paciente, 'tarefas': tarefas, 'consultas': consultas, 'tuple_grafico' : tuple_grafico })
    
    elif request.method == 'POST':
        humor = request.POST.get('humor')
        registro_geral = request.POST.get('registro_geral')
        video = request.FILES.get('video')
        tarefa = request.POST.getlist('tarefas')

        consultas = Consultas(
            humor = int(humor),
            registro_geral = registro_geral,
            video = video,
            paciente = paciente
        )
        consultas.save()

        for i in tarefas:
            tarefa=Tarefas.objects.get(id=i)
            consultas.tarefas.add(tarefa)
        consultas.save()
        messages.add_message(request, constants.SUCCESS, 'Registro de consulta adicionado com sucesso.')
        return redirect(f'/pacientes/{id}')

def atualizar_paciente(request, id):
    pagamento_em_dia = request.POST.get('pagamento_em_dia')
    paciente = Pacientes.objects.get(id=id)

    #if pagamento_em_dia == 'ativo':
        #paciente.pagamento_em_dia = True
    #else:
        #paciente.pagamento_em_dia = False 
    status = True if pagamento_em_dia == 'ativo' else False
    paciente.pagamento_em_dia = status
    paciente.save()

    return redirect(f'/pacientes/{id}')

def excluir_consulta(request, id):
    consulta = Consultas.objects.get(id=id)
    consulta.delete()
    return redirect(f'/pacientes/{consulta.paciente.id}')

def consulta_publica(request, id):
    consulta = Consultas.objects.get(id=id)
    view = Visualizacoes(
        consulta=consulta,
        ip=request.META['REMOTE_ADDR']
    )
    view.save()

    if not consulta.paciente.pagamento_em_dia:   #condição para poder ter acesso ao conteudo
        raise Http404()
    return render(request, 'consulta_publica.html',{'consulta': consulta})


