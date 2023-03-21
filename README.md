# 1- pip freeze > requirements.txt

### Python projemiz için gerekli tüm modülleri içeren bir metin dosyasıdır. Python proje dizinimize gidip yeni bir .txt belge oluşturarak  başlarız.

### pip freeze sürümleriyle birlikte kurulu tüm Python modüllerinin bir listesini çıkarır.
# 2- pip install -r requirements.txt
### Bu, Python gereksinimleri dosyamızda listelenen tüm modülleri proje ortamımıza yükler.

# 3-Selenium Grid
### docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:4.8.1-20230306

### Selenium grid ise bir docker ortamında browser image üreterek container içinde çalışmasını sağlamaktadır.

### Bu image alınmış container run ettiğimizde localhost:4444 portunda firefox browser ayağa kalktığını görürüz.

### localhost:7900 portunda ise firefox bir container içinde çalıştığını görebiliriz.






