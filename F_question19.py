def fibonacci_by_lamda(input_int):
    seeds = [0, 1]

    any(map(lambda _: seeds.append(sum(seeds[-2:])), range(2, input_int)))

    return seeds[:input_int]

print(fibonacci_by_lamda(int(input("Enter an integer : "))))