from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

# Ruta donde se encuentra el archivo en formato GenBank del escritorio (Hepacivirus C)
filename = "/mnt/c/Users/cesar/Desktop/bioinformatica/sequence.gb" 

def summarize_contents(filename):
	listA = []
	listA = os.path.split(filename)
	print("file:", listA[1], "\npath:", listA[0])
	all_records = []
	records = list(SeqIO.parse(filename, "genbank"))
	print("num_records = %i records" % len(records))
	print("records:")
	for seq_record in SeqIO.parse(filename, "genbank"):
		all_records.append(seq_record.name)
		print("- id:",seq_record.id)
		print("name: ", seq_record.name)
		print("description: ", seq_record.description)
		print("\n")
		
		summarize_contents(filename)
