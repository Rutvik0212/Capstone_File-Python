# Note : Your system should have 'fpdf' module install otherwise the code will throw an Error.
# To install this module just type "pip install fpdf" in your command prompt your are using.

from fpdf import FPDF 

# assing f as FPDF class
f = FPDF()

# While creating a pdf it consit of zero pages 
# so add new page 
f.add_page()

# setting font style and its size
f.set_font('Arial', size = 14)

# opening a txt file to read 
with open('sample.txt' , 'r') as file:
    
    # setting pointer to initial position
    file.seek(0)
    
    # reading line by line from given file
    for line in file:
        
        # adding line to pdf 
        f.cell(10,10, txt = line, ln = 1) 
    
# Saving pdf file 
f.output('sample.pdf')