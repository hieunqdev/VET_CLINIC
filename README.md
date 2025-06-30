# Hệ thống Quản lý Phòng khám Thú y (Vet Clinic Management)

> Module Odoo tùy chỉnh để quản lý toàn diện một phòng khám thú y.

---

## Tính năng chính

- Quản lý thông tin thú cưng
- Tạo và quản lý lịch hẹn khám bệnh
- Ghi nhận hồ sơ khám chữa bệnh
- Tạo hóa đơn thanh toán dịch vụ
- Tích hợp POS để bán hàng cho thú cưng
- Tích hợp Website & Customer Portal (đặt lịch trực tuyến)
- Cung cấp API để kết nối với hệ thống ngoài
- Tự động gửi email nhắc lịch qua cronjob

---

## Cách cài đặt

1. Sao chép thư mục `vet_clinic` vào thư mục `addons` của Odoo.
2. Khởi động lại server Odoo.
3. Vào **Chế độ Developer → Apps → Update App List**.
4. Tìm và cài đặt module **Vet Clinic Management**.

---

## 👥 Phân quyền

| Vai trò | Quyền |
|--------|-------|
| **Quản lý phòng khám** | Toàn quyền truy cập |
| **Bác sĩ thú y** | Xem & cập nhật hồ sơ khám |
| **Lễ tân** | Tạo lịch hẹn, xem thông tin cơ bản |
| **Người bán hàng (POS)** | Bán hàng liên quan thú cưng |

---

## Tác vụ định kỳ (cronjob)

- Gửi email nhắc lịch hẹn trước 1 ngày
- Cảnh báo thú cưng chưa khám lại sau 6 tháng

---

## API

| API | Mô tả |
|-----|------|
| `GET /api/pets` | Lấy danh sách thú cưng |
| `GET /api/pet/<id>` | Lấy thông tin chi tiết thú cưng |
| `POST /api/appointments` | Tạo lịch hẹn (có auth) |

> Xác thực bằng token.

---

## Báo cáo

- Báo cáo hồ sơ khám (PDF)
- Thống kê doanh thu theo dịch vụ/tháng
- Lịch sử khám theo từng thú cưng

---

## Tác giả

**Hiếu Dev**  
Email: hieundev@gmail.com  
