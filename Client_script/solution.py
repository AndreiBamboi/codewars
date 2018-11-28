import zipfile, os, pathlib, csv # to be able to manipulate zip, os paths locations and csv

#This will unzip the file
def unzip(path, zipname):
    location= pathlib.WindowsPath(path) # i have used this because i am working on a Windows machine
    zip_path=location / zipname
    if os.path.isfile(location / zip_path):
        arhiva = zipfile.ZipFile(zip_path)
        arhiva.extractall(location)
        arhiva.close()
        return print(zipname ,' found in', path, 'have been succesfully unziped')
    else:
        print('The archive doesnt exist')

#This function create the report and manage files based on the zip content
def create_csv (path,zipname,columns):
    location = pathlib.WindowsPath(path)
    ziplist = zipfile.ZipFile(location / zipname, 'r')
    if len(ziplist.namelist()) >= 0 : # I have put this if statement not to continue if the zip file is empty, i dont see the reason to continue....
        report = open('summary.csv', 'w')  # Create the the summary report with specified headers
        fieldnames = ['report', 'pos', 'neg', 'tot']
        writer = csv.DictWriter(report, fieldnames)
        writer.writeheader()
        for filename in ziplist.namelist():
            pos = 0
            neg = 0
            tot = 0
            zip_content = open(filename, 'r')
            csv_reader = csv.reader(zip_content)
            keynames = csv.DictReader(zip_content).fieldnames
            included_cols = columns
            for row in csv_reader:
                content = list(row[i] for i in included_cols)
                pos_values = content[0]
                neg_values = content[1]
                tot_values = content[2]
                print(pos_values, neg_values, tot_values)
                for c in pos_values:
                    pos = pos + int(c)
                for c in neg_values:
                    neg = neg + int(c)
                for c in tot_values:
                    tot = tot + int(c)
            writer.writerow({'report':filename, 'pos':pos, 'neg':neg, 'tot':tot})
            print (pos, neg, tot)
    else:
        print('Zip file is empty')

# After the report is build, i thought to clean the directory only for files that were contained by zip archive
def delete_extracted_csv(path, zipname): # i havent put any if statement here, no reason why because will delet only the files extracted from zip.
    location = pathlib.WindowsPath(path)
    zip = location / zipname
    csv_to_delete = zipfile.ZipFile(zip, 'r')
    for i in range(len(csv_to_delete.namelist())):
        list_to_remove = csv_to_delete.namelist()[i]
        os.remove(location/ list_to_remove)

#Bellow i have called the functions. I wanted to put all togheter in a class and make it more robust and simple to use, but i think this is just enough....
unzip('C:/Users/abamboi/PycharmProjects/codewars/Client_script/', 'data.zip')
create_csv('C:/Users/abamboi/PycharmProjects/codewars/Client_script/', 'data.zip',[3, 4, -1])
delete_extracted_csv('C:/Users/abamboi/PycharmProjects/codewars/Client_script/', 'data.zip')

