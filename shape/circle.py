class Circle:
    def __init__(self,centre,radius):
        if len(centre)!= 2:
            raise ValueError
        self.centre=tuple(centre)
        self.radius=radius

    def __contains__(self,point):
        if len(point)!= 2:
            return NotImplemented
        else:
            x0,y0=self.centre
            x,y= point
            
            squared_distance=(x-x0)**2+(y-y0)**2
            return squared_distance<= self.radius**2
    def __repr__(self):
        return f"Circle(centre={self.centre}, radius={self.radius})"
            

