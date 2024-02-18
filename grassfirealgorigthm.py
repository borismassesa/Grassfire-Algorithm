"""
    This Python program is designed to simulate a grid-based pathfinding scenario where obstacles are placed, 
    and a path is calculated from a starting cell to a destination cell using a simplified version of the Grassfire algorithm. 
    Once the path is calculated, it uses the matplotlib library to visualize the grid, the obstacles, the starting and ending points, and the path.
"""

import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Constants for minimum grid size
MIN_ROWS = 8
MIN_COLUMNS = 8

# This Function Asks the user to input the number of rows and columns for the grid, 
# ensuring they meet the minimum size requirements.
def prompt_grid_size():
    rows = cols = 0
    while rows < MIN_ROWS or cols < MIN_COLUMNS:
        try:
            rows = int(input(f"Enter the number of rows for the grid (minimum {MIN_ROWS}): "))
            cols = int(input(f"Enter the number of columns for the grid (minimum {MIN_COLUMNS}): "))
        except ValueError:
            print("Please enter integer values only.")
        if rows < MIN_ROWS or cols < MIN_COLUMNS:
            print(f"Grid must be at least {MIN_ROWS} rows and {MIN_COLUMNS} columns.")
    return rows, cols

#This Function Generates a set of unique obstacle positions based on the grid size and 
# the percentage of the grid that should be obstacles.
def create_obstacle_set(num_rows, num_cols, percentage):
    num_cells = num_rows * num_cols
    num_obstacles = round(percentage / 100 * num_cells)
    obstacles = set()
    while len(obstacles) < num_obstacles:
        obstacles.add((random.randint(0, num_rows - 1), random.randint(0, num_cols - 1)))
    return obstacles

#This Function Randomly selects the starting cell's column index on the first row of the grid.
def select_starting_position(num_cols):
    return 0, random.randint(0, num_cols - 1)

# This function Randomly selects the destination cell's position based on the criteria that it should be in the 
# lower half of the grid and to the right side in terms of columns.
def select_destination_position(num_rows, num_cols):
    row_threshold = num_rows // 2
    col_threshold = round(2 / 3 * num_cols)
    return random.randint(row_threshold + 1, num_rows - 1), random.randint(col_threshold, num_cols - 1)

# This Function Implements a pathfinding algorithm that marks the distance from the destination cell to all other cells, 
# then backtracks to find the shortest path from the start cell to the destination.
def grassfire_algorithm(obstacles, start_point, destination_point, num_rows, num_cols):
    field = np.full((num_rows, num_cols), np.inf)
    for obstacle in obstacles:
        field[obstacle] = np.nan  # Mark obstacles with NaN
    field[destination_point] = 0  # Set the destination value to 0

    queue = [destination_point]
    while queue:
        row, col = queue.pop(0)
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + d_row, col + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                if np.isinf(field[new_row, new_col]):
                    field[new_row, new_col] = field[row, col] + 1
                    queue.append((new_row, new_col))

    path = []
    if not np.isinf(field[start_point]):
        current_pos = start_point
        while current_pos != destination_point:
            path.append(current_pos)
            current_val = field[current_pos]
            current_pos = min(
                [(current_pos[0] + d_row, current_pos[1] + d_col) for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)] 
                 if 0 <= current_pos[0] + d_row < num_rows and 0 <= current_pos[1] + d_col < num_cols],
                key=lambda pos: (field[pos], -pos[0], -pos[1])  # Minimize field value, prioritize higher rows/cols
            )
            if field[current_pos] >= current_val:  # If no progress is made, no path is available
                return [], field
        path.append(destination_point)
    return path[::-1], field  # Return the path in reverse order

# This Function Uses matplotlib to draw the grid, the obstacles, the starting and ending cells, 
# and the path if one was found. The starting cell is labeled "START", and the destination cell is labeled "END".
def visualize_grid(obstacle_set, start, destination, path, num_rows, num_cols):
    fig, ax = plt.subplots(figsize=(num_cols, num_rows))
    ax.set_aspect('equal')  # set the x and y axes to the same scale
    plt.axis('off')  # turn off the axes

    # Draw the grid
    for x in range(num_cols + 1):
        ax.axhline(x, color='blue', linewidth=1)
        ax.axvline(x, color='blue', linewidth=1)

    # Draw the obstacles
    for obs in obstacle_set:
        ax.add_patch(patches.Rectangle((obs[1], num_rows - 1 - obs[0]), 1, 1, facecolor='black'))

    # Draw the start cell
    ax.add_patch(patches.Rectangle((start[1], num_rows - 1 - start[0]), 1, 1, facecolor='green'))
    ax.text(start[1] + 0.5, num_rows - 0.5 - start[0], 'START', color='white', 
            fontsize=8, ha='center', va='center', fontweight='bold')

    # Draw the destination cell
    ax.add_patch(patches.Rectangle((destination[1], num_rows - 1 - destination[0]), 1, 1, facecolor='red'))
    ax.text(destination[1] + 0.5, num_rows - 0.5 - destination[0], 'END', color='white', 
            fontsize=8, ha='center', va='center', fontweight='bold')

    # Optionally, draw the path if you have one
    for position in path:
        if position != start and position != destination:  # Avoid overwriting start/end cells
            ax.add_patch(patches.Rectangle((position[1], num_rows - 1 - position[0]), 1, 1, facecolor='orange'))

    plt.gca().invert_yaxis()  # Invert y-axis to have the origin at the top-left corner
    plt.show()


# Main execution
def main():
    num_rows, num_cols = prompt_grid_size()
    obstacle_percentage = 15  # Can be prompted from user as well
    obstacle_set = create_obstacle_set(num_rows, num_cols, obstacle_percentage)
    starting_position = select_starting_position(num_cols)
    destination_position = select_destination_position(num_rows, num_cols)
    shortest_path, grassfire_field = grassfire_algorithm(obstacle_set, starting_position, destination_position, num_rows, num_cols)
    visualize_grid(obstacle_set, starting_position, destination_position, shortest_path, num_rows, num_cols)

# The if __name__ == "__main__": part ensures that main() is called only when the script is executed as the main program, 
# not when it is imported as a module in another script.
if __name__ == "__main__":
    main()
