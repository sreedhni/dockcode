def draw_single_hexagon(size):
    """
    Function to draw a single hexagon for honeycomb pattern
    """
    hexagon = []

    # Hexagon with 6 sides
    for i in range(size):
        hexagon.append(" " * (size - 1 - i) + "/ " + " " * (2 * i) + "\\")

    for i in range(size):
        hexagon.append(" " * i + "\\ " + " " * (2 * (size - 1 - i)) + "/")

    return hexagon

def draw_hexagon_column(rows, size, offset):
    """
    Function to draw a column of hexagons in honeycomb pattern
    """
    column = []
    single_hex = draw_single_hexagon(size)
    for i in range(rows):
        if offset and i % 2 == 1:
            # Offset every other hexagon
            column.extend([" " * (2 * size) + line for line in single_hex])
        else:
            column.extend([" " * (2 * size) + line for line in single_hex])

    return column

def draw_hexagon_grid(rows, cols, size):
    """
    Function to draw a honeycomb grid of hexagons
    """
    grid = []
    hex_height = 2 * size

    for row in range(rows):
        offset = (row % 2 == 1)
        hex_column = draw_hexagon_column(cols, size, offset)

        # Add each line of the current hex column to the grid
        for line_idx in range(hex_height):
            grid_line = ""
            for col in range(cols):
                if col > 0 and not (offset and row % 2 == 1):
                    grid_line += hex_column[col * hex_height + line_idx][2 * size + 1:]
                else:
                    grid_line += hex_column[col * hex_height + line_idx]
            grid.append(grid_line)

    return "\n".join(grid)

# Take input from the user for number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
size = 3  # Size of each hexagon

# Draw and print the honeycomb hexagon grid
hexagon_grid = draw_hexagon_grid(rows, cols, size)
print(hexagon_grid)
