import cv2

print("Type your file name (example: file.jpeg)")
input_path = input()
while ".jpeg" not in input_path:
    print("Input file format must be .jpeg")
    print("ENTER NEW INPUT FILE NAME")
    input_path = input()

img = cv2.imread(input_path)
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayImgHeight, grayImgWidth = grayImg.shape

print("Type your output file name (example: file.txt)")
output_path = input()

while ".txt" not in output_path:
    print("Output file format must be .txt")
    print("ENTER NEW OUTPUT FILE NAME")
    output_path = input()

f = open(output_path, "w")

intensity = '@%#*+=-:. '


def calculate_intensity(x):
    f.write(intensity[int((x * (len(intensity)-1)) / 255)])


for i in range(grayImgHeight):
    f.write("\n")
    for k in range(grayImgWidth):
        calculate_intensity(grayImg[i][k])

print("Check your {} file".format(output_path))
