from fpdf import FPDF
import glob
import os

pdf = FPDF(orientation="P", unit="mm", format="A4")  # set up a single pdf file object

filepaths = glob.glob("text_files/*txt")  # add all .txt files to the variable filepaths

for filepath in filepaths:
    file = os.path.basename(filepath)  # extract filename
    filename = file.split('.')[0]

    file = open(filepath)  # extract the file content to a variable
    content = file.read()
    print(content)
    print()

    pdf.add_page()  # create pdf page
    pdf.set_font(family="Times", size=16, style="B")  # set the font
    pdf.cell(w=50, h=8, txt=filename.capitalize(), ln=1)
    # add a cell containing the extracted filename capitalized, ln=1 prepares a break for next cell

    pdf.set_font(family="Times", size=12)  # set the font
    pdf.multi_cell(w=0, h=6, txt=content)


pdf.output("output.pdf")
