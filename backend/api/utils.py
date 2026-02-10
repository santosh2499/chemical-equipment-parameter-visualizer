"""
Utility functions for API operations
"""
import pandas as pd
from io import BytesIO
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from datetime import datetime


def process_csv_file(file_path):
    """
    Process CSV file and return DataFrame
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise ValueError(f"Error reading CSV file: {str(e)}")


def validate_csv_columns(df, required_columns):
    """
    Validate that DataFrame has required columns
    """
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
    return True


def generate_pdf_report(dataset):
    """
    Generate PDF report for a dataset
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                           rightMargin=72, leftMargin=72,
                           topMargin=72, bottomMargin=18)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1a237e'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#283593'),
        spaceAfter=12,
        spaceBefore=12
    )
    
    # Title
    title = Paragraph("Chemical Equipment Analysis Report", title_style)
    elements.append(title)
    elements.append(Spacer(1, 12))
    
    # Dataset Information
    info_data = [
        ['Dataset Name:', dataset.name],
        ['Upload Date:', dataset.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')],
        ['Total Equipment:', str(dataset.total_count)],
        ['Uploaded By:', dataset.user.username],
    ]
    
    info_table = Table(info_data, colWidths=[2*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e8eaf6')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    
    elements.append(info_table)
    elements.append(Spacer(1, 20))
    
    # Summary Statistics
    elements.append(Paragraph("Summary Statistics", heading_style))
    
    stats_data = [
        ['Parameter', 'Average', 'Unit'],
        ['Flowrate', f"{dataset.avg_flowrate:.2f}", 'L/min'],
        ['Pressure', f"{dataset.avg_pressure:.2f}", 'bar'],
        ['Temperature', f"{dataset.avg_temperature:.2f}", '°C'],
    ]
    
    stats_table = Table(stats_data, colWidths=[2*inch, 2*inch, 2*inch])
    stats_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3f51b5')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(stats_table)
    elements.append(Spacer(1, 20))
    
    # Equipment Type Distribution
    elements.append(Paragraph("Equipment Type Distribution", heading_style))
    
    type_data = [['Equipment Type', 'Count', 'Percentage']]
    for eq_type, count in dataset.equipment_types.items():
        percentage = (count / dataset.total_count) * 100
        type_data.append([eq_type, str(count), f"{percentage:.1f}%"])
    
    type_table = Table(type_data, colWidths=[2.5*inch, 1.5*inch, 1.5*inch])
    type_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3f51b5')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(type_table)
    elements.append(Spacer(1, 20))
    
    # Equipment Details (first 20 items)
    elements.append(Paragraph("Equipment Details (Sample)", heading_style))
    
    equipment_data = [['Name', 'Type', 'Flow', 'Pressure', 'Temp']]
    equipment_list = dataset.equipment.all()[:20]
    
    for eq in equipment_list:
        equipment_data.append([
            eq.equipment_name[:25],  # Truncate long names
            eq.equipment_type[:15],
            f"{eq.flowrate:.1f}",
            f"{eq.pressure:.1f}",
            f"{eq.temperature:.1f}"
        ])
    
    eq_table = Table(equipment_data, colWidths=[2*inch, 1.5*inch, 1*inch, 1*inch, 1*inch])
    eq_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3f51b5')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(eq_table)
    
    if dataset.total_count > 20:
        elements.append(Spacer(1, 12))
        note = Paragraph(
            f"<i>Note: Showing 20 of {dataset.total_count} total equipment items</i>",
            styles['Normal']
        )
        elements.append(note)
    
    # Footer
    elements.append(Spacer(1, 30))
    footer_text = f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    footer = Paragraph(footer_text, styles['Normal'])
    elements.append(footer)
    
    # Build PDF
    doc.build(elements)
    
    buffer.seek(0)
    return buffer
