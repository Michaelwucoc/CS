import pygame
import random

# 初始化Pygame
pygame.init()

# 设置屏幕尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("弹砖块游戏")

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# 字体设置
font = pygame.font.Font(None, 36)


# 定义球类
class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = 4
        self.dy = -4

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # 碰到左右边界反弹
        if self.x <= 0 or self.x >= screen_width:
            self.dx = -self.dx
        # 碰到上边界反弹
        if self.y <= 0:
            self.dy = -self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, white, (self.x, self.y), self.radius)


# 定义板子类
class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dx = 0

    def move(self):
        self.x += self.dx
        # 限制板子在屏幕范围内
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > screen_width:
            self.x = screen_width - self.width

    def draw(self, screen):
        pygame.draw.rect(screen, blue, (self.x, self.y, self.width, self.height))


# 定义砖块类
class Brick:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hit = False

    def draw(self, screen):
        if not self.hit:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


# 定义道具类
class PowerUp:
    def __init__(self, x, y, width, height, color, effect):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.effect = effect
        self.dy = 2

    def move(self):
        self.y += self.dy

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


# 创建砖块阵列
def create_bricks(level):
    bricks = []
    brick_rows = random.randint(3, 20)
    brick_cols = random.randint(8, 10)
    brick_width = 60
    brick_height = 20
    brick_padding = 10
    colors = [red, green, blue, yellow]
    for row in range(brick_rows):
        for col in range(brick_cols):
            brick_x = col * (brick_width + brick_padding) + brick_padding
            brick_y = row * (brick_height + brick_padding) + brick_padding
            color = random.choice(colors)
            bricks.append(Brick(brick_x, brick_y, brick_width, brick_height, color))
    return bricks


# 显示开始菜单
def show_start_menu():
    screen.fill(black)
    title_text = font.render("弹砖块游戏", True, white)
    mode_text_1 = font.render("按 1 选择无限模式", True, white)
    mode_text_2 = font.render("按 2 选择闯关模式", True, white)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 3))
    screen.blit(mode_text_1, (screen_width // 2 - mode_text_1.get_width() // 2, screen_height // 2))
    screen.blit(mode_text_2, (screen_width // 2 - mode_text_2.get_width() // 2, screen_height // 2 + 40))
    pygame.display.flip()


# 游戏初始化
ball = Ball(screen_width // 2, screen_height // 2, 10)
paddle = Paddle(screen_width // 2 - 50, screen_height - 30, 100, 10)
bricks = []
powerups = []

# 分数
score = 0
level = 1

# 游戏状态
game_over = False
game_won = False
game_mode = None

# 主游戏循环
running = True
clock = pygame.time.Clock()

while running:
    if game_mode is None:
        show_start_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_mode = "infinite"
                    bricks = create_bricks(level)
                elif event.key == pygame.K_2:
                    game_mode = "level"
                    bricks = create_bricks(level)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle.dx = -9
                elif event.key == pygame.K_RIGHT:
                    paddle.dx = 9
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    paddle.dx = 0

        if not game_over:
            # 移动球和板子
            ball.move()
            paddle.move()

            # 碰撞检测：球和板子
            if ball.y + ball.radius >= paddle.y and paddle.x <= ball.x <= paddle.x + paddle.width:
                ball.dy = -ball.dy

            # 碰撞检测：球和砖块
            for brick in bricks:
                if not brick.hit:
                    if brick.x < ball.x < brick.x + brick.width and brick.y < ball.y < brick.y + brick.height:
                        ball.dy = -ball.dy
                        brick.hit = True
                        score += 10
                        if random.random() < 0.9:
                            powerup_x = brick.x + brick.width // 2
                            powerup_y = brick.y + brick.height
                            powerup = PowerUp(powerup_x, powerup_y, 20, 20, yellow, 'expand')
                            powerups.append(powerup)
                        break

            # 碰撞检测：球和道具
            for powerup in powerups:
                powerup.move()
                if paddle.y < powerup.y + powerup.height < paddle.y + paddle.height and paddle.x < powerup.x + powerup.width < paddle.x + paddle.width:
                    if powerup.effect == 'expand':
                        paddle.width += 20
                    powerups.remove(powerup)
                    break

            # 检查球是否落出屏幕底部
            if ball.y > screen_height:
                game_over = True

            # 检查是否赢得游戏
            if all(brick.hit for brick in bricks):
                if game_mode == "level":
                    level += 1
                    bricks = create_bricks(level)
                    ball = Ball(screen_width // 2, screen_height // 2, 10)
                    paddle = Paddle(screen_width // 2 - 50, screen_height - 30, 100, 10)
                elif game_mode == "infinite":
                    bricks = create_bricks(level)
                    ball = Ball(screen_width // 2, screen_height // 2, 10)
                    paddle = Paddle(screen_width // 2 - 50, screen_height - 30, 100, 10)
                else:
                    game_won = True
                    game_over = True

            # 清屏
            screen.fill(black)

            # 绘制球、板子、砖块和道具
            ball.draw(screen)
            paddle.draw(screen)
            for brick in bricks:
                brick.draw(screen)
            for powerup in powerups:
                powerup.draw(screen)

            # 显示分数
            score_text = font.render(f"Score: {score}", True, white)
            screen.blit(score_text, (10, 10))

        else:
            # 游戏结束或成功
            screen.fill(black)
            if game_won:
                end_text = font.render("You Win!", True, green)
            else:
                end_text = font.render("Game Over", True, red)
            score_text = font.render(f"Final Score: {score}", True, white)
            screen.blit(end_text, (
            screen_width // 2 - end_text.get_width() // 2, screen_height // 2 - end_text.get_height() // 2))
            screen.blit(score_text,
                        (screen_width // 2 - score_text.get_width() // 2, screen_height // 2 + end_text.get_height()))

        # 更新屏幕
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
