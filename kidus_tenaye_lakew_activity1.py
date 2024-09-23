from turtle import Turtle,Screen
from project_functions import table, cake_maker,cake_decorations

sc = Screen()
turta = Turtle()
width = int(input("Enter the width (100-200) for the table: "))
height = int(input("Enter the height (0-100) for the table: "))
table_color = input("Enter a color for the table: ")
layer1_color = input("Enter a color for the first layer of cake: ")
layer2_color = input("Enter a color for the second layer of cake: ")
layer3_color = input("Enter a color for the third layer of cake: ")



table(width, height, table_color, turta)
cake_maker(width, layer1_color, layer2_color, layer3_color, turta)
cake_decorations(width, turta)
print("Your cake is loading! Happy Birthday!")
print("Press any key to exit......")


sc.exitonclick()