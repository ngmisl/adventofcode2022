def main() -> None:
    part1()
    part2()


def part1() -> None:
    with open("input.txt", "r") as f:
        lines = f.readlines()

    max_res = 0
    curr_res = 0

    for elf in lines:
        if elf != "\n":
            curr_res += int(elf)
        else:
            if curr_res > max_res:
                max_res = curr_res

            curr_res = 0

    print(max_res)


def part2() -> None:
    with open("input.txt", "r") as f:
        lines = f.readlines()

    top_three = []
    curr_res = 0

    for elf in lines:
        if elf != "\n":
            curr_res += int(elf)
        else:
            top_three.append(curr_res)
            curr_res = 0

    result = sorted(zip(top_three), reverse=True)[:3]
    print(result)


if __name__ == "__main__":
    main()
