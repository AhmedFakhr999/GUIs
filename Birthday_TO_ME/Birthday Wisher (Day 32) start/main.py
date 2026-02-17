import smtplib 
import pandas as pd 
import datetime as dt
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import requests
import os




def get_random_photo():
    response = requests.get("https://picsum.photos/800/600")
    if response.status_code == 200:
        file_name = "birthday_photo.png"
        with open(file_name, "wb") as f:
            f.write(response.content)
        return file_name


my_email = os.environ.get("MY_EMAIL") 
password = os.environ.get("MY_PASSWORD")

today=dt.datetime.now()

today_tuple=(today.month,today.day)


data=pd.read_csv("birthday_data.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = "letter.txt"
    with open(file_path, encoding="utf-8") as file: 
        content = file.read() 
        
    # Create a multipart message to support attachments
    msg = MIMEMultipart()
    msg["Subject"] = "Happy Birthday!"
    msg["From"] = my_email
    msg["To"] = birthday_person["email"]

    # Attach the text content
    msg.attach(MIMEText(content, "plain", "utf-8"))

    # Get a random photo and attach it
    photo_path = get_random_photo()
    if photo_path:
        with open(photo_path, 'rb') as f:
            img_data = f.read()
            image = MIMEImage(img_data, name=os.path.basename(photo_path))
            msg.attach(image)

    with smtplib.SMTP("smtp.gmail.com") as connections: 
        connections.starttls() 
        connections.login(user=my_email, password=password)
        connections.send_message(msg)





# connection=smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,to_addrs="agad9808@gmail.com",msg="Subject:Talking to your girl \nTest Test 7awhl")
# connection.close()



# quotes_file="quotes.txt"
# with open(quotes_file) as file : 
#     quotes_list=file.readlines()
#     print(quotes_list)


# import requests
# import os 


# folder_name="photos"






# def get_random_photo():
#     response = requests.get("https://picsum.photos/800/600")
#     if response.status_code == 200:
#         with open("birthday_photo.png", "wb") as f:
#             os.path.join(folder_name,"birthday_photo.png")
#         return "birthday_photo.png"


# get_random_photo() 
