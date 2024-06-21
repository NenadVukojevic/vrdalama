import pygame
import sys

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
CELL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Directions for moving in the maze
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Solver")
clock = pygame.time.Clock()

# Simple maze as a 2D list (1 = wall, 0 = path)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Start and end positions
start = (1, 1)
end = (7, 8)

def draw_maze(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = WHITE if cell == 0 else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_path(path):
    for x, y in path:
        pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_current(current):
    x, y = current
    pygame.draw.rect(screen, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def dfs(maze, start, end):
    stack = [start]
    path = []
    visited = set()
    
    def dfs_recursive():
        while stack:
            current = stack.pop()
            if current == end:
                yield path
            if current not in visited:
                visited.add(current)
                path.append(current)
                yield current  # Yield the current position
                
                x, y = current
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 0:
                        stack.append((nx, ny))
        
        yield path  # Final path
        
    return dfs_recursive()

# Main Pygame loop
def main():
    running = True
    maze_generator = dfs(maze, start, end)
    path = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_maze(maze)
        draw_path(path)
        try:
            current = next(maze_generator)
            draw_current(current)
            path.append(current)
        except StopIteration:
            pass

        pygame.display.flip()
        clock.tick(10)  # Control the speed of the visualization

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
