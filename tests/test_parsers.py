# write tests for parsers

from seqparser import (transcribe, reverse_transcribe,
        FastaParser,
        FastqParser)

import pytest
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

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    data_dir = pathlib.Path(__file__).resolve().parent / "data"
    fasta_file = data_dir / "test.fa"

    # Create instance of FastaParser        
    fasta_parser = FastaParser(fasta_file)
    for seq_name, seq in fasta_parser:
        print(seq_name, transcribe(seq))
    # check file type and file content class/type (?)
    
    # check that a few lines of "test.fa" match whats read
    
    # pass


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    
    # Create instance of FastqParser        

    
    # check file type and file content class/type (?)
    
    # check that a few lines of "test.fq" match whats read
    
    
    # pass
