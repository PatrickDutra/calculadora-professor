
import streamlit as st

class Turma:
    def __init__(self, nome, numero_aulas, numero_alunos):
        self.nome = nome
        self.numero_aulas = numero_aulas
        self.numero_alunos = numero_alunos

def calcular_salario_total(valor_base_aula, numero_aulas, turmas, fator_adicional):
    salario_base = valor_base_aula * numero_aulas
    adicional = sum(t.numero_aulas * t.numero_alunos * fator_adicional for t in turmas)
    return salario_base + adicional

st.title("💼 Calculadora de Remuneração de Professores")

# Entrada dos dados principais
valor_base_aula = st.number_input("Valor base por aula (VA)", min_value=0.0, step=1.0, value=50.0, format="%.2f")
numero_total_aulas = st.number_input("Número total de aulas ministradas (NA)", min_value=0, step=1, value=20)
fator_adicional = st.number_input("Fator adicional por aluno (FA)", min_value=0.0, step=0.5, value=2.0, format="%.2f")

numero_turmas = st.number_input("Número total de turmas (NT)", min_value=1, step=1, value=2)

turmas = []
for i in range(numero_turmas):
    st.subheader(f"Turma {i+1}")
    nome = st.text_input(f"Nome da turma {i+1}", value=f"Turma {i+1}")
    numero_aulas = st.number_input(f"Número de aulas na turma {i+1}", min_value=0, step=1, value=10, key=f"aulas_{i}")
    numero_alunos = st.number_input(f"Número de alunos na turma {i+1}", min_value=0, step=1, value=20, key=f"alunos_{i}")
    turmas.append(Turma(nome, numero_aulas, numero_alunos))

if st.button("Calcular Salário"):
    salario = calcular_salario_total(valor_base_aula, numero_total_aulas, turmas, fator_adicional)
    st.success(f"💰 Salário total do professor: R$ {salario:.2f}")
