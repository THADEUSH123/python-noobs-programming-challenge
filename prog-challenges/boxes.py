"""Bython Challenge."""

my_rectangle1 = {
    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 2,

    # width and height
    'width': 3,
    'height': 4,

}


my_rectangle2 = {
    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,

    # width and height
    'width': 2,
    'height': 4,

}


def overlap(rec1, rec2):
    """Caculate overlap of two rectangles."""
    grid = [[0 for _ in range(10)] for _ in range(10)]

    for x in range(rec1['left_x'], rec1['left_x'] + rec1['width']):
        for y in range(rec1['bottom_y'], rec1['bottom_y'] + rec1['height']):
            grid[x][y] += 1

    for x in range(rec2['left_x'], rec2['left_x'] + rec2['width']):
        for y in range(rec2['bottom_y'], rec2['bottom_y'] + rec2['height']):
            grid[x][y] += 1

    for row in grid:
        print row

overlap(my_rectangle1, my_rectangle2)
