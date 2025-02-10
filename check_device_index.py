import pyaudio

# สร้าง PyAudio object
p = pyaudio.PyAudio()

# แสดงรายการอุปกรณ์เสียงทั้งหมด
for i in range(p.get_device_count()):
    device_info = p.get_device_info_by_index(i)
    print(f"Device Index: {i}, Name: {device_info['name']}")
