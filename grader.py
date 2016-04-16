from __future__ import print_function
import sys
import math
import coordinates_tuples
import coordinates_dicts

'''
TEST DRIVER

DO NOT MODIFY

USAGE:

python grader.py [type] [number]

type is either 'tuples' or 'dicts' to specify running a test on the
implementation in coordinates_tuples or coordinates_dicts

number is the test number (1, 2, ...).

If you do not provide any arguments, the script will execute all tests
for both the tuples and dicts implementation.

If type is provided but the test number is not, all tests of that type
will run.

Examples:

python grader.py
python grader.py tuples
python grader.py tuples 4
python grader.py dicts
python grader.py dicts 3

These calls will run (1) all tests, (2) all tuples tests, (3) the fourth
tuples test, (4) all dicts tests, and (5) the third dicts test
'''

# A bunch of static data
SPACING = '     '
TOL = 1e-4
TESTS = {'tuples': [], 'dicts': []}
 
tuples_func_table = {'sphere2cart': coordinates_tuples.sphere2cart,
                    'sphere2cyl': coordinates_tuples.sphere2cyl,
                    'cyl2sphere': coordinates_tuples.cyl2sphere,
                    'cyl2cart': coordinates_tuples.cyl2cart,
                    'cart2sphere': coordinates_tuples.cart2sphere,
                    'cart2cyl': coordinates_tuples.cart2cyl,
                    'convert_points': coordinates_tuples.convert_points}

dicts_func_table = {'sphere2cart': coordinates_dicts.sphere2cart,
                   'sphere2cyl': coordinates_dicts.sphere2cyl,
                   'cyl2sphere': coordinates_dicts.cyl2sphere,
                   'cyl2cart': coordinates_dicts.cyl2cart,
                   'cart2sphere': coordinates_dicts.cart2sphere,
                   'cart2cyl': coordinates_dicts.cart2cyl,
                   'detect_type': coordinates_dicts.detect_type}

tuples_testpt1_cart = (1.0, 2.0, 3.0)
tuples_testpt1_cyl = (2.2360679774997898, 1.1071487177940904, 3.0)
tuples_testpt1_sphere = (3.7416573867739413, 0.6405223126794245, 1.1071487177940904)

dicts_testpt1_cart = {'x': tuples_testpt1_cart[0], 'y': tuples_testpt1_cart[1],
                      'z': tuples_testpt1_cart[2]}
dicts_testpt1_cyl = {'rho': tuples_testpt1_cyl[0], 'phi': tuples_testpt1_cyl[1],
                     'z': tuples_testpt1_cyl[2]}
dicts_testpt1_sphere = {'r': tuples_testpt1_sphere[0],
                        'theta': tuples_testpt1_sphere[1],
                        'phi': tuples_testpt1_sphere[2]}

tuples_testpt2_cart = (-1.0, -3.0, 2.0)
tuples_testpt2_cyl = (3.1622776601683795, -1.8925468811915389, 2.0)
tuples_testpt2_sphere = (3.7416573867739413, 1.0068536854342678, -1.8925468811915389)

dicts_testpt2_cart = {'x': tuples_testpt2_cart[0], 'y': tuples_testpt2_cart[1],
                      'z': tuples_testpt2_cart[2]}
dicts_testpt2_cyl = {'rho': tuples_testpt2_cyl[0], 'phi': tuples_testpt2_cyl[1],
                     'z': tuples_testpt2_cyl[2]}
dicts_testpt2_sphere = {'r': tuples_testpt2_sphere[0],
                        'theta': tuples_testpt2_sphere[1],
                        'phi': tuples_testpt2_sphere[2]}

tuples_testpt3_cart = (4.619397662556433, 1.9134171618254485, 8.6602540378443873)
tuples_testpt3_cyl = (4.9999999999999991, 0.39269908169872414, 8.6602540378443873)
tuples_testpt3_sphere = (10.0, math.pi / 6, math.pi / 8)

dicts_testpt3_cart = {'x': tuples_testpt3_cart[0], 'y': tuples_testpt3_cart[1],
                      'z': tuples_testpt3_cart[2]}
dicts_testpt3_cyl = {'rho': tuples_testpt3_cyl[0], 'phi': tuples_testpt3_cyl[1],
                     'z': tuples_testpt3_cyl[2]}
