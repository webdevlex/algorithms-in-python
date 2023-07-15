def draw_line(screen, width, x1, x2, y):
    # check if start is a multiple of 8
    start_offset = x1 % 8

    # get "index" position of the first full byte
    first_full_byte = x1 // 8

    # if the start bit is not at the beggining of a byte then round up to the next pixel
    if start_offset != 0:
        first_full_byte += 1

    # check if end is a multiple of 8
    end_offset = x2 % 8

    # get "index" position of the last full byte
    last_full_byte = x2 // 8

    # if the end bit is not at the end of a byte then round down to the previous pixel
    if end_offset != 7:
        last_full_byte -= 1

    # For each full bytes, Set full bytes by using their "index"
    for b in range(first_full_byte, last_full_byte + 1):
        screen[(width // 8) * y + b] = 0xFF

    # Create masks for start and end of line, this is incase the starting and ending
    # bits are in the middle of a pixel then we need to set only part of the pixel
    start_mask = 0xFF >> start_offset
    end_mask = -(0xFF >> (end_offset + 1))

    # Set start and end of line
    if (x1 // 8) == (x2 // 8):  # x1 and x2 are in the same byte
        mask = start_mask & end_mask
        screen[(width // 8) * y + (x1 // 8)] = mask
    else:
        # if starting bit is in the middle of a pixel then only set the correct pixels
        if start_offset != 0:
            byte_number = (width // 8) * y + first_full_byte - 1
            screen[byte_number] = start_mask

        # if ending bit is in the middle of a pixel then only set the correct pixels
        if end_offset != 7:
            byte_number = (width // 8) * y + last_full_byte + 1
            screen[byte_number] = end_mask
