<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>``
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">GUÍA DE LABORATORIO</span><br />
<span></span>
</div>

<div aling="center">
<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Python</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>04</td><td>AÑO LECTIVO:</td><td>2022 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA DE PRESENTACIÓN: </td><td>05-Jun-2022</td><td>HORA DE PRESENTACIÓN: </td><td colspan="3">11:00 pm</td>
</tr>
<tr><td colspan="4">INTEGRANTE(S): 
<ul>
<li>ACO TITO, Anthony Edwin (aacot@unsa.edu.pe)</li>
<li>CALCINA PUMA, Esteven Antonio (ecalcinap@unsa.edu.pe)</li>
<li>CHAMBILLA PERCA, Valentina Milagros (vchambillap@unsa.edu.pe)</li>
<li>GALVEZ QUILLA, Henry Isaias (hgalvezq@unsa.edu.pe)</li>
</ul>
</td>
<td>NOTA: </td>
<td width="150"></td>
</<tr>
<tr><td colspan="6">DOCENTES:
<ul>
<li>Richart Smith Escobedo Quispe (rescobedoq@unsa.edu.pe)</li>
</ul>
</td>
</<tr>
</tdbody>
</table>
</div>

# ACOTACIONES PRELIMINARES

Para la elaboración de los ejercicios propuestos se hizo uso de los archivos entregados por el docente encargado, los cuales son:

## Archivo piece.py

Este archivo representaba por medio de un arreglo de Strings las piezas de ajedres. Por ejemplo:
<img src="https://github.com/stevenAnto/Lab04-pweb2/blob/main/imagenes/CapturaArchivoPieces.PNG?raw=true" alt="ValentinaChambillaCapCommits" style="width:100%; margin: auto; display: block;"/>
Cada ficha esta representada por un arreglo de 58 Strings, los cuales tienen una longitud de 58 caracteres.

## Archivo chessPictures.py

En este archivo se nos proporciona los objetos de clase Picture, declarados en la siguientes lineas
<img src="https://github.com/stevenAnto/Lab04-pweb2/blob/main/imagenes/CapturaArchivoPicture.PNG?raw=true" alt="ValentinaChambillaCapCommits" style="width:100%; margin: auto; display: block;"/>

## Archivo picture.py

La clase picture esta definida en este archivo, además de estar sus funciones las cuales determinarán su impresión. Este archivo será completado con distintas funciones que permitirán su interactividad y correcta impresión.

## Archivo colors.py

Este archivo es importado en picture.py. Este nos proporciona los codigos de color de cada caracter, asi como su inversión de color.

# SOLUCIÓN Y RESULTADOS

## I. SOLUCIÓN DE EJERCICIOS/PROBLEMAS

### a) Ejercicio: Implementación de los métodos de la clase Picture

#### Método verticalMirror(self)
- Encargado: CALCINA PUMA, Esteven Antonio

Este método debia devolver el espejo vertical de la imagen.
Para elaborar ello, primeramente se generó un nuevo Array (arreglo) llamado *vertical* que almacene el nuevo arreglo de string y una variable Integer (entera) llamada *contador* la cual almacenará el último indice del arreglo de la pieza, la cual es la longitud del arreglo menos 1 (Ya que los arreglos inician en 0). Luego, con el bucle for, el cual se manejaría por un contador *i* iniciado en 0 (predeterminado) hasta el rango que se indicara por la longitud del arreglo, en este caso, al ser 58 elementos, el contador *i* irá desde 0 hasta 57.
Finalemente, se va agregando en cada iteración al array *vertical* con la función *append* desde los últimos elementos de la pieza hasta el primero, reduciendole al contador uno en cada iteraación para que llegue a 0 al final. Se retorna el arreglo *vertical*.

#### Método horizontalMirror(self)
- Encargado: 

Este método debia devolver el espejo horizontal de la imagen.
Para su elaboración, se usará una función llamada *invertirString*, esta función con ayuda del buble for invierte una cadena de caracteres.
Con un buble for, en el método horizontalMirror, hacemos iteraciones con un contador *i* con las mismas especificaciones que en el anterior método. La diferencia esta que en este método se va ir cambiando los Strings por su inversión usando uso de la función *invertirString*.

#### Método negative(self)
- Encargado: 

Este método debia devolver el negativo de la imagen.

#### Método join(self, p)
- Encargado: 

Este método debia devolver la imagen del segundo argumento al lado derecho de la figura actual.
Para su elaboración se hizo uso de un bucle for con las mismas condiciones que en el caso de verticalMirror y horizontalMirror. En cada iteración se le daba como valor al elemento que tocaba de *self.img* el mismo concatenado con la la linea que tocaba de *p.img*. Ello da como resultado la imagen almacenada en self, y a su derecha, pa imagen almacenada en p. El return se hace del objeto de la clase Picture almacenado en *self*.

