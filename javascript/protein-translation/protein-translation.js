// translate breaks RNA into codons and then translates it to polypeptide
export const translate = (rna) => {
  if (rna == "" || rna == null) {
		return []
  }

  let polypeptide = [];
  let codons = [];
  let rnaDict = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "Stop",
    "UAG": "Stop",
    "UGA": "Stop",
  };

  for (let i = 0; i < rna.length; i += 3) {
    codons.push(rna.substring(i, i + 3));
  }

  for (let codon in codons) {
    if (rnaDict[codons[codon]] == "Stop") {
      break;
    } else if (rnaDict[codons[codon]] == null) {
			throw 'Invalid codon';
		}
		else {
      polypeptide.push(rnaDict[codons[codon]]);
    }
  }
  return polypeptide;
};

/*
console.log(translate("UUUUUU"));
console.log(translate("UUAUUG"));
console.log(translate("AUGUUUUGG"));
console.log(translate("UAGUGG"));
console.log(translate("AUGUUUUAA"));
console.log(translate("UGGUAGUGG"));
console.log(translate("UGGUGUUAUUAAUGGUUU"));
console.log(translate("AAA"));
console.log(translate("XYZ"));
console.log(translate("AUGU"));
console.log(translate("UUCUUCUAAUGGU"));
*/






