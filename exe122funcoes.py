def lascado(divida, tempo, taxa):
    total = 0
    
    juros = divida * tempo * taxa
    total = divida + juros

    print(f"Total é {total}")
    