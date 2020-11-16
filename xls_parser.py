import xlrd
import glob

# C:\Users\LumináT\Desktop\spp ftizol

all_books = glob.glob('*.xls')
file_count = 0
total_meters = 0
error_books = []
empty_books = []

for book in all_books:
    try:
        workbook = xlrd.open_workbook(book)
        worksheet = workbook.sheet_by_index(0)
        if(worksheet.cell(6, 3).value == ""):
            empty_books.append(book)

        total_meters += worksheet.cell(6, 3).value
        file_count += 1

    except:
        error_books.append(book)
        #print("fucked up")


print("Celkově navrtaných metrů v SOUPIS PROVEDENÝCH PRACÍ: " + str(total_meters))
print("Celkový počet dokumentů: " + str(len(all_books)))
print("z nich se mi podařilo analyzovat " + str(file_count) + " dokumentů")
print("Tyto se mi nepovedly:")
print(*empty_books, sep = "\n")

print(*error_books, sep = "\n")
