from pathlib import Path
import os
import platform

sistema = platform.system()
home = Path.home()
actual = Path.cwd()

def plantillas():
    plantilla = actual / "Plantillas"
    plantilla_home = home / ".vim" / "Plantillas"
    vimrc = actual / "Plantillas" / "vimrc"
    vimrc_home = home / ".vimrc"
    
    if vimrc_home.exists() or vimrc_home.is_symlink():
        vimrc_home.unlink()
    
    vimrc_home.symlink_to(vimrc)
    print('Enlance creado')

print(f'Sistema operativo: {sistema}')
plantillas()
