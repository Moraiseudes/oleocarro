# INFORME O ANO DO VEÍCULO A PARTIR DO ANO DE FABRICAÇÃO
tipos_oleo = ["", "MINERAL", "SEMISSINTÉTICO", "SINTÉTICO"]

# SOLICITA AO USUÁRIO ANO DE FABRICAÇÃO DE VEÍCULO
def obter_ano_fabricacao():
    while True:
        ano_veiculo = int(input("Informe o ano de fabricação do veículo (ex: 2018) ou digite 0 para sair: "))
        if ano_veiculo == 0:
            return None
        elif 1966 <= ano_veiculo <= 2023:
            return ano_veiculo
        else:
            print("DIGITE UM ANO VÁLIDO")

# DETERMINA ÓLEO RECOMENDADO A PARTIR DO ANO
def determinar_tipo_oleo(ano_veiculo):
    if 1966 <= ano_veiculo <= 2002:
        return tipos_oleo[1]
    elif 2003 <= ano_veiculo <= 2016:
        return tipos_oleo[2]
    elif 2017 <= ano_veiculo <= 2023:
        return tipos_oleo[3]
    else:
        return tipos_oleo[0]

# FUNÇÃO KM ATUAL X KM PRÓXIMA TROCA
def obter_km_atual():
    return int(input("Informe KM atual do veículo (ex: 24000): "))

# FUNÇÃO DE CALCULAR A PRÓXIMA QUILOMETRAGEM DE TROCA DE ÓLEO
def calcular_km_proxima_troca(km_atual, tipo_oleo):
    quilometragem_recomendada = 7000 if tipo_oleo == "MINERAL" or tipo_oleo == "" else 10000
    return km_atual + quilometragem_recomendada

# FUNÇÃO DE BLOCO PRINCIPAL
def main():
    while True:
        ano_veiculo = obter_ano_fabricacao()
        if ano_veiculo is None:
            break  # Sai do loop se o usuário escolher sair
        tipo_oleo = determinar_tipo_oleo(ano_veiculo)
        km_atual = obter_km_atual()
        km_troca = calcular_km_proxima_troca(km_atual, tipo_oleo)

        # Imprime o tipo de óleo recomendado e a quilometragem da próxima troca
        print(f"ÓLEO RECOMENDADO: {tipo_oleo}")
        print(f"PRÓXIMA TROCA: {km_troca}")
        print("TROCA DE ÓLEO GRÁTIS EM EUZINO AUTO PEÇAS E SERVIÇOS!!!")
        print("3324-2393")

# FUNÇÃO DE EXECUÇÃO DO PROGRAMA
if __name__ == "__main__":
    main()



