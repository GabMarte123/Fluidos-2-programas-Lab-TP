#tempo t 
#vel horizontal u
#vel vertical v 
#programa vai ler .txt pegar o primeiro segundo e terceiro valor e fazer a conta

def corrigir_numero(numero):
    if isinstance(numero, str):
        numero = numero.replace(',', '.')
    try:
        return float(numero)
    except ValueError:
        return None


def processar_arquivo(nome_arquivo):
    dados = {"tempo": [], "velocidade_horizontal": [], "velocidade_vertical": []}
    
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            partes = linha.strip().split("\t")  # Divide os números usando TAB
            
            if len(partes) >= 3:  # Garante que há pelo menos 3 números na linha
                try:
                    tempo, vel_h, vel_v = map(corrigir_numero, partes[:3])
                    
                    # Armazena os valores nas listas do dicionário
                    dados["tempo"].append(tempo)
                    dados["velocidade_horizontal"].append(vel_h)
                    dados["velocidade_vertical"].append(vel_v)

                except ValueError:
                    print(f"Erro ao processar linha: {linha.strip()}")
    
    return dados

arq00 = processar_arquivo('00.txt')
arq10 = processar_arquivo('10.txt')
arq20 = processar_arquivo('20.txt')
arq30 = processar_arquivo('30.txt')
arq40 = processar_arquivo('40.txt')
arq50 = processar_arquivo('50.txt')
arq60 = processar_arquivo('60.txt')
arq70 = processar_arquivo('70.txt')
arq80 = processar_arquivo('80.txt')

print('todos os arquivos foram carregados com succsexo ')

def velocidade_instantanea(arq):

    somatoria_v_horizontal = sum(arq["velocidade_horizontal"])/len(arq["velocidade_horizontal"])
    
    somatoria_v_vertical = sum(arq["velocidade_vertical"])/len(arq["velocidade_vertical"])
    
    return f'''A somatória vertical v é: {somatoria_v_vertical}
A somatória horizontal u é: {somatoria_v_horizontal}\n'''

print(f'''arquivo 00.txt:
{velocidade_instantanea(arq00)}''')
print(f'''arquivo 10.txt
{velocidade_instantanea(arq10)}''')
print(f'''arquivo 20.txt:
{velocidade_instantanea(arq20)}''')
print(f'''arquivo 30.txt
{velocidade_instantanea(arq30)}''')
print(f'''arquivo 40.txt:
{velocidade_instantanea(arq40)}''')
print(f'''arquivo 50.txt
{velocidade_instantanea(arq50)}''')
print(f'''arquivo 60.txt:
{velocidade_instantanea(arq60)}''')
print(f'''arquivo 70.txt
{velocidade_instantanea(arq70)}''')
print(f'''arquivo 80.txt
{velocidade_instantanea(arq80)}''')

print('Obrigado por usar este programa')