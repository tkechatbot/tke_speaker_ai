Dự án cá nhân tke speaker ai 
Hoạt động online
Các chức năng chính:
- Nghe nhạc online trên : Youtube, zingmp3
- Kết nối Home Assistant --> Điều khiển thiết bị, sensor
- Mosquitto MQTT Broker --> Điều khiển thiết bị, sensor , Alarm LINE Notify
- Chat Gemini
- Chat GPT
- Hỏi thời tiết tất cả các địa danh   v.v.v
+ Hướng dẫn sử dụng:
-Kết nối Wifi : Sau khi khởi động nếu có cài sẳn Pass và Name WIFI thì hệ thống tự kết nối. Nếu không có kết nối được Wifi thì Raspberry tự chuyển qua phát (AP)Wifi : Tên Rpi-raspberrypi --> Kết nối -> sau đó vào trình duyệt Web truy cập địa chỉ: http://192.168.42.1  Chọn mạng Wifi kết nối cho raspberry (Lưu ý Rapberry pi2W chỉ kết nối băng tần 2.4G).
- Sau khi biết được địa chỉ IP kết nối Wifi của Raspi-> sau đó vào trình duyệt Web truy cập địa chỉ: http://192.168.x.x:5000 --> pass: speakerai để vào giao diện web cài đặt cho các API cần thiết cho tke speaker ai
  
+ Hướng dẫn đánh thức tke speaker ai: bạn gọi: Chào chát bốt --> bạn ra câu lệnh cho speaker thức hiện.
- Nghe nhạc trên Youtube: Bạn gọi: Chào chát bốt --> Mở nhạc + tên bài hát bạn muốn nghe
- Nghe nhạc trên Zingmp3: Gọi: Chào chát bốt --> Mở nhạc trên zing + tên tên bài hát bạn muốn nghe
- Nghe Radio: Chào chát bốt --> mở đài (hay radio) vov1 
                           --> mở đài (hay radio) vov2
                           --> mở đài (hay radio) vov3
                           --> mở đài (hay radio) vov1
                                     giao thông hà nội
                      giao thông thành phố hồ chí minh
                                            mở đài voh
- Điều khiển thiết bị câu lệnh : Mở/tắt,Bật/Đóng/Ngắt..
- Kiểm tra trạng thái thiết bị: Chào chát bốt --> Kiểm tra trạng thái + tên thiết bị...
Hướng dẫn cài đặt nâng cao:
- Sau khi biết được địa chỉ IP kết nối Wifi của Raspi -> vào WinSCP trên máy tính (Nếu chưa cài thì vào địa chỉ: https://winscp.net/eng/download.php)  Password truy cập Raspberry:
- Name: pi
- pass: raspberry
Kết nối Rapberry để thấy được Folder: tke_speaker_ai -> Mở -> bạn thấy các file .JSON . các file này dùng để thiết lập thay đổi các chức năng cho tke speaker ai
- File : api_key_tke.json là file chứa các api key cho hệ thống
- clients_info.json -> cấu hình các subscribe/publish MQTT Broker client 
- setup_wakeup.json -> thay đổi các file picovoice cho lệnh đánh thức tke speaker ai
- vvvvvvvvvvv
