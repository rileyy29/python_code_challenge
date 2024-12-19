from robot import PathfindingRobot

def main():
    grid_size = (16, 16)
    start = (1, 0)
    goal = (8, 9) 
    obstacles = [
        (4, 6),
        *[(x, y) for x in range(3, 6) for y in range(3, 6)],
        *[(x, y) for x in range(9, 12) for y in range(9, 12)],
        (7, 6), (9, 7), (5, 7), (2, 7), (0, 6), (2, 8),
        *[(7, y) for y in range(8, 15)],
        (1, 1), (2, 2), (2, 1), (2, 0), (4, 10), (10, 4), (13, 13), (12, 6)
    ]

    robot = PathfindingRobot(grid_size, start, goal, obstacles)
    path = robot.run()

    if path:
        robot.print_path(path)
    else:
        print("No path found.")

main()