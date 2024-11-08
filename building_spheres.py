from math import pi
class Sphere(object):
    def __init__(self,radius,mass):
        self.radius = radius
        self.mass = mass 
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        volume = round(4 * pi * (self.radius**3) / 3, 5)      
        return volume
    def get_surface_area(self):
        surface_area = round((4 * pi *(self.radius)**2),5)
        return surface_area
    def get_density(self):
        density = round(self.mass/(4/3 * (pi * (self.radius)**3)),5)
        return density