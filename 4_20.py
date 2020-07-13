import pyuca
coll = pyuca.Collator()
fruits = ['caju', 'atemoia', 'caja', 'acai', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)
print(sorted_fruits)