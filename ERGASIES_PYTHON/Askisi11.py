try:
    file=input("Πληκτρολόγησε το όνομα του αρχείου: ")
    file+=".txt"
    f = open(file, "r")

    text=(f.read()).split()
    if(len(text)>3):
        triades=[]
        for i in range(len(text)-2):
            triada=""
            for j in range(3):
                triada+=text[i+j].upper()+" "
            triades.append(triada)      

        final_text=""
        for i in triades:
            final_text+=str(i)
        print(final_text)

    else:
        print("Διάλεξε άλλο αρχείο με περισσότερες απο τρείς λέξεις.")
except:
    print("Το αρχείο δεν υπάρχει στο φάκελο.😕")