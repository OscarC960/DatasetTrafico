# Proyecto Final Fundamentos de Ingeniería de Software
## Integrantes:
- Diego Vélez García
&nbsp;
- Sebastián González Forero
&nbsp;
- Oscar Carrillo González
&nbsp;

## Propósito del Aplicativo

El proyecto que se quiere realizar consta de una aplicación web que permita mostrar información estadística o gráfica relacionada con el conjunto de datos elegido. Para esto se requiere hacer uso de diferentes recursos externos como librerías especializadas para realizar estas gráficas y así proporcionar una base para hacer algún análisis relevante y mostrar de manera más dinámica el conjunto de datos.

## Dataset Elegido

El conjunto de datos elegido pertenece al Ministerio de Tecnologías de la Información y las Comunicaciones. Su fecha de actualización corresponde al 24 de septiembre del año en curso. Este dataset contiene información acerca del tráfico diario reportado por los proveedores de servicio de Internet en Colombia, desde Abril de 2020 hasta septiembre de 2021.
 
El dataset corresponde a la información general de tráfico de internet  de distintos proveedores para cada día desde abril de 2020 hasta fechas recientes, tiempo afectado por la pandemia del COVID-19 . En él se detalla información de cada proveedor de internet: el tráfico de datos a nivel nacional (NAP Colombia), nivel internacional, cantidad de tráfico por acuerdos de tránsito o peering directo, tráfico de datos local y la totalidad de tráfico para cada proveedor. Además posee la hora pico de cada día de cada proveedor de servicios.

El dataset contiene la información de varios proveedores pero elegimos solo 7 de ellos ya que son más conocidos y tienen más información sobre distintos tipos de tráfico.

