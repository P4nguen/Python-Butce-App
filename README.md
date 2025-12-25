# 💰 Finansal Asistanım

Python ve Flask kullanılarak geliştirilmiş, kullanıcı dostu bir kişisel gelir-gider takip uygulaması. Harcamalarınızı kategorilere ayırabilir, grafiklerle analiz edebilir ve bütçenizi kontrol altında tutabilirsiniz.

## 🚀 Özellikler

* **Gelir/Gider Ekleme:** Tarih, kategori ve açıklama ile işlem kaydı.
* **Görsel Analiz:** Pasta ve çubuk grafiklerle (Pie & Bar Charts) harcama dağılımı.
* **Filtreleme:** Tarihe veya türe göre işlemleri süzme.
* **Veri Saklama:** JSON tabanlı hafif veri tabanı (Kurulum gerektirmez).
* **Modern Arayüz:** Tailwind CSS ile şık ve responsive tasarım.

## 🛠 Kurulum ve Çalıştırma

Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin.

### Gereksinimler
Bilgisayarınızda **Python**'un yüklü olması gerekir.

### 1. Projeyi Bilgisayarınıza İndirin
Terminali açın ve projeyi klonlayın (veya ZIP olarak indirip çıkarın):

```bash
git clone [https://github.com/KULLANICI_ADIN/python-butce-app.git](https://github.com/KULLANICI_ADIN/python-butce-app.git)
cd python-butce-app
```

### 2. Gerekli Kütüphaneyi Yükleyin
Proje Flask kütüphanesini kullanır. Terminalde şu komutu çalıştırın:

```bash
pip install flask
```

### 3. Uygulamayı Çalıştırın
Kurulum tamamlandıktan sonra uygulamayı başlatmak için:

```bash
python app.py
```

Terminalde şuna benzer bir çıktı göreceksiniz:

Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 4. Tarayıcıda Açın
Tarayıcınızın adres çubuğuna şu adresi yazın: http://127.0.0.1:5000

📂 Proje Yapısı
app.py: Ana Python uygulaması ve backend kodları.

templates/index.html: Frontend tasarımı ve JavaScript kodları.

transactions.json: Verilerin kaydedildiği dosya (Otomatik oluşur).

İyi günlerde kullanın! 🐍

























