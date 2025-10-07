def read_grid(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def search_word_in_direction(grid, word, start_row, start_col, dr, dc):
    rows, cols = len(grid), len(grid[0])
    
    for i in range(len(word)):
        r = start_row + i * dr
        c = start_col + i * dc
        
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        
        if grid[r][c] != word[i]:
            return False
    
    return True

def count_word_occurrences(grid, word):
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    
    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                if search_word_in_direction(grid, word, row, col, dr, dc):
                    count += 1
    
    return count

def is_valid_x_mas(grid, center_row, center_col):
    rows, cols = len(grid), len(grid[0])
    
    if (center_row - 1 < 0 or center_row + 1 >= rows or 
        center_col - 1 < 0 or center_col + 1 >= cols):
        return False
    
    if grid[center_row][center_col] != 'A':
        return False
    
    top_left = grid[center_row - 1][center_col - 1]
    top_right = grid[center_row - 1][center_col + 1]
    bottom_left = grid[center_row + 1][center_col - 1]
    bottom_right = grid[center_row + 1][center_col + 1]
    
    diagonal1 = top_left + 'A' + bottom_right
    diagonal1_valid = diagonal1 == 'MAS' or diagonal1 == 'SAM'
    
    diagonal2 = top_right + 'A' + bottom_left
    diagonal2_valid = diagonal2 == 'MAS' or diagonal2 == 'SAM'
    
    return diagonal1_valid and diagonal2_valid

def count_x_mas_patterns(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if is_valid_x_mas(grid, row, col):
                count += 1
    
    return count

def part_one(grid):
    word = "XMAS"
    total_count = count_word_occurrences(grid, word)
    print(f"Part One: The word '{word}' appears {total_count} times in the word search.")
    return total_count

def part_two(grid):
    total_count = count_x_mas_patterns(grid)
    print(f"Part Two: X-MAS patterns appear {total_count} times in the word search.")
    return total_count

def main():
    grid = read_grid('input.txt')
    
    print("=== Advent of Code Day 4 ===")
    part_one_result = part_one(grid)
    part_two_result = part_two(grid)
    
    return part_one_result, part_two_result

if __name__ == "__main__":
    main()
