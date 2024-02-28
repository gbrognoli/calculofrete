import math

def calcular_viagens(objetivo_faturamento_semanal, objetivo_toneladas_dia, preco_por_tonelada, capacidade_por_viagem):
    toneladas_semana = objetivo_faturamento_semanal / preco_por_tonelada
    viagens_semana = math.ceil(toneladas_semana / capacidade_por_viagem)

    toneladas_mes = toneladas_semana * 4
    viagens_mes = math.ceil(toneladas_mes / capacidade_por_viagem)

    return viagens_semana, viagens_mes

def main():
    preco_por_tonelada = 55  # Preço médio por tonelada
    capacidade_por_viagem = 50  # Capacidade de toneladas por viagem

    objetivo_faturamento_semanal = float(input("Digite o objetivo de faturamento total por semana: "))
    objetivo_toneladas_dia = float(input("Digite o objetivo de toneladas por dia: "))

    viagens_semana, viagens_mes = calcular_viagens(objetivo_faturamento_semanal, objetivo_toneladas_dia, preco_por_tonelada, capacidade_por_viagem)

    print("\nPara atingir o objetivo de faturamento total por semana de R$", objetivo_faturamento_semanal)
    print("e o objetivo de", objetivo_toneladas_dia, "toneladas por dia:\n")
    print("Número de viagens necessárias por semana:", viagens_semana)
    print("Número de viagens necessárias por mês:", viagens_mes)

if __name__ == "__main__":
    main()
