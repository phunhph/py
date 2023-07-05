import cv2

# Mở camera
cam = cv2.VideoCapture(0)

# Xét chiều dài chiều rộng
cam.set(3, 640)
cam.set(4, 480)

# Load file phát hiện khuôn mặt
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = input('Nhập ID: ')
print('\nKhởi tạo camera....')

# Biến khởi tạo để đếm khuôn mặt
count = 0

while True:
    ret, img = cam.read()

    # Chuyển thành ảnh đen trắng
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Chọn vùng mặt
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Bắt khuôn mặt từ cam
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Tăng số count
        count += 1

        # Lưu ảnh
        cv2.imwrite(f"dataset/User.{str(face_id)}.{str(count)}.jpg", gray[y:y+h, x:x+w])

    # Hiển thị hình ảnh
    cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27 or count >= 30:
        break

print("\nHoàn thành.")

# Tắt camera
cam.release()

# Đóng tất cả cửa sổ
cv2.destroyAllWindows()
