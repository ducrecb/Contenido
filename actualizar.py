import os
import requests

print("Iniciando la actualización de la lista M3U desde Paraguay...")

# Enlaces de tus listas M3U o fuentes de canales
# (Puedes cambiar estas URLs de ejemplo por las tuyas reales más adelante)
FUENTES_M3U = [
    "https://githubusercontent.com",
    "https://githubusercontent.com"
]

contenido_final = "#EXTM3U\n#   Actualizado automaticamente por GitHub Actions\n\n"

for url in FUENTES_M3U:
    try:
        print(f"Descargando canales desde: {url}")
        respuesta = requests.get(url, timeout=10)
        if respuesta.status_code == 200:
            linhas = respuesta.text.split("\n")
            for linha in linhas:
                # Evitamos repetir la cabecera en el archivo final
                if not linha.startswith("#EXTM3U") and linha.strip() != "":
                    contenido_final += linha + "\n"
        else:
            print(f"Error al descargar de la URL (Código {respuesta.status_code})")
    except Exception as e:
        print(f"No se pudo conectar a la fuente debido a: {e}")

# Guardamos la lista M3U actualizada en el repositorio
nombre_archivo_salida = "lista_actualizada.m3u"
with open(nombre_archivo_salida, "w", encoding="utf-8") as f:
    f.write(contenido_final)

print(f"¡Proceso terminado con éxito! Tu nueva lista se guardó en {nombre_archivo_salida}")
