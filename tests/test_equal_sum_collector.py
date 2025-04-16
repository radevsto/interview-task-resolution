import os
import sys
from io import StringIO

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from equal_sum_collector import find_unique_pairs_with_equal_sum  # noqa: E402


def test_find_unique_pairs_with_equal_sum(capsys):
    input_array = [6, 4, 7, 5, 10, 1, 3]

    # Redirect stdout to capture print statements
    find_unique_pairs_with_equal_sum(input_array)

    # Capture the output
    captured = capsys.readouterr()

    # Verify the output
    expected_output = (
        "Pairs : ( 6, 4 ) ( 7, 3 ) have sum : 10\n"
        "Pairs : ( 6, 7 ) ( 10, 3 ) have sum : 13\n"
        "Pairs : ( 6, 5 ) ( 4, 7 ) ( 10, 1 ) have sum : 11\n"
        "Pairs : ( 6, 1 ) ( 4, 3 ) have sum : 7\n"
        "Pairs : ( 6, 3 ) ( 4, 5 ) have sum : 9\n"
        "Pairs : ( 7, 1 ) ( 5, 3 ) have sum : 8\n"
    )

    assert captured.out == expected_output


def test_no_pairs():
    input_array = [1, 2, 3]
    # We expect no output since there are no pairs with the same sum

    output_buffer = StringIO()
    sys.stdout = output_buffer

    find_unique_pairs_with_equal_sum(input_array)

    sys.stdout = sys.__stdout__  # Reset redirect.
    output = output_buffer.getvalue()
    assert output == ""
