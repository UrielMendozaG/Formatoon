string = """asdadasada/n/nasadsaadadadsadadasdasdassdsadasdsa/n
         asdadadsadsasdsadasdadssadasdadsadas/nnasadsaadadadsadadasdasdassdsadasdsa/n
         asdadadsadsasdsadasdadssadasdadsadas/nnasadsaadadadsadadasdasdassdsadasdsa/n
         asdadadsadsasdsadasdadssadasdadsadas/n"""


x = string.split("/n")

for item in x:
    if item != "":
        print(item.strip())