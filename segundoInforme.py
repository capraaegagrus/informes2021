from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

imaxes = []

imaxe = Image (0,0, 500, 102, "/home/manuel/Descargas/logoCole.jpg" )

debuxo  = Drawing (500,102)
debuxo.translate (0,700)
debuxo.add (imaxe)
imaxes.append (debuxo)

debuxo2 = Drawing (250,51)
debuxo2.add(imaxe)
debuxo2.rotate (45)
debuxo2.translate (500,50)
debuxo2.scale (0.5, 1.5)

imaxes.append (debuxo2)


documento = Drawing (A4[0], A4[1])
for elemento in imaxes:
   documento.add (elemento)
renderPDF.drawToFile (documento, "segundoInforme.pdf")