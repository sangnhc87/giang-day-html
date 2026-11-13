#import "template.typ": *
#pagebreak(weak: true)
#heading(level: 1, numbering: none, outlined: true)[Phụ lục: ba mươi chiêu nhanh để dán trên bàn]
Khi không có thời gian lật sách, thầy cô chỉ cần liếc qua bảng này. Mỗi chiêu là một cái tên, thầy cô nhớ tên sẽ nhớ cách làm.
#v(0.5em)
#let rows = (
 ("Mười phút thả ga", "Nói chuyện riêng", "Cho nói đúng ba phút rồi vào học"),
 ("Ba mươi giây cười có kiểm soát", "Cả lớp cười rộ", "Cười thật to có bấm giờ"),
 ("Đổi vai năm phút", "Chọc bạn", "Ngồi vào chỗ bạn rồi kể cảm giác"),
 ("Chức vụ có đi lại", "Không ngồi yên", "Giao việc phát và thu bài"),
 ("Ba cây gậy lời", "Nói leo", "Que giữ lượt, hết que thì ghi ra vở"),
 ("Tài khoản giây", "Lớp ồn", "Ghi số giây nợ, cuối tiết trả bằng đọc công thức"),
 ("Thầy thì thầm", "Lớp rã rời", "Nói nhỏ dần, ai muốn nghe tự im"),
 ("Nhạc trưởng", "Gõ bàn trêu thầy", "Thầy chỉ huy chính tiếng gõ"),
 ("Chấm xanh yên tĩnh", "Ồn khi thầy vắng", "Mười chấm xanh đổi một phần thưởng"),
 ("Vé vào lớp", "Đi trễ", "Ghi lý do thật và một việc làm khác"),
 ("Thư viện của thầy", "Quên sách", "Mượn sách, đọc to đoạn mở bài"),
 ("Giấy hẹn trả", "Quên bài", "Ký hẹn ngày nộp, đúng hẹn được khen"),
 ("Một ngày làm quản gia lớp", "Quên trực nhật", "Kiểm tra cả lớp trong mười phút"),
 ("Bàn đứng cuối lớp", "Ngủ gật", "Đứng học năm phút cho tỉnh"),
 ("Nhật ký giờ ngủ ba ngày", "Thức khuya chơi game", "Ghi giờ ngủ, tự thấy mối liên hệ"),
 ("Điện thoại đi nghỉ", "Dùng điện thoại", "Gửi máy vào khách sạn có thẻ phòng"),
 ("Xóa cùng nhau", "Quay chụp lén", "Xóa trước mặt, viết về cảm giác người bị quay"),
 ("Hũ từ thay thế", "Nói tục", "Ghi từ tục, nghĩ từ thay thế sáng tạo"),
 ("Biệt danh tử tế", "Biệt danh xúc phạm", "Đặt biệt danh nói về điểm mạnh"),
 ("Ba điều thật sự đẹp", "Đùa ngoại hình", "Viết ba điều đẹp không về ngoại hình"),
 ("Hoãn cuộc cãi", "Cãi thầy", "Hẹn ra chơi nghe cho kỹ"),
 ("Hộp góp ý có điều kiện", "Chê thầy dạy dở", "Góp ý ba dòng cụ thể"),
 ("Nhật ký phần của tôi", "Ăn không trong nhóm", "Ghi phần việc từng người"),
 ("Cây bút chung", "Hai bạn giận nhau", "Hai người một cây bút, mỗi người một chữ"),
 ("Chép mà hiểu", "Chép bài", "Giải thích một bước bằng lời mình"),
 ("Đọc to để hỏi", "Bài chép mạng", "Đọc to và giải thích đoạn văn"),
 ("Tiết dạy lại", "Trốn tiết", "Học từ bạn rồi dạy lại thầy năm phút"),
 ("Họa sĩ trả bàn", "Vẽ bậy lên bàn", "Lau bàn, cho một nơi vẽ hợp lệ"),
 ("Bảo mẫu của cây", "Khắc tên lên cây", "Chăm cây một tháng"),
 ("Phiếu miễn phạt", "Em đang không ổn", "Dùng phiếu, thầy không nhắc bài"),
)
#table(
  columns: (auto, 1.2fr, 2fr), inset: 6pt, stroke: 0.4pt + mist, fill: (x, y) => if y == 0 { navy } else if calc.odd(y) { softbg } else { white },
  table.header(text(fill: white, weight: "bold")[Chiêu], text(fill: white, weight: "bold")[Dùng khi], text(fill: white, weight: "bold")[Cách làm một dòng]),
  ..for r in rows { (text(weight: "bold", size: 9.5pt)[#r.at(0)], text(size: 9.5pt)[#r.at(1)], text(size: 9.5pt)[#r.at(2)]) }
)
#v(1.5em)
#block(fill: softbg, stroke: (left: 3pt + teal), inset: 12pt, radius: (right: 4pt), width: 100%)[
  #text(font: serif, style: "italic")[Một hình phạt hay là hình phạt mà học sinh kể lại cho bạn nghe và còn mỉm cười, nhưng lần sau vẫn nhớ không làm. Chúc thầy cô nhiều chiêu hay, và nhiều học sinh biết ơn.]
]
