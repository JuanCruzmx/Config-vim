from pathlib import Path
import os
import platform

sistema = platform.system()
actual = Path.cwd()
home = Path.home()

def config():
    plantilla = actual / "Plantillas"
    vimrc = actual / "Plantillas" / "vimrc"
    vimrc_home = home / ".vimrc"
    plantillas(vimrc, plantilla)
    comandos(vimrc)
   
    if vimrc_home.exists() and vimrc_home.is_symlink():
        print('Enlazado')
    else:
        vimrc_home.unlink(missing_ok=True)
        vimrc_home.symlink_to(vim)
        print('Enlace creado')
        print('Plantillas creadas')

def plantillas(vimrc, ruta):
    archivos = []
    with open(vimrc, 'r', encoding='utf-8') as a:
        contenido = a.read()

    for x in ruta.iterdir():
        if x.is_file():
            archivos.append((x, x.suffix))
    for x,y in archivos:
        if not 'vimrc' in str(x):
            comando = f'autocmd BufNewFile *{y} 0r {x}\n'
            if not comando in contenido:
                with open(vimrc, 'a', encoding='utf-8') as a:
                    a.write(comando)

def comandos(vimrc):
    c_latex = f'autocmd BufNewFile,BufRead *.tex nnoremap <C-b> :w<CR> :silent !pdflatex % && rm -f %:r.log %:r.aux %:r.toc %:r.out<CR> :redraw!<CR>\n'
    c_c = f'autocmd BufNewFile,BufRead *.c nnoremap <C-b> :w<CR> :silent !gcc % -o %:r<CR> :redraw!<CR>\n'
    
    with open(vimrc, 'r', encoding='utf-8') as a:
        contenido = a.read()

    if not (c_latex and c_c) in contenido:
        with open(vimrc, 'a', encoding='utf-8') as a:
            a.write(c_latex)
            a.write(c_c)

print(f'Sistema operativo: {sistema}')
config()
