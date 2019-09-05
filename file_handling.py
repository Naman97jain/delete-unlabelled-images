import os
import sys
path = sys.argv[1]
#path = "/home/invlab/Desktop/kunal_demand"

file_list_txt = []
file_list_jpg = []
deleted_list = []

total = 0
count_empty_txt = 0
count_jpg_without_txt = 0
count_txt_without_jpg = 0

print("All txt files")
for r,d,f in os.walk(path):
    for files in f:
        if  files.endswith('.txt'):
            file_list_txt.append(files)

print(file_list_txt)

print("All jpg files")
for r,d,f in os.walk(path):
    for files in f:
        if files.endswith('.jpg'):
            file_list_jpg.append(files)

print(file_list_jpg)

print("Deleting those jpg whose txt is not present")
for f in file_list_jpg:
    x = f[:-4:] + '.txt'
    if x not in file_list_txt:
        count_jpg_without_txt += 1
        deleted_list.append(f)

print(deleted_list)


print("Deleting those txt whose jpg is not present")
for f in file_list_txt:
    x = f[:-4:] + '.jpg'
    if x not in file_list_jpg:
        count_txt_without_jpg += 1
        deleted_list.append(f)

print(deleted_list)

print("Removing undesirable files")
for f in file_list_txt:
    x = f[:-4:] + '.jpg'
    if os.stat(os.path.join(path,f)).st_size == 0:
        if x in file_list_jpg:
            count_empty_txt += 1
            deleted_list.append(f)
            deleted_list.append(x)


print(deleted_list)
total = count_empty_txt + count_jpg_without_txt + count_txt_without_jpg
print("You have these unwanted files: ",total)
print("TXT(s) with no corresponding JPG(s): ",count_txt_without_jpg)
print("JPG(s) with no corresponding TXT(s): ",count_jpg_without_txt)
print("Empty TXT(s) having corresponding JPG(s)): ",count_empty_txt)

answer = input("Do you want to proceed for deletion Y/N? If you will proceed then it cannot be undone. ")
# print(answer)
if answer[0].lower()=='y':
    for f in deleted_list:
        os.remove(os.path.join(path,f))
        print("File Deleted ",os.path.join(path,f))
else:
    print("Exiting without any deletion")


























#     elif x not in file_list_jpg:
#         print("running when not in jpg")
#         #os.remove(os.path.join(path,f))
#         print("file removed",os.path.join(path,f))
#         file_list_txt.remove(f)

# print(file_list_jpg)
# print(file_list_txt)

# while file_list_jpg:
#     f = file_list_jpg[0]
#     y = f[-5::-1]
#     y = y + '.txt'
#     if y not in file_list_txt:
#         #os.remove(os.path.join(path,f))
#         print("file removed",os.path.join(path,f))
#         file_list_jpg.remove(f)
#         print(file_list_jpg)
#         print(file_list_txt)