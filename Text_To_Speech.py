from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

# ข้อความที่ปนกันระหว่างไทยและอังกฤษ
text = "สวัสดีจ้าาา วันนี้คาว่าทานพุดดิ้งไปสามถ้วยเลยนะ อร่อยมากๆเลยจ้า! "

# สร้างไฟล์เสียงด้วย gTTS
tts = gTTS(text=text, lang='th', slow=False)  # ใช้ภาษาไทยเป็นหลัก
tts.save("output.mp3")  # บันทึกเป็นไฟล์ .mp3

# เล่นไฟล์เสียง (ใช้สำหรับทดสอบ)
os.system("start output.mp3")  # บน Windows
