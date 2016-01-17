# Import the modulo python library
import modulo
import colorutils

# This callback function will run whenever the knob position changes
def onPositionChanged(knob) :
    # Get the angle of the knob (between 0 and 360)
    angle = knob.getAngle()

    # Divide the angle by 360 to get the hue, which is between 0 and 1
    hue = angle/360.0

    # When the knob is pressed, set the saturation to 0.
    saturation = 1-knob.getButton()

    # Set the color. The value is always 1.0 (full brightness)
    knob.setHSV(hue, saturation, 1.0)

    # First, clear the display
    display.clear()

    # Draw text showing the rgb and hue values, and write them in
    # the same color as the knob.
    (r, g, b) = colorutils.HSVtoRGB(hue, saturation, 1.0)
    display.setTextColor(r, g, b)
    print >>display, "hue = %0.2g" % hue
    print >>display, "rgb [%0.2g, %0.2g, %0.2g]" % (r, g, b)

    # Draw a circle in the same color, and place it horizontally based on the knob position.
    display.setLineColor(r, g, b)
    display.setFillColor(r, g, b)
    display.drawCircle(10 + hue*60, 40, 10)

    # Call refresh to update the display
    display.refresh()


# Create a new Port object using the first Modulo Controller it finds.
port = modulo.Port()

# Create a Knob object attached to the port
knob = modulo.Knob(port)

# Create a Display object attached to the port
display = modulo.Display(port)

# Register our callback function
knob.positionChangeCallback = onPositionChanged

# Process events until the program is terminated.
port.runForever()