dicts_testpt3_sphere = {'r': tuples_testpt3_sphere[0],
                        'theta': tuples_testpt3_sphere[1],
                        'phi': tuples_testpt3_sphere[2]}

tuples_testpt4_cart = (5.3033008588991066, 5.3033008588991057, -8.0)
tuples_testpt4_cyl = (7.5, math.pi / 4, -8.0)
tuples_testpt4_sphere = (10.965856099730654, 2.3884413726275988, 0.78539816339744828)

dicts_testpt4_cart = {'x': tuples_testpt4_cart[0], 'y': tuples_testpt4_cart[1],
                      'z': tuples_testpt4_cart[2]}
dicts_testpt4_cyl = {'rho': tuples_testpt4_cyl[0], 'phi': tuples_testpt4_cyl[1],
                     'z': tuples_testpt4_cyl[2]}
dicts_testpt4_sphere = {'r': tuples_testpt4_sphere[0],
                        'theta': tuples_testpt4_sphere[1],
                        'phi': tuples_testpt4_sphere[2]}


def run_tuples_test(i, name, input, output):
  print('\nrunning tuples test %d...' % i)

  def compare_result(actual, expected):
    for exp, elmt in zip(expected, actual):
      if abs(elmt - exp) / abs(exp) > TOL:
        print('%s FAILED (expected: %s, actual: %s)' % (SPACING, str(expected),
                                                      str(actual)))
        return False
    return True

  if name is 'convert_points':
    try:
      result = tuples_func_table[name](**input)
    except:
      print('%s FAILED could not run tuples function %s' % (SPACING, name))
      return False
    if not type(result) == type([]):
      print('%s FAILED expected list type, input was: %s' % (SPACING,
          str(input['points'])))
    if len(result) != len(input['points']):
      print('%s FAILED: expected %d elements in list, but there were %d' % (
          SPACING, len(input['points']), len(result)))
      return False
    for res, out in zip(result, output):
      if not compare_result(res, out):
        return False
  else:
    result = tuples_func_table[name](input)
    if not compare_result(result, output):
      return False
  
  print('%s SUCCESS' % SPACING)
  return True


def run_dicts_test(i, name, input, output):
  print('\nrunning dicts test %d...' % i)

  try:
    result = dicts_func_table[name](input)
  except:
    print('%s FAILED could not run dicts function %s' % (SPACING, name))
    return False

  if name is 'detect_type':
    if output != result:
      print('%s FAILED (expected %s, actual: %s)' % (SPACING, output,
                                                     str(result)))
      return False
  else:
    for key in output:
      if key not in result:
        print('%s FAILED (missing key: %s)' % (SPACING, key))
        return False
      
      if abs(result[key] - output[key]) / abs(output[key]) > TOL:
        print('%s FAILED on %s (expected: %s, actual: %s)' % (SPACING,
                                                              str(key),
                                                              str(output[key]),
                                                              str(result[key])))
        print('%s input was: %s' % (SPACING, str(input)))
        return False

  print('%s SUCCESS' % SPACING)
  return True


def create_test(i, name, input, output, type):
  TESTS[type].append({'i': i, 'name': name, 'input': input, 'output': output})


def init_tuples_tests():
  create_test(1, 'cart2cyl',
              tuples_testpt1_cart, tuples_testpt1_cyl, 'tuples')
  create_test(2, 'cyl2cart',
              tuples_testpt1_cyl, tuples_testpt1_cart, 'tuples')
  create_test(3, 'cart2sphere',
              tuples_testpt1_cart, tuples_testpt1_sphere, 'tuples')
  create_test(4, 'sphere2cart',
              tuples_testpt1_sphere, tuples_testpt1_cart, 'tuples')
  create_test(5, 'sphere2cyl',
              tuples_testpt1_sphere, tuples_testpt1_cyl, 'tuples')
  create_test(6, 'cyl2sphere',
              tuples_testpt2_cyl, tuples_testpt2_sphere, 'tuples')
  create_test(7, 'cart2cyl',
              tuples_testpt2_cart, tuples_testpt2_cyl, 'tuples')
  create_test(8, 'sphere2cart',
              tuples_testpt2_sphere, tuples_testpt2_cart, 'tuples')
  create_test(9, 'cyl2cart',
              tuples_testpt2_cyl, tuples_testpt2_cart, 'tuples')
  create_test(10, 'sphere2cyl',
              tuples_testpt2_sphere, tuples_testpt2_cyl, 'tuples')

  create_test(11, 'convert_points',
              {'points': [tuples_testpt1_cart, tuples_testpt2_cart],
               'type': 'cart', 'new_type': 'sphere'},
              [tuples_testpt1_sphere, tuples_testpt2_sphere], 'tuples')
  create_test(12, 'convert_points',
              {'points': [tuples_testpt1_cart, tuples_testpt2_cart],
               'type': 'cart', 'new_type': 'cyl'},
              [tuples_testpt1_cyl, tuples_testpt2_cyl], 'tuples')
  create_test(13, 'convert_points',
              {'points': [tuples_testpt1_cyl, tuples_testpt2_cyl],
               'type': 'cyl', 'new_type': 'cart'},
              [tuples_testpt1_cart, tuples_testpt2_cart], 'tuples')
  create_test(14, 'convert_points',
              {'points': [tuples_testpt3_sphere] * 4 + [tuples_testpt4_sphere] * 6,
               'type': 'sphere', 'new_type': 'cart'},
              [tuples_testpt3_cart] * 4 + [tuples_testpt4_cart] * 6, 'tuples')
  create_test(15, 'convert_points',
              {'points': [], 'type': 'cyl', 'new_type': 'sphere'},
              [], 'tuples')


