from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(file_name, order_number, client, products):
    """
    Creates a PDF file with the given order details.

    Parameters:
        file_name (str): The name of the output file (including .pdf extension).
        order_number (int): Order number.
        client (dict): Client info as dictionary {'Name': str, 'Address': str}
        products (list): List of dictionaries representing products. Keys should include ['Product Name', 'Price']. Example structure:
                           [{'Product Name': 'Product 1', 'Price': '$50'}, ...]
    """
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Custom Heading3-like style
    h3_custom_style = styles["Heading3"]
    h3_custom_style.fontSize -= 2

    # Add the title as a heading
    h1_style = styles["Title"]
    h1_title = f"<font size=24><center>Order n° {order_number}</center></font>"
    elements.append(Paragraph(h1_title, h1_style))
    elements.append(Spacer(1, 16))

    # Add the client information as a subheading
    h3_client_label = "<font size=12><b>Client:</b></font>"
    h3_address_label = "<font size=12><b>Address:</b></font>"
    h3_client = f"{h3_client_label} <font size=12>{client['Name']}</font>"
    h3_address = f"{h3_address_label} <font size=12>{client['Address']}</font>"
    elements.append(Paragraph(h3_client, h3_custom_style))
    elements.append(Spacer(1, 8))
    elements.append(Paragraph(h3_address, h3_custom_style))
    elements.append(Spacer(1, 16))

    doc.build(elements)


if __name__ == "__main__":
    create_pdf("sample.pdf", 12345, {"Name": "Jane Smith", "Address": "123 Main St"},
               [{"Product Name": "Product 1", "Price": "50"}, {"Product Name": "Product 2", "Price": "100"}])