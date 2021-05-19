from manim import *

class proof(Scene):
    def construct(self):
        square = Square().scale(2)
        square.shift([0,-1,0])
        dots = [square.point_from_proportion(i/4 + 1/16) for i in range(4)]
        corners = [square.point_from_proportion(i/4) for i in range(4)]
        line1 = Polygon(dots[0],dots[1])
        line2 = Polygon(dots[1],dots[2])
        line3 = Polygon(dots[2],dots[3])
        line4 = Polygon(dots[3],dots[0])
        lines = [line1,line2,line3,line4]
        
        self.play(
            Create(square),
    
        )
        # square.generate_target
        # square.target.shift([0,-2,0])
        # self.play(MoveToTarget(square))
        self.play(
            *[Create(line) for line in lines],
            
        )
        #self.wait(2)
        text1 = Tex("Total"," Area","="," Area of inner Square"," + "," Area of four Triangles").shift([0,1,0]).shift([0,2,0])
        text2 = MathTex("(","a","+","b",")","(","a","+","b",")","=","c^2"," + ","4","{1 \\over","2}","(","a","b",")").shift([-2,1.98,0])
         
        a = TexMobject("a").set_color(BLUE)
    
        b = TextMobject("b").set_color(GREEN)
        c = TextMobject("c").set_color(RED)

        self.play(
            Write(a.copy().next_to(square,RIGHT).shift(DOWN)),
            Write(a.copy().next_to(square,DOWN).shift(LEFT)),
            Write(a.copy().next_to(square,LEFT).shift(UP)),
            Write(a.copy().next_to(square,UP).shift(RIGHT)),
            
            Write(b.copy().next_to(square,RIGHT).shift(UP + [0,0.5,0])),
            Write(b.copy().next_to(square,DOWN).shift(RIGHT + [0.5,0,0])),
            Write(b.copy().next_to(square,LEFT).shift(DOWN + [0,-0.5,0] )),
            Write(b.copy().next_to(square,UP).shift(LEFT + [-0.5,0,0])),

            Write(c.copy().next_to(line1.get_center()).shift([-0.2,-0.4,0])),
            Write(c.copy().next_to(line2.get_center()).shift([-0.6,0,0])),
            Write(c.copy().next_to(line3.get_center()).shift([-0.2,0.2,0])),
            Write(c.copy().next_to(line4.get_center()))
            




        )

        middle_square = Polygon(dots[0],dots[1],dots[2],dots[3], color= YELLOW, opacity = 0.5)
        middle_square.generate_target
        middle_square.set_fill(color = YELLOW, opacity = 0.2)
        square.generate_target()
        square.target.set_fill(BLUE,0.8)
        text1[3].set_color(YELLOW)
        text1[4:6].set_color(BLUE)

        text2[12:20].set_color(BLUE)
        text2[19].set_colour(YELLOW)
        text2[11].set_color(YELLOW)

        self.play(Write(text1[0:4]))
        self.play(Create(middle_square))
        self.wait(2)

        self.play(
            Write(text1[4:6])

        )




        
        triangle1 = Polygon(dots[0],corners[1],dots[1], color= BLUE, opacity = 0.5).set_fill(BLUE,0.2)
        triangle2 = Polygon(dots[1],corners[2],dots[2], color = BLUE, opacity = 0.5).set_fill(BLUE,0.2)
        triangle3 = Polygon(dots[2],corners[3],dots[3],color = BLUE, opacity = 0.2).set_fill(BLUE,0.2)
        triangle4 = Polygon(dots[3],corners[0],dots[0], color = BLUE, opacity = 0.2).set_fill(BLUE,0.2)

        self.play(
            #Transform(square,square.target),
            Create(triangle1),
            Create(triangle2),
            Create(triangle3),
            Create(triangle4)
            
        ) 
        self.wait(5) 
        
        self.play(
            Transform(text1[0:3].copy(),text2[0:11]),
            #Transform(text1[3].copy(),text2[9:13])
            
        )            
        self.wait(2)
        self.play(
            Transform(text1[3].copy(),text2[11])
        )
        self.wait(1)
        self.play(
            Transform(text1[5].copy(),text2[12:len(text2)+1])
        )
        self.wait(2)
        
        


        #pos_a = [dots[0]+[-1,0,0], dots[1] + [0,-1,0], dots[2] + [1,0,0], dots[3] + [0,1,0]]
        

    
        
        














        # right_square = Square().scale(2)
        # self.play(Create(left_square),Create(right_square))
        # left_square.generate_target()
        # left_square.target.shift([-4,0,0])
        # right_square.generate_target()
        # right_square.target.shift([4,0,0])
        # self.play(MoveToTarget(left_square), MoveToTarget(right_square))
        # triangle1 = Polygon([0,0,0],[0,1,0],[4,0,0])
        # triangle1.shift([-6,-2,0])
         
        # self.play(Create(triangle1))
      
        # self.wait(5)
        
        