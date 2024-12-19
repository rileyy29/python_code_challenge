import numpy as np
import matplotlib.pyplot as plt
import heapq
from matplotlib.animation import FuncAnimation

class PathfindingRobot:
    def __init__(self, grid_size, start, goal, obstacles):
        self.grid_size = grid_size
        self.start = start
        self.goal = goal
        self.obstacles = obstacles
        self.grid = self.init_grid()

    def init_grid(self):
        grid = np.zeros(self.grid_size, dtype=int)
        for obstacle in self.obstacles:
            grid[obstacle] = -1 
        return grid

    def is_valid(self, position):
        x, y = position
        return (0 <= x < self.grid_size[0] and 0 <= y < self.grid_size[1] and self.grid[x, y] != -1)

    def calc(self, position):
        return abs(position[0] - self.goal[0]) + abs(position[1] - self.goal[1])

    def run(self):
        open_set = []
        heapq.heappush(open_set, (0 + self.calc(self.start), 0, self.start, []))  # (f-score, g-score, position, path)

        visited = set()

        while open_set:
            _, g_score, current, path = heapq.heappop(open_set)

            if current in visited:
                continue
            visited.add(current)

            path = path + [current]

            if current == self.goal:
                return path

            # only permit up/down/left/right
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
                neighbor = (current[0] + dx, current[1] + dy)
                if self.is_valid(neighbor) and neighbor not in visited:
                    heapq.heappush(open_set, (g_score + 1 + self.calc(neighbor), g_score + 1, neighbor, path))

        return []  

    def print_path(self, path):
        fig, ax = plt.subplots(figsize=(8, 8))
        grid_display = self.grid.copy()

        def update(frame):
            ax.clear()
            if frame > 0:
                for pos in path[:frame]:
                    grid_display[pos] = 2 
            grid_display[self.start] = 3  
            grid_display[self.goal] = 4 
            ax.imshow(grid_display, cmap="coolwarm", origin="upper")
            ax.set_title(f"Pathfinding Animation (Step {frame}/{len(path)})")

        anim = FuncAnimation(fig, update, frames=len(path) + 1, interval=500, repeat=False)
        plt.show()