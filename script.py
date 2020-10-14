from Bio.Seq import seq
from Bio.SeqFeature import SeqFeature, Featurelocation
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
def summarize_contents(filename):
record = SeqIO.read(filename, "genbank")
print(record)
summarize_contents(filename)

