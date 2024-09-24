import os
from dotenv import load_dotenv
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  
from email import encoders
from datetime import datetime
from io import BytesIO
import ssl
import smtplib
from openpyxl import Workbook
from control_bd import BaseDatos  

def generar_excel_inventario():
    libro = Workbook()
    pag = libro.active
    datos = BaseDatos.leerFilas() 
    
    pag["A1"] = "Nombre"
    pag["C1"] = "Cantidad"
    pag["D1"] = "Und/Medida"

    for i in range(2, len(datos) + 2):
        pag.merge_cells(f"A{i}:B{i}")
        pag[f"A{i}"] = datos[i - 2][0]
        pag[f"C{i}"] = datos[i - 2][1]
        pag[f"D{i}"] = datos[i - 2][2]
        
    excel_en_memoria = BytesIO()
    libro.save(excel_en_memoria)
    excel_en_memoria.seek(0)
    
    return excel_en_memoria

def enviar_email_con_adjunto():
    try:
        load_dotenv()
        email_envi = "c1677672@gmail.com"
        email_rec = "c1677672@gmail.com"
        contra = os.getenv("CODIGO")
        horaActual = datetime.now()
        fecha = horaActual.strftime("%Y-%m-%d")
        hora = horaActual.strftime("%H:%M")
        sub = f"exportaciones {fecha}"
        cuerpo = f"generado {hora}"

        archivo_excel = generar_excel_inventario()

        em = MIMEMultipart()
        em["From"] = email_envi
        em["To"] = email_rec
        em["Subject"] = sub
        em.attach(MIMEText(cuerpo, "plain"))  

        adjunto = MIMEBase("application", "octet-stream")
        adjunto.set_payload(archivo_excel.read())
        encoders.encode_base64(adjunto)
        adjunto.add_header(
            "Content-Disposition",
            f"attachment; filename=Inventario-{fecha}.xlsx"
        )
        em.attach(adjunto)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_envi, contra)
            smtp.sendmail(email_envi, email_rec, em.as_string())

        print("Correo enviado con éxito.")

    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        

