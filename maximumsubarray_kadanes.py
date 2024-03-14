def max_sum_subarray(arr):
    size = len(arr)
    curr_sum = 0
    max_so_far = arr[0]
    st = 0  
    end = 0  
    poi = 0  

    # Loop through the array
    for i in range(0, size):
        curr_sum = curr_sum + arr[i]  

        # If current sum is greater than the maximum sum so far, update max_so_far and the start and end indices
        if max_so_far < curr_sum:
            max_so_far = curr_sum
            st = poi  
            end = i  

        # If current sum becomes zero, reset curr_sum and move the pointer to the next element
        if curr_sum == 0:
            curr_sum = 0
            poi = i + 1

    # Print the maximum sum subarray and its indices
    print("Maximum sum Subarray is: ", max_so_far)
    print("Start index is: ", st)
    print("End index is: ", end)

# Example usage
arr = [4, -3, -2, 2, 3, 1, -2, -3, 6, -6, -4, 2, 1]
max_sum_subarray(arr)





    

   