print('Example Project of Data Mining with Python')

#open the data file
files = open('datas.csv', 'r')

#Read the file and splits its' lines
lines = files.read().splitlines()

#denoting every lines to a single variable
kovid = lines[1]
spandan = lines[2]
rohan = lines[3]
subash = lines[4]
anuj = lines[5]
bibek = lines[6]
pratik = lines[7]
samir = lines[8]
akshaya = lines[9]
acp = lines[10]

#Printing the data of the files
print("Name : " + kovid[5:10]  + "      , "  +  "    Roll no : " + kovid[11])

print("Name : " + spandan[9:16]  + "    , "  +  "    Roll no : " + spandan[17])

print("Name : " + rohan[8:13]  + "      , "  +  "    Roll no : " + rohan[14])

print("Name : " + subash[10:16]  + "     , "  +  "    Roll no : " + subash[17])

print("Name : " + anuj[7:11]  + "       , "  +  "    Roll no : " + anuj[12])

print("Name : " + bibek[7:12]  + "      , "  +  "    Roll no : " + bibek[13])

print("Name : " + pratik[4:10]  + "     , "  +  "    Roll no : " + pratik[11])

print("Name : " + samir[8:13]  + "      , "  +  "    Roll no : " + samir[14])

print("Name : " + akshaya[8:15]  + "    , "  +  "    Roll no : " + akshaya[16])

print("Name : " + acp[6:15]  + "  , "  +  "    Roll no : " + acp[16:18])


input('Press Enter Key To Exit!')

