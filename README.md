# Robot Pathfinding with Grassfire Algorithm

This project is an implementation of a pathfinding algorithm for a robot using the Grassfire algorithm. It is designed to automatically generate a search map for the robot and find the shortest path within a user-defined grid space, taking into account randomly placed obstacles.

## Features

- **Grid Initialization**: Set up the search region by defining the grid size with custom rows and columns.
- **Obstacle Placement**: Randomly generate obstacle cells within the grid based on a user-defined percentage.
- **Start and Destination Initialization**: Define the starting point and the destination cell for the robot's pathfinding.
- **Shortest Path Calculation**: Utilize the Grassfire algorithm to calculate and display the shortest path.

## How to Use

### Part 1: Setting up the Grid

1. **Define the Grid Size**: Enter the number of rows and columns for the grid. The minimum size is an 8x8 grid.
2. **Identify Obstacle Cells**: Input a percentage (10% - 20%) to randomly generate obstacles within the grid.
3. **Initialize Starting Cell**: Input a random number (less than the number of columns) to set the starting cell in the first row.
4. **Initialize Destination Cell**: Input the indices for the destination cell, ensuring the row index is greater than half the total number of rows and the column index is greater than two-thirds the total number of columns.

### Part 2: Pathfinding

Run the program to generate the search map and calculate the shortest path using the Grassfire algorithm. The search map can be displayed graphically or in matrix format, and the shortest path(s) will be printed out.

### Part 3: Graphical User Interface 

A GUI is provided for enhanced interaction. It visualizes the search map and results with appealing graphics.

## Installation

1. Clone the repository:
