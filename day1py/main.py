def main() -> None:
    part1()


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


if __name__ == "__main__":
    main()
