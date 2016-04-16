import math

'''
Convert a tuple of spherical coordinates to a tuple of cylindrical coordinates.

coords is a tuple in (r, theta, phi) form
return value is a tuple in (rho, phi, z) form
'''
def sphere2cyl(coords):
  # From lecture 2 slides
  # x, y, z = coords
  r, theta, phi = coords
  x, y, z = sphere2cart(coords)
  coords = (x,y,z)
  row,phi,z = cart2cyl(coords)
  return (row,phi,z)

'''
Convert a tuple of spherical coordinates to a tuple of cartesian coordinates.

coords is a tuple in (r, theta, phi) form
return value is a tuple in (x, y, z) form
'''
def sphere2cart(coords):
  # IMPLEMENT THIS FUNCTION
  r, theta, phi = coords
  x = r*math.sin(theta)*math.cos(phi)
  y = r*math.sin(theta)*math.sin(phi)
  z = r*math.cos(theta)
  return (x,y,z)



'''
Convert a tuple of cylindrical coordinates to a tuple of spherical coordinates.

coords is a tuple in (rho, phi, z) form
return value is a tuple in (r, theta, phi) form
'''
def cyl2sphere(coords):
  # IMPLEMENT THIS FUNCTION
  row, phi, z = coords
  x, y, z = cyl2cart(coords)
  coords = (x,y,z)
  r,theta,phi = cart2sphere(coords)
  return (r,theta,phi)


'''
Convert a tuple of cylindrical coordinates to a tuple of spherical coordinates.

coords is a tuple in (rho, phi, z) form
return value is a tuple in (x, y, z) form
'''
def cyl2cart(coords):
  # IMPLEMENT THIS FUNCTION
  row, phi, z = coords
  x = row*math.cos(phi)
  y = row*math.sin(phi)
  z = z
  return (x,y,z)



'''
Convert a tuple of cartesian coordinates to a tuple of spherical coordinates.

coords is a tuple in (x, y, z) form
return value is a tuple in (r, theta, phi) form
'''
def cart2sphere(coords):
  # From lecture 2 slides
  x, y, z = coords
  r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
  theta = math.acos(z / r)
  phi = math.atan2(y, x)
  return (r, theta, phi)


'''
Convert a tuple of cartesian coordinates to a tuple of cylindrical coordinates.

coords is a tuple in (x, y, z) form
return value is a tuple in (rho, phi, z) form
'''
def cart2cyl(coords):
  # From lecture 2 slides
  x, y, z = coords
  row = math.sqrt(x ** 2 + y ** 2)
  phi = math.atan2(y,x)
  z=z
  return (row, phi, z)



'''
Convert a new list of points from one type to another

points is a list of tuples of points
type is the type of points in the list.  type is one of 'cart', 'sphere', 'cyl'
new_type is the type of 
'''
def convert_points(points, type = ' ', new_type = ' '):
    if type is new_type: #Create a copy instead of returning the exact list
     return points[: ]
    elif type == 'cyl' and new_type == 'cart': #Create a copy instead of returning the exact list
     ans = []
     for i in range(len(points)):
      coords = points[i]
      sample = cyl2cart(coords)
      ans.append(sample)
     return ans[:]
    elif type == 'cart' and new_type == 'sphere': #Create a copy instead of returning the exact list
     ans = []
     for i in range(len(points)):
      coords = points[i]
      sample = cart2sphere(coords)
      ans.append(sample)
     return ans[:]
     #sreturn cart2sphere(points)
    elif type == 'sphere' and new_type == 'cart': #Create a copy instead of returning the exact list
     ans = []
     for i in range(len(points)):
      coords = points[i]
      sample = sphere2cart(coords)
      ans.append(sample)
     return ans[:]
    elif type == 'cart' and new_type == 'cyl': #Create a copy instead of returning the exact list
     ans = []
     for i in range(len(points)):
      coords = points[i]
      sample = cart2cyl(coords)
      ans.append(sample)
     return ans[:]
    elif type == 'sphere' and new_type == 'cyl': #Create a copy instead of returning the exact list
     ans = []
     for i in range(len(points)):
      coords = points[i]
      sample = sphere2cyl(coords)
      ans.append(sample)
     return ans[:]
    elif type == 'cyl' and new_type == 'sphere': #Create a copy instead of returning the exact list
     ans = []
     for i in range(len(points)):
      coords = points[i]
      sample = cyl2sphere(coords)
      ans.append(sample)
     return ans[:]
	 

  # FINISH THIS FUNCTIONS
  # HINT: it may be useful to use a list comprehension

  #return []
