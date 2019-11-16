from case_study_code import VignereCipher
from case_study_code import combine_character
from case_study_code import separate_character


def test_encode():
    cipher = VignereCipher("TRAIN")
    encoded = cipher.encode("ENCODEDINPYTHON")
    assert encoded == "XECWQXUIVCRKHWA"

def test_encode_character():
    cipher = VignereCipher("TRAIN")
    encoded = cipher.encode("E")
    assert encoded == "X"

def test_encoded_spaces():
    cipher = VignereCipher("TRAIN")
    encoded = cipher.encode("ENCODED IN PYTHON")
    assert encoded == "XECWQXUIVCRKHWA"

def test_encoded_lowercase():
    cipher = VignereCipher("TRain")
    encoded = cipher.encode("encoded in python")
    assert encoded == "XECWQXUIVCRKHWA"

def test_combine_character():
    assert combine_character("E", "T") == "X"
    assert combine_character("N", "R") == "E"

def test_extend_keyword():
    cipher = VignereCipher("TRAIN")
    extended = cipher.extend_keyword(16)
    assert extended == "TRAINTRAINTRAINT"

def test_separate_character():
    assert separate_character("X", "T") == "E"
    assert separate_character("E", "R") == "N"

def test_decode():
    cipher = VignereCipher("TRAIN")
    encoded = cipher.decode("XECWQXUIVCRKHWA")
    assert encoded == "ENCODEDINPYTHON"

