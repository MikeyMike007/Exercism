# dictionary to be used to translate proteins into codons
protein_to_codon_translator = {
        "Methionine":    ["AUG"],
        "Phenylalanine": ["UUU", "UUC"],
        "Leucine":       ["UUA", "UUG"],
        "Serine":        ["UCU", "UCC", "UCA", "UCG"],
        "Tyrosine":      ["UAU", "UAC"],
        "Cysteine":      ["UGU", "UGC"],
        "Tryptophan":    ["UGG"],
        None:          ["UAA", "UAG", "UGA"]
        }

# a codon has three characters
len_codon = 3


def proteins(strand: str) -> list:
    """
    Create a list of codons to translate from the DNA strand. Translate and return proteins related to the codons.
    """
    codons_to_translate = codonify(strand)
    return translation(codons_to_translate)
    
def codonify(strand: str) -> list:
    """
    Create and return a list of codons from the DNA strand.
    """

    # Loops through the whole string and slices every set of three characters into
    # the list codons
    codons = [strand[index : index + len_codon] for index in range(0,len(strand),len_codon)]
    return codons


def translation(codons_to_translate: list) -> list:
    """
    Translate codons into proteins. Return the proteins in a list.
    """
    proteins_translated = []
    
    # loop through all the codons that are about to be translated
    for codon in codons_to_translate:

        # loop though the protein_to_codon_translator and save the protein that
        # relates to the codon
        translated_protein = [protein for protein in protein_to_codon_translator if codon in protein_to_codon_translator[protein]]

        # break the loop if the protein is the "stop" protein i.e. None
        if not translated_protein[0]:
            break

        # append the list proteins_translated
        proteins_translated.append(translated_protein[0])

    return proteins_translated