El dataset mencionado se puede consultar directamente en el siguiente [enlace](https://www.datos.gov.co/dataset/Tr-fico-de-Internet-COVID-19/wbvk-p64m)

## Alcance

El alcance de la aplicación está delimitado por una aplicación web que muestre de la mejor manera posible la información contenida el conjunto de datos elegido, haciendo lo posible por realizarlo de manera dinámica y usando diferentes tipos de gráficos que ayuden a interpretar toda la información del dataset elegido. De esta manera será una web sencilla con algún encabezado, el contenido limitado a las cabeceras de título, sus gráficos correspondientes y su respectiva navegabilidad.

## Requisitos Funcionales

|Requerimiento|Descripción|
|Requerimiento|Descripción|
|:----|:----|
|RF01_Ver Tráfico Proveedores|Muestra la gráfica correspondiente a la información de tráfico total de los 7 proveedores.|
|RF02_Ver Hora Pico|Mostrar una gráfica donde se pueda observar la hora pico de tráfico de unas fechas elegidas para cada uno de los 7 proveedores.|
|RF03_Ver Fecha Pico|Mostrar una gráfica donde se pueda observar la fecha pico de tráfico de unas fechas elegidas para cada uno de los 7 proveedores.|
|RF04_Ver Trafico Internacional|Mostrar una gráfica donde se pueda observar la cantidad de GB de tráfico Internacional de los 7 proveedores.|
|RF05_Ver Tráfico Nacional|Mostrar una gráfica donde se pueda observar la cantidad de GB de tráfico Nacional de los 7 proveedores.|
|RF06_Ver Tráfico Peering|Mostrar una gráfica donde se pueda observar la cantidad de GB de tráfico por modalidad/acuerdos peering de los 7 proveedores.|
|RF07_Ver Entradas del dataset|Mostrar una tabla con una o varias entradas del dataset según los criterios de búsqueda del usuario (filtrar un proveedor, un rango de fechas, un rango límite de tráfico).|

## Requisitos No Funcionales

|Requerimiento|Descripción|
|:----|:----|
|RNF01_Gráficos Dinámicos|El aplicativo debe mostrar las gráficas de manera dinámica y en tiempo real de acuerdo a los datos que se tienen en el dataset. Con posibilidad de hacer zoom en ellos.|
|RNF02_Tipos de Gráficos|El aplicativo web debe emplear en su preferencia la mayor cantidad de tipos de gráficos según los 7 proveedores elegidos.|
|RNF03_Presentación de Gráficos|El aplicativo debe mostrar en los casos necesarios, la opción para elegir alguno de los proveedores para un gráfico particular. (Filtros a los que haya lugar, més, proveedor, etc...).|

## Historias de Usuario

|Historia de Usuario|Nombre: Ver Tráfico total|
|:----|:----|
|Código: |HU_01|
|Actores: |Usuario|
|Como |usuario de la aplicación web|
|Quiero |elegir un rango de fechas y un tipo de tráfico|
|Para |ver un gráfico de barras que refleje el tráfico total de ese tipo en ese rango de fechas para los 7 proveedores|

&nbsp;
&nbsp;

|Historia de Usuario|Nombre: Ver Hora pico |
|:----|:----|
|Código: |HU_02|
|Actores: |Usuario|
|Como |usuario de la aplicación web|
|Quiero |elegir un rango de fechas|
|Para |ver una gráfica de puntos con las hora picos de los 7 proveedores en cada dia de ese rango de fechas|

&nbsp;
&nbsp;

|Historia de Usuario|Nombre: Ver Tráfico diario |
|:----|:----|
|Código: |HU_03|
|Actores: |Usuario|
|Como |usuario de la aplicación web|
|Quiero |elegir un rango de fechas y un tipo de trafico|
|Para |ver un gráfico de líneas que refleje ese tipo de tráfico durante cada una de esas fechas para los 7 proveedores|

&nbsp;
&nbsp;

|Historia de Usuario|Nombre: Ver Tráficos |
|:----|:----|
|Código: |HU_04|
|Actores: |Usuario|
|Como |usuario de la aplicación web|
|Quiero |elegir un rango de fechas|
|Para |ver un gráfico de barras agrupado por tipo de tráfico que refleje la cantidad total de todos los tipos de tráfico en ese rango de fechas para los 7 proveedores.|

&nbsp;
&nbsp;

|Historia de Usuario|Nombre: Ver Entradas dataset |
|:----|:----|
|Código: |HU_05|
|Actores: |Usuario|
|Como |usuario de la aplicación web|
|Quiero |elegir un rango de fechas|
|Para |ver las entradas del dataset que corresponden a las fechas elegidas|


## Metodología de Desarrollo 
Extreme Programing (XP)

## Lenguaje de programación
Python

Con las herramientas:
- Numpy 
- Panda 
- Plotly 
- Dash
- Tecnologías Web (Html y CSS)

## Plan de Entrega

### Caldendario de Trabajo
|Fecha|Tarea|
|:----|:----|
|29 de Septiembre|Planteamiento de Requerimientos e historias de usuario|
|30 de Septiembre|Presentación y Negociación de requerimientos e historias de usuario con el profesor|
|1 y 2 de Octubre|Desarrollo de RF01 y RF05|
|3 y 4 de Octubre|Desarrollo de RF02, RF03, RF04|
|5 de Octubre|Entrega y retroalimentación con el profesor|
|6 de Octubre|Desarrollo de RF02, RF03, RF04|
|7 de Octubre|Entrega y retroalimentación con el profesor|
|8 al 10 de Octubre|Desarrollo de Requerimientos no funcionales|
|11 de Octubre|Entrega Final|

### Plan de Iteracion

|Iteración|Historia de Usuario|Tarea|
|:----|:----|:----|
|1|Ver Tráfico total|Agrupamiento de entradas del dataset en un rango de fechas|
|1|Ver Tráfico total|Separación de datos de tráfico y proveedor y sumatoria de tráfico|
|1|Ver Tráfico total|Implementación de la gráfica de barras que va a mostrar los datos correspondientes|
|1|Ver Entradas dataset|Agrupamiento de entradas del dataset por distintos filtros|
|1|Ver Entradas dataset|Implementación de la tabla que mostrará las entradas del dataset correspondientes|
|1|Ver Hora Pico|Agrupamiento de entradas del dataset en un rango de fechas * |
|1|Ver Hora Pico|Separación de datos de Hora Pico, fecha y proveedor|
|1|Ver Hora Pico|Implementación de la gráfica de puntos que va a mostrar los datos correspondientes|
|1|Ver Trafico diario|Agrupamiento de entradas del dataset en un rango de fechas y por proveedores|
|1|Ver Trafico diario|Separación de datos de Tráfico total, fecha y proveedor|
|1|Ver Trafico diario|Implementación de la gráfica de líneas que va a mostrar los datos correspondientes|
|1|Ver Tráficos|Agrupamiento de entradas del dataset en un rango de fechas * |
|1|Ver Tráficos|Separación de datos de Tráfico de acuerdos de tránsito, peering directo y local, y proveedor|
|1|Ver Tráficos|Implementación de la gráfica de barras agrupadas que va a mostrar los datos correspondientes|
|2|Ver Trafico total|Implementación de la interfaz de usuario que permite seleccionar un rango de fechas y tipo de tráfico y mostrar la gráfica|
|2|Ver Entradas dataset|Implementación de la interfaz de usuario que permite seleccionar un rango de fechas * |
|2|Ver Hora Pico|Implementación de la interfaz de usuario que permite seleccionar un rango de fechas y mostrar la gráfica * |
|2|Ver Trafico diario|Implementación de la interfaz de usuario que permite seleccionar un rango de fechas y tipo de trafico y mostrar la gráfica  * |
|2|Ver Tráficos|Implementación de la interfaz de usuario que permite seleccionar un rango de fechas y mostrar la gráfica * |

\* No es una tarea nueva, se puede reutilizar el código anterior.

