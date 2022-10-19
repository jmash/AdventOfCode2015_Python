import sys

if __name__ == '__main__':
    if sys.argv[1] == 'part1':
        with open('./Day2/gift_dimensions.txt', 'r', encoding="utf-8") as f:
            read_dimensions = f.readlines()
            read_dimensions_stripped = list(map(str.strip, read_dimensions))
            total_wrapping_paper = 0
            for dimensions in read_dimensions_stripped:
                dimension_values = dimensions.split('x')
                int_dimension_values = list(map(int, dimension_values))
                min_surface_area = min(int_dimension_values[0] * int_dimension_values[1],
                                       int_dimension_values[1] * int_dimension_values[2],
                                       int_dimension_values[0] * int_dimension_values[2])
                total_wrapping_paper += \
                    2 * (int_dimension_values[0] * int_dimension_values[1]) + \
                    2 * (int_dimension_values[1] * int_dimension_values[2]) + \
                    2 * (int_dimension_values[0] * int_dimension_values[2]) + \
                    min_surface_area
            print(total_wrapping_paper)

    if sys.argv[1] == 'part2':
        with open('./Day2/gift_dimensions.txt', 'r', encoding="utf-8") as f:
            read_dimensions = f.readlines()
            read_dimensions_stripped = list(map(str.strip, read_dimensions))
            total_ribbon = 0
            for dimensions in read_dimensions_stripped:
                dimension_values = dimensions.split('x')
                int_dimension_values = list(map(int, dimension_values))
                min_dimensions = sorted(int_dimension_values)[:2]
                min_perimeter = 2*min_dimensions[0] + 2*min_dimensions[1]
                gift_volume = int_dimension_values[0]*int_dimension_values[1]*int_dimension_values[2]
                total_ribbon += min_perimeter + gift_volume
            print(total_ribbon)