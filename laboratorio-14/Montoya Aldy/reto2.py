import time

test_results = []

def record_test(test_name, condition):
    marker = "[true]" if condition else "[false]"
    test_results.append(f"{marker} {test_name}")

def constant_sum(n):
    """Calculate sum of 1 to n using O(1) logic with divmod.
    Returns (sum, elapsed_time). Returns -1 and elapsed time if input is invalid."""
    start = time.time()
    
    if not isinstance(n, int) or n < 0:
        end = time.time()
        return -1, end - start

    prod = n * (n + 1)
    total, _ = divmod(prod, 2)

    end = time.time()
    return total, end - start

def test_o1_2():
    s, _ = constant_sum(0)
    record_test("o1.2.1 n=0 -> sum==0", s == 0)

    s, _ = constant_sum(1)
    record_test("o1.2.2 n=1 -> sum==1", s == 1)

    s, _ = constant_sum(10)
    record_test("o1.2.3 n=10 -> sum==55", s == 55)

    out = constant_sum(5)
    record_test("o1.2.4 returns (int, float)", isinstance(out[0], int) and isinstance(out[1], float))

    s_err, _ = constant_sum(-3)
    record_test("o1.2.5 invalid input returns -1", s_err == -1)

test_o1_2()

for r in test_results:
    print(r)
