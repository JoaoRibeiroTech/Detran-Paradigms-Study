# 🚦 Sistema Detran: Simulação de Processo de Habilitação (Python)

Este repositório apresenta um sistema de simulação do processo de habilitação do Detran, desenvolvido para fins acadêmicos. O objetivo principal é demonstrar a aplicação de dois paradigmas de programação fundamentais em **Python**: o **Estruturado (Procedural)** e o **Orientado a Objetos (POO)**.

## 📌 Sobre o Projeto

O software simula as etapas reais para a obtenção da Carteira Nacional de Habilitação (CNH), incluindo validações de nota e pré-requisitos para avançar entre as fases.

### Funcionalidades Implementadas:
* **Cadastro de Candidato**: Registro de nome e CPF.
* **Etapa 1 (Saúde)**: Simulação de aprovação em exames médicos e psicológicos.
* **Etapa 2 (Legislação)**: Realização de aulas teóricas e prova de legislação com exigência de nota mínima de 21 pontos (escala 0-30).
* **Etapa 3 (Prática)**: Simulação de aulas de direção e exame prático final.
* **Etapa Final (Emissão)**: Verificação de todos os status para emissão da CNH.

---

## 📂 Estrutura do Repositório

O projeto está dividido em dois arquivos principais para fins comparativos:

1.  **`Detran_estruturado.py`**: Implementação baseada em lógica sequencial, utilizando variáveis de controle e estruturas de decisão diretas.
2.  **`Detran_POO.py`**: Implementação modular utilizando classes. Inclui a classe `Candidato` para gerenciamento de estado e a classe `ProcessoHabilitacao` para gerenciamento das regras de negócio.

---

## 🛠️ Comparação de Paradigmas

| Característica | Versão Estruturada | Versão POO |
| :--- | :--- | :--- |
| **Organização** | Fluxo linear e procedural. | Baseada em objetos e métodos. |
| **Estado** | Armazenado em variáveis locais. | Armazenado em atributos da classe `Candidato`. |
| **Escalabilidade** | Ideal para scripts rápidos. | Facilita a manutenção e expansão do sistema. |

---

## 🚀 Como Executar

Certifique-se de ter o Python 3.x instalado.

1. Clone este repositório:
   ```bash
   git clone [https://github.com/JoaoRibeiroTech/Trabalho_Academico_Detran.git](https://github.com/JoaoRibeiroTech/Trabalho_Academico_Detran.git)
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd Trabalho_Academico_Detran
   ```

3. Execute a versão desejada:
   ```bash
   # Para testar a versão Estruturada
   python Detran_estruturado.py

   # Para testar a versão Orientada a Objetos
   python Detran_POO.py
   ```

---

## 👨‍💻 Autor

**João Ribeiro** GitHub: [@JoaoRibeiroTech](https://github.com/JoaoRibeiroTech)

---
*Este projeto foi desenvolvido como parte de um estudo sobre paradigmas de programação.*
