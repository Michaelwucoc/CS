import pygame
import random
import math

# 初始化Pygame
pygame.init()

# 屏幕尺寸
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("坦克大战")

# 颜色定义
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# 地图参数
TILE_SIZE = 40
MAP_WIDTH = SCREEN_WIDTH // TILE_SIZE
MAP_HEIGHT = SCREEN_HEIGHT // TILE_SIZE


# 创建随机地图
def create_random_map():
    return [[random.choice([0, 1]) for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]


# 绘制地图
def draw_map(map_data):
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == 1:
                pygame.draw.rect(screen, GREEN, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))


# 碰撞检测
def check_collision(x, y, size, map_data):
    if x < 0 or x + size > SCREEN_WIDTH or y < 0 or y + size > SCREEN_HEIGHT:
        return True
    tile_x = x // TILE_SIZE
    tile_y = y // TILE_SIZE
    if map_data[tile_y][tile_x] == 1:
        return True
    return False


# 坦克类
class Tank:
    def __init__(self, x, y, color=RED):
        self.x = x
        self.y = y
        self.size = TILE_SIZE
        self.color = color
        self.speed = 5

    def move(self, dx, dy, map_data):
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed
        if not check_collision(new_x, new_y, self.size, map_data):
            self.x = new_x
            self.y = new_y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))


# 子弹类
class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.size = 5
        self.color = YELLOW
        self.speed = 10
        self.direction = direction

    def move(self):
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

    def is_off_screen(self):
        return self.x < 0 or self.x > SCREEN_WIDTH or self.y < 0 or self.y > SCREEN_HEIGHT


# 游戏主循环
def main():
    clock = pygame.time.Clock()
    running = True

    player_tank = Tank(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    ai_tank = Tank(random.randint(0, SCREEN_WIDTH - TILE_SIZE), random.randint(0, SCREEN_HEIGHT - TILE_SIZE),
                   color=BLACK)
    map_data = create_random_map()
    bullets = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                direction = 0  # 默认向右发射
                bullets.append(
                    Bullet(player_tank.x + player_tank.size // 2, player_tank.y + player_tank.size // 2, direction))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_tank.move(-1, 0, map_data)
        if keys[pygame.K_RIGHT]:
            player_tank.move(1, 0, map_data)
        if keys[pygame.K_UP]:
            player_tank.move(0, -1, map_data)
        if keys[pygame.K_DOWN]:
            player_tank.move(0, 1, map_data)

        # AI坦克简单移动逻辑（随机移动）
        ai_tank.move(random.choice([-1, 1, 0]), random.choice([-1, 1, 0]), map_data)

        # 更新子弹位置和移除屏幕外的子弹
        for bullet in bullets[:]:
            bullet.move()
            if bullet.is_off_screen():
                bullets.remove(bullet)

        screen.fill(WHITE)
        draw_map(map_data)
        player_tank.draw(screen)
        ai_tank.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
