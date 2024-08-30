
# **TIF Chido - Proyecto ingenieria de software Equipo 2.9**

Aplicacion de facturacion, inventario y transacciones


## **Autores**

- [@Juan Pablo Gaviria](https://github.com/Darkblack595)
- [@Miguel Angel Peña](https://github.com/DarthKar)
- [@Juan Pablo Zuluaga](https://github.com/Ritz38)
- [@Jose Miguel Arroyave](https://github.com/JoseArroyave)
- [@Daniel Steven de la Rosa](https://github.com/Danieldlr13)

## **instalacion**
### Hay dos opciones para la instalacion: 

**1. Para la instalacion se debe descargar el archivo .rar de la seccion de link para posteriormente abrir el .exe (deshabilitar windows defender ya que puede bloquear el archivo por ser de un editor desconocido)**

**2. se puede ejecutar solo el archivo main.py del codigo o si se quiere ejecutar como una aplicacion se debe seguir los pasos siguientes:**

**se puede clonar el repositorio de github y en visual studio, copiar y pegar el siguiente codigo en la consola**

ejecutar primero
```bash
  pip install pyinstaller
  pip install openpyxl
  pip install sqlite3
  ```
luego 
```bash
  pyinstaller --noconfirm --onedir --windowed --icon "invoice.ico" --add-data "addPlatoAc_ui.py;." --add-data "control_bd.py;." --add-data "dialogoAgregarPlatos.py;." --add-data "dialogoOrden_ui.py;." --add-data "estado.json;." --add-data "exporControl.py;." --add-data "formBorrarInv_ui.py;." --add-data "formEditarInv_ui.py;." --add-data "formularioAI_ui.py;." --add-data "formularioControl.py;." --add-data "Inventario.db;." --add-data "paginaPrincipal.py;." --add-data "paginaPrincipal_ui.py;." --add-data "recursos_rc.py;." --add-data "recursos_rc;recursos_rc/" --add-data "build;build/" "main.py"

```

## 🔗 Link de Google Drive con .rar de la app
### **Abrir con el correo institucional**
[![Google Drive](https://img.shields.io/badge/Google-Drive-brightgreen?style=for-the-badge)](https://drive.google.com/drive/folders/1zoSKRpFsc0OLEEUo7WeTwHGpCTneCezx?usp=drive_link)


Para abrir la aplicacion se debe ejecutar el archivo llamado TIF-Chido dentro de la carpeta dist/main luego de descargar la carpeta completa
