"""Week 1 exercises for Python collection syntax."""


def list_demo() -> None:
    numbers = [1, 2, 3, 4, 5]

    numbers.append(6)
    squares = [number**2 for number in numbers]
    even_numbers = [number for number in numbers if number % 2 == 0]

    print("List:", numbers)
    print("Squares:", squares)
    print("Even numbers:", even_numbers)


def dict_demo() -> None:
    users = {
        1: "Alice",
        2: "Bob",
        3: "Charlie",
    }

    users[4] = "David"

    print("User 2:", users.get(2))
    print("Unknown user:", users.get(99, "Not found"))

    for user_id, name in users.items():
        print(f"{user_id}: {name}")


def set_demo() -> None:
    numbers = [1, 1, 2, 2, 3, 4]
    unique_numbers = set(numbers)

    first_group = {1, 2, 3}
    second_group = {3, 4, 5}

    print("Unique:", unique_numbers)
    print("Intersection:", first_group & second_group)
    print("Union:", first_group | second_group)
    print("Difference:", first_group - second_group)


def tuple_demo() -> None:
    user = (1, "Alice", "admin")
    user_id, name, role = user

    print(f"ID={user_id}, name={name}, role={role}")


def iteration_demo() -> None:
    names = ["Alice", "Bob", "Charlie"]
    scores = [90, 85, 95]

    for index, name in enumerate(names, start=1):
        print(f"{index}. {name}")

    for name, score in zip(names, scores):
        print(f"{name}: {score}")


def main() -> None:
    list_demo()
    dict_demo()
    set_demo()
    tuple_demo()
    iteration_demo()


if __name__ == "__main__":
    main()