# ⌨️ Prompting the researcher to enter the DNA sequence
wheat_DNA =input("please enter the DNA sequence \n").upper()
#Counting Guanine (G) bases in the DNA sequence
guanine_count =wheat_DNA.count("G")
print(f"Total guanine (G) bases found:{guanine_count}")
#Counting Cytosine (C) bases in the DNA sequence
cytosine_count=wheat_DNA.count("C")
print(f"Total cytosine (C) bases found:{cytosine_count }")
# 🧬 Calculating DNA sequence length
length_DNA =len (wheat_DNA )
print (f"DNA length:{length_DNA}bases")
# 📊 Determining the percentage of Guanine and Cytosine
gc_content =((cytosine_count + guanine_count) / length_DNA) * 100
print(f"Calculated GC-Content:{gc_content:.2f}%")
if gc_content > 50:
    print("Result: High GC-Content! This gene structure indicates potential thermal and environmental stability")
else:
    print("Result: Normal GC-Content. Standard environmental stability")
