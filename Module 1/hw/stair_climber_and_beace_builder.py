

def stair_ways(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    return stair_ways(n - 1) + stair_ways(n - 2)



def trace_stair_ways(n, level=0):
    print("  " * level + f"stair_ways({n})")

    if n == 0:
        print("  " * level + "Return 1")
        return 1

    if n < 0:
        print("  " * level + "Return 0")
        return 0

    result1 = trace_stair_ways(n - 1, level + 1)
    result2 = trace_stair_ways(n - 2, level + 1)

    result = result1 + result2

    print("  " * level + f"Return {result}")
    return result



def generate_braces(total_pairs):
    result = []

    def generate(current, open_count, close_count):
        if len(current) == 2 * total_pairs:
            result.append(current)
            return

        # Add an opening brace if available
        if open_count < total_pairs:
            generate(current + "{",
                     open_count + 1, close_count)

        # Add a closing brace if valid
        if close_count < open_count:
            generate(current + "}",
                     open_count, close_count + 1)

    generate("", 0, 0)
    return result



n = int(input("Enter number of stairs: "))

print("\nNumber of ways to climb:", stair_ways(n))

print("\nRecursive Call Tree:")
trace_stair_ways(n)

pairs = int(input("\nEnter number of brace pairs: "))

print("\nValid balanced brace combinations:")
print(generate_braces(pairs))
