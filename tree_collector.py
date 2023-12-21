from graphics import *
import time
import random

# Class to create tree

class Tree(Rectangle):

    def __init__(self, win, x, y, unit):

        trunk = Rectangle(Point(x - unit/2, y), Point(x + unit/2, y + unit * .825))
        trunk.setFill('brown')
        trunk.setOutline('brown')
        trunk.draw(win)
        crown = Polygon(Point(x - unit * 2, y + unit * .825), Point(x, y + unit * 4.575), Point(x + unit * 2, y + unit * .825))
        crown_color = random.choice(['green', 'green2', 'green4', 'yellow', 'yellow2', 'yellow4', 'purple', 'purple2', 'purple4'])
        crown.setFill(crown_color)
        crown.setOutline(crown_color)
        crown.draw(win)
        rec_p1 = Point(x - unit*2, y)
        rec_p2 = Point(x + unit*2, y + unit*4.575)
        self.trunk = trunk
        self.crown = crown
        self.crown_color = crown_color
        super().__init__(rec_p1, rec_p2)
        score = 11 - 10*unit
        self.score = score
        color = crown_color
        self.color = color

    # Function to return color of tree
    
    def getColor(self):
        
         return self.color

    # Function to return score value of clicked tree
    
    def getScore(self):

        return self.score

    # Function to move tree
    
    def move(self, dx, dy = 0):

        self.trunk.move(dx, dy)
        self.crown.move(dx, dy) 
        super().move(dx, dy)
    
        return

    # Function to undraw tree
    
    def undraw(self):

        self.trunk.undraw()
        self.crown.undraw()

        return

# Function to check if tree is clicked

def isClicked(pclick, rec):

    if rec.getP2().getX() > pclick.x > rec.getP1().getX() and rec.getP2().getY() > pclick.y > rec.getP1().getY():

        return True

    return False

