from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.current_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.current_speed *= 0.9

    def hit_upper_wall(self):
        return self.ycor() > 280

    def hit_lower_wall(self):
        return self.ycor() < -280

    def hit_left_wall(self):
        return self.xcor() < -380

    def hit_right_wall(self):
        return self.xcor() > 380

    def hit_right_paddle(self, right_paddle):
        return self.distance(right_paddle) < 50 and self.xcor() > 320

    def hit_left_paddle(self, left_paddle):
        return self.distance(left_paddle) < 50 and self.xcor() < -320

    def reset_position(self):
        self.current_speed = 0.1
        self.home()
        self.bounce_x()
