import sys

sys.stdin = open("input.txt", "r") # Comment this line out when submitting on the platform

seq_length, take_out = int(input()), int(input())

seq = [int(input()) for _ in range(seq_length)]
lengths = [0] * seq_length

max_seq = 0
window = seq_length - 1
current = 0
partial_seq_lengths = [0] * (take_out + 1)
skip_outer = False

# Fill DP table
for i in range(seq_length):
    if i == 0:
        lengths[i] = 1
    elif seq[i] > seq[i-1]:
        lengths[i] = lengths[i-1] + 1
    else:
        lengths[i] = 1

# Get the first max sequence length, taking out take_out elements
i = 0
while i < take_out and window >= 0:
    current = lengths[window]
    current_length = 0 
    
    # If you find a partial sequence that is already longer than max, update the max sequence length
    if window - 1 >= 0 and lengths[window - 1] > max_seq:
        max_seq = lengths[window - 1]

    if current > max_seq:
        max_seq = current
    
    # Go to the before-first element of this partial sequence    
    while current >= 2 and lengths[window] != 2:
        window -= 1
    
    # Length of the sequence starting from the before-first element of this partial sequence
    right_length = current - 1
    left_length = lengths[window - 2]

    # Checking if removing the first element of this partial sequence and adding the last element of the sequence to the left of this partial sequence will give a longer sequence
    if window - 2 >= 0 and seq[window - 2] < seq[window]:
        current_length = left_length + right_length
        partial_seq_lengths[i] = right_length
        partial_seq_lengths[i+1] = left_length

    while lengths[window] != 1:
        window -= 1
        
    right_length = current
    left_length = lengths[window - 2]
    
    # Checking if you can remove a number between the end of one and beginning of another sequence
    if window - 2 >= 0 and seq[window - 2] < seq[window] and left_length + right_length > current_length:
        # current_length would still be left_length + right_length, but we don't need it
        partial_seq_lengths[i] = right_length
        partial_seq_lengths[i+1] = left_length
        # Making sure that we remember that we're skipping the first element of the sequence
        skip_outer = True
    
    window -= 1
    if skip_outer:
        window -= 1
        skip_outer = False
    i += 1

# Now, we update the max length
max_seq = sum(partial_seq_lengths)

# Find the maximum sequence length, taking out the specified number of elements
while window >= 0:
    current = lengths[window]
    current_length = 0
    temp_left_length = 0

    # If you find a partial sequence that is already longer than max, update the max sequence length
    if window - 1 >= 0 and lengths[window - 1] > max_seq:
        max_seq = lengths[window - 1]
    
    # If the length of the current partial sequence is greater than the max sequence length, update the max sequence length
    if current > max_seq:
        max_seq = current
    
    # Go to the before-first element of this partial sequence    
    while current >= 2 and lengths[window] != 2:
        window -= 1
    
    # Length of the sequence starting from the before-first element of this partial sequence
    right_length = current - 1
    left_length = lengths[window - 2]
    
    # Checking if removing the first element of this partial sequence and adding the last element of the sequence to the left of this partial sequence will give a longer sequence
    if window - 2 >= 0 and seq[window - 2] < seq[window] and left_length + right_length > max_seq:
        current_length = left_length + right_length
        temp_left_length = left_length
        
    while lengths[window] != 1:
        window -= 1
        
    right_length = current
    left_length = lengths[window - 2]
    
    # Checking if you can remove a number between the end of one and beginning of another sequence
    if window - 2 >= 0 and seq[window - 2] < seq[window] and left_length + right_length > current_length:
        temp_left_length = left_length
        # Making sure that we remember that we're skipping the first element of the sequence
        skip_outer = True
    
    partial_seq_lengths.pop(0)
    partial_seq_lengths.append(temp_left_length)
    
    if sum(partial_seq_lengths) > max_seq:
        max_seq = sum(partial_seq_lengths)
    
    window -= 1
    if skip_outer:
        window -= 1
        skip_outer = False
    
# Now, we update the max length
print(max_seq)
