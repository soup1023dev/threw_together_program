from PIL import Image
import numpy as np
# dot positions (bit order):
# 1 4
# 2 5
# 3 6
# 7 8
DOTS = [(0, 0, 1 << 0), (1, 0, 1 << 1), (2, 0, 1 << 2),(0, 1, 1 << 3), (1, 1, 1 << 4), (2, 1, 1 << 5),(0, 2, 1 << 6), (1, 2, 1 << 7)]
def video_to_braille(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        img = img.convert("L")
        braille_art = image_to_braille(img)
        print(braille_art)
        cv2.waitKey(33)  # 30fps

    cap.release()


def image_to_braille(path, target_width=200, target_height=200, threshold=128):
    img = Image.open(path).convert("L")
    img = img.resize((target_width, target_height))
    w, h = img.size
    w2 = w - (w % 2)
    h2 = h - (h % 4)
    print("size(w/h) = " + str(w2) + ", " + str(h2))
    img = img.crop((0, 0, w2, h2))
    pixels = np.array(img)
    output_lines = []
    for y in range(0, h2, 4):
        line = ""
        for x in range(0, w2, 2):
            dots = 0
            for dy, dx, bit in DOTS:
                if y + dy < h2 and x + dx < w2:
                    if pixels[y + dy, x + dx] < threshold:
                        dots |= bit
            char = chr(0x2800 + dots)
            line += char
        output_lines.append(line)
    return "\n".join(output_lines)

photo=""
ascii_braille = image_to_braille(photo, 400, 628)
print(Image.open(photo).convert("L").size)
print(ascii_braille)
