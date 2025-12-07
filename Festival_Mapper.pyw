import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, Toplevel
import vgamepad as vg
import pygame
import threading
import time
import json
import os
import keyboard

# --- GÖRÜNÜM AYARLARI ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")
CONFIG_FILE = "config.json"

# --- DİL VERİTABANI ---
LANGUAGES = {
    "TR": {
        "title": "FESTIVAL MAPPER",
        "profile": "Profil:",
        "conn_sec": "1. GİTAR BAĞLANTISI:",
        "btn_conn": "Bağlan",
        "btn_refresh": "Yenile",
        "mode_sec": "2. ÇIKIŞ MODU:",
        "mode_xbox": "Xbox Kontrolcüsü (Fortnite)",
        "mode_key": "Klavye (Clone Hero)",
        "adv_sec": "4. GELİŞMİŞ ÖZELLİKLER:",
        "chk_tilt": "Tilt (Gitar Dikme) Aktif",
        "btn_tilt": "Tilt Eksenini Tanıt",
        "lbl_axis": "Eksen: Yok",
        "btn_overlay": "🎥 Yayıncı Modunu Aç (Overlay)",
        "btn_start": "BAŞLAT",
        "btn_stop": "DURDUR",
        "status_ready": "Hazır.",
        "status_wait": "BAS: '{key}' için gitara bas...",
        "status_conn": "Bağlandı: {dev}",
        "status_stop": "Durduruldu.",
        "status_tilt_ok": "Tilt Tanıtıldı!",
        "err_no_dev": "Önce gitarı bağla!",
        "err_vigem": "ViGEmBus sürücüsü eksik!",
        "overlay_drag": ":: SÜRÜKLE ::",
        "msg_del_confirm": "Bu profili silmek istiyor musun: {name}?",
        "err_last_profile": "Son kalan profili silemezsin!"
    },
    "EN": {
        "title": "FESTIVAL MAPPER",
        "profile": "Profile:",
        "conn_sec": "1. GUITAR CONNECTION:",
        "btn_conn": "Connect",
        "btn_refresh": "Refresh",
        "mode_sec": "2. OUTPUT MODE:",
        "mode_xbox": "Xbox Controller (Fortnite)",
        "mode_key": "Keyboard (Clone Hero)",
        "adv_sec": "4. ADVANCED FEATURES:",
        "chk_tilt": "Tilt Active",
        "btn_tilt": "Bind Tilt Axis",
        "lbl_axis": "Axis: None",
        "btn_overlay": "🎥 Open Streamer Mode (Overlay)",
        "btn_start": "START",
        "btn_stop": "STOP",
        "status_ready": "Ready.",
        "status_wait": "PRESS: Press guitar button for '{key}'...",
        "status_conn": "Connected: {dev}",
        "status_stop": "Stopped.",
        "status_tilt_ok": "Tilt Bound!",
        "err_no_dev": "Connect guitar first!",
        "err_vigem": "ViGEmBus driver missing!",
        "overlay_drag": ":: DRAG ::",
        "msg_del_confirm": "Delete this profile: {name}?",
        "err_last_profile": "Cannot delete the last profile!"
    },
    "ES": {
        "title": "FESTIVAL MAPPER",
        "profile": "Perfil:",
        "conn_sec": "1. CONEXIÓN DE GUITARRA:",
        "btn_conn": "Conectar",
        "btn_refresh": "Refrescar",
        "mode_sec": "2. MODO DE SALIDA:",
        "mode_xbox": "Controlador Xbox (Fortnite)",
        "mode_key": "Teclado (Clone Hero)",
        "adv_sec": "4. FUNCIONES AVANZADAS:",
        "chk_tilt": "Inclinación Activa",
        "btn_tilt": "Asignar Eje de Inclinación",
        "lbl_axis": "Eje: Ninguno",
        "btn_overlay": "🎥 Modo Streamer (Overlay)",
        "btn_start": "INICIAR",
        "btn_stop": "DETENER",
        "status_ready": "Listo.",
        "status_wait": "PRESIONA: Toca botón para '{key}'...",
        "status_conn": "Conectado: {dev}",
        "status_stop": "Detenido.",
        "status_tilt_ok": "¡Inclinación Asignada!",
        "err_no_dev": "¡Conecta la guitarra primero!",
        "err_vigem": "¡Falta el controlador ViGEmBus!",
        "overlay_drag": ":: ARRASTRAR ::",
        "msg_del_confirm": "¿Borrar este perfil: {name}?",
        "err_last_profile": "¡No puedes borrar el último perfil!"
    },
    "PT": {
        "title": "FESTIVAL MAPPER",
        "profile": "Perfil:",
        "conn_sec": "1. CONEXÃO DA GUITARRA:",
        "btn_conn": "Conectar",
        "btn_refresh": "Atualizar",
        "mode_sec": "2. MODO DE SAÍDA:",
        "mode_xbox": "Controlador Xbox (Fortnite)",
        "mode_key": "Teclado (Clone Hero)",
        "adv_sec": "4. RECURSOS AVANÇADOS:",
        "chk_tilt": "Inclinação Ativa",
        "btn_tilt": "Vincular Eixo",
        "lbl_axis": "Eixo: Nenhum",
        "btn_overlay": "🎥 Modo Streamer (Overlay)",
        "btn_start": "INICIAR",
        "btn_stop": "PARAR",
        "status_ready": "Pronto.",
        "status_wait": "PRESSIONE: Aperte botão para '{key}'...",
        "status_conn": "Conectado: {dev}",
        "status_stop": "Parado.",
        "status_tilt_ok": "Eixo Vinculado!",
        "err_no_dev": "Conecte a guitarra primeiro!",
        "err_vigem": "Driver ViGEmBus ausente!",
        "overlay_drag": ":: ARRASTAR ::",
        "msg_del_confirm": "Excluir este perfil: {name}?",
        "err_last_profile": "Não é possível excluir o último perfil!"
    },
    "RU": {
        "title": "FESTIVAL MAPPER",
        "profile": "Профиль:",
        "conn_sec": "1. ПОДКЛЮЧЕНИЕ ГИТАРЫ:",
        "btn_conn": "Подключить",
        "btn_refresh": "Обновить",
        "mode_sec": "2. РЕЖИМ ВЫВОДА:",
        "mode_xbox": "Xbox геймпад (Fortnite)",
        "mode_key": "Клавиатура (Clone Hero)",
        "adv_sec": "4. ДОПОЛНИТЕЛЬНО:",
        "chk_tilt": "Наклон активен",
        "btn_tilt": "Назначить ось наклона",
        "lbl_axis": "Ось: Нет",
        "btn_overlay": "🎥 Режим стримера",
        "btn_start": "СТАРТ",
        "btn_stop": "СТОП",
        "status_ready": "Готов.",
        "status_wait": "НАЖМИТЕ: Нажмите кнопку для '{key}'...",
        "status_conn": "Подключено: {dev}",
        "status_stop": "Остановлено.",
        "status_tilt_ok": "Наклон назначен!",
        "err_no_dev": "Сначала подключите гитару!",
        "err_vigem": "Драйвер ViGEmBus отсутствует!",
        "overlay_drag": ":: ПЕРЕТАЩИТЬ ::",
        "msg_del_confirm": "Удалить профиль: {name}?",
        "err_last_profile": "Нельзя удалить последний профиль!"
    },
    "DE": {
        "title": "FESTIVAL MAPPER",
        "profile": "Profil:",
        "conn_sec": "1. GITARRENANSCHLUSS:",
        "btn_conn": "Verbinden",
        "btn_refresh": "Aktualisieren",
        "mode_sec": "2. AUSGABEMODUS:",
        "mode_xbox": "Xbox Controller (Fortnite)",
        "mode_key": "Tastatur (Clone Hero)",
        "adv_sec": "4. ERWEITERTE FUNKTIONEN:",
        "chk_tilt": "Neigung Aktiv",
        "btn_tilt": "Neigungsachse binden",
        "lbl_axis": "Achse: Keine",
        "btn_overlay": "🎥 Streamer-Modus (Overlay)",
        "btn_start": "STARTEN",
        "btn_stop": "STOPPEN",
        "status_ready": "Bereit.",
        "status_wait": "DRÜCKEN: Taste für '{key}'...",
        "status_conn": "Verbunden: {dev}",
        "status_stop": "Gestoppt.",
        "status_tilt_ok": "Neigung gebunden!",
        "err_no_dev": "Gitarre zuerst anschließen!",
        "err_vigem": "ViGEmBus-Treiber fehlt!",
        "overlay_drag": ":: ZIEHEN ::",
        "msg_del_confirm": "Profil löschen: {name}?",
        "err_last_profile": "Das letzte Profil kann nicht gelöscht werden!"
    }
}

