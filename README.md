# Proyecto Final Fundamentos de Ingeniería de Software
## Integrantes:
- Diego Vélez García
&nbsp;
- Sebastián González Forero
&nbsp;
- Oscar Carrillo González
&nbsp;

## Dataset Elegido

El conjunto de datos elegido pertenece al Ministerio de Tecnologías de la Información y las Comunicaciones. Su fecha de actualización corresponde al 24 de septiembre del año en curso. Este dataset contiene información acerca de la Información de línea base de tráfico reportada por los proveedores de servicio de Internet en Colombia, para los meses de enero, febrero y marzo.
 
El conjunto de datos se encuentra dividido en dos partes, una general y una específica cada parte siendo un dataset individual. En primer dataset corresponde a la información general de tráfico de internet para los meses de enero, febrero y marzo del año en curso. En él se detalla información de cada proveedor de servicios en relación con el mes correspondiente, el tráfico de datos a nivel nacional (NAP Colombia), nivel internacional, cantidad de tráfico por acuerdos de tránsito o peering directo, tráfico de datos local y la totalidad de tráfico para cada proveedor y mes. Además posee información relacionada con la hora y la fecha pico por mes relacionada directamente a cada proveedor de servicios. El segundo dataset contiene la misma información pero detallada día a día para cada proveedor pero cuenta con un período desde el 30 de Marzo de 2020 hasta el 21 de septiembre de 2021 fechas relevantes por el uso intensivo de la red debido a la emergencia sanitaria por la COVID-19.

El dataset mencionado se puede consultar directamente en el siguiente [enlace](https://www.datos.gov.co/dataset/Tr-fico-de-Internet-COVID-19/wbvk-p64m)

## Propósito del Aplicativo

El proyecto que se quiere realizar consta de una aplicación web que permita mostrar información estadística o gráfica relacionada con el conjunto de datos elegido. Para esto se requiere hacer uso de diferentes recursos externos como librerías especializadas para realizar estas gráficas y así proporcionar una base para hacer algún análisis relevante y mostrar de manera más dinámica el conjunto de datos.

## Alcance

El alcance de la aplicación está delimitado por una aplicación web que muestre de la mejor manera posible la información contenida el conjunto de datos elegido, haciendo lo posible por realizarlo de manera dinámica y usando diferentes tipos de gráficos que ayuden a interpretar toda la información del dataset elegido. De esta manera será una web sencilla con algún encabezado, el contenido limitado a las cabeceras de título y sus gráficos correspondientes y algún pie de página.

## Requisitos Funcionales

|Requerimiento|Descripción|
|:---:|:---:|
|RF01_Ver Tráfico Proveedores|Muestra la gráfica correspondiente a la información de tráfico total de los 7 proveedores de servicio elegidos.|
|RF02_Ver Hora Pico|Mostrar una gráfica donde se pueda observar la hora pico de tráfico de un mes elegido para cada uno de los 7 servidores elegidos.|
|RF03_Ver Fecha Pico|Mostrar una gráfica donde se pueda observar la fecha pico de tráfico de un mes elegido para cada uno de los 7 proveedores elegidos.|
|RF04_Ver Trafico Internacional|Mostrar una gráfica donde se pueda observar la cantidad de GB de tráfico Internacional de los 7 proveedores elegidos.|
|RF05_Ver Tráfico Nacional|Mostrar una gráfica donde se pueda observar la cantidad de GB de tráfico Nacional de los 7 proveedores elegidos.|
|RF06_Ver Tráfico Peering|Mostrar una gráfica donde se pueda observar la cantidad de GB de tráfico por modalidad/acuerdos peering de los 7 proveedores elegidos.|
|RF07_Ver Entrada del data set|Mostrar una tabla con una o varias entradas del dataset según los criterios de búsqueda del usuario (filtrar un proveedor, un rango de fechas, un rango limite de trafico)|

## Requisitos No Funcionales

|Requerimiento|Descripción|
|:----|:----|
|RNF01_Gráficos Dinámicos|El aplicativo debe mostrar las gráficas de manera dinámica y en tiempo real de acuerdo a los datos que se tienen en el dataset. Con posibilidad de hacer zoom en ellos.|
|RNF02_Tipos de Gráficos|El aplicativo web debe emplear en su preferencia la mayor cantidad de tipos de gráficos según los 7 proveedores elegidos.|
|RNF03_Presentación de Gráficos|El aplicativo debe mostrar en los casos necesarios, la opción para elegir alguno de los proveedores para un gráfico particular. (Filtros a los que haya lugar, mes, proveedor, etc...).|

## Historias de Usuario

|Historia de Usuario|Nombre: Ver tráfico|
|:----|:----|
|Código: |HU_01|
|Actores: |Usuario|
|Descripción:| |
|Como |usuario de la aplicación web|
|Quiero |elegir un mes y un tipo de tráfico|
|Para |ver un gráfico de barras que refleje el tráfico de ese tipo en ese mes para los 7 proveedores elegidos|

&nbsp;
&nbsp;

|Historia de Usuario|Nombre: Ver Hora pico |
|:----|:----|
|Código: |HU_02|
|Actores: |Usuario|
|Descripción:| |
|Como |usuario de la aplicación web|
|Quiero |elegir un mes|
|Para |ver una gráfica de puntos con las hora picos de los 7 proveedores elegidos durante ese mes|

&nbsp;
&nbsp;

|Historia de Usuario|Nombre: Ver Tráfico en un rango de fechas |
|:----|:----|
|Código: |HU_03|
|Actores: |Usuario|
|Descripción:| |
|Como |usuario de la aplicación web|
|Quiero |elegir un rango de fechas y uno o varios proveedores|
|Para |ver un gráfico de líneas que refleje el tráfico total durante cada una de esas fechas para los proveedores elegidos|

&nbsp;
&nbsp;

|Historia de Usuario|Nombre: Ver tráficos agrupados por mes |
|:----|:----|
|Código: |HU_04|
|Actores: |Usuario|
|Descripción:| |
|Como |usuario de la aplicación web|
|Quiero |elegir un mes|
|Para |ver un gráfico de barras agrupado por tipo de tráfico que refleje la cantidad de tráfico en GB en ese mes para los 7 proveedores elegidos.|

&nbsp;
&nbsp;

|Historia de Usuario|Nombre: Ver Entradas data set |
|:----|:----|
|Código: |HU_05|
|Actores: |Usuario|
|Descripción:| |
|Como |usuario de la aplicación web|
|Quiero |elegir uno o varios filtros (ciertos proveedores, un rango de fechas, un rango limite de trafico)|
|Para |ver las entradas del dataset que corresponden a los filtros elegidos|


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