def init_dicts_tests():
  create_test(1, 'cart2cyl',
              dicts_testpt1_cart, dicts_testpt1_cyl, 'dicts')
  create_test(2, 'cyl2cart',
              dicts_testpt1_cyl, dicts_testpt1_cart, 'dicts')
  create_test(3, 'cart2sphere',
              dicts_testpt1_cart, dicts_testpt1_sphere, 'dicts')
  create_test(4, 'sphere2cart',
              dicts_testpt1_sphere, dicts_testpt1_cart, 'dicts')
  create_test(5, 'sphere2cyl',
              dicts_testpt1_sphere, dicts_testpt1_cyl, 'dicts')
  create_test(6, 'cyl2sphere',
              dicts_testpt2_cyl, dicts_testpt2_sphere, 'dicts')
  create_test(7, 'cart2cyl',
              dicts_testpt2_cart, dicts_testpt2_cyl, 'dicts')
  create_test(8, 'sphere2cart',
              dicts_testpt2_sphere, dicts_testpt2_cart, 'dicts')
  create_test(9, 'cyl2cart',
              dicts_testpt2_cyl, dicts_testpt2_cart, 'dicts')
  create_test(10, 'cyl2sphere',
              dicts_testpt2_cyl, dicts_testpt2_sphere, 'dicts')

  create_test(11, 'detect_type', dicts_testpt3_cart, 'cart', 'dicts')
  create_test(12, 'detect_type', dicts_testpt3_cyl, 'cyl', 'dicts')
  create_test(13, 'detect_type', dicts_testpt3_sphere, 'sphere', 'dicts')
  create_test(14, 'detect_type', dicts_testpt2_cart, 'cart', 'dicts')
  create_test(15, 'detect_type', dicts_testpt2_cyl, 'cyl', 'dicts')


def main():
  init_tuples_tests()
  init_dicts_tests()

  test_type = None
  if len(sys.argv) > 1:
    test_type = sys.argv[1]
    if test_type not in ['tuples', 'dicts']:
      print("UNKNOWN testing type: %s.  Use 'tuples' or 'dicts'." % test_type)
      return

  test_number = None
  if len(sys.argv) > 2:
    test_number = int(sys.argv[2])
    if not 0 < test_number <= len(TESTS[test_type]):
      print('invalid test number: ' + sys.argv[2])
      return

  test_funcs = {'tuples': run_tuples_test, 'dicts': run_dicts_test}

  total_tests = 0
  successes = 0
  if test_number is not None:
    if test_funcs[test_type](**TESTS[test_type][test_number - 1]):
      successes += 1
    total_tests += 1
  elif test_type is not None:
    for test in TESTS[test_type]:
      if test_funcs[test_type](**test):
        successes += 1
      total_tests += 1
  else:
    for test in TESTS['tuples']:
      if run_tuples_test(**test):
        successes += 1
      total_tests += 1
    for test in TESTS['dicts']:
      if run_dicts_test(**test):
        successes += 1
      total_tests += 1

  print('\n%d / %d correct (%f)' % (successes, total_tests,
                                    float(successes) / total_tests))


if __name__ == "__main__":
  main()
