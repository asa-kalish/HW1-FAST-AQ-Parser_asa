# write tests for parsers

from seqparser import (transcribe, reverse_transcribe,
        FastaParser,
        FastqParser)

import pathlib
def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

def get_filepath(which):
    data_dir = pathlib.Path(__file__).resolve().parent.parent / "data"
    if which == "fasta":
        return data_dir / "test.fa"
    else:
        return data_dir / "test.fq"

def open_fastq_reference():
    f = pathlib.Path(__file__).resolve().parent / "fastq-check.txt"
    with f.open() as f:
        seqs = list(map(lambda l: l.strip().split("|"), f.readlines()))
    return seqs  # will be list of lists with seq, quality that were parsed from the test files using get-seq.sh

def open_fasta_reference():
    f = pathlib.Path(__file__).resolve().parent / "fasta-check.txt"
    with f.open() as f:
        seqs = list(map(lambda l: l.strip(), f.readlines()))
    return seqs  # will be a list of seqs, quality that were parsed from the test files using get-seq.sh


def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
# i know that seq0 is TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA
    groundtruth = "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA"
        
    fasta_file = get_filepath("fasta")
        
    # Create instance of FastaParser        
    fasta_parser = FastaParser(fasta_file)
    
    sequences = []
    for seq_name, seq in fasta_parser:
        sequences.append(seq)
            
    assert sequences[0] == groundtruth
    # pass


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    
    # ground truth
    true_seq = "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG"
    true_quality = "*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7"94(>7='(!5"2/!%"4#32="
                                                                                                      
    fastq_file = get_filepath("fastq")
        
    # Create instance of FastqParser        
    fastq_parser = FastqParser(fastq_file)
    
    sequences = []
    qualities = []
    for seq_name, seq, quality in fastq_parser:
        sequences.append(seq)
        qualities.append(quality)
        
            
    assert (sequences[0] == true_seq) and (qualities[0] == true_quality) 
