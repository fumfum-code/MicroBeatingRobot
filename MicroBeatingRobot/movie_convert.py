import glob
import cv2

img_array = []
for filename in sorted(glob.glob("result/*.png")):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

clip_fps = 20.0
name = 'result/result_numparticle_4_pi_2.mp4'
out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'MP4V'),clip_fps, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
