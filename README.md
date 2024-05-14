# Script traductor de log a Query
## Introducción
Este es un script para tomar los logs que genera el plugin [The Towers Champagne](https://github.com/katanya04/The-Towers) y los convierte a querys de base de datos

### [Revisa el último release aquí](https://github.com/nicoliee/Nicolie-MariaDB-Script/releases)

## Indice
* [Funcionamiento](#funcionamiento)
* [Restricciones](#restricciones)
## Funcionamiento
1. Se coloca el log en el siguiente path: Nicolie's Script\dist
2. Inicia el main.exe del mismo path 
2. La consola te pedirá ingresar el nombre del archivo del log (junto con su extensión)
3. Si encuentra el archivo entonces generará un output con la traducción realizada, de lo contrario se cerrará el programa
## Restricciones
El log que se utilice deberá ser modificado, para que la única línea que exista sea donde se realicen los Querys a la base de datos