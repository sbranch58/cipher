from cipher import *  

def test_getChar_hi():
    assert getChar("Hi") == ["H", "i"]

def test_getChar_punctuation():
    assert getChar("Happy Birthday! :)") == ["H", "a", "p", "p", "y", " ", "B", "i", "r", "t", "h", "d", "a", "y", "!", " ", ":", ")"]

def test_generatePad_length_10():
    assert len(generatePad("0123456789")) == 10

def test_generatePad_length_26():
    assert len(generatePad("abcdefghijklmnopqrstuvwxyz")) == 26

def test_generatePad_random():
    assert generatePad("asdfghjnhbvvomafibhfq") != generatePad("tmsgkjcbvcvbnmkiuytr")

def test_generatePad_random2():
    assert generatePad("asdfghjnhbvvomafibhfq") != generatePad("asdfghjnhbvvomafibhfq")

def test_decipher():
    assert decipher("encrypted-message.txt", "pad.txt") == readFile("sbranch58-decrypted-message.txt")