#### Método up(self, p)
- Encargado: 

Este método debia devolver la imagen del segundo argumento encima de la figura actual

#### Método under(self, p)
- Encargado: CHAMBILLA PERCA, Valentina Milagros

Este método debia devolver la imagen del segundo argumento encima de la figura actual
Para su elaboración se hizo uso de un bucle for con las mismas condiciones que en el caso de los métodos que buscaban espejos. En cada iteración, se fue agregando a self.img com la función *insert*, la cual permite agregar elementos a arreglos en un indice especifico. Ello se realizó con el fin que al arreglo *self.img* se agregaran en orden las lineas de el arreglo *p.img*. Retorna el objeto picture resultante del arreglo *self.img*

#### Método horizontalRepeat(self, n)
- Encargado: GALVEZ QUILLA, Henry Isaias

Este método devía devolver una nueva figura repitiendo la figura actual al costado la cantidad de veces que indique el valor de n.
Se hizo uso de un bucle for con las mismas condiciones que en el caso de los métodos que buscaban espejos. En cada iteración, se guarda en una variable *aux* el elemento ue le toca, y posteriormente se desarrolla un bucle con el contador j que va desde 0 hasta la cantidad de repeticiones menos 1, y en cada una de ellas, se le da como valor a el elemento que se le toca el valor de la variable *aux* concatenado con su propio valor. Se retorna el objeto de clase Picture que se obtiene en el arreglo *self.img*.

#### Método verticalRepeat(self, n)
- Encargado: 

Este método devía devolver una nueva figura repitiendo la figura actual debajo la cantidad de veces que indique el valor de n.
Primero, se creo un Array llamado *figura*. Se colocón un buble for con contador *c* que devolvería desde 0 hasta el número de repeticiones representado por *n*, ya que ello serían las repeticiones que se pidieron más la ficha inicial. Dentro de dicho buble se encuentra el bucle for con contador *t* que representará los elementos del arreglo *self.img*. Finalemente se va almacenando en el arreglo *figura* por completo, repitiendose ello las veces que indique el primer bucle.

#### Método rotate(self)
- Encargado: 

Este método devía devolver una figura rotada 90 grados en sentido horario o antihorario.
Primero, se creo un Array llamado *figura* vacio y una variable String llamada *text*. Se colocón un buble for con contador *c* que tiene las mismas caracteristicas de los bucles usados en mirror. Dentro de ese buble se encuentra el bucle for con contador *t* que representará los elementos del arreglo *self.img*. Luego se almacenará en la variable *text* el caracter en posición *c* de la cadena *t* que pertenece al arreglo *self.img*, agregandose en el arreglo *figura* por cada iteración y siendo dado su valor de *text* como "" para evitar reiteración, dando así una rotación de 90 grados en sentido horario. Se retorna el objeto Picture del arreglo *figura*.

## CUESTIONARIO
###   ¿Qué son los archivos *.pyc?
-los archivos .pyc son versiones compiladas de los archivos de texto sin formato ".py", creados en tiempo de ejecución para hacer que los programas se ejecuten más rápido. Los archivos .pyc se crean (y posiblemente se sobrescriben) solo cuando ese archivo python es importado por algún otro script. Si se llama a la importación, Python comprueba si la marca de tiempo interna del archivo .pyc coincide con el archivo .py correspondiente. Si lo hace, carga el .pyc; si no lo hace o si el .pyc aún no existe, Python compila el archivo .py en un .pyc y lo carga.
### ¿Para qué sirve el directorio __pycache__?
-Para acelerar la carga de módulos, Python cachea las versiones compiladas de cada módulo en el directorio __pycache__ bajo el nombre module.version.pyc dónde la versión codifica el formato del archivo compilado; generalmente contiene el número de version de Python.
###   ¿Cuáles son los usos y lo que representa el subguión en Python?
-Utilizarlo en Internacionalización (i18n) o Localización (l10n).
-Almacenar el valor de la última expresión en intérprete.
-Separar los dígitos de un número.
-Ignorar valores específicos.
-Dar significados especiales (y funciones) al nombre de variables o funciones.
#

## REFERENCIAS
-   https://www.w3schools.com/python/python_reference.asp
-   https://docs.python.org/3/tutorial/

#

[license]: https://img.shields.io/github/license/rescobedoq/pw2?label=rescobedoq
[license-file]: https://github.com/rescobedoq/pw2/blob/main/LICENSE

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]


[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]
