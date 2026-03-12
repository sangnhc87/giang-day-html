import os

base_dir = "/workspaces/giang-day-html/truyen-tich-cam-hung-quyen-36/chapters"

files = {
    "ch01-em-co-biet.tex": r"""\chapter{Em Có Biết Gì Đâu}
\chapterintro{Lý do lý trấu}{Tuyển tập những màn chống chế, lý do lý trấu quen thuộc nhất của học trò mỗi khi quên bài, đi trễ, được gò chuốt theo đúng nhịp bằng trắc ngũ ngôn.}

\poem{Bài 01}{Ngũ ngôn tứ tuyệt}{Em có biết gì đâu}{Ngồi trong lớp đã lâu}{Thầy kêu sao chẳng nhớ}{Lại gãi trán xoa đầu}
\poem{Bài 02}{Ngũ ngôn tứ tuyệt}{Em có biết gì đâu}{Trời mưa nước ngập cầu}{Đạp xe đành đi trễ}{Chứ vội từ ban đầu}
\poem{Bài 03}{Ngũ ngôn tứ tuyệt}{Em có biết gì đâu}{Bài văn khó quá sâu}{Nhìn hoài mà chẳng hiểu}{Nên cắn bút ôm sầu}
\poem{Bài 04}{Ngũ ngôn tứ tuyệt}{Em có biết gì đâu}{Cùng bàn lỡ chép nhau}{Ai dè cô thấy được}{Cười gượng giấu niềm đau}
\poem{Bài 05}{Ngũ ngôn tứ tuyệt}{Em có biết gì đâu}{Tờ phao giấu rất sâu}{Gió đưa bay rớt xuống}{Cô nhặt khẽ nghiêng đầu}
\poem{Bài 06}{Ngũ ngôn tứ tuyệt}{Em có biết gì đâu}{Bài thi điểm rớt sâu}{Bao nhiêu lời hứa hẹn}{Trôi tuột mất đuôi đầu}
\poem{Bài 07}{Ngũ ngôn tứ tuyệt}{Em có biết gì đâu}{Thề ngoan sẽ ráng lâu}{Sáng ra nghe tiếng báo}{Lại ngủ ngáy quên sầu}
\poem{Bài 08}{Ngũ ngôn tứ tuyệt}{Em có biết gì đâu}{Giờ văn ngáp rất sâu}{Vừa nghe thầy gọi trúng}{Lắp bắp chẳng nên câu}
\poem{Bài 09}{Ngũ ngôn tứ tuyệt}{Em có biết gì đâu}{Tình cờ đụng trúng nhau}{Mà tim đập loạn nhịp}{Đỏ mặt đến hồi lâu}
\poem{Bài 10}{Ngũ ngôn tứ tuyệt}{Em có biết gì đâu}{Chỉ mong hết xó sầu}{Ra chơi vui nắng ấm}{Quên hết chữ trong đầu}
""",
    "ch02-em-co-lam.tex": r"""\chapter{Em Có Làm Gì Đâu}
\chapterintro{Góc oan uổng}{Khi lỗi rành rành nhưng miệng vẫn chối đây đẩy. Những tình huống cắn hạt dưa, vẽ bậy, làm ồn được ghi lại bằng giọng thơ hóm hỉnh.}

\poem{Bài 11}{Ngũ ngôn tứ tuyệt}{Em có làm gì đâu}{Bút tự rớt đó thôi}{Mực văng trúng áo bạn}{Bạn khóc ướt cả môi}
\poem{Bài 12}{Ngũ ngôn tứ tuyệt}{Em có làm gì đâu}{Chỉ đùa nhẹ một câu}{Mà ai kia giận gắt}{Ngoảnh mặt suốt canh thâu}
\poem{Bài 13}{Ngũ ngôn tứ tuyệt}{Em có làm gì đâu}{Đang yên giấc mộng sâu}{Thầy lay vai tỉnh dậy}{Đánh rớt chép bài đầu}
\poem{Bài 14}{Ngũ ngôn tứ tuyệt}{Em có làm gì đâu}{Quà vặt giấu tay sâu}{Mới nhai nghe cái rắc}{Cả tổ ngó nhìn nhau}
\poem{Bài 15}{Ngũ ngôn tứ tuyệt}{Em có làm gì đâu}{Chỉ sai dấu một câu}{Nên bài thi rớt hạng}{Buồn bã đến mai sau}
\poem{Bài 16}{Ngũ ngôn tứ tuyệt}{Em có làm gì đâu}{Bảng dơ chẳng phải tôi}{Tay vô tình quẹt phải}{Phấn dính trắng nguyên người}
\poem{Bài 17}{Ngũ ngôn tứ tuyệt}{Em có làm gì đâu}{Trêu nhau tựa phép mầu}{Bạn giận đi mét lớp}{Để lại khúc ưu sầu}
\poem{Bài 18}{Ngũ ngôn tứ tuyệt}{Em có làm gì đâu}{Đọc sai một chữ thôi}{Nguyên nguyên hàng áo trắng}{Cười mãi chẳng phai phôi}
\poem{Bài 19}{Ngũ ngôn tứ tuyệt}{Em có làm gì đâu}{Ném thư giấy qua cầu}{Bay ngay bàn cô giáo}{Đứng phạt mỏi hai đầu}
\poem{Bài 20}{Ngũ ngôn tứ tuyệt}{Em có làm gì đâu}{Ánh nhìn chỉ thoảng qua}{Ai dè người đáp lại}{Hồng má nắng chiều xa}
""",
    "ch03-em-chi-dua.tex": r"""\chapter{Em Chỉ Đùa Thôi Mà}
\chapterintro{Trêu ghẹo bạn hiền}{Những tiếng cười vỡ òa từ các trò tinh nghịch tuổi học đường, trêu bạn đỏ mặt rồi lại vội vã xin lỗi làm hòa.}

\poem{Bài 21}{Ngũ ngôn tứ tuyệt}{Em chỉ đùa thôi nha}{Làm chi giận tới già}{Lời trêu vừa cất dứt}{Đã méc với thầy a}
\poem{Bài 22}{Ngũ ngôn tứ tuyệt}{Em chỉ đùa thôi nha}{Đừng mang cầm chổi chà}{Rượt vòng quanh sân lớp}{Kẻo ngã xước da đà}
\poem{Bài 23}{Ngũ ngôn tứ tuyệt}{Em chỉ đùa thôi nha}{Nói ai thích Tuấn à}{Mà tai sao đỏ ửng}{Mắt giấu vội vàng ta}
\poem{Bài 24}{Ngũ ngôn tứ tuyệt}{Em chỉ đùa thôi nha}{Chép bài chậm thế a}{Nhìn sang trang bạn kế}{Chữ rối xéo như xà}
\poem{Bài 25}{Ngũ ngôn tứ tuyệt}{Em chỉ đùa thôi nha}{Bài sai nét nhạt nhòa}{Bút đỏ phê ngập mặt}{Lặng lẽ cất đi nà}
\poem{Bài 26}{Ngũ ngôn tứ tuyệt}{Em chỉ đùa thôi nha}{Kéo vai mượn chiếc là}{Quên mang không chịu trả}{Bạn mắng rung cả nhà}
\poem{Bài 27}{Ngũ ngôn tứ tuyệt}{Em chỉ đùa thôi nha}{Gọi em béo tựa trà}{Trà sữa trân châu ngập}{Em giận chẳng khuyên hòa}
\poem{Bài 28}{Ngũ ngôn tứ tuyệt}{Em chỉ đùa thôi nha}{Hù ma khóc thét òa}{Nước mắt rơi rớt giọt}{Xin lỗi mãi khôn ra}
\poem{Bài 29}{Ngũ ngôn tứ tuyệt}{Em chỉ đùa thôi nha}{Nói chia chỗ cách xa}{Mặt buồn như mất sổ}{Thấy tội quá đi mà}
\poem{Bài 30}{Ngũ ngôn tứ tuyệt}{Em chỉ đùa thôi nha}{Trêu xong để giảng hòa}{Tuổi học trò vui nhất}{Giận dỗi vút mây qua}
""",
    "ch04-thich-ma-khong.tex": r"""\chapter{Thích Mà Không Nói Ra}
\chapterintro{Tình cảm giấu kín}{Khúc rẽ đầy rung động của tuổi học trò. Một chút cảm nắng, một cái nhìn trộm, và những mộng mơ thuở mười sáu, mười bảy.}

\poem{Bài 31}{Ngũ ngôn tứ tuyệt}{Thích mà chẳng nói ra}{Lặng nhìn dáng bước qua}{Cứ vờ như chẳng thấy}{Mà tim đập giao hòa}
\poem{Bài 32}{Ngũ ngôn tứ tuyệt}{Thích mà chẳng nói ra}{Tên ai cứ nhẩn nha}{Vẽ vòng trên giấy nháp}{Đỏ mặt lúc tan ca}
\poem{Bài 33}{Ngũ ngôn tứ tuyệt}{Thích mà chẳng nói ra}{Giữ riêng một khúc ca}{Chờ ai nơi góc cửa}{Để lén ngó sương pha}
\poem{Bài 34}{Ngũ ngôn tứ tuyệt}{Thích mà chẳng nói ra}{Hành lang nắng nhạt nhòa}{Đưa ô che lúc gắt}{Vội vã bước lùi xa}
\poem{Bài 35}{Ngũ ngôn tứ tuyệt}{Thích mà chẳng nói ra}{Ngày thi sợ cách xa}{Chúc đôi câu điểm tốt}{Chôn giấu mộng mây sa}
\poem{Bài 36}{Ngũ ngôn tứ tuyệt}{Thích mà chẳng nói ra}{Lén mua kẹo chanh trà}{Đặt nhanh trong hộc sách}{Giữ kín mãi đây mà}
\poem{Bài 37}{Ngũ ngôn tứ tuyệt}{Thích mà chẳng nói ra}{Dù cho chớp mắt qua}{Nhưng nụ cười năm ấy}{Vẫn sáng tựa sao sa}
\poem{Bài 38}{Ngũ ngôn tứ tuyệt}{Thích mà chẳng nói ra}{Đành cam đứng phía xa}{Chụp chung bao ảnh lớp}{Chỉ ngắm bóng ngọc ngà}
\poem{Bài 39}{Ngũ ngôn tứ tuyệt}{Thích mà chẳng nói ra}{Viết lưu bút giấy hoa}{Bao điều mong muốn kể}{Gom lại một câu chào}
\poem{Bài 40}{Ngũ ngôn tứ tuyệt}{Thích mà chẳng nói ra}{Đẹp như ánh tuyết pha}{Góc sân trường thầm lặng}{Giữ mãi một tình ca}
""",
    "ch05-ban-cung-ban.tex": r"""\chapter{Bạn Cùng Bàn Năm Ấy}
\chapterintro{Góc kỷ niệm bàn bên}{Người bạn ngồi chung bàn, chia vạch phấn, chép bài giúp và che chở nhau mỗi cơn buồn ngủ. Thanh xuân đẹp nhất là chiếc bàn gỗ nhỏ này.}

\poem{Bài 41}{Ngũ ngôn tứ tuyệt}{Bạn cùng bàn năm ấy}{Hay nghiêng tóc che tay}{Mùi hương thơm bay nhẹ}{Trôi suốt tháng năm dài}
\poem{Bài 42}{Ngũ ngôn tứ tuyệt}{Bạn cùng bàn năm ấy}{Mượn gôm chép bài sai}{Cãi nhau chê chữ xấu}{Lườm nguýt hết một ngày}
\poem{Bài 43}{Ngũ ngôn tứ tuyệt}{Bạn cùng bàn năm ấy}{Che chung cái áo quài}{Trưa hè oi bức quá}{Quạt giấy mát hai vai}
\poem{Bài 44}{Ngũ ngôn tứ tuyệt}{Bạn cùng bàn năm ấy}{Lên bảng đứng khoanh tay}{Quay nhìn chờ nhắc nhở}{Tôi nhắc gật đầu thay}
\poem{Bài 45}{Ngũ ngôn tứ tuyệt}{Bạn cùng bàn năm ấy}{Khóc nhè mắt sưng mày}{Tôi đưa tờ khăn mỏng}{Lau hết lệ sầu phai}
\poem{Bài 46}{Ngũ ngôn tứ tuyệt}{Bạn cùng bàn năm ấy}{Lười bôi bảng nhăn mày}{Tôi cầm bao giẻ sạch}{Chùi vội phấn trắng bay}
\poem{Bài 47}{Ngũ ngôn tứ tuyệt}{Bạn cùng bàn năm ấy}{Ăn chia nửa bánh này}{Ngọt bùi thơm lớp học}{Đầy tuổi trẻ ngây ngây}
\poem{Bài 48}{Ngũ ngôn tứ tuyệt}{Bạn cùng bàn năm ấy}{Ngủ quên tiết học dài}{Tôi làm bia đỡ đạn}{Che chắn khỏi thầy la}
\poem{Bài 49}{Ngũ ngôn tứ tuyệt}{Bạn cùng bàn năm ấy}{Ngày chia cách chia tay}{Mắt đỏ hoen không nói}{In đậm dấu chân mai}
\poem{Bài 50}{Ngũ ngôn tứ tuyệt}{Bạn cùng bàn năm ấy}{Về đâu phía tương lai}{Xin nhớ bàn hai đứa}{Lưu bóng khắc chưa phai}
""",
    "ch06-tan-hoc-doi.tex": r"""\chapter{Tan Học Đợi Nhau Về}
\chapterintro{Đường về chung đôi}{Hình ảnh lãng mạn cuối cùng của cuốn sách, nán lại cổng trường, chiếc xe đạp đôi, hoàng hôn và những bến đỗ bình yên.}

\poem{Bài 51}{Ngũ ngôn tứ tuyệt}{Tan học đợi nhau về}{Đường xanh rợp nắng hè}{Xe song quanh con phố}{Gió gọi rộn trên đê}
\poem{Bài 52}{Ngũ ngôn tứ tuyệt}{Tan học đợi nhau về}{Chờ qua chuông báo lề}{Bước nhanh nơi hàng cửa}{Sợ bỏ lỡ câu thề}
\poem{Bài 53}{Ngũ ngôn tứ tuyệt}{Tan học đợi nhau về}{Nhìn nhau chẳng dám chê}{Lặng im đi một đoạn}{Mộng tưởng hóa si mê}
\poem{Bài 54}{Ngũ ngôn tứ tuyệt}{Tan học đợi nhau về}{Bạn khen tiếng hát thề}{Tôi cười trong e lệ}{Lòng rực ánh say mê}
\poem{Bài 55}{Ngũ ngôn tứ tuyệt}{Tan học đợi nhau về}{Mưa bay ướt góc lề}{Nép hiên nhà trú tạm}{Nghe giọt nước lê thê}
\poem{Bài 56}{Ngũ ngôn tứ tuyệt}{Tan học đợi nhau về}{Phượng rơi đỏ lối quê}{Tiếc thời gian ngắn quá}{Đâu thỏa hết đam mê}
\poem{Bài 57}{Ngũ ngôn tứ tuyệt}{Tan học đợi nhau về}{Lặng ôm cặp mải mê}{Kể bao điều trên lớp}{Chuyện cô mắng não nề}
\poem{Bài 58}{Ngũ ngôn tứ tuyệt}{Tan học đợi nhau về}{Trà chanh đá vỉa hè}{Ngồi bên chia ly nước}{Cười nói tiếng pha lê}
\poem{Bài 59}{Ngũ ngôn tứ tuyệt}{Tan học đợi nhau về}{Đường xa chẳng não nề}{Bởi chung người bạn quý}{Rảo bước mãi không chê}
\poem{Bài 60}{Ngũ ngôn tứ tuyệt}{Tan học đợi nhau về}{Giờ như giấc ngủ mê}{Còn đâu ngày chung lối}{Ngơ ngẩn nhớ bến quê}
"""
}

for fname, content in files.items():
    path = os.path.join(base_dir, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
print("CREATED 6 chapters successfully.")
