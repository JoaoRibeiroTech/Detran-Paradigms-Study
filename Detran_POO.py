import time

class Candidato:
    """
    Representa um candidato no processo de habilitação.
    Armazena informações básicas e o status de aprovação em cada etapa.
    """
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.aprovado_exames_iniciais = False
        self.aprovado_teorico = False
        self.aprovado_pratico = False

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")

class ProcessoHabilitacao:
    """
    Gerencia as etapas do processo de habilitação para um candidato.
    """
    def __init__(self, candidato):
        self.candidato = candidato
        print("--- Bem-vindo(a) ao Processo de Habilitação Simplificado do Detran! ---")
        print("Vamos verificar seu progresso para tirar a CNH.\n")
        print(f"Olá, {self.candidato.nome}! Vamos começar o seu processo.\n")

    def _pausar(self, segundos):
        time.sleep(segundos)

    def etapa_exames_iniciais(self):
        print("##### Etapa 1: Exames Médicos e Psicológicos no Detran #####")
        print("Você precisa fazer e ser aprovado(a) nos exames iniciais.")
        self._pausar(2)

        aprovado_medico = True
        aprovado_psicologico = True

        if aprovado_medico and aprovado_psicologico:
            print(f"Parabéns, {self.candidato.nome}! Você foi APROVADO(A) nos exames médico e psicológico!")
            self.candidato.aprovado_exames_iniciais = True # Atualiza o status do candidato
        else:
            print(f"Ops! {self.candidato.nome}, você não foi aprovado(a) em todos os exames iniciais. Precisa refazê-los.")
            self.candidato.aprovado_exames_iniciais = False

    def etapa_aulas_e_exame_teorico(self):
        # Simula a etapa de aulas e exame teórico
        if not self.candidato.aprovado_exames_iniciais:
            print("\nVocê não pode avançar para as aulas teóricas e exame teórico sem a aprovação inicial.")
            return 

        print("\n##### Etapa 2: Aulas Teóricas na Autoescola e Exame Teórico #####")
        print("Você precisa cursar as aulas teóricas e fazer a prova de legislação no Detran.")
        self._pausar(2)

        print(f"{self.candidato.nome} concluiu as aulas teóricas na autoescola.")
        self._pausar(1.5)

        print("Agora, vamos para o exame teórico no Detran...")
        nota_teorica = int(input("Qual foi sua nota no exame teórico (0 a 30)? "))

        if nota_teorica >= 21:
            print(f"Excelente, {self.candidato.nome}! Você foi APROVADO(A) no exame teórico com nota {nota_teorica}!")
            self.candidato.aprovado_teorico = True # Atualiza o status do candidato
        else:
            print(f"Que pena, {self.candidato.nome}! Você REPROVOU no exame teórico com nota {nota_teorica}. Precisa estudar mais e refazer a prova.")
            self.candidato.aprovado_teorico = False

    def etapa_aulas_e_exame_pratico(self):
        # Simula a etapa de aulas e exame prático
        if not self.candidato.aprovado_teorico:
            print("\nVocê não pode avançar para as aulas práticas e exame prático sem aprovação no exame teórico.")
            return

        print("\n##### Etapa 3: Aulas Práticas de Direção e Exame Prático #####")
        print("Agora é hora de praticar a direção e fazer a prova no Detran.")
        self._pausar(2)

        print(f"{self.candidato.nome} concluiu as aulas práticas na autoescola.")
        self._pausar(1.5)

        print("Chegou o dia do exame prático de direção no Detran...")
        input("Pressione Enter para simular seu desempenho na prova de direção... ")
        resultado_pratico = "aprovado" # Simulação: sempre aprovado no prático

        if resultado_pratico == "aprovado":
            print(f"Muito bem, {self.candidato.nome}! Você foi APROVADO(A) no exame prático de direção!")
            self.candidato.aprovado_pratico = True # Atualiza o status do candidato
        else:
            print(f"Infelizmente, {self.candidato.nome}! Você REPROVOU no exame prático. Precisa de mais aulas e refazer a prova.")
            self.candidato.aprovado_pratico = False

    def etapa_final_emissao_cnh(self):
        # Simula a etapa final de emissão da CNH
        print("\n##### Etapa Final: Emissão da Carteira de Habilitação (CNH) #####")
        if self.candidato.aprovado_exames_iniciais and self.candidato.aprovado_teorico and self.candidato.aprovado_pratico:
            print(f"\nPARABÉNS, {self.candidato.nome}! Com o CPF {self.candidato.cpf}, todos os seus exames estão aprovados!")
            print("Sua Carteira Nacional de Habilitação (CNH) será EMITIDA em breve. Você é um(a) novo(a) motorista!")
        else:
            print(f"\n{self.candidato.nome}, você ainda não cumpriu todos os requisitos para a emissão da CNH.")
            print("Verifique as etapas anteriores para saber o que precisa ser refeito.")
        print("\n--- Fim do Processo de Habilitação Simplificado ---")

# --- Execução do programa ---
if __name__ == "__main__":
    nome = input("Digite o seu nome completo: ")
    cpf = int(input("Digite seu CPF sem os pontos: "))

    # Cria uma instância de Candidato
    candidato1 = Candidato(nome, cpf)

    # Cria uma instância de ProcessoHabilitacao, passando o objeto candidato
    processo = ProcessoHabilitacao(candidato1)

    # Executa as etapas do processo
    processo.etapa_exames_iniciais()
    processo.etapa_aulas_e_exame_teorico()
    processo.etapa_aulas_e_exame_pratico()
    processo.etapa_final_emissao_cnh()