# This algorithm is a specific case of the DFS algorithm family.
import turtle
from random import shuffle
import time
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        inorder(root.right)

def height(root):
    if root is None:
        return -1
    else:
        return max(height(root.left), height(root.right)) + 1


def draw_node(draw, draw2, node, x, y, dx, lst, _count=0):
    
    if node:
        if _count > 0:
            draw.pendown()
        else:
            draw.penup()
        draw.goto(x, y)
        draw.dot(8, 'orange')
        draw.hideturtle()
        
        draw.write(node.val, align='center', font=('Arial', 16, 'normal'))
        
        lst[-1].remove(node.val)
        lst.append([])
        lst[-1].extend(lst[-2])
        draw_list(draw2, lst)
        time.sleep(0.1)
        draw.showturtle()
        draw.penup()
        draw_node(draw,draw2, node.left, x-dx, y-60, dx/2, lst, _count+1)
        draw.goto(x, y)
        draw_node(draw,draw2, node.right, x+dx, y-60, dx/2, lst, _count+1)

def draw_list(draw2, lst):
    #draw2.clear()
    y_offset = len(lst) * 16
    draw2.goto(-420, -10 - y_offset)
    if isinstance(lst[-1], list):
        for i in lst[-1]:
            draw2.write(i, align='center', font=('Arial', 12, 'normal'))
            draw2.forward(20)

if __name__ == '__main__':
    
    # Input list
    for i in range(1, 5):
        time.sleep(1)
        print(i)
    nums = list(range(1, 20))
    shuffle(nums)

    root = None
    for num in nums:
        root = insert(root, num)

    
    inorder(root)

  
    h = height(root)
    WIDTH = 1000
    HEIGHT = 800
    Y_OFFSET = HEIGHT / 4
    NODE_OFFSET_Y = (HEIGHT / 2 ) - 40
    # Set up the window and its attributes
    turtle.setup(WIDTH, HEIGHT)

    # Create a turtle for drawing
    draw = turtle.Turtle()
    draw2 = turtle.Turtle()
    draw.penup()
    draw2.penup()
    draw.speed(3)
    draw2.hideturtle()
    
    draw.showturtle()
    
    

# Draw the tree
    draw_node(draw, draw2, root, 0, NODE_OFFSET_Y, 200, [nums.copy()])
    draw_list(draw2, nums)


    # Wait for user to close window
    turtle.mainloop()
