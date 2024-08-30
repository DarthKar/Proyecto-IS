
# TIF Chido - Proyecto ingenieria de software Equipo 2.9

Aplicacion de facturacion, inventario y transacciones


## Autores

- [@Juan Pablo Gaviria](https://github.com/Darkblack595)
- [@Miguel Angel Peña](https://github.com/DarthKar)
- [@Juan Pablo Zuluaga](https://github.com/Ritz38)
- [@Jose Miguel Arroyave](https://github.com/JoseArroyave)
- [@Daniel Steven de la Rosa](https://github.com/Danieldlr13)


## instalacion

Para la instalacion se debe descargar el archivo .rar de la seccion de link para posteriormente abrir el .exe (deshabilitar windows defender ya que puede bloquear el archivo por ser de un editor desconocido) o se puede clonar el repositorio de github y en visual studio, copiar y pegar el siguiente codigo en la consola.

primero ejecutar:
```bash
  pip install pyinstaller 
```
luego de termiando el proceso, ejecutar:
```bash

  
  pyinstaller --noconfirm --onedir --windowed --icon "invoice.ico" --add-data "addPlatoAc_ui.py;." --add-data "control_bd.py;." --add-data "dialogoAgregarPlatos.py;." --add-data "dialogoOrden_ui.py;." --add-data "estado.json;." --add-data "exporControl.py;." --add-data "formBorrarInv_ui.py;." --add-data "formEditarInv_ui.py;." --add-data "formularioAI_ui.py;." --add-data "formularioControl.py;." --add-data "Inventario.db;." --add-data "paginaPrincipal.py;." --add-data "paginaPrincipal_ui.py;." --add-data "recursos_rc.py;." --add-data "recursos_rc;recursos_rc/" --add-data "build;build/" "main.py"

```
    
