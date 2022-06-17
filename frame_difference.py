import cv2
import os
import shutil

filename = 'video.mp4'
video = cv2.VideoCapture(filename)
i = 0
cnt = 0
save = 'frame'
if os.path.exists(save):
    shutil.rmtree(save)
os.mkdir(save)

last_frame_delta_path = 'last_delta'
if os.path.exists(last_frame_delta_path):
    shutil.rmtree(last_frame_delta_path)
os.mkdir(last_frame_delta_path)

while True:
    success, frame = video.read()
    if not success:
        print('video is all read')
        break
    # 一秒抽三帧
    if i % 5 == 0:
        frame = cv2.resize(frame, (500, 400), interpolation=cv2.INTER_CUBIC)
        if cnt == 0:
            last_frame = frame
        else:
            frame_delta = cv2.absdiff(last_frame, frame)
            last_frame = frame
        last_delta_pic_path = os.path.join(last_frame_delta_path, str(cnt) + '.jpg')
        save_path = os.path.join('frame', str(cnt) + '.jpg')
        cv2.imwrite(save_path, frame)
        if cnt > 0:
            cv2.imwrite(last_delta_pic_path, frame_delta)
        cnt += 1
        print('image of %s is saved' % (save_path))
    i += 1

other_frame_delta = 'other_frame_delta'
if os.path.exists(other_frame_delta):
    shutil.rmtree(other_frame_delta)
os.mkdir(other_frame_delta)

pic_path = os.listdir('frame')
n = len(pic_path)


for i in range(n):
    pic = cv2.imread(os.path.join('frame', pic_path[i]))
    every_pic_path = os.path.join(other_frame_delta,str(i))
    if os.path.exists(every_pic_path):
        shutil.rmtree(every_pic_path)
    os.mkdir(every_pic_path)
    for j in range(i + 1, n):
        other_pic = cv2.imread(os.path.join('frame', pic_path[j]))
        frame_delta = cv2.absdiff(pic, other_pic)
        save_dealta_path = os.path.join(every_pic_path, str(i)+'VS'+str(j) + '.jpg')
        cv2.imwrite(save_dealta_path, frame_delta)
