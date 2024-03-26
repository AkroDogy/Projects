from PIL import Image, ImageDraw, ImageFont

def copy_photo(name_cv):
    try:
        with open("bin/example.jpg", "rb") as f:
            image = Image.open(f)
            image.save(f"export/{name_cv}.jpg")
        print(f">> CV-ul tau s-a initializat, poti adauga celelalte date. (Nume cv: {name_cv}.jpg)")
    except Exception as err:
        print(f">> Eroare: {err}")


def adaugare_date():
    ed_1_name_cv = ""
    ed_1_an_cv = ""
    ed_2_name_cv = ""
    ed_2_an_cv = ""
    lang_1_cv = ""
    lang_2_cv = ""
    lang_3_cv = ""
    hobby_cv = ""
    work_cv = ""
    work_an_cv = ""
    name_cv=input(">> Adauga Numele tau complet: ")
    born_cv=input(">> Adauga anul,luna si data in care te-ai nascut (EX: zz.ll.an): ")
    temp_1 = input(">> Care este ultima forma de educatie pe care ai terminat-o? \n(1 - Liceu, 2 - Facultate)\nSelecteaza numarul 1 sau 2: ")
    while temp_1 not in ['1', '2']:
        print(">> Optiunea selectata nu este valida. Te rugam sa selectezi 1 sau 2.")
        temp_1 = input(">> Selecteaza numarul 1 sau 2: ")
    if temp_1 == '1':
        ed_1_name_cv = input(">> Care este numele liceului pe care l-ai terminat?: ")
        ed_1_an_cv = input(">> Care este perioada în care ai facut liceul?: ")
    elif temp_1 == '2':
        ed_1_name_cv = input(">> Care este numele liceului pe care l-ai terminat?: ")
        ed_1_an_cv = input(">> Care este perioada în care ai facut liceul?: ")
        ed_2_name_cv = input(">> Care este numele facultatii pe care ai terminat-o?: ")
        ed_2_an_cv = input(">> Care este perioada în care ai facut facultatea?: ")
    temp_2 = input(">> Cate limbi cunosti? (Max 3):")
    while temp_2 not in ['1', '2', '3']:
        print(">> Optiunea selectata nu este valida. Te rugam sa selectezi 1 sau 2 sau 3.")
        temp_2 = input(">> Selecteaza numarul 1 sau 2 sau 3: ")
    if temp_2 == '1':
        lang_1_cv = input(">> Limba 1: ")
    elif temp_2 == '2':
        lang_1_cv = input(">> Limba 1: ")
        lang_2_cv = input(">> Limba 2: ")
    elif temp_2 == '3':
        lang_1_cv = input(">> Limba 1: ")
        lang_2_cv = input(">> Limba 2: ")
        lang_3_cv = input(">> Limba 3: ")
    tari_cv=input(">> Ce tari ai vizitat?: ")
    cert_cv=input(">> Ce diplome si certificate ai obtinut?: ")
    empl_cv=input(">> Introduceti postul ocupat: ")
    num_cv=input(">> Numar telefon: ")
    adress_cv=input(">> Adresa ta: ")
    email_cv=input(">> Email-ul tau: ")
    hobby_cv = input(">> Spune-ne cate ceva despre tine (max 100 cuvinte): ")
    work_cv = input(">> La ce firma ai lucrat si ce ai facut acolo: ")
    work_an_cv = input(f">> Spune-ne perioada in care ai lucrat: ")
    copy_photo(name_cv)
    creare_cv(name_cv,num_cv,adress_cv,email_cv,born_cv,ed_1_name_cv,ed_1_an_cv,ed_2_name_cv,ed_2_an_cv,lang_1_cv,lang_2_cv,lang_3_cv,tari_cv,cert_cv,empl_cv,hobby_cv,work_cv,work_an_cv)
    return ">> Te rog sa astepti..."

def fix(text, cuvinte_pe_rand=50):
    cuvinte = text.split()
    text_formatat = []
    for i in range(0, len(cuvinte), cuvinte_pe_rand):
        rand = ' '.join(cuvinte[i:i+cuvinte_pe_rand])
        text_formatat.append(rand)
    return text_formatat
def creare_cv(name_cv,num_cv,adress_cv,email_cv,born_cv,ed_1_name_cv,ed_1_an_cv,ed_2_name_cv,ed_2_an_cv,lang_1_cv,lang_2_cv,lang_3_cv,tari_cv,cert_cv,empl_cv,hobby_cv,work_cv,work_an_cv):
    img = Image.open(f"export/{name_cv}.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 25)
    draw.text((147, 561), num_cv, font=font)
    draw.text((147, 653), email_cv, font=font)
    draw.text((147, 750), adress_cv, font=font)
    draw.text((544, 139), name_cv, fill=(0, 0, 0), font=ImageFont.truetype("arial.ttf", 50))
    draw.text((544, 202), empl_cv, fill=(0, 0, 0), font=ImageFont.truetype("arial.ttf", 30))
    hobby_cv_formatat = fix(hobby_cv)
    y_1 = 255
    for line_1 in hobby_cv_formatat:
        draw.text((544, y_1), line_1, fill=(0, 0, 0), font=ImageFont.truetype("arial.ttf", 25))
        y_1 += 30
    draw.text((544, 1772), f"Data nasterii: {born_cv}", fill=(0, 0, 0), font=ImageFont.truetype("arial.ttf", 25))
    draw.text((89, 942), ed_1_an_cv, font=font)
    draw.text((89, 989), ed_1_name_cv, font=font)
    draw.text((89, 1067), ed_2_an_cv, font=font)
    draw.text((89, 1115), ed_2_name_cv, font=font)
    draw.text((89, 1773), lang_1_cv, font=font)
    draw.text((122, 1318), cert_cv, font=font)
    draw.text((89, 1817), lang_2_cv, font=font)
    draw.text((89, 1861), lang_3_cv, font=font)
    draw.text((584, 545), f"Tari vizitate: {tari_cv}",fill=(0, 0, 0), font=font)
    draw.text((584, 921), work_an_cv,fill=(0, 0, 0), font=font)
    work_cv_formatat = fix(work_cv)
    y_2 = 974
    for line_2 in work_cv_formatat:
        draw.text((584, y_2), line_2, fill=(0, 0, 0), font=ImageFont.truetype("arial.ttf", 25))
        y_2 += 30
    img.save(f"export/{name_cv}_output.jpg")


if __name__ == "__main__":
    adaugare_date()
