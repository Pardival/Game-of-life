import pygame
import random

# nb case in width and nb_case in height
def make_map(width, height) : 
    return [[0 for i in range(width)] for i in range(height)]


def draw_map(map, screen, window_dimension) :
    # (width, height)
    case_dimension = (window_dimension[0] / len(map[0]), window_dimension[1] / len(map))
    color = (255,0,0)
    for row in range(len(map)) :
        for col in range(len(map[row])) :
            if map[row][col] == 1 :
                pygame.draw.rect(screen, color, 
                pygame.Rect(row * case_dimension[0], col * case_dimension[1], case_dimension[0], case_dimension[1]))

def update_map(map, new_map) :
    for row in range(len(map)) :
        for col in range(len(map[row])) :
            alive = count_alive(map, row, col)
            if alive == 3 :
                new_map[row][col] = 1
            elif alive == 2  :
                new_map[row][col] = map[row][col]
            else : 
                new_map[row][col] = 0
    return new_map

def count_alive(map, current_row, current_col) :
    nb_alive = 0
    for row in range(-1, 2) :
        for col in range(-1, 2) :
            if (current_row + row >= 0 and current_col + col >= 0 and 
            current_row + row < len(map) and current_col + col < len(map[current_row]) and 
            (row != 0 or col != 0) and
            map[current_row + row][current_col + col] == 1) :
                nb_alive += 1
    return nb_alive    

def generate_random_alive(map, nb_cases) :
    for i in range(nb_cases) :
        x = random.randint(0, len(map[0]) - 1)
        y = random.randint(0, len(map) - 1)
        map[x][y] = 1
    return map

def clear_map(screen) :
    screen.fill((0,0,0))

def main() :
    dimension = (400, 400)
    screen = pygame.display.set_mode(dimension)
    map = make_map(40, 40)
    map = generate_random_alive(map, 300)
    draw_map(map, screen, dimension)
    pygame.display.flip()
    pygame.time.wait(5000)
    while (True) :
        clear_map(screen)
        map = update_map(map, make_map(40, 40))
        draw_map(map, screen, dimension)
        pygame.display.flip()
        pygame.time.wait(50)

main()