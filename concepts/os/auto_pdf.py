# Automating PDF
# pip install pdfplumber
# pip install pandas
# pip install reportlab
import pdfplumber
import pandas as pd
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter
# READ PDF
# Extract Text
filename = 'test.pdf'
with pdfplumber.open(filename) as pdf:
    for p in pdf.pages:
        print(p.extract_text())
# Extract Tables
with pdfplumber.open(filename) as pdf:
    for p in pdf.pages:
        table = p.extract_tables()
        pd.DataFrame(table[1::],columns=table[0]).to_csv('test.csv')

# CREATE PDF
pdf = Canvas('test.pdf')
# Set Title
pdf.setTitle('Test')
# Add Text on PDF
pdf.drawString(100,100,'Medium')
pdf.save()
# Set Page Size
pdf = Canvas('test.pdf',pagesize=(200,200))
# Set Font Size
pdf.setFont('Helvetica',20)
# Add Images 
pdf.drawImage('test.png',0,0,200,200)
# Add text to Center
pdf.drawCentredString(100,100,'Medium')
# Add text to Right
pdf.drawRightString(100,100,'Medium')
# Add text to Left
pdf.drawString(100,100,'Medium')
# save PDF
pdf.save()
# Add Tables
doc = SimpleDocTemplate("simple_table.pdf", pagesize=letter)
table = []
data = [['col1', 'col2', 'col3'],[1,2,3],[4,5,6]]
table.append(Table(data))
doc.build(table)