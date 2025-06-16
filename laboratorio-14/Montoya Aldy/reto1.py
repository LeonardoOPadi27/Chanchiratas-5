import time

test_results = []

def record_test(test_name, condition):
    result = "PASS" if condition else "FAIL"
    test_results.append(f"{result}: {test_name}")

def logarithmic_complexity(n):
    """Count how many times 1 must be doubled to exceed n.
    Returns (count, elapsed_time). Returns (-1, elapsed_time) on invalid input."""
    start = time.time()

    if not isinstance(n, int) or n < 1:
        end = time.time()
        return -1, end - start

    count = 0
    value = 1
    while value <= n:
        value *= 2
        count += 1

    end = time.time()
    elapsed = end - start
    return count, elapsed

def test_o1_1():
    # Test case 1: n = 1 → count = 1
    cnt, _ = logarithmic_complexity(1)
    record_test("Test 1: n=1 → count==1", cnt == 1)

    # Test case 2: n = 10 → count = 4 (1→2→4→8→16)
    cnt, _ = logarithmic_complexity(10)
    record_test("Test 2: n=10 → count==4", cnt == 4)

    # Test case 3: n = 100 → count = 7 (1→...→128)
    cnt, _ = logarithmic_complexity(100)
    record_test("Test 3: n=100 → count==7", cnt == 7)

    # Test case 4: Check return types
    out = logarithmic_complexity(5)
    record_test("Test 4: Return types (int, float)", isinstance(out[0], int) and isinstance(out[1], float))

    # Test case 5: Invalid input (string)
    cnt_err, _ = logarithmic_complexity("a")
    record_test("Test 5: Invalid input string → returns -1", cnt_err == -1)

    # Test case 6: Invalid input (negative)
    cnt_err, _ = logarithmic_complexity(-5)
    record_test("Test 6: Invalid input negative → returns -1", cnt_err == -1)

# Run tests
test_o1_1()

# Show summary
for result in test_results:
    print(result)
