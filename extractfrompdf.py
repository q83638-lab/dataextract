import PyPDF2 as p
import io
import urllib.request
file1 =urllib.request.urlopen('https://www.student.cs.uwaterloo.ca/~cs341/lectures/lecture-1-intro/lecture-1-intro.pdf')
#initalize a pdfile reader object, read into memory
pd= p.PdfFileReader(io.BytesIO(file1.read()))
#
x = pd.getPage(0)
y = pd.getPage(1)
print(y.extractText())
