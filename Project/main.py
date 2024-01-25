from sgraph import SGraph

def main():
    # Sample graph as per the problem description
    edges = {
        1: {'a': 2, 'b': 3},
        2: {'a': 3, 'b': 4},
        3: {'a': 4, 'b': 5},
        4: {'a': 5, 'b': 6},
        5: {'a': 6, 'b': 1},
        6: {'a': 1, 'b': 2}
    }

    graph = SGraph(edges)

    while True:
        print("\nMenu:")
        print("1. Move Robot")
        print("2. Count Commands")
        print("3. Solve Puzzle")
        print("4. Find Hardest Problem Instance")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            initpos = int(input("Enter initial position: "))
            sequence = input("Enter move sequence (e.g., 'abab'): ")
            finalpos = graph.move(initpos, sequence)
            print(f"Final position after move: {finalpos}")

        elif choice == 2:
            initpos = int(input("Enter initial position: "))
            dest = int(input("Enter destination: "))
            n = int(input("Enter command length: "))
            count = graph.count(initpos, dest, n)
            print(f"Number of commands of length {n} moving robot from {initpos} to {dest}: {count}")

        elif choice == 3:
            initpos = int(input("Enter initial position: "))
            states = list(map(bool, map(int, input("Enter target switch states (e.g., 0 1 0 0 for OFF ON OFF OFF): ").split())))
            command = graph.solve(initpos, states)
            if command:
                print(f"Shortest command sequence to reach the state: {command}")
            else:
                print("No such sequence found.")

        elif choice == 4:
            m = int(input("Enter size m of 2-regular digraph: "))
            instance = graph.find_hardest(m)
            if instance:
                graph_def, initpos, states, command = instance
                print(f"Hardest instance for m={m}:")
                print(f"Graph: {graph_def}")
                print(f"Initial Position: {initpos}")
                print(f"Switch States: {' '.join(['ON' if s else 'OFF' for s in states])}")
                print(f"Command: {command}")
            else:
                print(f"No hardest instance found for m={m}.")

        elif choice == 5:
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
