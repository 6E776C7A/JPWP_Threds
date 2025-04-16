def volume_to_color(volume_percent):
    if volume_percent < 50:
        r = int(255 * (volume_percent / 50))
        g = 255
    else:
        r = 255
        g = int(255 * (1 - (volume_percent - 50) / 50))
    return f'#{r:02x}{g:02x}00'