import os
from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

follaEstilo = getSampleStyleSheet()

doc = []


cabeceira = follaEstilo ['Heading4']
cabeceira.pageBreakBefore = 0
cabeceira.keepWithNext = 1
cabeceira.backColor = colors.ivory
parragrafo = Paragraph("Cabeceria do documento", cabeceira)
doc.append (parragrafo)


cadea = "Creamos unha cadea de recheo. " * 700
corpoTexto = follaEstilo ['BodyText']
parragrafo = Paragraph (cadea, corpoTexto)
doc.append (parragrafo)

doc.append (Spacer (0, 20))

imaxe = Image (os.path.realpath("/home/manuel/Descargas/logoCole.jpg"), width =392, height=53 )
doc.append (imaxe)


informe = SimpleDocTemplate ("exemploInforme.pdf", pagesize=A4, showBoundary = 1)
informe.build(doc)
