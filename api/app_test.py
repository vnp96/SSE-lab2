from app import process_query


def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") ==\
            "Dinosaurs ruled the Earth 200 million years ago"


def test_your_name():
    assert process_query("What is your name") ==\
            "Vishnu"


def test_largest_number():
    assert process_query("Which of the following numbers \
            is the largest: 21, 29, 84?") == "84"


def test_plus():
    assert process_query("What is 41 plus 99?") == \
            "140"


def test_square_cube():
    assert process_query("Which of the following \
            numbers is both a square and a cube: \
            1085, 1796, 343, 3359, 64, 3655,\
            169?") == "64"


def test_mul():
    assert process_query("What is 70 multiplied by 52?") \
            == "3640"


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"
