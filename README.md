# uniqseq
Remove duplicated protein/nucleic acid sequences, keeping the first occurrence.

## Usage
`uniqseq [-h] [-f {fasta,clustal,embl,genbank,imgt,phd,pir,tab}] [-v]
               [inseqfile] [outseqfile]`

It works like the Unix 'uniq' command, but for sequences and it does not require any previous sorting. It can be inserted in command pipes.

## Dependencies
* Python3
* Biopython

## Installation
This is a Python script, so, you can just run the uniqseq.py file or put a symbolic link in any directory of your PATH (e.g. /usr/local/bin). The second option is recommend.

## OSs
It runs in Linux, probably in Mac OS too, but not tested.

## Examples

`uniqseq input_redundant_seqs.fasta output_uniq_seqs.fasta`

`uniqseq input_redundant_seqs.pir output_seqs.pir -f pir`

`cat redundant_seqs.fasta | uniqseqs > uniq_seqs.fasta`

