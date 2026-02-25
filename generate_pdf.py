from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_pdf():
    # Setup document
    doc = SimpleDocTemplate(
        "/Users/pol/.gemini/antigravity/scratch/espai-vall-roure/taula-cultius-estiu.pdf",
        pagesize=landscape(A4),
        rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30
    )
    elements = []
    styles = getSampleStyleSheet()
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#246946'),  # Brand green
        alignment=1, # Center
        spaceAfter=20
    )
    elements.append(Paragraph("Taula Completa d'Associació de Cultius d'Estiu", title_style))
    
    # Description
    desc_style = ParagraphStyle(
        'CustomDesc',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#44403c'),
        alignment=1,
        spaceAfter=30
    )
    elements.append(Paragraph(
        "Aquesta és la guia estesa per a l'Espai Vall-Roure. "
        "Utilitza el codi de colors per planificar els teus bancals amb èxit.", 
        desc_style
    ))

    # Legend
    legend_data = [
        ['Llegenda:', 
         'B = Bon Veí (Beneficiós)', 
         'M = Mal Veí (Perjudicial)', 
         'N = Neutre (Indiferent)']
    ]
    legend_table = Table(legend_data, colWidths=[80, 150, 150, 150])
    legend_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#dcfce7')), # Green
        ('BACKGROUND', (2,0), (2,0), colors.HexColor('#fee2e2')), # Red
        ('BACKGROUND', (3,0), (3,0), colors.HexColor('#f3f4f6')), # Gray
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('GRID', (0,0), (-1,-1), 1, colors.white),
    ]))
    elements.append(legend_table)
    elements.append(Spacer(1, 20))


    # Data (Rows and columns)
    crops = [
        "Tomata", "Pebrot", "Albergínia", "Carbassó", "Cogombre", "Meló/Síndria", 
        "Mongeta", "Ceba/All", "Enciam", "Pastanaga", "Bleda/Espinac", "Alfàbrega", "Dacsa (Blat)"
    ]
    
    # M = Mal (Red), B = Bon (Green), N = Neutre (White/Default)
    # simplified matrix just for the PDF visually
    matrix = [
        [''] + crops, # Header row
        ["Tomata",      "N", "N", "N", "M", "N", "N", "M", "B", "B", "B", "B", "B", "N"],
        ["Pebrot",      "N", "N", "N", "N", "N", "N", "M", "N", "B", "B", "B", "B", "N"],
        ["Albergínia",  "N", "N", "N", "N", "N", "N", "B", "N", "N", "N", "B", "N", "N"],
        ["Carbassó",    "M", "N", "N", "N", "M", "M", "B", "N", "B", "N", "B", "N", "B"],
        ["Cogombre",    "N", "N", "N", "M", "N", "M", "B", "B", "B", "N", "N", "N", "B"],
        ["Meló/Síndria","N", "N", "N", "M", "M", "N", "N", "N", "N", "N", "N", "N", "B"],
        ["Mongeta",     "M", "M", "B", "B", "B", "N", "N", "M", "N", "B", "N", "N", "B"],
        ["Ceba/All",    "B", "N", "N", "N", "B", "N", "M", "N", "B", "B", "B", "N", "N"],
        ["Enciam",      "B", "B", "N", "B", "B", "N", "N", "B", "N", "B", "N", "N", "N"],
        ["Pastanaga",   "B", "B", "N", "N", "N", "N", "B", "B", "B", "N", "B", "N", "N"],
        ["Bleda/Esp.",  "B", "B", "B", "B", "N", "N", "N", "B", "N", "B", "N", "N", "N"],
        ["Alfàbrega",   "B", "B", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
        ["Dacsa",       "N", "N", "N", "B", "B", "B", "B", "N", "N", "N", "N", "N", "N"]
    ]

    table = Table(matrix)
    
    # Base styling
    style = [
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), # Header top
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'), # Header left
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e5e7eb')), # Top row bg
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#e5e7eb')), # Left col bg
        ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#d1d5db')),
        ('PADDING', (0,0), (-1,-1), 8),
    ]

    # Apply colors based on B, M, N
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            val = matrix[i][j]
            if val == 'B':
                style.append(('BACKGROUND', (j, i), (j, i), colors.HexColor('#dcfce7')))
                style.append(('TEXTCOLOR', (j, i), (j, i), colors.HexColor('#166534')))
            elif val == 'M':
                style.append(('BACKGROUND', (j, i), (j, i), colors.HexColor('#fee2e2')))
                style.append(('TEXTCOLOR', (j, i), (j, i), colors.HexColor('#991b1b')))
            elif val == 'N':
                style.append(('TEXTCOLOR', (j, i), (j, i), colors.HexColor('#9ca3af')))

    table.setStyle(TableStyle(style))
    elements.append(table)
    
    # Footer notes
    elements.append(Spacer(1, 30))
    elements.append(Paragraph(
        "<b>Nota important:</b> Aquesta taula és orientativa. L'èxit pot variar depenent de la qualitat del sòl, el reg i l'exposició solar de la parcel·la.",
        styles['Italic']
    ))
    
    doc.build(elements)
    print("PDF creat amb èxit!")

if __name__ == "__main__":
    create_pdf()
