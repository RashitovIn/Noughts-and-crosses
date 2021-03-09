import sys, pygame

pygame.init()
size_block = 100
margin = 15

back_color = (30,30,30)
blue_blocks = (255,255,255)
white = (205,205,205)
red = (224, 0, 0)
green = (21,159,92)
black = (0, 0, 0)

width = height = size_block * 3 + margin * 4

size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Крестики нолики")

def check_win(field, sign):
    zero = 0
    for row in field:
        zero += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if field[0][col] == sign and field[1][col] == sign and field[2][col] == sign:
            return sign
    if field[0][0] == sign and field[1][1] == sign and field[2][2] == sign:
        return sign
    if field[0][2] == sign and field[1][1] == sign and field[2][0] == sign:
        return sign
    if zero == 0:
        return 'Ничья'
    return False

field = [[0] * 3 for i in range(3)]

query = 0
screen.fill(black)
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if field[row][col] == 0:
                if query % 2 == 0:
                    field[row][col] = 'x'
                else:
                    field[row][col] = 'o'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            field = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(black)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if field[row][col] == 'x':
                    color = red
                elif field[row][col] == 'o':
                    color = green
                else:
                    color = white
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))

                if color == red:
                    pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 3)
                    pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 3)
        if (query - 1) % 2 == 0:
            game_over = check_win(field, 'x')
        else:
            game_over = check_win(field, 'o')

        if game_over:
            screen.fill(black)
            font = pygame.font.SysFont('stxingkai', 80)
            text1 = font.render(game_over, True, white)
            text_rect = text1.get_rect()
            text_x = size[0] / 2 - text_rect.width / 2
            text_y = size[1] / 2 - text_rect.height / 2
            screen.blit(text1, [text_x, text_y])

    pygame.display.update()