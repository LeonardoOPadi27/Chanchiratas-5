# Indice

[^1]: Como clonar el repositorio.
[^2]: Como hacer un commit.
[^3]: Como sincronizarte con el repositorio principal.

# Como clonar el repositorio [^1]

Pequeño tutorial para los integrantes del equipo "Chanchiratas 5" :P

Si traen laptop solo lo tienen que hacer una vez, a los que no, guardenlo en la memoria "C:" para no perderlo

## Crear tu rama

1- Ve al link del repositorio original.

https://github.com/AldyJn/Chanchiratas-5

2- Da click en el botón de display de `Fork`.

3- Click a `Create a new fork`.

4- Click al botón `Create fork`.

## Configurar Git

1- Instalar git (Para los de laptop que no lo tengan, las PCs de Tecsup ya lo tienen)

2- Configura git usando estos comandos

``` bash
git config --global user.name "Tu Nombre"
```

```bash
git config --global user.email "tuCorreoTecsup"
```

## Clona el repositorio

1- Vas a ir a tu rama del repositorio principal.

https://github.com/ [Tu nombre de usuario de Github] /Chanchiratas-5

2- Vas a darle click a `<> Code`.

3- Dale click al icono de la derecha del link de la pestaña HTTPS para copiar el link de su rama.

4- Abre git

5- dale click derecho donde quieras clonar el repositorio y abre con Git.

6- escribe lo siguiente

```bash
git clone "pega el link de tu rama"
```

# Hacer un commit [^2]

Guía para que hagan un commit para que se actualice el repositorio original que será lo que realmente va a observar el profesor ya que será el link que se va a usar.

## Realizar un commit

1- Abrir la terminal de Visual Studio Code

2- Dar click al lado de botón "+", el cual esta al lado de donde dice "terminal"

3- Seleccionan `bash`

4- Escriben en la terminal

```bash
git add .
```

```bash
git commit -m"Aquí escriben una descripción de lo que hicieron"
```

```bash
git push
```

5- Ve a tu rama en GitHub y dale click en el botón de `Sync fork`

6- Despues, dale click al botón Pull Requests -> New Pull Request

# Sincronizarte con el repositorio [^3]

A continuación, una guía de como sincronizar tu rama clonada en tu PC/Laptop.

## Para la primera vez

```Bash
git remote add fuentes https://github.com/AldyJn/Chanchiratas-5.git
git fetch fuentes
git merge fuentes/main main
```

## Despues de la primera vez

```Bash
git fetch fuentes
git merge fuentes/main main
```