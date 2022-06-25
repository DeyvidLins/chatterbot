import direciona_sites
import reconhecimento_rosto
import inicia_programas
import agenda_horario

# Invoca às classes e as ações dela
def invoke_acoes(texto):
    #Chama à classe Sites
    sites = direciona_sites.Sites(texto)
    sites.direcionar_sites()

    # Chama à classe Reconhecimento
    reconhecimento_facial = reconhecimento_rosto.Reconhecimento(texto)
    reconhecimento_facial.reconhecimento_facial()

    # Chama à classe Programas
    start_programas = inicia_programas.Programas(texto)
    start_programas.start_programas()

    # Chama à classe Agenda
    agenda = agenda_horario.Agenda(texto)
    agenda.verificar_horario()