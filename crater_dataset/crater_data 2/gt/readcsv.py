locations = []
with open('gt_tile3_24.csv', 'rb') as file:
    for row in file:
        entry = map(int, row.strip('\n').split(','))
        print entry

print locations
