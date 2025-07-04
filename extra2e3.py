gigabytes = float(input("Valor Gigabytes "))

megabytes = 0
kilobytes = 0

megabytes = gigabytes * 1024
kilobytes = gigabytes * 1024 * 1024

print(f"O tamaho do arquivo em Megabytes é {megabytes} e o tamanho em Kilobytes é {kilobytes}")