KEYBOARD_MAP = {
    "GREEN": "a", "RED": "s", "YELLOW": "j", "BLUE": "k", "ORANGE": "l",
    "STRUM_UP": "up", "STRUM_DOWN": "down", "SELECT": "space", "START": "enter", "WHAMMY": None
}

class OverlayWindow(Toplevel):
    def __init__(self, master, lang_code="TR"):
        super().__init__(master)
        self.lang_code = lang_code
        self.title("Input Overlay")
        self.geometry("450x150") 
        self.attributes('-topmost', True)
        self.overrideredirect(True)
        self.config(bg='magenta')
        self.attributes('-transparentcolor', 'magenta')
        
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<ButtonRelease-1>", self.stop_move)
        self.bind("<B1-Motion>", self.do_move)
        
        self.widgets = {}
        self.counters = {}
        self.prev_states = {}

        strum_color = "#800080"
        fret_colors = ["#00FF00", "#FF0000", "#FFFF00", "#0000FF", "#FFA500"]
        fret_keys = ["GREEN", "RED", "YELLOW", "BLUE", "ORANGE"]

        # --- STRUM UP (Sol Üst) ---
        self.create_overlay_key("STRUM_UP", x=10, y=30, width=70, height=50, color=strum_color, label="UP")

        # --- STRUM DOWN (Sol Alt) ---
        self.create_overlay_key("STRUM_DOWN", x=10, y=85, width=70, height=50, color=strum_color, label="DOWN")

        # --- FRET TUŞLARI (Sağda Yatay) ---
        start_x = 90
        y_pos = 55 

        for i, key in enumerate(fret_keys):
            self.create_overlay_key(key, x=start_x + (i*70), y=y_pos, width=65, height=65, color=fret_colors[i])

        drag_txt = LANGUAGES[self.lang_code].get("overlay_drag", ":: DRAG ::")
        lbl_drag = tk.Label(self, text=drag_txt, bg="black", fg="white", font=("Arial", 8))
        lbl_drag.place(x=10, y=5)

    def create_overlay_key(self, key, x, y, width, height, color, label=None):
        frame = tk.Frame(self, bg="black", width=width, height=height)
        frame.pack_propagate(False)
        frame.place(x=x, y=y)
        
        lbl = tk.Label(frame, bg="black")
        lbl.pack(expand=True, fill="both")
        
        canvas = tk.Canvas(lbl, width=width, height=height, bg="black", highlightthickness=0)
        canvas.pack()
        
        rect = canvas.create_rectangle(2, 2, width-2, height-2, fill="#111", outline=color, width=3)
        
        text_id = canvas.create_text(width/2, height/2, text="0", fill="white", font=("Arial", 14, "bold"))
        
        if label:
            canvas.create_text(width/2, height - 12, text=label, fill=color, font=("Arial", 8, "bold"))

        self.widgets[key] = (canvas, rect, text_id, color)
        self.counters[key] = 0
        self.prev_states[key] = False

    def update_state(self, key, active):
        if key in self.widgets:
            canvas, rect, text_id, color = self.widgets[key]
            
            if active and not self.prev_states[key]:
                self.counters[key] += 1
                canvas.itemconfig(text_id, text=str(self.counters[key]))
            
            self.prev_states[key] = active

            fill_col = color if active else "#111"
            text_col = "black" if active else "white"
            
            canvas.itemconfig(rect, fill=fill_col)
            canvas.itemconfig(text_id, fill=text_col)

    def start_move(self, event): self.x = event.x; self.y = event.y
    def stop_move(self, event): self.x = None; self.y = None
    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

class FestivalApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x800")
        self.resizable(False, False)
        
        # --- YAPILANDIRMA YÜKLEME ---
        self.full_config = self.load_config()
        
        # Dil ve Profil
        self.current_lang = self.full_config.get("global", {}).get("language", "TR")
        self.current_profile_name = self.full_config.get("global", {}).get("last_profile", "Fortnite Festival")
        self.profiles = self.full_config.get("profiles", {})
        
        if self.current_profile_name not in self.profiles:
            self.create_default_profile(self.current_profile_name)
        
        self.mapping = self.profiles[self.current_profile_name]["mapping"]
        
        # Sistem Değişkenleri
        self.gamepad = None
        self.target_joystick = None
        self.is_running = False
        self.binding_mode = False
        self.binding_key = None
        self.overlay_win = None
        
        pygame.init()
        pygame.joystick.init()
        
        self.create_ui()
        self.update_ui_text()
        self.populate_devices()
        self.load_profile_ui()

        self.listener_thread = threading.Thread(target=self.input_listener, daemon=True)
        self.listener_thread.start()

    def get_text(self, key):
        return LANGUAGES.get(self.current_lang, LANGUAGES["TR"]).get(key, key)

    def create_default_profile(self, name):
        self.profiles[name] = {
            "mapping": {},
            "mode": "XBOX",
            "tilt_enabled": False,
            "tilt_axis": None
        }
        self.save_config()

    def create_ui(self):
        # --- HEADER ---
        head_frame = ctk.CTkFrame(self, fg_color="#111", height=60)
        head_frame.pack(fill="x")
        
        self.lbl_title = ctk.CTkLabel(head_frame, text="FESTIVAL MAPPER V8", font=("Impact", 22), text_color="#4CAF50")
        self.lbl_title.pack(side="left", padx=20)
        
        # DİL SEÇİMİ
        self.combo_lang = ctk.CTkComboBox(head_frame, width=60, values=list(LANGUAGES.keys()), command=self.change_language)
        self.combo_lang.set(self.current_lang)
        self.combo_lang.pack(side="right", padx=10)

        # Profil Seçimi ve Butonlar
        self.lbl_profile = ctk.CTkLabel(head_frame, text="Profil:", text_color="gray")
        self.lbl_profile.pack(side="left", padx=(20, 5))
        self.combo_profile = ctk.CTkComboBox(head_frame, width=150, command=self.change_profile)
        self.combo_profile.pack(side="left")
        
        # EKLE (+)
        ctk.CTkButton(head_frame, text="+", width=30, command=self.add_profile).pack(side="left", padx=5)
        # SİL (-)
        ctk.CTkButton(head_frame, text="-", width=30, fg_color="#D32F2F", hover_color="#B71C1C", command=self.delete_profile).pack(side="left", padx=2)

        # --- 1. CİHAZ ---
        self.dev_frame = ctk.CTkFrame(self, fg_color="#222")
        self.dev_frame.pack(fill="x", padx=10, pady=10)
        self.lbl_conn_sec = ctk.CTkLabel(self.dev_frame, text="...", font=("Arial", 12, "bold"))
        self.lbl_conn_sec.pack(anchor="w", padx=10)
        
        self.combo_devices = ctk.CTkComboBox(self.dev_frame, width=350, state="readonly")
        self.combo_devices.pack(side="left", padx=10, pady=5)
        self.btn_conn = ctk.CTkButton(self.dev_frame, text="...", width=80, command=self.select_device)
        self.btn_conn.pack(side="left", padx=5)
        self.btn_refresh = ctk.CTkButton(self.dev_frame, text="...", width=60, fg_color="#444", command=self.populate_devices)
        self.btn_refresh.pack(side="left")

        # --- 2. MOD ---
        self.mode_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        self.mode_frame.pack(fill="x", padx=10, pady=5)
        self.lbl_mode_sec = ctk.CTkLabel(self.mode_frame, text="...", font=("Arial", 12, "bold"))
        self.lbl_mode_sec.pack(side="left", padx=10)
        self.radio_var = tk.StringVar(value="XBOX")
        self.rb_xbox = ctk.CTkRadioButton(self.mode_frame, text="...", variable=self.radio_var, value="XBOX", command=self.save_settings)
        self.rb_xbox.pack(side="left", padx=10)
        self.rb_key = ctk.CTkRadioButton(self.mode_frame, text="...", variable=self.radio_var, value="KEYBOARD", command=self.save_settings)
        self.rb_key.pack(side="left", padx=10)

        # --- 3. TUŞLAR ---
        self.map_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        self.map_frame.pack(fill="x", padx=10, pady=5)
        
        keys_inner = ctk.CTkFrame(self.map_frame, fg_color="transparent")
        keys_inner.pack(pady=5)
        self.btn_widgets = {}
        for c in ["GREEN", "RED", "YELLOW", "BLUE", "ORANGE"]:
            btn = ctk.CTkButton(keys_inner, text=c, width=60, height=60, fg_color=c.lower(), 
                                text_color="black" if c in ["YELLOW", "GREEN", "ORANGE"] else "white", 
                                command=lambda k=c: self.start_bind(k))
            btn.pack(side="left", padx=5)
            self.btn_widgets[c] = btn

        ctrl_inner = ctk.CTkFrame(self.map_frame, fg_color="transparent")
        ctrl_inner.pack(pady=5)
        self.create_map_btn(ctrl_inner, "STRUM_UP", "STRUM UP", "#333")
        self.create_map_btn(ctrl_inner, "STRUM_DOWN", "STRUM DOWN", "#333")
        self.create_map_btn(ctrl_inner, "SELECT", "SELECT", "#444")
        self.create_map_btn(ctrl_inner, "START", "START", "#444")
        
        whammy_frame = ctk.CTkFrame(self.map_frame, fg_color="transparent")
        whammy_frame.pack(pady=5)
        self.create_map_btn(whammy_frame, "WHAMMY", "WHAMMY BAR", "purple")

        # --- 4. GELİŞMİŞ ---
        adv_frame = ctk.CTkFrame(self, fg_color="#2b2b2b")
        adv_frame.pack(fill="x", padx=10, pady=10)
        self.lbl_adv_sec = ctk.CTkLabel(adv_frame, text="...", font=("Arial", 12, "bold"), text_color="orange")
        self.lbl_adv_sec.pack(anchor="w", padx=10)

        tilt_row = ctk.CTkFrame(adv_frame, fg_color="transparent")
        tilt_row.pack(fill="x", padx=10, pady=5)
        self.chk_tilt = ctk.CTkCheckBox(tilt_row, text="...", command=self.save_settings)
        self.chk_tilt.pack(side="left")
        self.btn_tilt_bind = ctk.CTkButton(tilt_row, text="...", width=150, fg_color="orange", text_color="black", command=self.bind_tilt)
        self.btn_tilt_bind.pack(side="right")
        self.lbl_tilt_status = ctk.CTkLabel(tilt_row, text="...", text_color="gray", width=80)
        self.lbl_tilt_status.pack(side="right", padx=10)

        over_row = ctk.CTkFrame(adv_frame, fg_color="transparent")
        over_row.pack(fill="x", padx=10, pady=5)
        self.btn_overlay = ctk.CTkButton(over_row, text="...", fg_color="#E91E63", command=self.toggle_overlay)
        self.btn_overlay.pack(fill="x")

        # --- 5. AKSİYON ---
        act_frame = ctk.CTkFrame(self, fg_color="transparent")
        act_frame.pack(fill="x", padx=10, pady=10, side="bottom")
        self.btn_start = ctk.CTkButton(act_frame, text="...", height=50, fg_color="green", font=("Arial", 16, "bold"), state="disabled", command=self.start_mapping)
        self.btn_start.pack(fill="x", pady=5)
        self.btn_stop = ctk.CTkButton(act_frame, text="...", height=40, fg_color="red", state="disabled", command=self.stop_mapping)
        self.btn_stop.pack(fill="x", pady=5)

        self.lbl_info = ctk.CTkLabel(self, text="...", text_color="gray")
        self.lbl_info.pack(side="bottom")

    def create_map_btn(self, parent, key, text, color):
        btn = ctk.CTkButton(parent, text=text, fg_color=color, command=lambda: self.start_bind(key))
        btn.pack(side="left", padx=5)
        self.btn_widgets[key] = btn

    # --- DİL FONKSİYONLARI ---
    def update_ui_text(self):
        self.title(self.get_text("title"))
        self.lbl_title.configure(text=self.get_text("title"))
        self.lbl_profile.configure(text=self.get_text("profile"))
        self.lbl_conn_sec.configure(text=self.get_text("conn_sec"))
        self.btn_conn.configure(text=self.get_text("btn_conn"))
        self.btn_refresh.configure(text=self.get_text("btn_refresh"))
        self.lbl_mode_sec.configure(text=self.get_text("mode_sec"))
        self.rb_xbox.configure(text=self.get_text("mode_xbox"))
        self.rb_key.configure(text=self.get_text("mode_key"))
        self.lbl_adv_sec.configure(text=self.get_text("adv_sec"))
        self.chk_tilt.configure(text=self.get_text("chk_tilt"))
        self.btn_tilt_bind.configure(text=self.get_text("btn_tilt"))
        self.btn_overlay.configure(text=self.get_text("btn_overlay"))
        self.btn_start.configure(text=self.get_text("btn_start"))
        self.btn_stop.configure(text=self.get_text("btn_stop"))
        
        prof = self.profiles[self.current_profile_name]
        t_axis = prof.get("tilt_axis", None)
        axis_txt = self.get_text("lbl_axis")
        self.lbl_tilt_status.configure(text=f"{axis_txt.split(':')[0]}: {t_axis}" if t_axis is not None else axis_txt)
        
        if not self.is_running:
            self.lbl_info.configure(text=self.get_text("status_ready"))

    def change_language(self, selection):
        self.current_lang = selection
        self.full_config["global"]["language"] = selection
        self.save_config()
        self.update_ui_text()

    # --- KONFİGÜRASYON ---
    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    data = json.load(f)
                    if "global" not in data:
                        return {"global": {"language": "TR", "last_profile": "Fortnite Festival"}, "profiles": data}
                    return data
            except: pass
        return {"global": {"language": "TR", "last_profile": "Fortnite Festival"}, "profiles": {}}

    def save_config(self):
        self.full_config["profiles"] = self.profiles
        self.full_config["global"]["last_profile"] = self.current_profile_name
        self.full_config["global"]["language"] = self.current_lang
        with open(CONFIG_FILE, 'w') as f:
            json.dump(self.full_config, f, indent=4)

    def load_profile_ui(self):
        self.combo_profile.configure(values=list(self.profiles.keys()))
        self.combo_profile.set(self.current_profile_name)
        
        prof = self.profiles[self.current_profile_name]
        self.mapping = prof["mapping"]
        self.radio_var.set(prof.get("mode", "XBOX"))
        self.chk_tilt.select() if prof.get("tilt_enabled", False) else self.chk_tilt.deselect()
        self.update_ui_text()
        
        for k, btn in self.btn_widgets.items():
            if k in self.mapping: btn.configure(fg_color="green", text_color="white")
            elif k in ["GREEN","RED","YELLOW","BLUE","ORANGE"]: 
                btn.configure(fg_color=k.lower(), text_color="black" if k in ["YELLOW","GREEN","ORANGE"] else "white")
            elif k == "WHAMMY": btn.configure(fg_color="purple")
            else: btn.configure(fg_color="#333")

    def change_profile(self, selection):
        self.current_profile_name = selection
        self.save_config()
        self.load_profile_ui()

    def add_profile(self):
        dialog = ctk.CTkInputDialog(text=self.get_text("profile"), title="New Profile")
        name = dialog.get_input()
        if name and name not in self.profiles:
            self.create_default_profile(name)
            self.current_profile_name = name
            self.save_config()
            self.load_profile_ui()
    
    def delete_profile(self):
        name = self.current_profile_name
        if len(self.profiles) <= 1:
            messagebox.showerror("Error", self.get_text("err_last_profile"))
            return
        
        msg = self.get_text("msg_del_confirm").format(name=name)
        if messagebox.askyesno("Delete", msg):
            del self.profiles[name]
            # Kalanlardan birini seç
            self.current_profile_name = list(self.profiles.keys())[0]
            self.save_config()
            self.load_profile_ui()

    def save_settings(self):
        prof = self.profiles[self.current_profile_name]
        prof["mode"] = self.radio_var.get()
        prof["tilt_enabled"] = bool(self.chk_tilt.get())
        self.save_config()

    # --- CİHAZ ---
    def populate_devices(self):
        pygame.joystick.quit(); pygame.joystick.init()
        devs = [f"{i}: {pygame.joystick.Joystick(i).get_name()}" for i in range(pygame.joystick.get_count())] or ["None"]
        self.combo_devices.configure(values=devs); self.combo_devices.set(devs[0])

    def select_device(self):
        sel = self.combo_devices.get()
        if "None" in sel: return
        try:
            self.target_joystick = pygame.joystick.Joystick(int(sel.split(":")[0])); self.target_joystick.init()
            msg = self.get_text("status_conn").format(dev=self.target_joystick.get_name())
            self.lbl_info.configure(text=msg, text_color="#00FF00")
            self.btn_start.configure(state="normal")
        except Exception as e: messagebox.showerror("Error", str(e))

    def input_listener(self):
        while True:
            if not self.target_joystick:
                time.sleep(1); continue
            
            if not self.is_running:
                pygame.event.pump()
            
            if self.binding_mode:
                found = None
                
                if self.binding_key == "TILT_AXIS":
                    for i in range(self.target_joystick.get_numaxes()):
                        if abs(self.target_joystick.get_axis(i)) > 0.8:
                            self.profiles[self.current_profile_name]["tilt_axis"] = i
                            self.save_config()
                            self.lbl_info.configure(text=self.get_text("status_tilt_ok"), text_color="green")
                            self.binding_mode = False; self.update_ui_text(); time.sleep(0.5); break
                else:
                    for i in range(self.target_joystick.get_numbuttons()):
                        if self.target_joystick.get_button(i): found = ('button', i); break
                    if not found:
                        for i in range(self.target_joystick.get_numhats()):
                            h = self.target_joystick.get_hat(i)
                            if h[1]!=0: found = ('hat_up' if h[1]==1 else 'hat_down', i); break
                    if not found and self.binding_key == "WHAMMY":
                         for i in range(self.target_joystick.get_numaxes()):
                             if abs(self.target_joystick.get_axis(i)) > 0.5: found = ('axis', i); break

                    if found:
                        self.mapping[self.binding_key] = {'type': found[0], 'index': found[1]}
                        self.save_config()
                        self.load_profile_ui()
                        self.binding_mode = False
                        time.sleep(0.2)
            time.sleep(0.01)

    def start_bind(self, key):
        if not self.target_joystick: 
            self.lbl_info.configure(text=self.get_text("err_no_dev"), text_color="red")
            return
        self.binding_mode = True; self.binding_key = key
        msg = self.get_text("status_wait").format(key=key)
        self.lbl_info.configure(text=msg, text_color="yellow")

    def bind_tilt(self):
        if not self.target_joystick: return
        self.binding_mode = True; self.binding_key = "TILT_AXIS"
        self.lbl_info.configure(text="TILT: GİTARI DİK!", text_color="orange")

    def toggle_overlay(self):
        if self.overlay_win:
            self.overlay_win.destroy(); self.overlay_win = None
        else:
            self.overlay_win = OverlayWindow(self, self.current_lang)

    def start_mapping(self):
        if not self.target_joystick: return
        self.is_running = True
        self.btn_start.configure(state="disabled"); self.btn_stop.configure(state="normal")
        self.combo_devices.configure(state="disabled"); self.combo_profile.configure(state="disabled")
        self.combo_lang.configure(state="disabled")
        self.binding_mode = False 
        
        prof = self.profiles[self.current_profile_name]
        mode = prof.get("mode", "XBOX")
        
        if mode == "XBOX":
            try: self.gamepad = vg.VX360Gamepad()
            except: messagebox.showerror("Error", self.get_text("err_vigem")); self.stop_mapping(); return
        
        threading.Thread(target=self.game_loop, daemon=True).start()

    def stop_mapping(self):
        self.is_running = False
        if self.gamepad: 
            del self.gamepad; self.gamepad = None
        self.btn_start.configure(state="normal"); self.btn_stop.configure(state="disabled")
        self.combo_devices.configure(state="normal"); self.combo_profile.configure(state="normal")
        self.combo_lang.configure(state="normal")
        self.lbl_info.configure(text=self.get_text("status_stop"), text_color="yellow")

    def game_loop(self):
        prof = self.profiles[self.current_profile_name]
        mode = prof.get("mode", "XBOX")
        tilt_on = prof.get("tilt_enabled", False)
        tilt_axis = prof.get("tilt_axis", None)
        
        while self.is_running:
            pygame.event.pump()
            state = {}
            for k, v in self.mapping.items():
                if v['index'] is None: state[k] = False; continue
                try:
                    if v['type'] == 'button': state[k] = self.target_joystick.get_button(v['index'])
                    elif 'hat' in v['type']:
                        h = self.target_joystick.get_hat(v['index'])
                        state[k] = (h[1]==1 and 'up' in v['type']) or (h[1]==-1 and 'down' in v['type'])
                    elif v['type'] == 'axis':
                        state[k] = abs(self.target_joystick.get_axis(v['index'])) > 0.1
                except: state[k] = False
            
            tilt_active = False
            if tilt_on and tilt_axis is not None:
                try:
                    if abs(self.target_joystick.get_axis(tilt_axis)) > 0.85: tilt_active = True
                except: pass

            if self.overlay_win:
                for k in ["STRUM_UP", "STRUM_DOWN", "GREEN", "RED", "YELLOW", "BLUE", "ORANGE"]:
                    self.overlay_win.update_state(k, state.get(k, False))

            if mode == "XBOX" and self.gamepad:
                if state.get("GREEN"): self.gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                else: self.gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                if state.get("RED"): self.gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                else: self.gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                if state.get("YELLOW"): self.gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                else: self.gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                if state.get("BLUE"): self.gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                else: self.gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                if state.get("ORANGE"): self.gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
                else: self.gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
                
                if state.get("START"): self.gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
                else: self.gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
                
                if state.get("SELECT") or tilt_active: self.gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
                else: self.gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)

                dpad = 0
                if state.get("STRUM_UP"): dpad |= vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
                if state.get("STRUM_DOWN"): dpad |= vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
                if dpad: self.gamepad.press_button(dpad)
                else: 
                    self.gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                    self.gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)

                if "WHAMMY" in self.mapping and self.mapping["WHAMMY"]["index"] is not None:
                      try:
                          val = self.target_joystick.get_axis(self.mapping["WHAMMY"]["index"])
                          self.gamepad.right_joystick(x_value=int(val*32000), y_value=0)
                      except: pass
                self.gamepad.update()

            elif mode == "KEYBOARD":
                for k, key_char in KEYBOARD_MAP.items():
                    if not key_char: continue
                    is_pressed = state.get(k, False)
                    if k == "SELECT" and tilt_active: is_pressed = True
                    if is_pressed: keyboard.press(key_char)
                    else: keyboard.release(key_char)

            time.sleep(0.001)

if __name__ == "__main__":
    app = FestivalApp()
    app.mainloop()
