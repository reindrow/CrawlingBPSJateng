import streamlit as st
import snscrape.modules.twitter as sntwitter
import pandas as pd
from PIL import Image
from googleapiclient.discovery import build

st.markdown("""<hr style="height:1px;border:none;color:#333;background-color:#333;"/>""",unsafe_allow_html=True)

option = st.sidebar.selectbox(
    "Menu📋",
    ("Halaman Utama🏠", "Crawling Twitter🟦","Crawling YouTube🟥", "Profil BPS Jateng👤")
)

if option == 'Halaman Utama🏠' or option == '':
    image = Image.open('LogoBPSFix.png')
    st.image(image)
    image = Image.open('bps jateng 2.jpg')
    st.image(image)

elif option == 'Crawling Twitter🟦':
    image = Image.open('LogoBPSFix.png')
    st.image(image)
    st.write("""# Crawling Data Twitter""")
    crawling=st.text_input("Masukan nama atau judul data yang ingin dicrawling")
    number = st.text_input ('Jumlah data yang ingin dicrawling')
    namatwt=st.text_input("Download dengan nama file: ") 
    hasil=st.button("Cari🔍")
    
    if hasil:
        maxTweets = int(number)
        tweets = []
        tdf = None
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(crawling).get_items()) :
            if i >  maxTweets :
                break
            username = tweet.username
            text = tweet.content
            pubdate = tweet.date
            permalink = tweet.url
            tweets.append({
                "permalink":permalink,
                "pubdate":pubdate,
                "text":text,
                "username":username
            })
        
    
        df = pd.DataFrame (tweets, columns = ['permalink', 'pubdate', 'username', 'text'])
        print(df)
        st.success("Berhasil. Silahkan download file anda di bawah⬇️")
        st.download_button("Download📥", df.to_csv(),file_name= namatwt+'.csv',mime = 'text/csv')

elif option=='Crawling YouTube🟥':
    image = Image.open('LogoBPSFix.png')
    st.image(image)
    st.write("""# Crawling Komentar YouTube""")
    video_id=st.text_input("Masukan ID link YouTube: ") #5tucmKjOGi8
    st.info('Link vidio : https://www.youtube.com/watch?v=dQw4w9WgXcQ. ID link :blue[dQw4w9WgXcQ] ', icon="💡")
    namayt=st.text_input("Download dengan nama file: ") 
    hasil=st.button("Cari🔍")

    if hasil:
	    def video_comments(video_id):
		    replies = []
		    youtube = build('youtube', 'v3', developerKey=api_key)
		    video_response = youtube.commentThreads().list(part='snippet,replies', videoId=video_id).execute()
		    while video_response:

			    for item in video_response['items']:
				    published = item['snippet']['topLevelComment']['snippet']['publishedAt']
				    user = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
				    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
				    likeCount = item['snippet']['topLevelComment']['snippet']['likeCount']
				    replies.append([published, user, comment, likeCount])
				    replycount = item['snippet']['totalReplyCount']

			    if replycount>0:
				    for reply in item['replies']['comments']:
					    published = reply['snippet']['publishedAt']
					    user = reply['snippet']['authorDisplayName']
					    repl = reply['snippet']['textDisplay']
					    likeCount = reply['snippet']['likeCount']
					    replies.append([published, user, repl, likeCount])

			    if 'nextPageToken' in video_response:
				    video_response = youtube.commentThreads().list(
					    part = 'snippet,replies',
					    pageToken = video_response['nextPageToken'], 
					    videoId = video_id
				    ).execute()
			    else:
				    break 
			    return replies

	    api_key = 'AIzaSyB51tfXdVREoLBoIRIGNBv-ygxiTrUjSWU'
	    comments = video_comments (video_id)
	    print(comments)
	
	    df = pd.DataFrame (comments, columns=['publishedAt', 'authorDisplayName', 'textDisplay', 'likeCount'])
	    print(df)
	    st.success("Berhasil. Silahkan download file anda di bawah⬇️") 
	    st.download_button("Download📥", df.to_csv(),file_name= namayt+'.csv',mime = 'text/csv')

elif option == 'Profil BPS Jateng👤':
    image = Image.open('LogoBPSFix.png')
    st.image(image)
    st.write("""# Profil BPS Jawa Tengah""")  
    st.subheader(':blue[Informasi Umum] :book:')
    st.write ('''Badan Pusat Statistik adalah Lembaga Pemerintah Non-Kementrian yang bertanggung jawab langsung kepada Presiden. Sebelumnya, BPS merupakan Biro Pusat Statistik, yang dibentuk berdasarkan UU Nomor 6 Tahun 1960 tentang Sensus dan UU Nomer 7 Tahun 1960 tentang Statistik. Sebagai pengganti kedua UU tersebut ditetapkan UU Nomor 16 Tahun 1997 tentang Statistik. Berdasarkan UU ini yang ditindaklanjuti dengan peraturan perundangan dibawahnya, secara formal nama Biro Pusat Statistik diganti menjadi Badan Pusat Statistik.''')

    st.subheader(':blue[Visi dan Misi] :book:')
    st.write ('''Dengan mempertimbangkan capaian kinerja, memperhatikan aspirasi masyarakat, potensi dan permasalahan, serta mewujudkan Visi Presiden dan Wakil Presiden maka visi Badan Pusat Statistik untuk tahun 2020-2024 adalah:

“Penyedia Data Statistik Berkualitas untuk Indonesia Maju”

(“Provider of Qualified Statistical Data for Advanced Indonesia”)

Dalam visi yang baru tersebut berarti bahwa BPS berperan dalam penyediaan data statistik nasional maupun internasional, untuk menghasilkan statistik yang mempunyai kebenaran akurat dan menggambarkan keadaan yang sebenarnya, dalam rangka mendukung Indonesia Maju.
Dengan visi baru ini, eksistensi BPS sebagai penyedia data dan informasi statistik menjadi semakin penting, karena memegang peran dan pengaruh sentral dalam penyediaan statistik berkualitas tidak hanya di Indonesia, melainkan juga di tingkat dunia. Dengan visi tersebut juga, semakin menguatkan peran BPS sebagai pembina data statistik.

Misi BPS dirumuskan dengan memperhatikan fungsi dan kewenangan BPS, visi BPS serta melaksanakan Misi Presiden dan Wakil Presiden yang Ke-1 (Peningkatan Kualitas Manusia Indonesia), Ke-2 (Struktur Ekonomi yang Produktif, Mandiri, dan Berdaya Saing) dan yang Ke-3 Pembangunan yang Merata dan Berkeadilan, dengan uraian sebagai berikut:
1. Menyediakan statistik berkualitas yang berstandar nasional dan internasional
2. Membina K/L/D/I melalui Sistem Statistik Nasional yang berkesinambungan
3. Mewujudkan pelayanan prima di bidang statistik untuk terwujudnya Sistem Statistik Nasional
4. Membangun SDM yang unggul dan adaptif berlandaskan nilai profesionalisme, integritas dan amanah''')
