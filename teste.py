import zipfile, os, pathlib, csv

locatie = pathlib.WindowsPath(r'C:\Users\abamboi\OneDrive - ENDAVA\Documents\DevOPS_work\python\w3resource/')
numele_zip = locatie / "data.zip"
numele_raport = locatie / "summary.csv"
zip_content = zipfile.ZipFile(numele_zip, 'r')

def dezarhivare():
    if os.path.isfile(locatie / numele_zip):
        arhiva = zipfile.ZipFile(numele_zip)
        arhiva.extractall(locatie)
        arhiva.close()
    else:
        print('Arhiva nu exista')

'''
def report():
    if os.path.isfile('data.zip'):
        zip_content = zipfile.ZipFile(numele_zip, 'r')
        print(zip_content.namelist())
        print(range(len(zip_content.namelist())))

    for index in range(len(zip_content.namelist())):
        with open(numele_raport, 'a+') as sumar:
            print(zip_content.namelist())
            fisier = zip_content.namelist()[index]
            sumar.write('\n')
            sumar.write(fisier)
            sumar.close()
    return zip_content
'''
def editeaza_raport():
    with open(numele_raport, 'a+') as raport:
        header = ['Report', 'Pos', 'Neg', 'Tot']
        writer = csv.DictWriter(raport, fieldnames=header)
        writer.writeheader()
        for nume in zip_content():
            coloane = [4,-1]
            nume_raport = nume
            print(nume)
            sum = 0
            for sume in coloane:
                coloane_sum = ssum








'''        
        for index in range(len(zip_content.namelist())):
            fisier = zip_content.namelist()[index]
            print(fisier)
            with open(fisier, 'r') as sumar_read:
                readerCSV = csv.reader(sumar_read)
                columns_to_sum = [2,4,-1]
                for column in readerCSV:
                    sum

            sumar_read.close()
            with open(numele_raport, 'a+') as sumar_write:
                writer = csv.writer(sumar_write)
                nume = str(fisier)
                writer.writerow(nume)
                print(fisier)
            sumar_write.close()

'''

def sterge_fisiere():
    fisiere_de_sters = zipfile.ZipFile(numele_zip, 'r')
    for i in range(len(fisiere_de_sters.namelist())):
        de_sters = fisiere_de_sters.namelist()[i]
        os.remove(locatie / de_sters)
'''
        with open('summary.csv', 'a') as file:
            for fisier in zip.ZipFile('data.zip'):
            file.write("hdfh\n")
            file.close()

    else:
        print("Fisierul zip nu exista")
'''
dezarhivare()
#report()
editeaza_raport()
sterge_fisiere()

