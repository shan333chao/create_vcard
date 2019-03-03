import vobject
import os
from random_name import random_chinese_name

def get_vcard(contact):
    card = vobject.vCard()
    card.add('fn')
    card.fn.value = contact['fullname']
    card.add('n')
    card.n.value = vobject.vcard.Name(
        contact['last_name'], contact['first_name'])
    card.add('tel')
    card.tel.type_param = 'cell'
    card.tel.value = contact['contact_no']
    return card.serialize()

def read_folder(folder_path):
    db_all = []
    for parent, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.txt':
                file_path = os.path.join(parent, filename)
                db_all.append(file_path)
    return db_all



def convert_xlsx_to_vcard(txtfile):
    vcf_file=''

    file_object = open(txtfile,'rU')
    try: 
        for line in file_object:
            chinese_name=random_chinese_name()
            first_name=chinese_name[0:1]
            last_name=chinese_name[1:]
            contact = {
                'fullname': '',
                'first_name': '',
                'last_name': '',
                'contact_no': line.rstrip()
            }
            vcf_file += get_vcard(contact)
    finally:
        file_object.close() 
    return vcf_file

def create_vcard(folderPath):
    files= read_folder(folderPath)
    if len(files) == 0:
        print('no number files')   
        return
    for f in files:
        vcf_file = convert_xlsx_to_vcard(f)
        vcf_file_name=f+".vcf"
        with open(vcf_file_name,"w") as writer:
            writer.writelines(vcf_file)
        writer.close()





create_vcard("C:\\Users\\Administrator\\Desktop\\newcard")


 
