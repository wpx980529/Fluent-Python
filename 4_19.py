import locale
print(locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8'))
fruits = ['caju', 'atemoia', 'caja', 'acai', 'acerola']
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)