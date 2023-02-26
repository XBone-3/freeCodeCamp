class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
        self.set_side(self.width)
    def set_height(self, height):
        self.height = height
        self.set_side(self.height)
    def set_side(self, side):
        pass

    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return (self.width + self.height) * 2
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            pixel_row = ''
            for i in range(self.height):
                pixel_row += ("*" * self.width) + '\n'
            return pixel_row

    def get_amount_inside(self, obj):
        if obj.width > self.width or obj.height > self.height:
            return 0
        else:
            return (self.width // obj.width) * (self.height // obj.height)
        
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'



class Square(Rectangle):
    def __init__(self, side) -> None:
        self.side = side
        super().__init__(self.side, self.side)

    def set_side(self, side):
        self.side = side
        super().__init__(self.side, self.side)
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(side={self.side})'

