x_left, x_right = -0.5-0.25, -0.5+0.25
y_left, y_right = -0.5-0.25, -0.5+0.25
epsilon = 0.0001
delta = 0.1

def uslovie(x_left, x_right, y_left, y_right, epsilon):
    return sqrt(pow(x_left - x_right, 2) + pow(y_left - y_right, 2)) < epsilon

while uslovie(x_left, x_right, y_left, y_right, epsilon):
  x0 = (x_left + x_right) / 2
  y0 = (y_left + y_right) / 2

  x1 = x0 - delta
  x2 = x0 + delta
  y1 = y0 - delta
  y2 = y0 + delta

  fx1 = f(x1, y0)
  fx2 = f(x2, y0) 
  fy1 = f(x0, y1)
  fy2 = f(x0, y2)

  if fx1 > fx2:
    x_left = x1
  else:
    x_right = x2

  if fy1 > fy2:
    y_left = y1
  else:
    y_right = y2

  
    