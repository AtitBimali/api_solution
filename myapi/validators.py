
from django.core.exceptions import ValidationError
import os
#from moviepy.editor import VideoFileClip- was trying to get the video length


def validate_file_size(value):
    global filesize
    filesize= value.size
    
    if filesize > 1073741824:
        raise ValidationError("Files larger than 1 GB are not Supported. Please select a file under 1 GB")

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # returns path+filename
    valid_extensions = ['.mkv','.mp4']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported video file extension.')

def validate_payment(amount):
    global filesize,video_length
    payment = amount
    if filesize<524288000 and payment!=17.5 and video_length<3618:
        raise ValidationError("You need to pay 5$ to upload video below 500MB in size and additional 12.5$ for video of length below 6 minutes 18 second")
    if filesize>=524288000 and payment!=25 and video_length<3618:
        raise ValidationError("You need to pay 12.5$ to upload video above 500MB in size and additional 12.5$ for video of length below 6 minutes 18 second")
    if filesize>=524288000 and payment!=32.5 and video_length>=3618:
        raise ValidationError("You need to pay 12.5$ to upload video above 500MB in size and additional 20$ for video of length above 6 minutes 18 second")
    if filesize<524288000 and payment!=25 and video_length>=3618:
        raise ValidationError("You need to pay 5$ to upload video below 500MB in size and additional 20$ for video of length above 6 minutes 18 second")
    else:
        return video_length
    
def validate_length(length):
    global video_length
    video_length = length
    