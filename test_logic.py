from lotto import check_winning

winning = [1, 2, 3, 4, 5, 6]
bonus = 7

# Test 1st place
assert check_winning([1, 2, 3, 4, 5, 6], winning, bonus) == "1등"
# Test 2nd place
assert check_winning([1, 2, 3, 4, 5, 7], winning, bonus) == "2등"
# Test 3rd place
assert check_winning([1, 2, 3, 4, 5, 8], winning, bonus) == "3등"
# Test 4th place
assert check_winning([1, 2, 3, 4, 8, 9], winning, bonus) == "4등"
# Test 5th place
assert check_winning([1, 2, 3, 8, 9, 10], winning, bonus) == "5등"
# Test Fail
assert check_winning([1, 2, 8, 9, 10, 11], winning, bonus) == "꽝"

print("All tests passed!")
