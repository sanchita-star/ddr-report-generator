import PyPDF2

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def extract_observations(text):
    areas = ["kitchen", "roof", "bathroom", "wall", "ceiling"]

    extracted = {}

    for area in areas:
        if area in text.lower():
            extracted[area] = f"Issue detected in {area}"

    return extracted