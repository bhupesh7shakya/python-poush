def my_range(start, stop, step = 1):
    print(start)
    if step > 0: # For increment
        if start < stop:
            my_range(start + step, stop, step)
        else:
            return
    else:
        if start > stop: # For decrement
            my_range(start + step, stop, step) # Since step is already a negative number we need to add to subtract
        else:
            return
    
my_range(1000, 100, -1)