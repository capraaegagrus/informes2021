from reportlab.pdfgen import canvas

cancion = ["El patio de mi casa", "es particular", "cuando llueve se moja", "como los demás"]

doc = canvas.Canvas ("documentoTexto.pdf")

obxTexto = doc.beginText ()
obxTexto.setTextOrigin (100,700)
obxTexto.setFont ('Courier', 14)
for estrofa in cancion:
    obxTexto.textLine(estrofa)
obxTexto.setFillGray (0.5)
textoLongo= """Este é un texto con varias liñas.
Neste caso imos a debuxar texto 
non como elementos dunha lista,
senón como un parragrafo."""
obxTexto.textLines(textoLongo)


obxTexto.setTextOrigin (100,500)
obxTexto.setFont ('Helvetica', 14)
for estrofa in cancion:
    obxTexto.textOut(estrofa)
    obxTexto.moveCursor (20,15)

obxTexto.setTextOrigin (100,400)
espazoCar = 1
obxTexto.setFont ('Times-Roman', 14)
for estrofa in cancion:
    obxTexto.setCharSpace (espazoCar)
    obxTexto.textLine(estrofa)
    espazoCar = espazoCar + 1

obxTexto.setTextOrigin (100,300)
obxTexto.setFont ('Courier', 14)
obxTexto.setCharSpace(0)
obxTexto.setWordSpace (8)
obxTexto.textLines(textoLongo)

doc.drawText(obxTexto)

doc.showPage()
doc.save()
