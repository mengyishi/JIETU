import cv2
#import time

CAP_DEVICE =  'D:/Code/Code/SHOUJI/JIE.mp4'   #视频地址
WIN_NAME = "JIE"  #OPENCV窗口标题

def cv2_capture_img():
    capture = cv2.VideoCapture(CAP_DEVICE)
    fps = capture.get(cv2.CAP_PROP_FPS) #获取视频的帧率
    frames_to_skip = int(0.1*fps)

    cv2.namedWindow(WIN_NAME)
    count = 3757

    success, frame = capture.read()
    while success:
        picpath1 = 'D:/Code/Code/SHOUJI/TU/'
        picpath1 = picpath1 + 'images{:}.jpg'.format(count)

        count +=1
        cv2.imwrite(picpath1, frame)
        print("已保存", picpath1)
        for _ in range(frames_to_skip - 1):
            success, frame = capture.read()
            if not success:
                break
        cv2.imshow(WIN_NAME, frame)
        key = cv2.waitKey(1)
        if key == 27:  # 按下 ESC 键关闭窗口
            break
    cv2.destroyAllWindows(WIN_NAME)
    capture.release()

if __name__ == '__main__':
    cv2_capture_img()
