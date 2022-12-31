from pacientes.models import Pacientes
import os, django


lista_pacientes = [
    {'nome':'urso','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'javali','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'búfalo','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'guepardo','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'molusco','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'caranguejo','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'lagostim','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'corvo','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'golfinho','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'pomba','cpf': 'não','endereco': 'não','cel': 'sim'},
    {'nome':'pato','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'elefante','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'flamingo','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'pulga','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'rã','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'morcego-da-fruta','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'girafa','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'mosquito','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'bode','cpf': 'não','endereco': 'não','cel': 'sim'},
    {'nome':'gorila','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'gaivota','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'hadoque','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'hamster','cpf': 'não','endereco': 'não','cel': 'sim'},
    {'nome':'falcão','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'abelha','cpf': 'não','endereco': 'sim','cel': 'sim'},
    {'nome':'mosca','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'joaninha','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'leopardo','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'leão','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'lagosta','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'lince','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'salamandra','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'polvo','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'gambá','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'órix','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'avestruz','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'periquito','cpf': 'não','endereco': 'não','cel': 'sim'},
    {'nome':'pinguim','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'faisão','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'pique','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'piranha','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'ornitorrinco','cpf': 'sim','endereco': 'sim','cel': 'não'},
    {'nome':'doninha','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'pónei','cpf': 'não','endereco': 'não','cel': 'sim'},
    {'nome':'toninha','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'puma','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'gato','cpf': 'sim','endereco': 'não','cel': 'sim'},
    {'nome':'guaxinim','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'rena','cpf': 'não','endereco': 'não','cel': 'sim'},
    {'nome':'ema','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'escorpião','cpf': 'sim','endereco': 'sim','cel': 'não'},
    {'nome':'cavalo marinho','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'leão marinho','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'verme','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'lesma','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'pardal','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'esquilo','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'estrela do Mar','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'arraia','cpf': 'sim','endereco': 'sim','cel': 'não'},
    {'nome':'cisne','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'cupim','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'sapo','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'tartaruga','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'tuatara','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'atum','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'abutre','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'vespa','cpf': 'não','endereco': 'sim','cel': 'não'},
    {'nome':'lobo','cpf': 'sim','endereco': 'não','cel': 'não'},
    {'nome':'minhoca','cpf': 'não','endereco': 'não','cel': 'não'},
    {'nome':'carriça','cpf': 'não','endereco': 'não','cel': 'não'}
]

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()


def gerando_pacientes():
    for paciente in lista_pacientes:
        nome = paciente['nome']
        cpf = paciente['cpf']
        endereco = paciente['endereco']
        cel = paciente['cel']
        paciente = Pacientes(nome=nome, cpf=cpf, endereco=endereco, cel=cel)
        paciente.save()


gerando_pacientes()

print('pacientes gerados')
