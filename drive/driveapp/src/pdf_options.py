from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(file_name, title, author, body):
    """
    Creates a PDF file with the given title and body.

    Parameters:
        file_name (str): The name of the output file (including .pdf extension).
        title (str): The title of the document.
        author (str): The author of the document.
        body (list): A list of strings containing the content of the document.
            Each string will be displayed on its own line.
    """
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Add the title as a heading
    h1_style = styles["Heading1"]
    h1_title = "<font size=24>%s</font>" % title
    elements.append(Paragraph(h1_title, h1_style))
    elements.append(Spacer(1, 12))

    # Add the author as a subheading
    h3_style = styles["Heading3"]
    h3_author = "<font size=12>Author: %s</font>" % author
    elements.append(Paragraph(h3_author, h3_style))
    elements.append(Spacer(1, 12))

    # Add each line from the body as a separate paragraph
    for text in body:
        p_style = styles["BodyText"]
        p = Paragraph(text, p_style)
        elements.append(p)
        elements.append(Spacer(1, 12))

    doc.build(elements)


if __name__ == "__main__":
    create_pdf("sample.pdf", "My Title", "John Doe", ["Line one.", "Line two."])