from manim import *

class HelloWorld(Scene):      
    def constructor(self):
        text1 = Text("Hello")
        text2 = Text("World")

        addition = Text(" ! + 1 = 2")

        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(1)
        self.play(FadeOut(text1), FadeOut(text2))
        self.play(Write(addition))
        self.wait(2)

        

  