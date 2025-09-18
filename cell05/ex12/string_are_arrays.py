import sys

if len(sys.argv) != 2:
    print("none")
else:
    input_str = sys.argv[1]
    z_conut = input_str.count('z')

    if "z_count" == 0:
        print("none")
    else:
        for _ in range(z_conut):
            print("2")