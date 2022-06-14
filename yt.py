from pytube import YouTube
link = input("Enter Youtube Video Link : ")
yt = YouTube(link)
videos = yt.streams.all()
video = list(enumerate(videos))
for i in video:
    print(i)

print("enter the desired format \n 1)144 \n 2)240 \n 3)360 \n 4)720 \n 5)1080 \n 6)1440 \n 7)2160")
dn_option = int(input("enter the qulity number from above : "))
dn_video = videos[dn_option]
dn_video.download()
print("download successfully")