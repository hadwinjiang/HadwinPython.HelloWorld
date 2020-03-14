import math
import reprlib


def mandel(real, imag):
    x = 0
    y = 0
    for i in range(1, 257):
        if x * x + y * y > 4.0:
            break
        xt = real + x * x - y * y
        y = imag + 2.0 * x * y
        x = xt
    return int(math.log(i) * 256 / math.log(256)) - 1


def mandelbrot(size_x, size_y):
    return [[mandel((3.5 * x / size_x) - 2.5,
                    (2.0 * y / size_y) - 1.0)
             for x in range(size_x)]
            for y in range(size_y)]


def write_grayscale(filename, pixels):
    """
    Args:
        filename: The name of the BMP file to me created
        pixels: A rectangular image stored as a sequence of rows.
        Each row must be an interable series of integers in the range 0-255
    """
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        # BMP Header
        bmp.write(b'BM')

        size_bookmark = bmp.tell()  # The next four bytes hold the filesize as a 32-bit
        bmp.write(b'\x00\x00\x00\x00')  # little-endian integer. Zero placeholder for now.

        bmp.write(b'\x00\x00')  # Unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00')  # Unused 16-bit integer - should be zero

        pixel_offset_bookmark = bmp.tell()  # The next four bytes hold the integer offset to the
        bmp.write(b'\x00\x00\x00\x00')  # pixel data. Zero placeholder for now.

        # Image Header
        bmp.write(b'\x28\x00\x00\x00')  # Image header size in bytes - 40 decimal
        bmp.write((_int32_to_bytes(width)))  # Image width in pixels
        bmp.write((_int32_to_bytes(height)))  # Image height in pixels
        bmp.write(b'\x01\x00')  # Number of image planes
        bmp.write(b'\x08\x00')  # Bits per pixel 8 for grayscale
        bmp.write(b'\x00\x00\x00\x00')  # No compression
        bmp.write(b'\x00\x00\x00\x00')  # Zero for uncompressed images
        bmp.write(b'\x00\x00\x00\x00')  # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')  # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')  # Use whole color table
        bmp.write(b'\x00\x00\x00\x00')  # All colors are important

        # Color palette - a linear grayscale
        for c in range(256):
            bmp.write(bytes((c, c, c, 0)))  # Blue, Green, Red, Zero

        # Pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):
            row_data = bytes(row)
            bmp.write(row_data)
            padding = b'\x00' * ((4 - (len(row) % 4)) % 4)  # Pad row to multiple of four bytes
            bmp.write(padding)

        # End of file
        eof_bookmark = bmp.tell()

        # Fill in file size placeholder
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))


def _int32_to_bytes(i):
    """Convert an integer to four bytes in little-endian format."""
    # &: Bitwise-and
    # >>: Right-shift
    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))


if __name__ == '__main__':
    pixels = mandelbrot(448, 256)
    reprlib.repr(pixels)

# reprlib.repr(pixels)
# demo8file.write_grayscale("mandel.bmp", pixels)
