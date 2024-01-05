# RobloxFriendRequestInsights
Este repositorio contiene un script de Python que analiza las solicitudes de amistad pendientes en Roblox. El script identifica a los usuarios con una mayor cantidad de seguidores y aquellos verificados por Roblox, ofreciendo información valiosa sobre las solicitudes de amistad basadas en el recuento de seguidores y la autenticación verificada de Roblox.

# Script para obtener datos de amigos de Roblox

Este script de Python te permite obtener datos de amigos de Roblox utilizando una cookie de seguridad. Sigue estos pasos para usar el script:

## Requisitos

- Python 3 instalado en tu sistema.

## Pasos para ejecutar el script

1. Descarga o clona este repositorio en tu computadora.
2. Abre una terminal o línea de comandos en la carpeta del repositorio.

### Uso

Ejecuta el script con el siguiente comando desde la terminal o línea de comandos:

```
python script.py start <cookie>
```

- Reemplaza `script.py` con el nombre de tu archivo Python.
- `<cookie>` es tu cookie de seguridad de Roblox. Si la cookie contiene espacios, asegúrate de incluirla entre comillas.

### Ejemplo de uso:

Si tu archivo se llama `my_script.py` y tu cookie es `mi_cookie_roblox_con_espacios`, el comando se vería así:

```
python my_script.py start "mi_cookie_roblox_con_espacios"
```

Esto ejecutará el script utilizando la cookie proporcionada y empezará a recopilar los datos de amigos de Roblox.

### Resultados

Los resultados se guardarán en dos archivos JSON dentro de la misma carpeta donde se encuentra el script:
- `follower_list.json`: Lista de amigos con información sobre sus seguidores.
- `verified_list.json`: Lista de amigos verificados.
