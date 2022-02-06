import math
import os
def menu():
    print('Trig Math Solver 1.0v\n'
          '=======================\n'
          'Command Format: -s 22 opp\n\n'
          'Sin: -s (opp/hyp)\n'
          'Cos: -c (adj/hpy)\n'
          'Tan: -t (opp/adj)')
    command = input('Command: ').lower()
    try:
        for formula in command[1].split('-s' and '-c' and '-t'):  # Finds Formula
            list1 = list(command.split(" "))
            global reference_angle,needed_angle,rad
            reference_angle = list1[1]
            #check = isinstance(reference_angle, int) For ref check
            needed_angle = list1[2]
            if needed_angle.isdigit() or formula.isdigit() is True: #Checks if formula or angle is an int
                print('Invalid Angle or Formula')
                menu()
            else:
                if formula == 's':
                    sin()
                if formula == 'c':
                    cosine()
                if formula == 't':
                    tan()
    except Exception as e:
        print(e)
        menu()

def sin():
    os.system('cls')
    rad = math.radians(int(reference_angle))
    sin = math.sin(rad)
    if needed_angle == 'hyp': #Finding Opposite Value
        adjacent_angle = int(input('Opposite Angle: '))
        sum_opposite = float(adjacent_angle / sin)
        print(f'Hyp Value: {sum_opposite}\n')
        menu()

    if needed_angle == 'opp': #Finding Opposite Angle
        hypotoneus_angle = int(input('Hypotoneus angle: '))
        sum_opposite = (hypotoneus_angle * sin)
        print(f'Opposite Angle: {sum_opposite}\n')
        menu()

    else:
        print('Error')


def cosine():
    os.system('cls')
    rad = math.radians(int(reference_angle))
    cosine = math.cos(rad)
    if needed_angle == 'adj':
        hyp_angle = int(input('Opposite Angle: '))
        cosine_sum_adjacent = float(hyp_angle * cosine)
        print(f'Adjacent Angle: {cosine_sum_adjacent}\n')
        menu()

    if needed_angle == 'hyp':
        cosine_sum_adjacent_hyp = int(input('Adjacent angle: '))
        cosine_sum_hyp = (cosine_sum_adjacent_hyp / cosine)
        print(f'Hyp Angle: {cosine_sum_hyp}\n')
        menu()


def tan():
    os.system('cls')
    rad = math.radians(int(reference_angle))
    tanget = math.tan(rad)
    if needed_angle == 'opp':
        adjacent_angle = int(input('Adjacent: '))
        tan_opposite_angle = float(adjacent_angle * tanget)
        print(f'Opposite Angle: {tan_opposite_angle}\n')
        menu()

    if needed_angle == 'adj':
        tan_adjacent_angle_angle = int(input('Opposite angle: '))
        tan_sum_adjacent = float(tan_adjacent_angle_angle / tanget)
        print(f'Adjacent Angle: {tan_sum_adjacent}\n')
        menu()


if __name__ == '__main__':
    menu()
