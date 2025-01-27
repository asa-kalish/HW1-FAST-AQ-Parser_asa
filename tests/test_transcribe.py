# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)


SEQ = "ACTGAACCC"

def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    
    I check that the transcribe function can correctly 
    transcribe a given sequence
    """
    assert transcribe(SEQ) == "UGACUUGGG"


def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    
    I check that the reverse_transcribe function can correctly 
    provide a reversed transcription of a given sequence
    """
    assert reverse_transcribe(SEQ) == "GGGUUCAGU"
