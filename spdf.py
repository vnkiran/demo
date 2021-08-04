import PyPDF2
import json
import pdfx


file = open("bs.pdf", "rb")
reader = PyPDF2.PdfFileReader(file)
print(reader.numPages)
page = reader.getPage(1)
pdfData = page.extractText()


print(type(pdfData))



for i in range(reader.numPages):
 page1 = reader.getPage(i)
 print(page1.extractText())
 #print(page1)




'''
page_data = get_data(pdfData)
json_data = json.dumps(page_data, indent=4)
print(json_data)'''
# or, instead of those last 3 lines, just do this:

# print(json.dumps(get_data(page_content), indent=4))
