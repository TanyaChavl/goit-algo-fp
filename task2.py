import turtle

def draw_tree(branch_len, t, recursion_depth):
    if recursion_depth > 0:
        t.forward(branch_len)
        t.right(25)
        draw_tree(branch_len * 0.75, t, recursion_depth - 1)
        t.left(50)
        draw_tree(branch_len * 0.75, t, recursion_depth - 1)
        t.right(25)
        t.backward(branch_len)

def pythagoras_tree(t, depth):
    t.left(90)
    draw_tree(100, t, depth)

def main():
    recursion_depth = int(input("Введіть рівень рекурсії: "))
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(0)
    pythagoras_tree(t, recursion_depth)
    screen.exitonclick()

if __name__ == "__main__":
    main()
