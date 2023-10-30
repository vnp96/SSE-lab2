from app import process_query


def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") ==\
            "Dinosaurs ruled the Earth 200 million years ago"


def test_your_name():
    assert process_query("What is your name") ==\
            "Vishnu"


def test_largest_number():
    assert process_query("Which of the following numbers \
            is the largest: 21, 29, 84?") == 84


def test_plus():
    assert process_query("What is 41 plus 99?") == \
            140


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"
