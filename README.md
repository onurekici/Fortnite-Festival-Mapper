# 🎸 Festival Mapper V8 (Ultimate)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)]()

**Festival Mapper V8**, allows you to use **any USB Guitar Controller** with **Fortnite Festival**, **Clone Hero**, or any rhythm game. It converts your guitar inputs into virtual Xbox 360 controller signals (XInput) or Keyboard presses.

---

### 🌍 Language / Dil
[🇺🇸 **English**](#-english-instructions) | [🇹🇷 **Türkçe**](#-türkçe-kullanım-kılavuzu)

---

<a name="-english-instructions"></a>
## 🇺🇸 English Instructions

### ✨ Features
* **Universal Support:** Works with any joystick/guitar recognized by Windows.
* **Dual Modes:**
    * 🎮 **Xbox Mode:** Emulates an Xbox 360 controller (Perfect for **Fortnite Festival**).
    * ⌨️ **Keyboard Mode:** Maps buttons to keys (Perfect for **Clone Hero**).
* **Tilt Support:** Activate "Overdrive" or "Star Power" by lifting your guitar neck!
* **Streamer Overlay:** A dedicated window showing your inputs and hit counts in real-time (OBS compatible).
* **Profile System:** Save/Load different configs for different games.
* **Multi-Language UI:** English, Turkish, Spanish, Portuguese, Russian, German.

### 🚀 Installation

1.  **Install Python:** Make sure Python 3.x is installed.
2.  **Install ViGEmBus Driver (Crucial):**
    * This software requires the **ViGEmBus** driver to create the virtual Xbox controller.
    * [Download ViGEmBus Setup here](https://github.com/ViGEm/ViGEmBus/releases/latest) and install it.
3.  **Install Dependencies:**
    Open terminal in the project folder and run:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the App:**
    ```bash
    python Festival_Mapper_Final_V9.pyw
    ```

### 🎮 How to Use
1.  **Connect Guitar:** Plug in your guitar. Click **"Refresh"** and select it from the list. Click **"Connect"**.
2.  **Select Mode:** Choose **Xbox Controller** for Fortnite.
3.  **Map Buttons:**
    * Click a colored button on the screen (e.g., GREEN).
    * Press the corresponding button on your guitar.
    * Repeat for all frets, strum bar, and whammy.
4.  **Tilt (Optional):** Check "Tilt Active", click "Bind Tilt Axis", and lift your guitar neck up.
5.  **Start:** Click the big **"START"** button. The app will minimize to tray or run in background.
6.  **Fortnite:** Open the game. It will recognize your guitar as an Xbox Controller immediately.

---

<a name="-türkçe-kullanım-kılavuzu"></a>
## 🇹🇷 Türkçe Kullanım Kılavuzu

### ✨ Özellikler
* **Geniş Destek:** Windows'un tanıdığı tüm USB gitarlar ve joystickler ile çalışır.
* **İki Farklı Mod:**
    * 🎮 **Xbox Modu:** Sanal bir Xbox 360 kolu oluşturur (**Fortnite Festival** için gereklidir).
    * ⌨️ **Klavye Modu:** Tuşları klavye harflerine atar (**Clone Hero** için idealdir).
* **Tilt (Dikme) Desteği:** Gitarı havaya kaldırdığınızda "Overdrive" özelliğini tetikler.
* **Yayıncı Modu (Overlay):** Ekranda tuş vuruşlarını ve sayacını gösteren, OBS'e eklenebilir şeffaf pencere.
* **Profil Sistemi:** Farklı oyunlar için ayarlarınızı kaydedin.
* **Çoklu Dil:** Türkçe dahil 6 farklı dil desteği.

### 🚀 Kurulum

1.  **Python Kurun:** Bilgisayarınızda Python 3.x yüklü olmalıdır.
2.  **ViGEmBus Sürücüsünü Yükleyin (Çok Önemli):**
    * Programın Xbox kolu taklidi yapabilmesi için bu sürücü şarttır.
    * [ViGEmBus İndir](https://github.com/ViGEm/ViGEmBus/releases/latest) linkinden indirip kurun.
3.  **Kütüphaneleri Yükleyin:**
    Proje klasöründe terminali açın ve şu komutu yazın:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Çalıştırın:**
    ```bash
    python Festival_Mapper_Final_V9.pyw
    ```

### 🎮 Nasıl Kullanılır?
1.  **Gitarı Bağlayın:** USB gitarınızı takın. Programdan **"Yenile"** diyip listeden seçin ve **"Bağlan"** butonuna basın.
2.  **Mod Seçin:** Fortnite oynayacaksanız **Xbox Controller** seçeneğini işaretleyin.
3.  **Tuşları Atayın:**
    * Ekrandaki renkli kutuya (örneğin YEŞİL) tıklayın.
    * Gitarınızdaki yeşil tuşa basın.
    * Bunu tüm tuşlar, strum (vuruş) çubuğu ve whammy için yapın.
4.  **Tilt (Dikme):** "Tilt Aktif" kutusunu işaretleyin, "Tilt Eksenini Tanıt"a basın ve gitarı havaya kaldırın.
5.  **Başlat:** Büyük yeşil **"BAŞLAT"** butonuna basın.
6.  **Oyuna Girin:** Fortnite'ı açın. Oyun gitarınızı otomatik olarak bir Xbox kolu gibi görecektir.

---

### ⚠️ Troubleshooting / Sorun Giderme

* **Error: ViGEmBus driver missing!**
    * You forgot to install the ViGEmBus driver. Please download and install it from the link above.
    * *ViGEmBus sürücüsünü kurmayı unuttunuz. Lütfen yukarıdaki linkten indirip kurun.*

* **App crashes on start / Program açılınca kapanıyor**
    * Ensure all libraries are installed: `pip install customtkinter vgamepad pygame keyboard`
    * *Kütüphanelerin tam yüklendiğinden emin olun.*

---

**Developer:** [Senin Kullanıcı Adın]
