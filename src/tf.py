from collections import Counter

# Calcula las term frecuency de cada item de un documento.
def tf(palabras_lemmatizadas):
  return Counter([palabra for _, palabra in palabras_lemmatizadas])
