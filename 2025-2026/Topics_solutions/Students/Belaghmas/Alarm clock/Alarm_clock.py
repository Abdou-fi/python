import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import time
import threading

class AdvancedAlarmClock:
    """ساعة إنذار متقدمة مع ميزات شاملة"""
   
    def __init__(self, root):
        self.root = root
        self.root.title("🔔 ساعة إنذار احترافية")
        self.root.geometry("450x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#f8f9fa")
       
        # متغيرات التحكم
        self.hour_var = tk.StringVar(value="15")
        self.minute_var = tk.StringVar(value="00")
        self.alarm_running = False
        self.alarm_thread = None
        self.target_time = None
       
        self.init_ui()
        self.live_clock()
   
    def init_ui(self):
        """تهيئة الواجهة الرسومية"""
       
        # العنوان الرئيسي
        header = tk.Label(
            self.root,
            text="⏰ ساعة إنذار ذكية",
            font=("Segoe UI", 18, "bold"),
            bg="#1e3a8a",
            fg="white",
            pady=20
        )
        header.pack(fill=tk.X)
       
        # إطار الإدخال
        input_frame = ttk.LabelFrame(
            self.root,
            text="📝 ضع وقت الإنذار",
            padding="15 20"
        )
        input_frame.pack(pady=15, padx=25, fill=tk.X)
       
        # الساعة
        ttk.Label(input_frame, text="الساعة (00-23):").grid(
            row=0, column=0, sticky=tk.W, pady=(0, 10), padx=(0, 15))
       
        hour_spinbox = ttk.Spinbox(
            input_frame,
            from_=0, to=23,
            width=10,
            textvariable=self.hour_var,
            font=("Arial", 12),
            state="readonly"
        )
        hour_spinbox.grid(row=0, column=1, pady=(0, 10))
       
        # الدقائق
        ttk.Label(input_frame, text="الدقائق (00-59):").grid(
            row=1, column=0, sticky=tk.W, pady=(0, 10), padx=(0, 15))
       
        minute_spinbox = ttk.Spinbox(
            input_frame,
            from_=0, to=59,
            width=10,
            textvariable=self.minute_var,
            font=("Arial", 12),
            state="readonly"
        )
        minute_spinbox.grid(row=1, column=1, pady=(0, 10))
       
        # أزرار التحكم
        control_frame = tk.Frame(self.root, bg="#f8f9fa")
        control_frame.pack(pady=25)
       
        self.start_alarm_btn = tk.Button(
            control_frame,
            text="▶️ بدء الإنذار",
            command=self.start_alarm,
            width=16,
            height=2,
            bg="#10b981",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            activebackground="#059669"
        )
        self.start_alarm_btn.pack(side=tk.LEFT, padx=12)
       
        self.stop_alarm_btn = tk.Button(
            control_frame,
            text="⏹️ إيقاف الإنذار",
            command=self.stop_alarm,
            width=16,
            height=2,
            bg="#ef4444",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            state=tk.DISABLED,
            activebackground="#dc2626"
        )
        self.stop_alarm_btn.pack(side=tk.LEFT, padx=12)
       
        # إطار الحالة
        status_frame = ttk.LabelFrame(
            self.root,
            text="📈 حالة النظام",
            padding="12 20"
        )
        status_frame.pack(pady=12, padx=25, fill=tk.X)
       
        self.status_var = tk.StringVar(value="🟢 جاهز للعمل")
        status_label = tk.Label(
            status_frame,
            textvariable=self.status_var,
            font=("Arial", 11),
            fg="#059669"
        )
        status_label.pack(pady=5)
       
        # الساعة الرقمية الحية
        clock_frame = ttk.LabelFrame(
            self.root,
            text="🕐 الساعة الحالية",
            padding="20 25"
        )
        clock_frame.pack(pady=12, padx=25, fill=tk.X)
       
        self.clock_display = tk.Label(
            clock_frame,
            font=("Consolas", 22, "bold"),
            fg="#1e40af",
            bg="white",
            relief=tk.RIDGE,
            padx=20,
            pady=10
        )
        self.clock_display.pack()
   
    def live_clock(self):
        """ساعة حية متجددة"""
        current = datetime.now().strftime("%H:%M:%S")
        self.clock_display.config(text=current)
       
        # فحص الإنذار النشط
        if self.alarm_running and self.target_time:
            now_time = datetime.now().strftime("%H:%M")
            if now_time == self.target_time:
                self.sound_alarm()
       
        # جدولة التحديث
        self.root.after(950, self.live_clock)
   
    def start_alarm(self):
        """تشغيل الإنذار"""
        hour = self.hour_var.get()
        minute = self.minute_var.get()
       
        if not (hour.isdigit() and minute.isdigit()):
            messagebox.showerror("❌ خطأ", "أدخل أرقام صحيحة فقط!")
            return
       
        hour_int, minute_int = int(hour), int(minute)
        if not (0 <= hour_int <= 23 and 0 <= minute_int <= 59):
            messagebox.showerror("❌ خطأ", "الساعة: 0-23 | الدقائق: 0-59")
            return
       
        # تنسيق الوقت
        self.target_time = f"{hour_int:02d}:{minute_int:02d}"
       
        # التحقق من الوقت المستقبلي
        current_time = datetime.now().strftime("%H:%M")
        if self.target_time <= current_time:
            messagebox.showwarning("⚠️ تنبيه",
                                 f"الوقت {self.target_time} قد انتهى! ختر وقتاً مستقبلياً ")
            return
        # تفعيل الإنذار
        self.alarm_running = True
        self.start_alarm_btn.config(state=tk.DISABLED, text="✅ نشط")
        self.stop_alarm_btn.config(state=tk.NORMAL)
        self.status_var.set(f"🔴 الإنذار نشط حتى: {self.target_time}")
       
        messagebox.showinfo("✅ تم", f"🔔 تم تفعيل الإنذار للساع {self.target_time}")

    def sound_alarm(self):
        """تشغيل إنذار صوتي"""
        self.alarm_running = False
       
        # إشعارات متتالية
        messagebox.showwarning("🔔🔔 إنذار!",
                              "⏰ حان وقت الاستيقاظ!💤 استيقظ الآن!")
       
        self.reset_alarm()
   
    def stop_alarm(self):
        """إيقاف الإنذار"""
        self.alarm_running = False
        self.reset_alarm()
        messagebox.showinfo("⏹️", "تم إيقاف الإنذار بنجاح ✅")
   
    def reset_alarm(self):
        """إعادة التهيئة"""
        self.alarm_running = False
        self.target_time = None
        self.start_alarm_btn.config(state=tk.NORMAL, text="▶️ بدء الإنذار")
        self.stop_alarm_btn.config(state=tk.DISABLED)
        self.status_var.set("🟢 جاهز للعمل")

def main():
    """نقطة الدخول الرئيسية"""
    root = tk.Tk()
    app = AdvancedAlarmClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()