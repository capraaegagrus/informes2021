from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

imaxes = []

imaxe = Image (0,0, 500, 102, "/home/manuel/Imaxes/logo-daniel-castelao.png" )

debuxo  = Drawing (500,102)
debuxo.add (imaxe)

imaxes.append (debuxo)

documento = Drawing (A4[0], A4[1])
for elemento in imaxes:
   documento.add (elemento)
renderPDF.drawToFile (documento, "segundoInforme.pdf")