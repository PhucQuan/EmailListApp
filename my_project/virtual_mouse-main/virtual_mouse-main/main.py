import cv2
import time
import numpy as np
import hand_detector as hd
import pyautogui
import keyboard
import os
from datetime import datetime
import subprocess


# Tăng kích thước màn hình camera để có thể lướt tay nhiều hơn
wCam, hCam = 1280, 720  # Tăng từ 640x480 lên 1280x720
frameR = 100
smoothening = 3  # Giảm từ 7 xuống 3 để giảm delay

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

# Khởi tạo điều khiển âm thanh bằng Windows API
def get_volume():
    try:
        result = subprocess.run(['powershell', '-Command', '(Get-AudioDevice -Playback).Volume'], 
                              capture_output=True, text=True)
        return float(result.stdout.strip())
    except:
        return 50.0

def set_volume(volume_level):
    try:
        subprocess.run(['powershell', '-Command', f'(Get-AudioDevice -Playback).Volume = {volume_level}'], 
                      capture_output=True)
    except:
        pass

# Tạo thư mục lưu ảnh chụp màn hình
screenshot_dir = "screenshots"
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
# Tăng FPS để giảm delay
cap.set(cv2.CAP_PROP_FPS, 30)
detector = hd.handDetector(detectionCon=0.7)
wScr, hScr = pyautogui.size()
print(f"Screen size: {wScr}x{hScr}")
print("=== VIRTUAL MOUSE CONTROLS ===")
print("1 finger: Move mouse")
print("2 fingers: Click")
print("3 fingers: Switch tabs (Alt+Tab)")
print("4 fingers: Screenshot")
print("5 fingers: Volume control")
print("Press 'q' to quit, 'ESC' to exit")

# Hàm chụp ảnh màn hình
def take_screenshot():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{screenshot_dir}/screenshot_{timestamp}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"Screenshot saved: {filename}")
    return filename

# Hàm điều khiển âm thanh
def adjust_volume(direction):
    current_volume = get_volume()
    if direction == "up":
        new_volume = min(100.0, current_volume + 10)
    else:  # down
        new_volume = max(0.0, current_volume - 10)
    set_volume(new_volume)
    print(f"Volume: {int(new_volume)}%")

# Hàm chuyển tab
def switch_tab():
    pyautogui.hotkey('alt', 'tab')
    print("Switched tab")

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    output = img.copy()

    if len(lmList) != 0:
        # print(lmList[4], lmList[8])
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        fingers = detector.fingersUp()
        # print(fingers)
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (205, 250, 255), -1)
        img = cv2.addWeighted(img, 0.5, output, 1 - .5, 0, output)

        # Đếm số ngón tay được giơ lên
        fingers_up = sum(fingers[1:])  # Bỏ qua ngón cái (fingers[0])
        
        # 1 ngón tay: Di chuyển chuột
        if fingers_up == 1 and fingers[1] == 1:
            # Convert Coordinates với vùng hoạt động lớn hơn
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            # Smoothen Values - giảm delay
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Move Mouse - tăng tốc độ di chuyển
            pyautogui.moveTo(wScr - clocX, clocY, duration=0)  # duration=0 để di chuyển ngay lập tức
            cv2.circle(img, (x1, y1), 8, (255, 28, 0), cv2.FILLED)  # Tăng kích thước vòng tròn
            cv2.putText(img, 'Moving Mode', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
            plocX, plocY = clocX, clocY

        # 2 ngón tay: Click chuột
        elif fingers_up == 2 and fingers[1] == 1 and fingers[2] == 1:
            # Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)

            # Click mouse if distance short - giảm ngưỡng để dễ click hơn
            if length < 50:  # Tăng từ 40 lên 50
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 8, (0, 255, 0), cv2.FILLED)
                cv2.putText(img, 'Click!!', (20, 80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                pyautogui.click()
            else:
                cv2.putText(img, 'Ready to Click', (20, 80), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)

        # 3 ngón tay: Chuyển tab
        elif fingers_up == 3:
            switch_tab()
            cv2.putText(img, 'Switching Tab', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)
            time.sleep(0.5)  # Tránh spam

        # 4 ngón tay: Chụp ảnh màn hình
        elif fingers_up == 4:
            take_screenshot()
            cv2.putText(img, 'Screenshot Taken!', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
            time.sleep(0.5)  # Tránh spam

        # 5 ngón tay: Điều khiển âm thanh
        elif fingers_up == 5:
            # Lấy vị trí ngón tay giữa để xác định hướng
            if len(lmList) >= 12:
                middle_finger_x = lmList[12][1]
                center_x = wCam // 2
                
                if middle_finger_x < center_x:
                    adjust_volume("down")
                    cv2.putText(img, 'Volume Down', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 100, 100), 2)
                else:
                    adjust_volume("up")
                    cv2.putText(img, 'Volume Up', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (100, 255, 100), 2)
            time.sleep(0.3)  # Tránh spam

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Hiển thị FPS trên màn hình
    cv2.putText(img, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    
    # Hiển thị hướng dẫn sử dụng
    cv2.putText(img, "1 finger: Move | 2: Click | 3: Switch Tab", (10, hCam - 60), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
    cv2.putText(img, "4: Screenshot | 5: Volume | 'q': Quit", (10, hCam - 40), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
    cv2.putText(img, "Press 'q' to quit", (10, hCam - 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

    cv2.imshow("Virtual Mouse Monitor", cv2.flip(img, 1))
    cv2.setWindowProperty("Virtual Mouse Monitor", cv2.WND_PROP_TOPMOST, 1)
    
    # Thêm cách thoát bằng phím 'q' hoặc ESC
    key = cv2.waitKey   (1) & 0xFF
    if key == ord('q') or key == 27:  # 'q' hoặc ESC
        print("Exiting...")
        break

# Giải phóng camera và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()
print("Program ended successfully!")
