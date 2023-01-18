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
        """
        a method to help retrieve test files
        """
    data_dir = pathlib.Path(__file__).resolve().parent.parent / "data"

    if which == "fasta":
        return data_dir / "test.fa"
    else:
        return data_dir / "test.fq"


def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    
    This might not be the most elegant test, but it automates something 
    I usually do when looking at new data. I'd look at the data in its
    raw file, and then print out a line of this file in python to make 
    sure the file has been read properly. in this case, i will store 
    the first sequence found in test.fa and then make sure that my 
    FastaParser class is properly storing that sequence. 
    """

    true_seq = "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA"
        
    fasta_file = get_filepath("fasta")
        
    # Create instance of FastaParser        
    fasta_parser = FastaParser(fasta_file)
    
    # iter over FasterParser object, store sequences
    sequences = []
    for seq_name, seq in fasta_parser:
        sequences.append(seq)
    
    # just check that seq0 is correct; could be extended to check more cases
    assert sequences[0] == true_seq


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    
    I follow the same logic as in test_FastaParser but include the quality values
    """
    
    # ground truth
    true_seq = "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG"
    true_quality = '''*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7"94(>7='(!5"2/!%"4#32='''                                                                                                  
    fastq_file = get_filepath("fastq")
        
    # Create instance of FastqParser        
    fastq_parser = FastqParser(fastq_file)
    
    sequences = []
    qualities = []
    for seq_name, seq, quality in fastq_parser:
        sequences.append(seq)  
        qualities.append(quality)
            
    assert (sequences[0] == true_seq) and (qualities[0] == true_quality)
