from pathlib import Path
import os
import platform

sistema = platform.system()
actual = Path.cwd()
home = Path.home()

def config():
    plantilla = actual / "Plantillas"
    vim = actual / "Plantillas" / "vimrc"
    vim_home = home / ".vimrc"
    plantillas(vim, plantilla)
    comandos(vim)
   
    if vim_home.exists() and vim_home.is_symlink():
        print('Enlazado')
    else:
        vim_home.unlink(missing_ok=True)
        vim_home.symlink_to(vim)
        print('Enlace creado')
        print('Plantillas creadas')

def plantillas(vim, ruta):
    archivos = []
    with open(vim, 'r', encoding='utf-8') as a:
        contenido = a.read()

    for x in ruta.iterdir():
        if x.is_file():
            archivos.append((x, x.suffix))
    for x,y in archivos:
        if not 'vimrc' in str(x):
            comando = f'autocmd BufNewFile *{y} 0r {x}\n'
            if not comando in contenido:
                with open(vim, 'a', encoding='utf-8') as a:
                    a.write(comando)

def comandos(vim):
    c_latex = f'autocmd BufNewFile,BufRead *.tex nnoremap <buffer> <C-b> :w<CR> :silent !pdflatex % && rm -f %:r.log %:r.aux %:r.toc %:r.out <CR>:redraw!<CR>\n'
    
    with open(vim, 'r', encoding='utf-8') as a:
        contenido = a.read()

    if not c_latex in contenido:
        with open(vim, 'a', encoding='utf-8') as a:
            a.write(c_latex)

print(f'Sistema operativo: {sistema}')
config()
