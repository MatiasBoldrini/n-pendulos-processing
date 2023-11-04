import math

class Pendulum:
    def __init__(self, temp_mass, temp_line_length, temp_pos_angle, temp_vel):
        self.mass = temp_mass
        self.line_length = temp_line_length
        self.pos_angle = temp_pos_angle
        self.vel = temp_vel

    def pos_x(self):
        return self.line_length * math.sin(self.pos_angle)

    def pos_y(self):
        return self.line_length * math.cos(self.pos_angle)

    def get_mass(self):
        return self.mass

    def get_pos_angle(self):
        return self.pos_angle

    def get_vel(self):
        return self.vel

# Ejemplo de cómo crear un objeto de la clase Pendulum en Python
# pendulum_obj = Pendulum(temp_mass, temp_line_length, temp_pos_angle, temp_vel)
