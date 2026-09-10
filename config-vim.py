from pathlib import Path
import os
import platform

sistema = platform.system()

def plantillas():
    actual = Path.cwd()
    home = Path.home()
    plantilla = actual / "Plantillas"
    plantilla_home = home / ".vim" / "Plantillas"
    vimrc = actual / "Plantillas" / "vimrc"
    vimrc_home = home / ".vimrc"
    plantilla_home.parent.mkdir(parents=True, exist_ok=True)

    if plantilla_home.exists() and plantilla_home.is_symlink():
        print('Plantillas activas')
    else:
        plantilla_home.unlink(missing_ok=True)
        plantilla_home.symlink_to(plantilla)
        print('Plantillas creadas')
   
    if vimrc_home.exists() and vimrc_home.is_symlink():
        print('Enlazado')
    else:
        vimrc_home.unlink(missing_ok=True)
        vimrc_home.symlink_to(vimrc)
        print('Enlace creado')

print(f'Sistema operativo: {sistema}')
plantillas()
