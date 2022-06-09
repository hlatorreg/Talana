## README
---------

* Solo con Docker
  1. `docker pull ghcr.io/hlatorreg/talana:latest`
  2. `docker run -i -p 5000:5000 ghcr.io/hlatorreg/talana:latest`

* Con código fuente + Docker
  1. `git clone https://github.com/hlatorreg/Talana.git`
  2. `cd Talana`
  3. `docker build -t talana .`
  4. `docker run -i -p 5000:5000 -t talana`

> En ambos casos acceder a la url [http://localhost:5000/api/v1/ui](http://localhost:5000/api/v1/ui) para visualizar Swagger UI

## Preguntas generales
----------------------

1. Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica cómo se
soluciona si hiciste push, y cómo si aún no hiciste.
De ser posible, que quede solo un commit con los cambios.
    
    R: Si no he pusheado, puedo agregar el archivo con `git add filename` y luego un `git commit --amend`.
    
    Si ya hice el push, puedo realizar los mismos pasos anteriores y al momento de pushear agregar el flag `--force`, aunque no es recomendable debido a que reescribe el historial de commits de todo el repositorio.

    Si trabajamos con merge/pull requests es mas sencillo ya que puedo no aceptar el merge/pull, agregar el archivo a mi rama local, commitearlo y realizar un `git rebase -i HEAD~2` y combinar los ultimos dos commits en uno.

    Si estoy trabajando en una rama distinta, puedo no aceptar el merge/pull request, agregar el nuevo archivo a mi rama local, commitearlo y dependiendo de los permisos del repositorio hacer un merge de forma local entre mi rama y la rama de *desarrollo* (por ejemplo) con el flag `--squash` para luego pushear *desarrollo*.


2. Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has trabajado?

    R: Generalmente un flujo de ramas, donde existe una rama por ambiente, cada *feature* es una rama individual que luego se une a las ramas principales de forma ascendiente.

3. ¿Cuál ha sido la situación más compleja que has tenido con esto?

    R: Nada serio, diría que al comienzo de la carrera laboral era mas complejo. Lo primero que se me viene a la mente son merges despues de un par de días, cuando el repositorio habia cambiado mucho y tener que lidiar con un monton de conflictos de forma manual, sin saber que existen herramientas para facilitar ese proceso.
     
4. ¿Qué experiencia has tenido con los microservicios?

    R: Mi primera experiencia con microservicios fue con NodeJS, ejecutando servicios en RasperryPies, publicando mensajes a Google Pub/Sub que posteriormente eran escuchados por un backend en Laravel. El fin de esta *arquitectura* era mantener un control sobre dispositivos de acceso (puertas, portones, camaras, etc).

    Actualmente trabajo en un backend en .NET3/5/6, con muchos servicios montados en un cluster de AKS y una serie de orquestadores realizando operaciones de negocios.

5. ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué?

    R: Me gusta GKE (google kubernetes engine), sin mucho conocimiento es posible tener un cluster auto-gestionado en poco tiempo. Los certificados SSL administrados por Google también son bastante comodos, rapidamente puedo crear un certificado, reservar una IP estática y agregar ambos al *ingress* para segurizar mi aplicación.
