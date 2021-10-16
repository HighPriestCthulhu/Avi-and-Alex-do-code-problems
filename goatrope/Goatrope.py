import sys
from typing import List
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
FILENAME="1.in"
ab=[]
def read_file_contents(filename=FILENAME):
    with open(filename, 'r') as f:
        txt=f.read()
        return txt.split()

def main():
    x=read_file_contents()
    g=process_file_contents(x)
    g.plot()
    # print(distance_between_points(x[0],x[1]))
    # print(distance_between_points(x[0],x[2]))

    # print(ab)
    # closest_corner(ab)

def process_file_contents(l:List):
    x=[[i,i+1] for i in range(0,len(l),2)]
    return Grid(x)


def distance_between_points(a,b):
  return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


if __name__ == '__main__':
    main()
class Grid:
  def __init__(self, l):
    self.pole = l[0]
    self.corner_bottom = l[1]
    self.corner_top = l[2]

  @property
  def house_width(self):
    return self.corner_top[0] - self.corner_bottom[0]

  def get_minimum_corner(self):
    if self.pole[0] >self.corner_top[0] and  self.pole[0] > self.corner_bottom[0]:
      x1d=self.pole[0]-self.corner_top[0]
      x2d=self.pole[0]-self.corner_bottom[0]
      return x1d if x1d < x2d else x2d
    elif self.pole[1] >self.corner_top[1] and  self.pole[1] > self.corner_bottom[1]:
      x1d=self.pole[1]-self.corner_top[1]
      x2d=self.pole[1]-self.corner_bottom[1]
      return x1d if x1d < x2d else x2d
    else 
      d1 = distance_between_points(self.pole, self.corner_top)
      d2 = distance_between_points(self.pole, self.corner_bottom)
      d3 = distance_between_points(self.pole, [self.corner_top[0],self.corner_bottom[1]])
      
  @property
  def house_height(self):
    return self.corner_top[1] - self.corner_bottom[1]

  def plot(self):
    fig, ax = plt.subplots()
    ax.scatter(self.pole[0], self.pole[1])
    ax.add_patch(Rectangle([self.corner_bottom[0], self.corner_bottom[1]], self.house_width, self.house_height))
    return fig