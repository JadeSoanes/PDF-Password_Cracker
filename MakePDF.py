
#import the reportlab module and bits we need to use to make our PDF

from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

# Create a new PDF file calles Crack_Me in a landscape, A4 format
pdf = canvas.Canvas("Crack_Me.pdf", pagesize=landscape(A4))

# Set the dimensions of the page
pdf_w, pdf_h = landscape(A4)


# Add some text to the PDF in an easy to read, black font
pdf.setFillColorRGB(0, 0, 0)  
pdf.setFont("Helvetica-Bold", 30)
pdf.drawCentredString(pdf_w / 2, pdf_h - 50 * mm, "You cracked the password! Congratulations")

# Set a password on the PDF file (which we will then crack in the next section!)
pdf.setEncrypt("teammaroonCFG")

# Save the PDF file
pdf.save()