def bfs(initial_sequence):

    transformations = {
                        "AC": "E",
                        "AB": "BC",
                        "BB": "E",
                        "E": "", # "Ex" = x
                    }

    queue = [initial_sequence]
    visited = set()
    while queue:
        
        print(queue)    
        current_sequence = queue.pop(0)
        visited.add(current_sequence)
        if current_sequence == "E": # Goal sequence (Meaning )
            return current_sequence

        # Add all "neighbours" for current sequence
        for i in range(0, len(current_sequence) - 1):

            if current_sequence[i] == "E":
                concat = current_sequence[i]
            else:
                concat = current_sequence[i] + current_sequence[i + 1]
        
            if concat in transformations:
                new_letters = transformations[concat]
                new_sequence = current_sequence[0:i] + new_letters + current_sequence[i + 2:]
                if new_sequence not in visited:
                    queue.append(new_sequence)
        
    return False

result = bfs(initial_sequence = "ABABAECCEC")#
print(result)