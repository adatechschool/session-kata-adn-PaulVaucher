from conversion import conversion_dict #Import du fichier conversion, transformé en dictionnaire

adn_file = open('adn', 'r') #Récuperer le fichier ADN

string_to_split = adn_file.read() #Lire le fichier ADN

# Transformer ADN en list de codons
codons_list = [(string_to_split[i:i+3]) for i in range(0, len(string_to_split), 3)]

#print(codons_list)

def protein_translation ():
    protein_array = conversion_dict.values()
    protein_list = ''.join(protein_array)
    print(protein_list)

protein_translation()

consensus_split = [(string_to_split[i:i+25]) for i in range(0, len(string_to_split), 25)]
print(type(consensus_split))

cleaned_list = [(consensus_split[i:i+5] for i in range(0, len(consensus_split), 5))]
print(cleaned_list)

