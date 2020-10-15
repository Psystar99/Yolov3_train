import glob
import cv2

'''
실행 법 
path에 None을 지우고 이미지 파일 경로를 입력
output_path에 None을 지우고 변경된 이미지 파일을 저장할 경로를 입력
주의점은 경로는 이미지 파일 이름까지 입력하지말고 이미지파일이 있는 폴더이름까지만
맨뒤에 / 붙이지 말것 EX) ./s/a/b/img 이런식으로 입력 input폴더 output폴더 모두 다!

돌리면 끝

결과물은 한사진에 대해 총 4개
시계방향 90도
시계방향 90도에대한 상하반전 좌우 반전 상하 좌우반전

'''

path = './OID/Dataset/train/Ambulance'  # 이미지 파일이 있는 경로 입력 EX. ./img
path = path + '/*.jpg'
images_list = glob.glob(path)

output_path = './OID/Dataset/train/Ambulance_90' # 회전된 이미지 파일이 저장될 경로
count = 0

for img_path in images_list:
    img = cv2.imread(img_path)

    img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  # 시계 방향 회전
    out_ = output_path + '{}_clockwise.jpg'.format(str(count))
    cv2.imwrite(out_, img_rotate_90_clockwise)

    # 시계방향 회전에 대한
    img_clockwise_ud = cv2.flip(img_rotate_90_clockwise, 0)  # 상하 반전
    out_ = output_path + '{}_clockwise_ud.jpg'.format(str(count))
    cv2.imwrite(out_, img_clockwise_ud)

    img_clockwise_lr = cv2.flip(img_rotate_90_clockwise, 1)  # 좌우반전
    out_ = output_path + '{}_clockwise_lr.jpg'.format(str(count))
    cv2.imwrite(out_, img_clockwise_lr)

    img_clockwise_ud_lr = cv2.flip(img_rotate_90_clockwise, -1)  # 상하 좌우 반전
    out_ = output_path + '{}_clockwise_ud_lr.jpg'.format(str(count))
    cv2.imwrite(out_, img_clockwise_ud_lr)
    count = count + 1
'''
    img_rotate_90_counterclockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 반시계 방향 회전=시계방향 상하좌우 반전
    out_ = output_path + '{}_counterclockwise.jpg'.format(str(count))
    cv2.imwrite(out_, img_rotate_90_counterclockwise)

    # 반시계방향 회전에 대한
    img_counterclockwise_ud = cv2.flip(img_rotate_90_counterclockwise, 0)  # 상하 반전=시계방향 좌우반전
    out_ = output_path + '{}_counterclockwise_ud.jpg'.format(str(count))
    cv2.imwrite(out_, img_counterclockwise_ud)

    img_counterclockwise_lr = cv2.flip(img_rotate_90_counterclockwise, 1)  # 좌우반전=시계방향 상하반전
    out_ = output_path + '{}_counterclockwise_lr.jpg'.format(str(count))
    cv2.imwrite(out_, img_counterclockwise_lr)

    img_counterclockwise_ud_lr = cv2.flip(img_rotate_90_counterclockwise, -1)  # 상하 좌우 반전=시계방향
    out_ = output_path + '{}_ccounterclockwise_ud_lr.jpg'.format(str(count))
    cv2.imwrite(out_, img_counterclockwise_ud_lr)
'''
   

