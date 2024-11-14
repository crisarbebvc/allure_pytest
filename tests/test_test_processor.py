import pytest  
from test_processor.test_processor import (  
    count_words,  
    reverse_string,  
    is_palindrome,  
    capitalize_text,  
)  
  
  
def test_count_words():  
    assert count_words("hello world") == 2  
    assert count_words("") == 0  
    assert count_words("one") == 1  
  
  
def test_reverse_string():  
    assert reverse_string("abc") == "cba"  
    assert reverse_string("hello") == "olleh"  
    assert reverse_string("") == ""  
  
  
def test_is_palindrome():  
    assert is_palindrome("A man a plan a canal Panama") is True  
    assert is_palindrome("Hello") is False  
    assert is_palindrome("RaC eCar") is True  
    assert is_palindrome("") is False  
  
  
@pytest.mark.parametrize( "text, expected",  
    [  
        ("hello", "Hello"),  
        ("HELLO", "Hello"),  
        ("123", "123"),  
        ("", False),  
        (None, False),  
    ],)  
def test_capitalize_text(text, expected):  
    assert capitalize_text(text) == expected
