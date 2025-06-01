import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def draw_snowflake(level):
    screen = turtle.Screen()
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(0)  
    pen.penup()
    pen.goto(-150, 90)
    pen.pendown()


    for _ in range(3):
        koch_curve(pen, 300, level)
        pen.right(120)

    screen.mainloop()

if __name__ == "__main__":
    try:
        level = int(input("Введіть рівень рекурсії (0-5): "))
        if 0 <= level <= 5:
            draw_snowflake(level)
        else:
            print("Будь ласка, введіть число від 0 до 5.")
    except ValueError:
        print("Помилка: потрібно ввести ціле число.")
