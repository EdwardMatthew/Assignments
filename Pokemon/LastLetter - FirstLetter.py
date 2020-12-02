def get_neighbors(word, choices):
    return set(x for x in choices if x[0] == word[-1])

def longest_path_from(word, choices):
    choices = choices - set([word])
    neighbors = get_neighbors(word, choices)

    if neighbors:
        paths = (longest_path_from(w, choices) for w in neighbors)
        max_path = max(paths, key=len)
    else:
        max_path = []

    return [word] + max_path

def longest_path(choices):
    return max((longest_path_from(w, choices) for w in choices), key=len)

if __name__ == "__main__":
    with open("pokemon.txt", "r") as file: data = file.read()
    pokemon = frozenset(data.split())
    print(longest_path(pokemon))