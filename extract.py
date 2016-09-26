import shutil
import os
if __name__=="__main__":
    file=open("document.xml","r")
    content=file.read()
    list_of_dir=os.listdir()
    for i in list_of_dir:
        if i=="result.txt":
            os.remove("result.txt")
    new_file=open("result.txt","a")
    flag=1
    first=0
    second=0
    threshold=0
    shift=0
    shift_2=0
    while(flag==1):
        first=content.find("</w:rPr>",threshold+1)
        second=content.find("</w:r>",threshold+1)
        hat_1=content.find("<w:t>",first,second)
        if hat_1==-1:
            hat_1 = content.find('<w:t xml:space="preserve">', first, second)
        hat_2=content.find("</w:t>",first,second)
        hat_3=content.find(">",hat_1,second)
        threshold=second
        if second==-1:
            break
        if len(content[hat_3+1:hat_2])==0:
            continue
        new_file.write(content[hat_3+1:hat_2]+"\n")

    new_file.close()
    file.close()

