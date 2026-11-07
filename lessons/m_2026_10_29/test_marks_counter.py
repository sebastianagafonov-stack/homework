import pytest


def marks_counter(marks):
    good = []
    bad_count = 0
    for mark in marks:
        if mark <= 3:
            bad_count = bad_count + 1
        else:
            good.append(mark)

    if bad_count == 0:
        bad_count = "Ноль"
        
    return good, bad_count


@pytest.mark.parametrize(
    'marks, good, bad_count',
    [
        # (marks, good, bad_count)
        ([5, 3, 4, 5], [5, 4, 5], 1),
        ([5], [5], "Ноль"),
        ([2], [], 1),
        ([4, 5, 3, 2], [4, 5], 2),
    ],
)
def test_marks_counter(marks, good, bad_count):
  good_result, bad_count_result = marks_counter(marks)
  assert (good_result, bad_count_result) == (good, bad_count)