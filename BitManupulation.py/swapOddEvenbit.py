def swap_all_odd_and_even_bits(n: int) -> int:
    N_big = int(n)

    # Create masks for even and odd bits
    even_mask = 0xAAAAAAAA  # Mask for even bits: 10101010...
    odd_mask = 0x55555555  # Mask for odd bits:  01010101...

    # Isolate even and odd bits using the masks
    even_bits = N_big & even_mask
    odd_bits = N_big & odd_mask

    # Shift even bits right and odd bits left
    even_bits >>= 1
    odd_bits <<= 1

    # Combine the shifted bits
    result = even_bits | odd_bits

    return result
