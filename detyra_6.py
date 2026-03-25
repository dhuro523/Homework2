def find_longest_line(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        if not lines:
            return "Error: The file is empty."
        
        longest = max(lines, key=len).strip()
        return f"Longest line: {longest}"

    except FileNotFoundError:
        return "Error: The file does not exist." 

print(find_longest_line('my_data.txt'))   