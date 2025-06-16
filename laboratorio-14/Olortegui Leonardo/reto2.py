import time

test_results = []

def record_test(test_name, condition):
    result = "PASS" if condition else "FAIL"
    test_results.append(f"{result}: {test_name}")

def constant_sum(n):
    """Calculate the sum of the first n natural numbers in constant time.
    Returns (sum, elapsed_time). If input invalid, returns (-1, elapsed_time)."""
    start = time.time()

    if not isinstance(n, int) or n < 0:
        end = time.time()
        return -1, end - start

    total = n * (n + 1) // 2

    end = time.time()
    elapsed = end - start
    return total, elapsed

def test_o1_2():
    # Test case 1: n = 0 → sum = 0
    s, _ = constant_sum(0)
    record_test("Test 1: n=0 → sum==0", s == 0)

    # Test case 2: n = 1 → sum = 1
    s, _ = constant_sum(1)
    record_test("Test 2: n=1 → sum==1", s == 1)

    # Test case 3: n = 10 → sum = 55
    s, _ = constant_sum(10)
    record_test("Test 3: n=10 → sum==55", s == 55)

    # Test case 4: Check return types
    out = constant_sum(5)
    record_test("Test 4: Return types (int, float)", isinstance(out[0], int) and isinstance(out[1], float))

    # Test case 5: Invalid input (string)
    s_err, _ = constant_sum("a")
    record_test("Test 5: Invalid input string → returns -1", s_err == -1)

    # Test case 6: Invalid input (negative)
    s_err, _ = constant_sum(-3)
    record_test("Test 6: Invalid input negative → returns -1", s_err == -1)

# Run tests
test_o1_2()

# Show summary
for result in test_results:
    print(result)
