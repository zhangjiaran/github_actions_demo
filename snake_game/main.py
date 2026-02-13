#!/usr/bin/env python3
"""
Snake Game - Classic snake game implementation using pygame
Supports headless mode for CI/CD testing
"""

import pygame
import random
import sys
import os
import argparse
from enum import Enum

# Initialize pygame
pygame.init()

# Game constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# FPS
FPS = 10


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Snake:
    def __init__(self):
        # Start in the middle of the screen
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.body = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
        self.direction = Direction.RIGHT
        self.growing = False

    def move(self):
        # Get the current head position
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value
        
        # Calculate new head position
        new_head = (head_x + dx, head_y + dy)
        
        # Add new head
        self.body.insert(0, new_head)
        
        # Remove tail if not growing
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False

    def change_direction(self, new_direction):
        # Prevent moving in opposite direction
        if new_direction == Direction.UP and self.direction != Direction.DOWN:
            self.direction = new_direction
        elif new_direction == Direction.DOWN and self.direction != Direction.UP:
            self.direction = new_direction
        elif new_direction == Direction.LEFT and self.direction != Direction.RIGHT:
            self.direction = new_direction
        elif new_direction == Direction.RIGHT and self.direction != Direction.LEFT:
            self.direction = new_direction

    def grow(self):
        self.growing = True

    def check_collision(self):
        head_x, head_y = self.body[0]
        
        # Check wall collision
        if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
            return True
        
        # Check self collision
        if self.body[0] in self.body[1:]:
            return True
        
        return False

    def get_head(self):
        return self.body[0]


class Food:
    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)

    def generate_position(self, snake_body):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake_body:
                return (x, y)

    def respawn(self, snake_body):
        self.position = self.generate_position(snake_body)


class SnakeGame:
    def __init__(self, test_mode=False):
        self.test_mode = test_mode
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.reset_game()

    def reset_game(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.score = 0
        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction(Direction.UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(Direction.DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(Direction.RIGHT)
                elif event.key == pygame.K_SPACE and self.game_over:
                    self.reset_game()
                elif event.key == pygame.K_ESCAPE:
                    return False
        return True

    def update(self):
        if not self.game_over:
            self.snake.move()
            
            # Check if snake ate food
            if self.snake.get_head() == self.food.position:
                self.snake.grow()
                self.food.respawn(self.snake.body)
                self.score += 10
            
            # Check collision
            if self.snake.check_collision():
                self.game_over = True

    def draw(self):
        # Clear screen
        self.screen.fill(BLACK)
        
        # Draw snake
        for segment in self.snake.body:
            x, y = segment
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - 2, GRID_SIZE - 2)
            pygame.draw.rect(self.screen, GREEN, rect)
        
        # Draw food
        food_x, food_y = self.food.position
        food_rect = pygame.Rect(food_x * GRID_SIZE, food_y * GRID_SIZE, GRID_SIZE - 2, GRID_SIZE - 2)
        pygame.draw.rect(self.screen, RED, food_rect)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw game over message
        if self.game_over:
            game_over_text = self.font.render("Game Over! Press SPACE to restart", True, WHITE)
            text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(game_over_text, text_rect)
        
        pygame.display.flip()

    def run(self):
        running = True
        frame_count = 0
        
        # In test mode, run for only a few frames
        max_frames = 30 if self.test_mode else -1
        
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            
            frame_count += 1
            if self.test_mode and frame_count >= max_frames:
                print(f"Test mode: Successfully ran {frame_count} frames")
                break
        
        pygame.quit()
        return 0


def is_ci_environment():
    """Check if running in CI environment"""
    return os.getenv('CI') == 'true' or os.getenv('GITHUB_ACTIONS') == 'true'


def main():
    parser = argparse.ArgumentParser(description='Snake Game')
    parser.add_argument('--test', action='store_true', help='Run in test mode (auto-exit after a few frames)')
    args = parser.parse_args()
    
    # Determine if we should run in test mode
    test_mode = args.test or is_ci_environment()
    
    # Set SDL to use dummy video driver in headless mode
    if test_mode:
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
        print("Running in test/headless mode")
    
    try:
        game = SnakeGame(test_mode=test_mode)
        return game.run()
    except Exception as e:
        print(f"Error running game: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
