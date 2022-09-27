def peso_congelado(antes_congelar, depois_congelar):    
    nao_congelado = (depois_congelar*100) / antes_congelar 
    peso_agua_congelada = 100 - nao_congelado
    final = f"{peso_agua_congelada:.1f}"
    final = float(final)
    return final
 
def main():
    antes_congelar = float(input())
    depois_congelar = float(input())
    
    qualidade = (peso_congelado(antes_congelar, depois_congelar))
    
    if qualidade < 5:
        qualidade_produto = "Produto qualis A"

    elif qualidade < 10:
        qualidade_produto = "Produto em conformidade"

    else:
        qualidade_produto = "Produto não conforme"

    print(f"{qualidade}% do peso do produto é de água congelada.\n{qualidade_produto}.")

if __name__ == "__main__":
    main()


