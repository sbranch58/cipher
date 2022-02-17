#in last class mentioned getting wrong/red results first so I made a file with wrong results since I can't do a before test with functions since they were made from a previous homework 

from cipher import * 

def test_getChar_wrong():
    assert getChar("Hi") == ["H", "i", "!"]

def test_generatePad_length_10_wrong():
    assert len(generatePad("0123456789101112131415")) == 10

def test_generatePad_length_26():
    assert len(generatePad("abcdefghijklmnopqrstuvwxyz")) == 43