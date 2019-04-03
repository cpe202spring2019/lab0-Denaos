def weight_on_planets():
    weight = int(input('What do you weigh on earth? '))
    weightmars =weight * 0.38
    weightjupiter =weight * 2.34
    print('')
    print('On Mars you would weigh {0:.2f} pounds.'.format(weightmars))
    print('On Jupiter you would weigh {0:.2f} pounds.'.format(weightjupiter))
   
if __name__ == '__main__':
    weight_on_planets()
