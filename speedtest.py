import speedtest

st = speedtest.Speedtest()

download_speed = st.download()
print(download_speed / (2 ** 20))

upload_speed = st.upload()
print(upload_speed / (2 ** 20))
