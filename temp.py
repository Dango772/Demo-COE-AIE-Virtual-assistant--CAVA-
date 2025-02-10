import pyaudio
import wave
from gtts import gTTS
from pydub import AudioSegment
import os

# 1. ฟังก์ชันสร้างเสียงจากข้อความ
def text_to_speech(text, output_file):
    """
    แปลงข้อความเป็นเสียงและบันทึกเป็นไฟล์ MP3
    """
    tts = gTTS(text=text, lang='th', slow=False)
    tts.save(output_file)
    print(f"เสียงถูกบันทึกในไฟล์: {output_file}")

# 2. ฟังก์ชันตรวจสอบอุปกรณ์เสียงและหา index ของ VB-Audio
def find_vb_audio_device():
    """
    ค้นหา device index ของ VB-Audio Virtual Cable
    """
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        if "CABLE Input" in device_info['name']:  # VB-Audio Virtual Cable
            print(f"พบ VB-Audio Virtual Cable ที่ Device Index: {i}")
            p.terminate()
            return i
    print("ไม่พบ VB-Audio Virtual Cable")
    p.terminate()
    return None

def convert_mp3_to_wav(input_file, output_file):
    """
    แปลงไฟล์ MP3 ให้เป็น WAV
    """
    sound = AudioSegment.from_mp3(input_file)
    sound.export(output_file, format="wav")
    print(f"ไฟล์ถูกแปลงเป็น WAV: {output_file}")

# 3. ฟังก์ชันเล่นไฟล์เสียงผ่าน VB-Audio
def play_audio_through_vb(file_path, device_index):
    """
    เล่นไฟล์เสียงผ่าน VB-Audio Virtual Cable
    """
    # เปิดไฟล์เสียง
    wf = wave.open(file_path, 'rb')
    p = pyaudio.PyAudio()
    
    # สร้าง stream เพื่อเล่นเสียง
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    output_device_index=device_index)
    
    print("กำลังเล่นเสียง...")
    # อ่านและเล่นเสียงทีละ frame
    data = wf.readframes(1024)
    while data:
        stream.write(data)
        data = wf.readframes(1024)
    
    # ปิด stream
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("การเล่นเสียงเสร็จสมบูรณ์")

# 4. ฟังก์ชันหลัก
def main():
    # ข้อความที่ต้องการแปลงเป็นเสียง
    text = "สวัสดีจ้าาา วันนี้คาว่าทานพุดดิ้งไปสามถ้วยเลยนะ อร่อยมากๆเลยจ้า!"
    
    # 1. แปลงข้อความเป็นเสียง
    mp3_file = "output.mp3"
    wav_file = "output.wav"
    text_to_speech(text, mp3_file)
    
    # แปลง MP3 เป็น WAV
    convert_mp3_to_wav(mp3_file, wav_file)
    
    # 2. ค้นหา VB-Audio Device Index
    vb_device_index = find_vb_audio_device()
    if vb_device_index is None:
        print("กรุณาตรวจสอบว่าคุณได้ติดตั้ง VB-Audio Virtual Cable แล้ว")
        return
    
    # 3. เล่นไฟล์เสียงผ่าน VB-Audio
    play_audio_through_vb(wav_file, vb_device_index)


# รันโปรแกรม
if __name__ == "__main__":
    main()
