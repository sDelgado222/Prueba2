Esto es lo que realice desde Git Hash
JOSE@HP-ZBOOK-15G3 MINGW64 /c
$ cd semana4

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4
$ git clone https://github.com/jaarcef/Prueba2byProfeStephanie.git
Cloning into 'Prueba2byProfeStephanie'...
remote: Enumerating objects: 27, done.
remote: Counting objects: 100% (27/27), done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 27 (delta 9), reused 16 (delta 2), pack-reused 0 (from 0)
Receiving objects: 100% (27/27), 4.34 KiB | 494.00 KiB/s, done.
Resolving deltas: 100% (9/9), done.

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4
$ git status
fatal: not a git repository (or any of the parent directories): .git

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4
$ ls
Prueba2byProfeStephanie/

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4
$ cd Prueba2byProfeStephanie/

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4/Prueba2byProfeStephanie (main)
$ ls
Ejemplo1.py  Ejemplo_ramita.py   README.md
Ejemplo3.py  Ejemplo_ramita1.py  ejemplo2.py

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4/Prueba2byProfeStephanie (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4/Prueba2byProfeStephanie (main)
$ git branch
* main

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4/Prueba2byProfeStephanie (main)
$ git branch ProyectoFinal

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4/Prueba2byProfeStephanie (main)
$ ls
Ejemplo1.py  Ejemplo_ramita.py   README.md
Ejemplo3.py  Ejemplo_ramita1.py  ejemplo2.py

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4/Prueba2byProfeStephanie (main)
$ git branch
  ProyectoFinal
* main

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4/Prueba2byProfeStephanie (main)
$ git checkout ProyectoFinal
Switched to branch 'ProyectoFinal'

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4/Prueba2byProfeStephanie (ProyectoFinal)
$ git status
On branch ProyectoFinal
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   Ejemplo_ramita1.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Clase2.py
        Practica2.py
        Problema 1.py
        Problema 2.py
        Problema 5.py
        Problema 6.py
        Problema1.py
        Problema2.py
        Prueba.py
        Solucion_Practica1.py
        ejercicio.py

no changes added to commit (use "git add" and/or "git commit -a")

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4/Prueba2byProfeStephanie (ProyectoFinal)
$ git add .

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4/Prueba2byProfeStephanie (ProyectoFinal)
$ git status
On branch ProyectoFinal
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   Clase2.py
        modified:   Ejemplo_ramita1.py
        new file:   Practica2.py
        new file:   Problema 1.py
        new file:   Problema 2.py
        new file:   Problema 5.py
        new file:   Problema 6.py
        new file:   Problema1.py
        new file:   Problema2.py
        new file:   Prueba.py
        new file:   Solucion_Practica1.py
        new file:   ejercicio.py


JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4/Prueba2byProfeStephanie (ProyectoFinal)
$ git commit -m "modificación del FORK de la Profesora Stephanie Delgado, Proyecto Final"
[ProyectoFinal 7347053] modificación del FORK de la Profesora Stephanie Delgado,
 Proyecto Final
 12 files changed, 185 insertions(+), 1 deletion(-)
 create mode 100644 Clase2.py
 create mode 100644 Practica2.py
 create mode 100644 Problema 1.py
 create mode 100644 Problema 2.py
 create mode 100644 Problema 5.py
 create mode 100644 Problema 6.py
 create mode 100644 Problema1.py
 create mode 100644 Problema2.py
 create mode 100644 Prueba.py
 create mode 100644 Solucion_Practica1.py
 create mode 100644 ejercicio.py

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4/Prueba2byProfeStephanie (ProyectoFinal)
$ git push
fatal: The current branch ProyectoFinal has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin ProyectoFinal

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.


JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4/Prueba2byProfeStephanie (ProyectoFinal)
$  git push --set-upstream origin ProyectoFinal
Enumerating objects: 14, done.
Counting objects: 100% (14/14), done.
Delta compression using up to 8 threads
Compressing objects: 100% (11/11), done.
Writing objects: 100% (12/12), 3.33 KiB | 851.00 KiB/s, done.
Total 12 (delta 0), reused 1 (delta 0), pack-reused 0 (from 0)
remote:
remote: Create a pull request for 'ProyectoFinal' on GitHub by visiting:
remote:      https://github.com/jaarcef/Prueba2byProfeStephanie/pull/new/Proyect
oFinal
remote:
To https://github.com/jaarcef/Prueba2byProfeStephanie.git
 * [new branch]      ProyectoFinal -> ProyectoFinal
branch 'ProyectoFinal' set up to track 'origin/ProyectoFinal'.

JOSE@HP-ZBOOK-15G3 MINGW64 /c/semana4/Prueba2byProfeStephanie (ProyectoFinal)
$
