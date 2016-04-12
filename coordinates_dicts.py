import math

'''
Convert a dictionary of spherical coordinates to a dictionary of
cylindrical coordinates.

coords is a dictionary with string keys 'r', 'theta', and 'phi' with
       corresponding values as spherical coordinate values
return value is a dictionary with keys 'rho', 'phi', and 'z'  with
       corresponding values as cylindrical coordinate values
'''
def sphere2cyl(coords):
  r = coords['r']
  theta = coords['theta']
  phi = coords['phi']

  # initialize empty dictionary
  cart_points = {}

  cart_points['x'] = r*math.sin(theta)*math.cos(phi)
  cart_points['y'] = r*math.sin(theta)*math.sin(phi)
  cart_points['z'] = r*math.cos(theta)
  
  cyl_points = cart2cyl(cart_points)

  return cyl_points

'''
Convert a dictionary of spherical coordinates to a dictionary of
cartesian coordinates.

coords is a dictionary with string keys 'r', 'theta', and 'phi' with
       corresponding values as spherical coordinate values
return value is a dictionary with keys 'x', 'y', and 'z'  with
       corresponding values as cartesian coordinate values
'''
def sphere2cart(coords):
  # From lecture 2 slides
  r = coords['r']
  theta = coords['theta']
  phi = coords['phi']

  # initialize empty dictionary
  cart_points = {}

  cart_points['x'] = r*math.sin(theta)*math.cos(phi)
  cart_points['y'] = r*math.sin(theta)*math.sin(phi)
  cart_points['z'] = r*math.cos(theta)

  return cart_points

'''
Convert a dictionary of cylindrical coordinates to a dictionary of
spherical coordinates.

coords is a dictionary with string keys 'rho', 'phi', and 'z' with
       corresponding values as cylindrical coordinate values
return value is a dictionary with keys 'r', 'theta', and 'phi'  with
       corresponding values as spherical coordinate values
'''
def cyl2sphere(coords):
  # From lecture 2 slides
  rho = coords['rho']
  phi = coords['phi']
  z = coords['z']

  # initialize empty dictionary
  cart_points = {}

  cart_points['x'] = rho*math.cos(phi)
  cart_points['y'] = rho*math.sin(phi)
  cart_points['z'] = z
  
  sphere_points = cart2sphere(cart_points)

  return sphere_points


'''
Convert a dictionary of cylindrical coordinates to a dictionary of
cartesian coordinates.

coords is a dictionary with string keys 'rho', 'phi', and 'z' with
       corresponding values as cylindrical coordinate values
return value is a dictionary with keys 'x', 'y', and 'z'  with
       corresponding values as cartesian coordinate values
'''
def cyl2cart(coords):
  # From lecture 2 slides
  rho = coords['rho']
  phi = coords['phi']
  z = coords['z']

  # initialize empty dictionary
  cart_points = {}

  cart_points['x'] = rho*math.cos(phi)
  cart_points['y'] = rho*math.sin(phi)
  cart_points['z'] = z

  return cart_points


'''
Convert a dictionary of cartesian coordinates to a dictionary of
spherical coordinates.

coords is a dictionary with string keys 'x', 'y', and 'z' with
       corresponding values as cartesian coordinate values
return value is a dictionary with keys 'r', 'theta', and 'phi'  with
       corresponding values as spherical coordinate values
'''
def cart2sphere(coords):
  # From lecture 2 slides
  x = coords['x']
  y = coords['y']
  z = coords['z']

  # initialize empty dictionary
  cart_points = {}

  cart_points['r'] = math.sqrt(x ** 2 + y ** 2 + z ** 2)
  cart_points['theta'] = math.acos(z / cart_points['r'])
  cart_points['phi'] = math.atan2(y, x)

  return cart_points


'''
Convert a dictionary of cartesian coordinates to a dictionary of
cylindrical coordinates.

coords is a dictionary with string keys 'x', 'y', and 'z' with
       corresponding values as cartesian coordinate values
return value is a dictionary with keys 'rho', 'phi', and 'z'  with
       corresponding values as cylindrical coordinate values
'''
def cart2cyl(coords):
  # From lecture 2 slides
  x = coords['x']
  y = coords['y']
  z = coords['z']

  # initialize empty dictionary
  cart_points = {}

  cart_points['rho'] = math.sqrt(x ** 2 + y ** 2)
  cart_points['phi'] = math.atan2(y,x)
  cart_points['z'] = z

  return cart_points

'''
Determine the type of the coordinate dictionary.

coords is a dictionary representing a point in either cartesian,
       spherical, or cylindrical coordinates
return value is a string of either 'cart', 'sphere', or 'cyl'

As an example:
  point1 = {'x': 1, 'y': 2, 'z': 3}
  point2 = cart2cyl(point1)
  print detect_type(point1) # should print 'cart'
  print detect_type(point2) # should print 'cyl'
'''
def detect_type(coords):
  # IMPLEMENT THIS FUNCTION
  if 'x' in coords and 'y' in coords and 'z' in coords:
   return 'cart'
  elif 'rho' in coords and 'phi' in coords and 'z' in coords:
   return 'cyl'
  elif 'r' in coords and 'theta' in coords and 'phi' in coords:
   return 'sphere'
