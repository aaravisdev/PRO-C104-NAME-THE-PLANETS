import cv2

# Read the image
img = cv2.imread("solar-system.jpg")

# Display the original image
cv2.imshow("output", img)
cv2.waitKey(0)

# Add text to the image for each planet
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
font_color = (255, 255, 255)  # White color

# Coordinates for placing text below each planet
planet_positions = {
    "Sun": (150, 500),
    "Mercury": (360, 500),
    "Venus": (530, 500),
    "Earth": (690, 500),
    "Mars": (880, 500),
    "Jupiter": (1060, 500),
    "Saturn": (1240, 500),
    "Uranus": (1430, 500),
    "Neptune": (1620, 500)
}

# Add text for each planet
for planet, position in planet_positions.items():
    cv2.putText(img, planet, position, font, font_scale, font_color, 2)

    # Display after each planet's text addition (uncomment to see each step)
    # cv2.imshow("output", img)
    # cv2.waitKey(0)

# Display the final image with planet names
cv2.imshow("output", img)
cv2.waitKey(0)

# Save the modified image with planet names
cv2.imwrite("Solar_system_with_names.jpg", img)

cv2.destroyAllWindows()
