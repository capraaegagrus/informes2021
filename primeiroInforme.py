from reportlab.pdfgen import canvas

documento = canvas.Canvas ("primeiroInforme.pdf")

documento.drawString( 0, 0, "Posición (X,Y) = (0,0)")
documento.drawString (50, 100, "Posición (X,Y) = (50,100)")
documento.drawString (150, 40, "Posición (X,Y) = (150,40)")
documento.drawImage("/home/manuel/Imaxes/vaquita.jpg", 0,200, 640,360)
documento.showPage()
documento.save()
