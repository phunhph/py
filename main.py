'cv.imread(path,flag) thể đọc ảnh path: đường dẫn ảnh flag: xác định loại ảnh dùng 1 cho ảnh màu 0 cho ảnh đen trắng, -1 ảnh có kênh'
'imshow() hiển thị ảnh cv2.imshow(window_name.ímage) (cua so hien thị, tên ảnh)'
import cv2
import os

path = r'C:\Users\Huu Phu\OneDrive - Đại học FPT- FPT University\Desktop\anh.jpg'
path1 = r'C:\Users\Huu Phu\OneDrive - Đại học FPT- FPT University\Desktop'
'img = cv2.imread(path)'
'cv2.imshow('',img)'
'lưu ảnh cv2.imwrite(filename,image)'
'lưu ở file khác'
'os.chdir(path1)'
filenam='anhmoi.png'
'cv2.imwrite(filenam,img)'

'dừng hình'
'cv2.waitKey()'
'kết nối camera'
'cv.VideoCapture'
'mở camera'
cap = cv2.VideoCapture(0)
'nhân ảnh liên túc tạo thành video cho đến khi nhấn q'
while True:
    _, image = cap.read()
    cv2.imshow('video',image)
    if cv2.waitKey(1) == ord('q'):
        break


'đọc frame'
'cv.videocapture.read'


