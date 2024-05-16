import pygame
import random
import time

# 初始化Pygame
pygame.init()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 定义常量
TILE_SIZE = 20
MARGIN = 5

# 定义难度
DIFFICULTIES = {
    'easy': (10, 10, 10),
    'medium': (16, 16, 40),
    'hard': (24, 24, 99)
}

# 获取难度选择
difficulty = input("选择难度（easy, medium, hard）: ").strip().lower()
if difficulty not in DIFFICULTIES:
    difficulty = 'easy'

rows, cols, mines = DIFFICULTIES[difficulty]

# 计算窗口尺寸
WINDOW_WIDTH = cols * (TILE_SIZE + MARGIN) + MARGIN
WINDOW_HEIGHT = rows * (TILE_SIZE + MARGIN) + MARGIN

# 创建窗口
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("扫雷")

# 初始化游戏板
board = [[0 for _ in range(cols)] for _ in range(rows)]
revealed = [[False for _ in range(cols)] for _ in range(rows)]
flagged = [[False for _ in range(cols)] for _ in range(rows)]

# 放置地雷
mines_positions = set()
while len(mines_positions) < mines:
    r = random.randint(0, rows - 1)
    c = random.randint(0, cols - 1)
    if (r, c) not in mines_positions:
        mines_positions.add((r, c))
        board[r][c] = -1

# 计算每个格子的数字
for r in range(rows):
    for c in range(cols):
        if board[r][c] == -1:
            continue
        mine_count = sum((nr, nc) in mines_positions for nr in range(r - 1, r + 2) for nc in range(c - 1, c + 2) if
                         0 <= nr < rows and 0 <= nc < cols)
        board[r][c] = mine_count

# 游戏主循环
running = True
start_time = time.time()
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            col = pos[0] // (TILE_SIZE + MARGIN)
            row = pos[1] // (TILE_SIZE + MARGIN)
            if event.button == 1:  # 左键点击
                if not flagged[row][col]:
                    revealed[row][col] = True
                    if board[row][col] == -1:
                        game_over = True
            elif event.button == 3:  # 右键点击
                flagged[row][col] = not flagged[row][col]

    screen.fill(BLACK)

    for row in range(rows):
        for col in range(cols):
            color = GRAY
            if revealed[row][col]:
                if board[row][col] == -1:
                    color = RED
                else:
                    color = WHITE
            elif flagged[row][col]:
                color = GREEN

            pygame.draw.rect(screen, color,
                             [(MARGIN + TILE_SIZE) * col + MARGIN, (MARGIN + TILE_SIZE) * row + MARGIN, TILE_SIZE,
                              TILE_SIZE])

            if revealed[row][col] and board[row][col] > 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(board[row][col]), True, BLACK)
                screen.blit(text, [(MARGIN + TILE_SIZE) * col + MARGIN + 5, (MARGIN + TILE_SIZE) * row + MARGIN + 5])

    pygame.display.flip()

    if game_over:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"游戏结束！用时: {elapsed_time:.2f} 秒")
        # 计算3BV
        bvs = sum(sum(1 for cell in row if cell != -1) for row in board)
        efficiency = bvs / elapsed_time
        print(f"3BV: {bvs}")
        sites = rows * cols

        print(f"效率: {efficiency:.2f} 3BV/s")
        running = False

pygame.quit()
