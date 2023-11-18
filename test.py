import math

def brightness_level(distance):
    brightness = 16 - (distance / 100) * 16
    if brightness < 0:
        brightness = 0
    return round(brightness)


def pygame_to_real_coords(pygame_coords, screen_width, screen_height):
    # Calculate the offset from the center of the screen
    x_offset = screen_width / 2
    y_offset = screen_height / 2

    # Convert Pygame coordinates to real-world coordinates
    real_x = pygame_coords[0] - x_offset
    real_y = pygame_coords[1] - y_offset

    return (real_x, real_y)


def distance(point1, point2):
    # Calculate the difference between the x-coordinates
    x_diff = point1[0] - point2[0]

    # Calculate the difference between the y-coordinates
    y_diff = point1[1] - point2[1]

    # Calculate the square of the difference in x-coordinates
    x_diff_squared = x_diff * x_diff

    # Calculate the square of the difference in y-coordinates
    y_diff_squared = y_diff * y_diff

    # Calculate the sum of the squares of the differences
    sum_of_squares = x_diff_squared + y_diff_squared

    # Take the square root of the sum of squares to find the distance
    distance = math.sqrt(sum_of_squares)

    return distance

