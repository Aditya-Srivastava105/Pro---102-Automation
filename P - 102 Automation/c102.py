import cv2
import dropbox
import time
import random
start_time = time.time()

def take_snapShot():
    number = random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0, cv2.CAP_DSHOW)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        image_name = "img"+ str(number)+ ".png"
        cv2.imwrite(image_name,frame)
        start_time = time.time
        result = False

    return image_name
    print("SnapShot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(image_name):
    access_tokken = "irZCqPjKAesAAAAAAAAAAdFyU10P6026ljOcDngasNQLGFt4C8_1MGPgEC3zyj_-"
    file = image_name
    file_from = file
    file_2 = "/CloudStorage/" + (image_name)
    dbx = dropbox.Dropbox(access_tokken)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_2, mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name = take_snapShot()
            upload_file(name)


main()