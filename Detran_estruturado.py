import time 

print("--- Bem-vindo(a) ao Processo de Habilitação Simplificado do Detran! ---")
print("Vamos verificar seu progresso para tirar a CNH.\n")

nome_candidato = input("Digite o seu nome completo: ")
cpf_candidato = int(input("Digite seu CPF sem os pontos: "))

print(f"\nOlá, {nome_candidato}! Vamos começar o seu processo.\n")

print("##### Etapa 1: Exames Médicos e Psicológicos no Detran #####")
print("Você precisa fazer e ser aprovado(a) nos exames iniciais.")
time.sleep(2)

aprovado_medico = True
aprovado_psicologico = True 

if aprovado_medico and aprovado_psicologico: 
    print(f"Parabéns, {nome_candidato}! Você foi APROVADO(A) nos exames médico e psicológico!")
    pode_avancar_para_aulas = True 
else: 
    print(f"Ops! {nome_candidato}, você não foi aprovado(a) em todos os exames iniciais. Precisa refazê-los.")
    pode_avancar_para_aulas = False

if pode_avancar_para_aulas: 
    print("\n##### Etapa 2: Aulas Teóricas na Autoescola e Exame Teórico #####")
    print("Você precisa cursar as aulas teóricas e fazer a prova de legislação no Detran.")
    time.sleep(2) 

    print(f"{nome_candidato} concluiu as aulas teóricas na autoescola.")
    time.sleep(1.5)

    print("Agora, vamos para o exame teórico no Detran...")
    nota_teorica = int(input("Qual foi sua nota no exame teórico (0 a 30)? ")) 

    if nota_teorica >= 21:
        print(f"Excelente, {nome_candidato}! Você foi APROVADO(A) no exame teórico com nota {nota_teorica}!")
        pode_avancar_para_pratica = True 
    else: 
        print(f"Que pena, {nome_candidato}! Você REPROVOU no exame teórico com nota {nota_teorica}. Precisa estudar mais e refazer a prova.")
        pode_avancar_para_pratica = False 

else: 
    print("\nVocê não pode avançar para as aulas teóricas e exame teórico sem a aprovação inicial.")
    pode_avancar_para_pratica = False

if pode_avancar_para_pratica: 
    print("\n##### Etapa 3: Aulas Práticas de Direção e Exame Prático #####") 
    print("Agora é hora de praticar a direção e fazer a prova no Detran.")
    time.sleep(2)

    print(f"{nome_candidato} concluiu as aulas práticas na autoescola.")
    time.sleep(1.5)

    print("Chegou o dia do exame prático de direção no Detran...") 
    input("Pressione Enter para simular seu desempenho na prova de direção... ") 
    resultado_pratico = "aprovado"

    if resultado_pratico == "aprovado":
        print(f"Muito bem, {nome_candidato}! Você foi APROVADO(A) no exame prático de direção!")
        pode_emitir_cnh = True
    else:
        print(f"Infelizmente, {nome_candidato}! Você REPROVOU no exame prático. Precisa de mais aulas e refazer a prova.") 
        pode_emitir_cnh = False
else: 
    print("\nVocê não pode avançar para as aulas práticas e exame prático sem aprovação no exame teórico.") 
    pode_emitir_cnh = False 

print("\n##### Etapa Final: Emissão da Carteira de Habilitação (CNH) #####") 
if pode_emitir_cnh:
    print(f"\nPARABÉNS, {nome_candidato}! Com o CPF {cpf_candidato}, todos os seus exames estão aprovados!") 
    print("Sua Carteira Nacional de Habilitação (CNH) será EMITIDA em breve. Você é um(a) novo(a) motorista!") 
else:
    print(f"\n{nome_candidato}, você ainda não cumpriu todos os requisitos para a emissão da CNH.") 
    print("Verifique as etapas anteriores para saber o que precisa ser refeito.") 
print("\n--- Fim do Processo de Habilitação Simplificado ---") 