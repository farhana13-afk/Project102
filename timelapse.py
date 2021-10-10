import cv2
import time 
import random
import dropbox
from dropbox.files import WriteMode

start_time = time.time()

# take the photos 
def takeSnapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.videoCapture(0)
    result = True

    while(result):
        ret, frame = VideoCaptureObject.read()

        img_name = "img" + str(number)+".png"
        cv2.imwrite(img_name, frame)

        start_time = time.time()
        result = False
    return img_name
    print("snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

#upload files
def upload_file(img_name):
    access_token="sl.A5qqEmy1PiepnG6ZVEzcCfBXGZN4hPgsxAbaPp1maatrV48KeuBB77wd7x8-rJNWmpUlnFuvukRtZjZ5CkGJlWlo6POuROQiheOQjyOPfzDBxFie4jCMcYQ9Em5lXz-JcuZ0R1Q"
    file=img_name
    file_from=file
    file_to="/NewFolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overWrite)
        print("File uploaded")

def main():
    while(True):
        if((time.time()- start_time) >=100):
            name = takeSnapshot()
            upload_file(name)

main()