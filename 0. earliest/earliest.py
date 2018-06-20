def get_earliest(*dates):
    """Calculates the earliest date
    """
    smallest = dates[0]
    smallest_val = (365*int(smallest.split("/")[2]) + 
        30*int(smallest.split("/")[0]) + int(smallest.split("/")[1]))

    for i in range(1, len(dates)):
        final_val = 0
        split_date = dates[i].split("/")
        final_val += 365*int(split_date[2]) # converting year to days
        final_val += 30*int(split_date[0]) # converting month to days
        final_val += int(split_date[1]) # adding days to final value

        if final_val < smallest_val:
            smallest_val = final_val
            smallest = dates[i]
            
    return smallest