def main():

    # Create Window
    
    win = GraphWin('Moving Trees', 800, 600)
    win.setCoords(0, 0, 40, 30)

    # Create sky
    
    bg = Rectangle(Point(0, 15), Point(40, 30))
    bg.setFill('light blue')
    bg.draw(win)

    # Create ground
    
    ground = Rectangle(Point(0, 0), Point(40, 15))
    ground.setFill('light green')
    ground.draw(win)

    # Create mountains
    
    mountain1 = Polygon(Point(0, 15), Point(15, 25), Point(35, 15))
    mountain1.setFill('dark green')
    mountain1.draw(win)

    mountain2 = Polygon(Point(10, 15), Point(23, 23), Point(40, 15))
    mountain2.setFill('dark green')
    mountain2.draw(win)

    # Create button
    
    button = Rectangle(Point(18, 1.5), Point(22, 3.5))
    button.setFill('light green')
    button.draw(win)

    label = Text(Point(20, 2.5), 'Start')
    label.setStyle('bold')
    label.draw(win)

    # Create main message
    
    top_message = Text(Point(20, 29), 'Please click the Start button to begin')
    top_message.setStyle('bold')
    top_message.setTextColor('green')
    top_message.draw(win)

    # Display Score
    
    score_title = Text(Point(17, 27), 'Current Score: ')
    score_title.setStyle('bold')
    score_title.setSize(18)
    score_title.setTextColor('blue')
    score_title.draw(win)

    score_message = Text(Point(23, 27), '0')
    score_message.setStyle('bold')
    score_message.setSize(18)
    score_message.setTextColor('blue')
    score_message.draw(win)

    # Display Color Counter
    
    clicked_colors_message = Text(Point(34, 23), '')
    clicked_colors_message.setStyle('bold')
    clicked_colors_message.setTextColor('purple')
    clicked_colors_message.draw(win)

    exit_bg = Rectangle(Point(5, 5), Point(35, 20))
    exit_bg.setFill('#000000')

    # Create Pause menu
    
    exit_message = Text(Point(20, 15), 'Click Exit to stop or Resume to continue')
    exit_message.setSize(18)
    exit_message.setStyle('bold')
    exit_message.setTextColor('red')

    confirm_button = Rectangle(Point(13, 7), Point(17, 9))
    confirm_button.setFill('#000000')
    confirm_button.setOutline('white')

    confirm_label = Text(Point(15, 8), 'Exit')
    confirm_label.setStyle('bold')
    confirm_label.setTextColor('white')

    go_back_button = Rectangle(Point(23, 7), Point(27, 9))
    go_back_button.setFill('#000000')
    go_back_button.setOutline('white')

    go_back_label = Text(Point(25, 8), 'Resume')
    go_back_label.setStyle('bold')
    go_back_label.setTextColor('white')

   # Initial conditions
   
    gameState = 0
    initial_time = 0
    val_tree_list = []
    color_dictionary = {}
    total_score = 0

    while True:

        point_of_click = win.checkMouse()

        # If there is no click and the game is in start mode: create a tree every second, and move it to the right
        
        if point_of_click == None and gameState == 1:

            current_time = time.time()

            if current_time - initial_time > 1:

                elapsed = current_time - initial_time
                
                rand_x = random.uniform(3.5, 4.5)
                rand_y = random.uniform(4, 16)
                rand_unit = random.uniform(.6, 1)

                tree = Tree(win, rand_x, rand_y, rand_unit)
        
                val_tree_list.append(tree)
                initial_time = current_time

                tree_list = []
                
                for i in val_tree_list:

                    i.move(4, 0)
                    x_tree = i.getP2().getX()

                    if x_tree >= 40:

                        i.undraw()

                    if x_tree < 40:

                        tree_list.append(i)

                val_tree_list = tree_list
                        
            text = ''
            
            for p in color_dictionary:

                color_counter = color_dictionary[p]
                string = str(p) + ' ' + str(color_counter)
                text = text + string + '\n'

            clicked_colors_message.setText(text)
            
       # If there is a click: get the x and y coordinates
       
        if point_of_click != None:

            if gameState == 1:
                
                update_tree_list = []
                x_coor = point_of_click.getX()
                y_coor = point_of_click.getY()

                # For each tree in the window: if the tree is clicked, undraw the tree, update score
                
                for k in val_tree_list:

                    if isClicked(point_of_click, k):
                        
                        score = int(k.getScore())
                        color = str(k.getColor())
                        k.undraw()

                        if color in color_dictionary:

                            color_dictionary[color] += 1
                            
                            if color_dictionary[color] == 6:
    
                                total_score -= score * 3
                                score_message.setText(str(total_score))
                                score_message.setTextColor('red')
                                color_dictionary[color] = 0

                            else:

                                total_score += score
                                score_message.setText(str(total_score))
                                score_message.setTextColor('blue')

                        else:

                            color_dictionary[color] = 1
                            total_score += 2*score
                            score_message.setText(str(total_score))
                            score_message.setTextColor('blue')
                
                    if isClicked(point_of_click, k) == False:

                        update_tree_list.append(k)

                val_tree_list = update_tree_list

            # If the game state is in initial mode: check to see if the user clicks the start button
            
            if gameState == 0:

                time.sleep(.1)

                x_coor = point_of_click.getX()
                y_coor = point_of_click.getY()
                
                if x_coor >= 18 and y_coor >= 1.5 and x_coor <= 22 and y_coor <= 3.5:

                    top_message.setText('Click a moving tree or Pause to stop')
                    label.setText('Pause')
                    gameState = 1

            # If the game state is in start mode: check to see if the user pauses the game
            
            elif gameState == 1:

                if x_coor >= 18 and y_coor >= 1.5 and x_coor <= 22 and y_coor <= 3.5:
                    
                    exit_bg.draw(win)
                    exit_message.draw(win)
                    confirm_button.draw(win)
                    go_back_button.draw(win)
                    confirm_label.draw(win)
                    go_back_label.draw(win)

                    gameState = 2

            # If the game state is in pause mode: check to see if user resumes or exits game
            
            elif gameState == 2:

                time.sleep(.1)
                x_coor = point_of_click.getX()
                y_coor = point_of_click.getY()


                if x_coor >= 13 and y_coor >= 7 and x_coor <= 17 and y_coor <= 9:

                    win.close()

                    break

                if x_coor >= 23 and y_coor >= 7 and x_coor <= 27 and y_coor <= 9:

                    exit_bg.undraw()
                    exit_message.undraw()
                    confirm_button.undraw()
                    go_back_button.undraw()
                    confirm_label.undraw()
                    go_back_label.undraw()

                    gameState = 1
                    
main()
