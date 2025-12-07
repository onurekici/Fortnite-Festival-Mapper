# 🎸 Festival Mapper - Ultimate Edition

**The Universal Guitar Controller Solution for PC Rhythm Games**

**Festival Mapper** allows you to connect **ANY** USB Guitar Controller (PS3/PS4 dongles, Wii adapters, Xbox X-plorers, generic joysticks) to your PC and use it seamlessly in games like **Fortnite Festival**, **Clone Hero**, or YARG. It translates your guitar inputs into either a virtual Xbox 360 controller or keyboard presses.

---

### 🌍 Select Language / Dil Seçimi
[🇺🇸 **English Instructions**](#-english-instructions) | [🇹🇷 **Türkçe Kullanım Kılavuzu**](#-türkçe-kullanım-kılavuzu)

---

<a name="-english-instructions"></a>
## 🇺🇸 English Instructions

### 🔥 Key Features

* **Universal Compatibility:** Works with virtually any guitar controller recognized by Windows as a USB device.
* **Dual Output Modes:**
    * 🎮 **Xbox Controller Mode:** Creates a virtual Xbox 360 controller, perfect for plug-and-play support in **Fortnite Festival**.
    * ⌨️ **Keyboard Mode:** Maps buttons to specific keys, ideal for **Clone Hero**.
* **Pro Streamer Overlay:** A dedicated, transparent window for streamers. Features a clean rectangular layout, real-time hit counters inside the keys, and separate indicators for Strum Up/Down.
* **Smart Profile System:** Create unlimited profiles for different games. Easily add (`+`) or delete (`-`) profiles from the UI. Your last used profile and settings auto-save.
* **Tilt Support (Star Power):** Map the guitar's tilt axis to activate "Overdrive" or "Star Power" by lifting the guitar neck.
* **Multi-Language UI:** Supports English, Turkish, Spanish, Portuguese, Russian, and German.

### 🛠️ Prerequisites

Before running the tool, ensure you have the following installed:

1.  **Python 3.x:** Python must be installed on your system. [Download Python here](https://www.python.org/downloads/).
    * *IMPORTANT: During installation, check the box **"Add Python to PATH"**.*
2.  **ViGEmBus Driver (Crucial for Xbox Mode):** This driver is required to create the virtual Xbox controller. Without it, Xbox Mode will fail.
    * [Download and Install ViGEmBus Driver](https://github.com/ViGEm/ViGEmBus/releases/latest)

### 📥 Installation & Running

1.  **Download the Repository:** Click the green **"Code"** button above and select **"Download ZIP"**. Extract the files to a folder.
2.  **Install Dependencies:**
    * Open a command prompt (terminal) inside the extracted folder.
    * Run the following command to install required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Tool:**
    * Double-click the `.pyw` script file (e.g., `Festival_Mapper.pyw`) to start the application.

### 🎮 Quick Usage Guide

1.  **Connect:** Plug in your USB guitar. In the app, click **"Refresh"**, select your device from the dropdown list, and click **"Connect"**.
2.  **Select Mode:** Choose **"Xbox Controller"** for Fortnite or **"Keyboard"** for Clone Hero.
3.  **Map Controls:**
    * Click a colored button in the app (e.g., **GREEN**).
    * Press the corresponding physical button on your guitar. The button will turn green to confirm.
    * Repeat for frets, strum bar, whammy, select, and start.
4.  **Tilt (Optional):** Check "Tilt Active", click "Bind Tilt Axis", and lift your guitar neck sharply to bind it.
5.  **Play:** Click the big green **"START"** button. Keep the app running in the background while playing.

---

### ❤️ Support
If you find this tool useful, please consider giving the repository a ⭐ **Star**!

---
---

<a name="-türkçe-kullanım-kılavuzu"></a>
## 🇹🇷 Türkçe Kullanım Kılavuzu

**PC Ritim Oyunları İçin Evrensel Gitar Kontrolcü Çözümü**

**Festival Mapper**, **HERHANGİ BİR** USB Gitar Kontrolcüsünü (PS3/PS4 alıcıları, Wii adaptörleri, Xbox X-plorer, standart joystickler) bilgisayarınıza bağlamanızı ve **Fortnite Festival**, **Clone Hero** veya YARG gibi oyunlarda sorunsuz kullanmanızı sağlar. Gitar girişlerinizi sanal bir Xbox 360 koluna veya klavye tuşlarına dönüştürür.

### 🔥 Temel Özellikler

* **Evrensel Uyumluluk:** Windows tarafından USB aygıtı olarak tanınan neredeyse tüm gitar kontrolcüleriyle çalışır.
* **İki Farklı Çıkış Modu:**
    * 🎮 **Xbox Kontrolcü Modu:** Sanal bir Xbox 360 kolu oluşturur, **Fortnite Festival**'de tak-çalıştır desteği için mükemmeldir.
    * ⌨️ **Klavye Modu:** Butonları klavye tuşlarına atar, **Clone Hero** için idealdir.
* **Profesyonel Yayıncı Katmanı (Overlay):** Yayıncılar için özel, şeffaf pencere. Temiz dikdörtgen tasarım, tuşların içinde anlık vuruş sayaçları ve ayrı Strum Aşağı/Yukarı göstergeleri içerir.
* **Akıllı Profil Sistemi:** Farklı oyunlar için sınırsız profil oluşturun. Arayüzden kolayca profil ekleyin (`+`) veya silin (`-`). Son kullandığınız ayarlar otomatik kaydedilir.
* **Tilt Desteği (Star Power):** Gitarı havaya kaldırarak "Overdrive" veya "Star Power" açmak için gitarın eğim eksenini atayabilirsiniz.
* **Çoklu Dil Arayüzü:** Türkçe, İngilizce, İspanyolca, Portekizce, Rusça ve Almanca desteği.

### 🛠️ Gereksinimler

Aracı çalıştırmadan önce aşağıdakilerin yüklü olduğundan emin olun:

1.  **Python 3.x:** Sisteminizde Python yüklü olmalıdır. [Python'u buradan indirin](https://www.python.org/downloads/).
    * *ÖNEMLİ: Kurulum sırasında **"Add Python to PATH"** kutucuğunu işaretlemeyi unutmayın.*
2.  **ViGEmBus Sürücüsü (Xbox Modu İçin Kritik):** Bu sürücü, sanal Xbox kolunu oluşturmak için gereklidir. O olmadan Xbox Modu çalışmaz.
    * [ViGEmBus Sürücüsünü İndir ve Kur](https://github.com/ViGEm/ViGEmBus/releases/latest)

### 📥 Kurulum ve Çalıştırma

1.  **Depoyu İndirin:** Yukarıdaki yeşil **"Code"** butonuna tıklayın ve **"Download ZIP"** seçeneğini seçin. Dosyaları bir klasöre çıkarın.
2.  **Kütüphaneleri Yükleyin:**
    * Çıkardığınız klasörün içinde bir komut istemi (terminal) açın.
    * Gerekli Python kütüphanelerini yüklemek için şu komutu çalıştırın:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Aracı Çalıştırın:**
    * Uygulamayı başlatmak için `.pyw` uzantılı script dosyasına (örneğin, `Festival_Mapper.pyw`) çift tıklayın.

### 🎮 Hızlı Kullanım Kılavuzu

1.  **Bağlan:** USB gitarınızı takın. Uygulamada **"Yenile"** butonuna tıklayın, listeden cihazınızı seçin ve **"Bağlan"**a tıklayın.
2.  **Mod Seçin:** Fortnite için **"Xbox Controller"**, Clone Hero için **"Klavye"** modunu seçin.
3.  **Tuşları Atayın:**
    * Uygulamadaki renkli bir butona tıklayın (örneğin, **YEŞİL**).
    * Gitarınızdaki karşılık gelen fiziksel tuşa basın. Buton onay için yeşil renge dönecektir.
    * Tüm perdeler (frets), strum çubuğu, whammy, select ve start için bunu tekrarlayın.
4.  **Tilt (Opsiyonel):** "Tilt Aktif"i işaretleyin, "Tilt Eksenini Tanıt"a tıklayın ve gitar sapını havaya kaldırın.
5.  **Oyna:** Büyük yeşil **"BAŞLAT"** butonuna tıklayın. Oynarken uygulamayı arka planda açık tutun.

---

### ❤️ Destek
Bu aracı faydalı bulduysanız, lütfen depoya bir ⭐ **Yıldız** vermeyi düşünün!
