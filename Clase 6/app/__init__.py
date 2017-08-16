# import re
#
# texto1 = 'casa'
# texto2 = 'casas'
# texto3 = 'pasa'
#
# if re.match(texto1, texto2):
#     print("t1 y t2 coinciden")
# else:
#     print("t1 y t2 no coinciden")
#
# if re.match(".asa", texto1):
#     print("t1 termina en asa")
#
# if re.match("\.mp4", input("Archivo")):
#     print("Perfecto")
# else:
#     print("No me funciona")
#
# archivos =   ['jpg','mp3','png']
# for archivo in archivos:
#     if re.match('jpg|png|gif|bmp', archivo):
#         print("Es una imagen")
#     else:
#         print("Formato invalido")

#..............................................

# import re
#
# if re.match("ca[0-5a-z][.:]", input(">  ")):
#     print("Salsa!")

# if re.match("ca(..|...)ta", input("> ")):
#     print("Valido")
# else:
#     print("Invalido")

#................................................................................................

#re.search
import re
if re.match("c(...|..)*a[a-z]?\s[A-Z]{1,4}", input("> ")):
    print("Valido")

if re.search("^ftp://", input("> ")):
    print("Valido")

if re.search(".com$", input("> ")):
    print("Valido")