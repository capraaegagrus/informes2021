import sqlite3 as dbapi

from reportlab.platypus import Table
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


listaTaboa =[]
listaTaboa.append (('Dni','Nome','Dirección','Edade','Sexo'))
try:
    bbdd = dbapi.connect("baseDatosTreeView.dat")
except dbapi.StandardError as e:
    print(e)
else:
    print("Base de datos aberta")
try:
    cursor = bbdd.cursor()
    cursor.execute("select * from usuarios")

    for fila in cursor.fetchall():
        print (fila)
        listaTaboa.append(fila)

except dbapi.DatabaseError as e:
    print("Erro facendo a consulta: " + str(e))
else:
    print("Consulta executada")
finally:
    cursor.close()
    bbdd.close()





taboa  = Table (listaTaboa)

taboa.setStyle ([('TEXTCOLOR',(0,0),(-1, 0),colors.red)])
taboa.setStyle ([('BACKGROUND', (0,1),(-1,-1), colors.aliceblue)])
taboa.setStyle ([('INNERGRID', (0,1),(-1,-1),0.25, colors.darkgrey)])
doc =[taboa]

documento = SimpleDocTemplate ("informeTaboaBD.pdf", pagesize = A4, showBoundary = 0)
documento.build (doc)
