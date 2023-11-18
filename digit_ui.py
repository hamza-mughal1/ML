import pygame
import sys
import pickle
import numpy
import math
import csv

def append_Data_to_csv(lst,file_name):
    file = open(f"{file_name}.csv","a",newline="",encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(lst)
    file.close()

def brightness_level(distance):
    brightness = 16 - (distance / 150) * 16
    if brightness < 0:
        brightness = 0
    return round(brightness)

def pygame_to_real_coords(pygame_coords, screen_width, screen_hight):
    # Calculate the offset from the center of the screen
    x_offset = screen_width / 2
    y_offset = screen_hight / 2

    # Convert Pygame coordinates to real-world coordinates
    real_x = pygame_coords[0] - x_offset
    real_y = pygame_coords[1] - y_offset

    return [real_x, real_y]

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

def coloring(number):
    step_size = 255/16
    return_color = [0,0,0]
    for i in range(number):
        return_color[0] += step_size
        return_color[1] += step_size
        return_color[2] += step_size
    return tuple(return_color)


# Initialize Pygame
pygame.init()

# Set the size of the window
width = 800
hight = 800

# Create the Pygame window
screen = pygame.display.set_mode((width, hight))

# Set the title of the window
pygame.display.set_caption("My Pygame Window")

color = (255,0,0)

lst = [0 for _ in range(64)]

def predict(lst):
    with open ("digit_model","rb") as f:
        model = pickle.load(f)
        predict_list = numpy.array([lst])
        return model.predict(predict_list)[0]

draw = False

while True:
    dic = {}
    rect_no = 0
    for j in range(0,800,100):
        current_x = 0
        for _ in range(8):
            rect = pygame.Rect(current_x,j,90,90)
            dic[rect_no] = (current_x,j)
            pygame.draw.rect(screen,coloring(lst[rect_no]),rect) 
            rect_no += 1 
            current_x += 100
        current_x = 0

    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
        elif event.type == pygame.MOUSEBUTTONUP:
            draw = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                lst = [0 for _ in range(64)]

            if event.key == pygame.K_UP:
                print(predict(lst))

            if event.key == pygame.K_1:
                lst.append(1)
                append_Data_to_csv(lst,"digit_data")
                print("done! = 1")
                lst = [0 for _ in range(64)]

            if event.key == pygame.K_2:
                lst.append(2)
                append_Data_to_csv(lst,"digit_data")
                print("done! = 2")
                lst = [0 for _ in range(64)]

            if event.key == pygame.K_3:
                lst.append(3)
                append_Data_to_csv(lst,"digit_data")
                print("done! = 3")
                lst = [0 for _ in range(64)]

            if event.key == pygame.K_4:
                lst.append(4)
                append_Data_to_csv(lst,"digit_data")
                print("done! = 4")
                lst = [0 for _ in range(64)]

            if event.key == pygame.K_5:
                lst.append(5)
                append_Data_to_csv(lst,"digit_data")
                print("done! = 5")
                lst = [0 for _ in range(64)]

            if event.key == pygame.K_6:
                lst.append(6)
                append_Data_to_csv(lst,"digit_data")
                print("done! = 6")
                lst = [0 for _ in range(64)]

            if event.key == pygame.K_7:
                lst.append(7)
                append_Data_to_csv(lst,"digit_data")
                print("done! = 7")
                lst = [0 for _ in range(64)]

            if event.key == pygame.K_8:
                lst.append(8)
                append_Data_to_csv(lst,"digit_data")
                print("done! = 8")
                lst = [0 for _ in range(64)]

            if event.key == pygame.K_9:
                lst.append(9)
                append_Data_to_csv(lst,"digit_data")
                print("done! = 9")
                lst = [0 for _ in range(64)]

            if event.key == pygame.K_0:
                lst.append(0)
                append_Data_to_csv(lst,"digit_data")
                print("done! = 0")
                lst = [0 for _ in range(64)]



    if draw:
        click_pos = pygame.mouse.get_pos()
        for key,value in dic.items():
                click_ps = pygame_to_real_coords(click_pos,width,hight)
                coordinates = pygame_to_real_coords(value,width,hight)
                coordinates[0] += 45
                coordinates[1] += 45
                distanc = distance(click_ps,coordinates)
                br = brightness_level(distanc)
                if lst[key] < br:
                    lst[key] = br
    

    # Draw graphics to the Pygame window
    pygame.display.update()



