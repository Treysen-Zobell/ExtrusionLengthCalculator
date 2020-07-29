
import itertools
import time

# 600 600 500 300 300 100 50 50 50 100 500 100 : Pretty Ridiculous, Don't Try For Most Efficiency, Just Let It Do A Few Iterations
# 600 600 500 300 300 100 50 50 50 100 500     : 215509 = 3m26s
# 600 600 500 300 300 100 50 50 50 100         : 20276  = 2s
# 600 600 500 300 300 100 50 50 200            : 4482   = 0.4s
# 600 600 500 300 300 100 50 50                : 3566   = 0.4s
# 600 600 500 300 300 100 50                   : 2394   = 0.2s
# 600 600 500 300 300 100                      : 2211   = 0.2s

start_time_millis = int(round(time.time() * 1000))

lengths = input('Extrusion Lengths(mm) Separated by Space: ').split(' ')
lengths = [int(i) for i in lengths]

extrusion_length = input('Extrusion Length(mm) to Divide Into: ')
extrusion_length = int(extrusion_length)

cut_width = 2

total_waste = sum(lengths)
most_efficient_order = lengths
extrusions_required = len(lengths)

i = 1
iterator = itertools.permutations(lengths)
for order in iterator:
    current_waste = 0
    current_extrusions_required = 1

    temp_extrusion_length = 0

    for length in order:
        if temp_extrusion_length + length + cut_width < extrusion_length:
            temp_extrusion_length += length + cut_width
        else:
            current_waste += extrusion_length - temp_extrusion_length
            current_extrusions_required += 1
            temp_extrusion_length = 0

    current_waste += extrusion_length - temp_extrusion_length
    current_extrusions_required += 1

    if current_waste < total_waste:
        total_waste = current_waste
        most_efficient_order = order
        extrusions_required = current_extrusions_required

        print('More Efficient Arrangement Found! [%i]' % i)
        print('   Total Waste: %i' % total_waste)
        print('   Order:', end='       ')
        temp_extrusion_length = 0
        for length in most_efficient_order:
            if temp_extrusion_length + length < extrusion_length:
                print(length, end=' ')
                temp_extrusion_length += length
            else:
                print('\n                %s' % length, end=' ')
                temp_extrusion_length = length
        end_time_millis = int(round(time.time() * 1000))
        print()
        print('Execution Time (ms): %i' % (end_time_millis - start_time_millis))

        i += 1

print('Most Efficient Arrangement:')
print('   Total Waste: %i' % total_waste)
print('   Order:', end='       ')
temp_extrusion_length = 0
for length in most_efficient_order:
    if temp_extrusion_length + length < extrusion_length:
        print(length, end=' ')
        temp_extrusion_length += length
    else:
        print('\n                %s' % length, end=' ')
        temp_extrusion_length = length
print()
print('Execution Time (ms): %i' % (end_time_millis - start_time_millis))

input('')
