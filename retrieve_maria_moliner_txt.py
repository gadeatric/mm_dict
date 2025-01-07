import os
import requests

# definimos el path en el que guardaremos el diccionario:
DICT_PATH = './diccionario_txt/'

# descargamos el archivo en txt. P.D: GRACIAS INTERNET ARCHIVE!!!!!!!!:

txt_url = "https://archive.org/stream/diccionario-de-uso-del-espanol-maria-moliner/Diccionario%20de%20uso%20del%20espanol%20-%20Maria%20Moliner_djvu.txt"

local_copy = "maria_moliner_dict_raw.txt"

data = requests.get(txt_url)

# guardamos una copia:
with open(local_copy, 'wb') as file:
    if not os.path.exists(DICT_PATH):
        os.makedirs(DICT_PATH)
    file.write(DICT_PATH + data.content)

# depuramos la copia: 
with open(DICT_PATH + "maria_moliner_dict.txt", "r") as mmtxt:
    """
    Revisando el archivo de txt, se observa que el diccionario y sus definiciones empiezan a partir de los caracteres "XXIII" y acaba cuando empieza el apéndice, precedido por el string "APÉNDICE".

    Por lo tanto, para optimizar los recursos, solo recogeremos el texto contenido entre ambos caracteres.
    """

    marmol = mmtxt.read()
    
    start_index = marmol.find("XXIII")
    end_index = marmol.find("APÉNDICE")

    marmol = marmol[start_index:end_index]
    
# guardamos el archivo que solamente contiene el diccionario:

with open(DICT_PATH + 'maria_moliner_only_dict.txt', 'w') as mm_save:
    mm_save.write(marmol)