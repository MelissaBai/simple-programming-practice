def merge_sorted_lists1(lista, listb):
    result = []
    indexa = 0
    indexb = 0

    while indexa < len(lista) and indexb < len(listb):
        if lista[indexa] <= listb[indexb]:
            result.append(lista[indexa])
            indexa += 1
        else:
            result.append(listb[indexb])
            indexb += 1
    if indexa < len(lista):
        result.extend(lista[indexa:])
    if indexb < len(listb):
        result.extend(listb[indexb:])
    return result

def merge_sorted_lists2(lista, listb):
    result = []
    while lista and listb:
        if lista[0] <= listb[0]:
            result.append(lista.pop(0))
        else:
            result.append(listb.pop(0))
    if lista:
        result.extend(lista)
    if listb:
        result.extend(listb)
    return result

print merge_sorted_lists2([1,4,6], [2,7,9])
print merge_sorted_lists2([1,4,6], [])
print merge_sorted_lists2([], [2,7,9])
print merge_sorted_lists2([], [])
