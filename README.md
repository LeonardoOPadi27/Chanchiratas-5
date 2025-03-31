# Chanchiratas-5

# CUANDO QUIERES HACER UN GIT PUSH (PARA HACER EL PULL REQUEST, ES DECIR ACTUALIZAR EL REPOSITORIO)

git add .

git commit -m" [Un mensaje de lo que hicieron] "

git push

# LA PRIMERA VEZ

git remote add fuentes https://github.com/AldyJn/Chanchiratas-5.git

# CADA VEZ QUE QUEREMOS SINCRONIZAR LAS RAMAS

git fetch fuentes

git merge fuentes/main main