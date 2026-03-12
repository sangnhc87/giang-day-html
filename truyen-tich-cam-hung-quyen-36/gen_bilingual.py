import os

base_dir = "/workspaces/giang-day-html/truyen-tich-cam-hung-quyen-36/chapters"

files = {
    "ch01-em-co-biet.tex": r"""\chapter{Em Có Biết Gì Đâu}
\chapterintro{Lý do lý trấu}{Những lời chống chế kinh điển của tuổi học trò mỗi khi bị thầy cô gọi bài cũ.}

\begin{poembox}{Bài 01}{Lúc thầy giáo gọi trả bài cũ mà trong đầu hoàn toàn trống rỗng.}
\pline{Em có biết gì đâu}{What do you even know?}
\pline{Ngồi trong lớp đã lâu}{Sitting in class so long,}
\pline{Thầy kêu sao chẳng nhớ}{Called up but remember nothing,}
\pline{Lại gãi trán xoa đầu}{Just rubbing your forehead.}
\end{poembox}

\begin{poembox}{Bài 02}{Biện bạch lý do đi trễ muôn thuở: đổ lỗi cho thời tiết.}
\pline{Em có biết gì đâu}{What do you even know?}
\pline{Trời mưa nước ngập cầu}{Rain flooded the whole bridge,}
\pline{Đạp xe đành đi trễ}{Cycling, I had to be late,}
\pline{Chứ vội từ ban đầu}{I rushed right from the start.}
\end{poembox}

\begin{poembox}{Bài 03}{Nhìn đề văn mà như nhìn bức vách, không biết phải viết gì.}
\pline{Em có biết gì đâu}{What do you even know?}
\pline{Bài văn khó quá sâu}{The essay was way too deep,}
\pline{Nhìn hoài mà chẳng hiểu}{Staring without understanding,}
\pline{Nên cắn bút ôm sầu}{So hugging sorrow, biting my pen.}
\end{poembox}

\begin{poembox}{Bài 04}{Bị cô bắt quả tang đang chép bề của bạn ngồi cạnh.}
\pline{Em có biết gì đâu}{What do you even know?}
\pline{Cùng bàn lỡ chép nhau}{Deskmates accidentally copied,}
\pline{Ai dè cô thấy được}{Who knew the teacher saw,}
\pline{Cười gượng giấu niềm đau}{Forcing a smile, hiding pain.}
\end{poembox}

\begin{poembox}{Bài 05}{Tình huống rớt "phao" cực kỳ éo le trong giờ kiểm tra.}
\pline{Em có biết gì đâu}{What do you even know?}
\pline{Tờ phao giấu rất sâu}{The cheat sheet hidden deep,}
\pline{Gió đưa bay rớt xuống}{Wind blew it falling down,}
\pline{Cô nhặt khẽ nghiêng đầu}{She picked it up, tilting her head.}
\end{poembox}

\begin{poembox}{Bài 06}{Khi điểm thi thấp tè và tự hứa với lòng nhưng chẳng bao giờ làm.}
\pline{Em có biết gì đâu}{What do you even know?}
\pline{Bài thi điểm rớt sâu}{Exam score dropped so low,}
\pline{Bao nhiêu lời hứa hẹn}{So many promised words,}
\pline{Trôi tuột mất đuôi đầu}{Slipped away entirely.}
\end{poembox}

\begin{poembox}{Bài 07}{Quyết tâm dậy sớm học bài nhưng báo thức reo đành vô tác dụng.}
\pline{Em có biết gì đâu}{What do you even know?}
\pline{Thề ngoan sẽ ráng lâu}{Swore to try hard for long,}
\pline{Sáng ra nghe tiếng báo}{Morning alarm rang out,}
\pline{Lại ngủ ngáy quên sầu}{Just snored forgetting all.}
\end{poembox}

\begin{poembox}{Bài 08}{Đang ngủ gật trong tiết Văn thì bỗng nhiên bị gọi tên.}
\pline{Em có biết gì đâu}{What do you even know?}
\pline{Giờ văn ngáp rất sâu}{Literature class, yawning deep,}
\pline{Vừa nghe thầy gọi trúng}{Barely heard the teacher call,}
\pline{Lắp bắp chẳng nên câu}{Stammering without a sentence.}
\end{poembox}

\begin{poembox}{Bài 09}{Khoảnh khắc lỡ va chạm nhẹ ở hành lang nhưng làm loạn nhịp tim.}
\pline{Em có biết gì đâu}{What do you even know?}
\pline{Tình cờ đụng trúng nhau}{We accidentally bumped,}
\pline{Mà tim đập loạn nhịp}{Yet heart beat wild out of tune,}
\pline{Đỏ mặt đến hồi lâu}{Face blushing for so long.}
\end{poembox}

\begin{poembox}{Bài 10}{Mong ngóng chuông ra chơi để thoát khỏi áp lực học tập.}
\pline{Em có biết gì đâu}{What do you even know?}
\pline{Chỉ mong hết xó sầu}{Just wish this gloom would end,}
\pline{Ra chơi vui nắng ấm}{Recess is fun in warm sun,}
\pline{Quên hết chữ trong đầu}{Forgetting all words in mind.}
\end{poembox}
""",
    "ch02-em-co-lam.tex": r"""\chapter{Em Có Làm Gì Đâu}
\chapterintro{Góc oan uổng}{Khi lỗi rành rành nhưng miệng vẫn chối đây đẩy. Những tình huống dở khóc dở cười vì lỡ mồm, lỡ tay.}

\begin{poembox}{Bài 11}{Chiếc bút phản chủ văng mực làm bẩn áo sơ mi trắng của bạn.}
\pline{Em có làm gì đâu}{I didn't do anything,}
\pline{Bút tự rớt đó thôi}{The pen just dropped itself,}
\pline{Mực văng trúng áo bạn}{Ink splashed upon your shirt,}
\pline{Bạn khóc ướt cả môi}{You cried, wetting your lips.}
\end{poembox}

\begin{poembox}{Bài 12}{Con gái sáng nắng chiều mưa, mới đùa một câu đã giận.}
\pline{Em có làm gì đâu}{I didn't do anything,}
\pline{Chỉ đùa nhẹ một câu}{Just made a little joke,}
\pline{Mà ai kia giận gắt}{Yet someone got so mad,}
\pline{Ngoảnh mặt suốt canh thâu}{Turned away all night long.}
\end{poembox}

\begin{poembox}{Bài 13}{Thầy vô tình làm bạn rơi mất dòng cảm hứng chép bài.}
\pline{Em có làm gì đâu}{I didn't do anything,}
\pline{Đang yên giấc mộng sâu}{Peaceful in deepest dream,}
\pline{Thầy lay vai tỉnh dậy}{Teacher shook my shoulder awake,}
\pline{Đánh rớt chép bài đầu}{Lost the first copied lines.}
\end{poembox}

\begin{poembox}{Bài 14}{Nhai bánh tráng lén lút mà tiếng "rắc" vang vọng cả không gian lạng ngắt.}
\pline{Em có làm gì đâu}{I didn't do anything,}
\pline{Quà vặt giấu tay sâu}{Snacks hidden deep in hands,}
\pline{Mới nhai nghe cái rắc}{Just chewed, a crunch resounds,}
\pline{Cả tổ ngó nhìn nhau}{The whole group looks around.}
\end{poembox}

\begin{poembox}{Bài 15}{Sai một ly đi một dặm, chỉ vì nhầm lẫn dấu toán học bé xíu.}
\pline{Em có làm gì đâu}{I didn't do anything,}
\pline{Chỉ sai dấu một câu}{Just missed a sign in one line,}
\pline{Nên bài thi rớt hạng}{So the test rank dropped down,}
\pline{Buồn bã đến mai sau}{Sad until tomorrow arrives.}
\end{poembox}

\begin{poembox}{Bài 16}{Làm ẩu thì lại không cẩn thận quẹt lưng vào phấn bảng.}
\pline{Em có làm gì đâu}{I didn't do anything,}
\pline{Bảng dơ chẳng phải tôi}{That dirty board wasn't me,}
\pline{Tay vô tình quẹt phải}{Hand brushed it by mistake,}
\pline{Phấn dính trắng nguyên người}{Chalk stuck fully white on me.}
\end{poembox}

\begin{poembox}{Bài 17}{Chỉ trêu ghẹo vui thế mà bạn đã đi mách lẻo với thầy.}
\pline{Em có làm gì đâu}{I didn't do anything,}
\pline{Trêu nhau tựa phép mầu}{Teasing like magic spells,}
\pline{Bạn giận đi mét lớp}{You got mad and told the class,}
\pline{Để lại khúc ưu sầu}{Leaving sadness behind.}
\end{poembox}

\begin{poembox}{Bài 18}{Khi tự tin đọc to đáp án sai khiến đồng bọn cười đau bụng.}
\pline{Em có làm gì đâu}{I didn't do anything,}
\pline{Đọc sai một chữ thôi}{Just read one word amiss,}
\pline{Cả hàng dãy áo trắng}{The whole row of white shirts,}
\pline{Cười mãi chẳng phai phôi}{Laughed with an endless bliss.}
\end{poembox}

\begin{poembox}{Bài 19}{Ném giấy chuyền nội dung cho bạn mà rớt lộ liễu trên bàn giáo viên.}
\pline{Em có làm gì đâu}{I didn't do anything,}
\pline{Ném thư giấy qua cầu}{Threw paper across the bridge,}
\pline{Bay ngay bàn cô giáo}{Flew to the teacher's desk,}
\pline{Đứng phạt mỏi hai đầu}{Stood penalized, aching so.}
\end{poembox}

\begin{poembox}{Bài 20}{Phát hiện ánh mắt giao nhau khiến mặt mũi chợt đỏ bừng.}
\pline{Em có làm gì đâu}{I didn't do anything,}
\pline{Ánh nhìn chỉ thoảng qua}{The glance was just so brief,}
\pline{Ai dè người đáp lại}{Who knew they would reply,}
\pline{Hồng má nắng chiều xa}{Rosy cheeks in late sun.}
\end{poembox}
""",
    "ch03-em-chi-dua.tex": r"""\chapter{Em Chỉ Đùa Thôi Mà}
\chapterintro{Trêu ghẹo bạn hiền}{Tiếng cười vỡ òa từ những trò tinh nghịch vô tư, trêu bạn giận rồi lại lẽo đẽo xin làm hòa.}

\begin{poembox}{Bài 21}{Bạn cùng bàn nhạy cảm, cứ động tí là đi méc cô.}
\pline{Em chỉ đùa thôi nha}{I am only joking, okay,}
\pline{Làm chi giận tới già}{Why hold a grudge so long,}
\pline{Lời trêu vừa cất dứt}{Once teasing word was out,}
\pline{Đã méc với thầy a}{Already told the teacher?}
\end{poembox}

\begin{poembox}{Bài 22}{Trò chạy rượt nhau kinh dị nơi hành lang lớp học.}
\pline{Em chỉ đùa thôi nha}{I am only joking, okay,}
\pline{Đừng mang cầm chổi chà}{Don't brandish that big broom,}
\pline{Rượt vòng quanh sân lớp}{Chasing round the classroom yard,}
\pline{Kẻo ngã xước da đà}{Lest you trip and scrape skin.}
\end{poembox}

\begin{poembox}{Bài 23}{Nhắc trúng tên crush của người ta giữa bàn dân thiên hạ.}
\pline{Em chỉ đùa thôi nha}{I am only joking, okay,}
\pline{Nói ai thích Tuấn à}{Said someone likes Tuan, huh?}
\pline{Mà tai sao đỏ ửng}{Why are your ears blushing red,}
\pline{Mắt giấu vội vàng ta}{Eyes hiding hastily?}
\end{poembox}

\begin{poembox}{Bài 24}{Tính hay săi soi chữ viết tồi tệ của đứa ngồi cạnh.}
\pline{Em chỉ đùa thôi nha}{I am only joking, okay,}
\pline{Chép bài chậm thế a}{Copying notes so slow?}
\pline{Nhìn sang trang bạn kế}{Glancing at the neighbor's page,}
\pline{Chữ rối xéo như xà}{Words tangled like snake tracks.}
\end{poembox}

\begin{poembox}{Bài 25}{Thấy bạn nhận bài kiểm tra be bét mực đỏ bèn buông lời "xát muối".}
\pline{Em chỉ đùa thôi nha}{I am only joking, okay,}
\pline{Bài sai nét nhạt nhòa}{Errors pale ink away,}
\pline{Bút đỏ phê ngập mặt}{Red marks cover the face,}
\pline{Lặng lẽ cất đi nà}{Quietly putting it away.}
\end{poembox}

\begin{poembox}{Bài 26}{Cái tật hay cầm nhầm bút thước mà không chịu trao trả khổ chủ.}
\pline{Em chỉ đùa thôi nha}{I am only joking, okay,}
\pline{Kéo vai mượn chiếc là}{Tap shoulder to borrow something,}
\pline{Quên mang không chịu trả}{Forgot and won't return,}
\pline{Bạn mắng rung cả nhà}{Friend scolds shaking the house.}
\end{poembox}

\begin{poembox}{Bài 27}{Sở thích uống quá nhiều trà sữa bị đem ra làm trò đùa.}
\pline{Em chỉ đùa thôi nha}{I am only joking, okay,}
\pline{Gọi em béo tựa trà}{Called you plump like the tea,}
\pline{Trà sữa trân châu ngập}{Filled with pearl milk sweetness,}
\pline{Em giận chẳng khuyên hòa}{You got mad, refusing peace.}
\end{poembox}

\begin{poembox}{Bài 28}{Giấu đồ hù dọa cô bạn nhút nhát để rồi phải hối hận.}
\pline{Em chỉ đùa thôi nha}{I am only joking, okay,}
\pline{Hù ma khóc thét òa}{Scared you into loud cries,}
\pline{Nước mắt rơi rớt giọt}{Tears dropping in small beads,}
\pline{Xin lỗi mãi khôn ra}{Apologized endlessly.}
\end{poembox}

\begin{poembox}{Bài 29}{Trả đũa bằng việc vạch phấn định ranh giới giữa hai nửa kỷ niệm.}
\pline{Em chỉ đùa thôi nha}{I am only joking, okay,}
\pline{Nói chia chỗ cách xa}{Said we divide our space,}
\pline{Mặt buồn như mất sổ}{Looked sad like losing cash,}
\pline{Thấy tội quá đi mà}{Felt too guilty inside.}
\end{poembox}

\begin{poembox}{Bài 30}{Một phút xốc nổi tuổi thanh xuân để rồi nhớ mãi tình bạn khảng khái.}
\pline{Em chỉ đùa thôi nha}{I am only joking, okay,}
\pline{Trêu xong để giảng hòa}{Teased just to reconcile,}
\pline{Tuổi học trò vui nhất}{Student years are the most fun,}
\pline{Giận dỗi vút mây qua}{Pouting flies past the clouds.}
\end{poembox}
""",
    "ch04-thich-ma-khong.tex": r"""\chapter{Thích Mà Không Nói Ra}
\chapterintro{Tình cảm giấu kín}{Khúc rẽ rung động ngây ngô của tuổi mười lăm mười bảy. Một chút cảm nắng, một cái nhìn trộm, một vương vấn mang theo mãi sau nầy.}

\begin{poembox}{Bài 31}{Ánh mắt luôn dõi theo bóng dáng quen thuộc qua hàng hiên.}
\pline{Thích mà chẳng nói ra}{Liking you, yet saying nothing.}
\pline{Lặng nhìn dáng bước qua}{Watching your shape pass by.}
\pline{Cứ vờ như chẳng thấy}{Pretending not to see.}
\pline{Mà tim đập giao hòa}{Yet my heart beats in sync.}
\end{poembox}

\begin{poembox}{Bài 32}{Thói quen viết đi viết lại tên một người trên tờ giấy nháp.}
\pline{Thích mà chẳng nói ra}{Liking you, yet saying nothing.}
\pline{Tên ai cứ nhẩn nha}{Writing someone's name slow.}
\pline{Vẽ vòng trên giấy nháp}{Drawing rings on scrap sheets.}
\pline{Đỏ mặt lúc tan ca}{Blushing bright when class ends.}
\end{poembox}

\begin{poembox}{Bài 33}{Sự chờ đợi âm thầm dù chỉ để nhìn thấy mặt nhau một giây.}
\pline{Thích mà chẳng nói ra}{Liking you, yet saying nothing.}
\pline{Giữ riêng một khúc ca}{Keeping a private song.}
\pline{Chờ ai nơi góc cửa}{Waiting by the door's edge.}
\pline{Để lén ngó sương pha}{Stealing a glance in mist.}
\end{poembox}

\begin{poembox}{Bài 34}{Chỉ một cái ô xòe vội dưới cơn nắng gắt cũng khiến lòng ấm êm.}
\pline{Thích mà chẳng nói ra}{Liking you, yet saying nothing.}
\pline{Hành lang nắng nhạt nhòa}{Sun fades on the hallway.}
\pline{Đưa ô che lúc gắt}{Offering shade in heat.}
\pline{Vội vã bước lùi xa}{Hastily stepping back.}
\end{poembox}

\begin{poembox}{Bài 35}{Thay vì nói câu yêu, đành gói ghém tình cảm vào câu trúc thi tốt.}
\pline{Thích mà chẳng nói ra}{Liking you, yet saying nothing.}
\pline{Ngày thi sợ cách xa}{Fearing distance on test day.}
\pline{Chúc đôi câu điểm tốt}{Wishing good grades for you.}
\pline{Chôn giấu mộng mây sa}{Burying dreams in clouds.}
\end{poembox}

\begin{poembox}{Bài 36}{Dúi kín kẹo vào hộc bàn của crush với hy vọng nhỏ nhoi.}
\pline{Thích mà chẳng nói ra}{Liking you, yet saying nothing.}
\pline{Lén mua kẹo chanh trà}{Secretly bought lime candy.}
\pline{Đặt nhanh trong hộc sách}{Put it fast in the desk.}
\pline{Giữ kín mãi đây mà}{Keeping the secret always.}
\end{poembox}

\begin{poembox}{Bài 37}{Một nụ cười khẽ nhoẻn đã in sâu trong ký ức trinh nguyên.}
\pline{Thích mà chẳng nói ra}{Liking you, yet saying nothing.}
\pline{Dù cho chớp mắt qua}{Even in a mere blink.}
\pline{Nhưng nụ cười năm ấy}{But the smile of that year.}
\pline{Vẫn sáng tựa sao sa}{Still shines like falling stars.}
\end{poembox}

\begin{poembox}{Bài 38}{Dịp chụp kỷ yếu đành đứng nép bên cạnh mà không dám ngỏ.}
\pline{Thích mà chẳng nói ra}{Liking you, yet saying nothing.}
\pline{Đành cam đứng phía xa}{Accepting to stand far.}
\pline{Chụp chung bao ảnh lớp}{Taking class pics together.}
\pline{Chỉ ngắm bóng ngọc ngà}{Only gazing at the fine shape.}
\end{poembox}

\begin{poembox}{Bài 39}{Cuốn sổ lưu bút lưu giữ những điều tiếc nuối chưa từng nói.}
\pline{Thích mà chẳng nói ra}{Liking you, yet saying nothing.}
\pline{Viết lưu bút giấy hoa}{Writing in floral yearbook.}
\pline{Bao điều mong muốn kể}{Many things I wished to tell.}
\pline{Gom lại một câu chào}{Gathered into one hello.}
\end{poembox}

\begin{poembox}{Bài 40}{Tình yêu tuổi học trò luôn rực rỡ và mong manh nhất.}
\pline{Thích mà chẳng nói ra}{Liking you, yet saying nothing.}
\pline{Đẹp như ánh tuyết pha}{Lovely like snowy light.}
\pline{Góc sân trường thầm lặng}{Quiet corner of the yard.}
\pline{Giữ mãi một tình ca}{Keeping a love song forever.}
\end{poembox}
""",
    "ch05-ban-cung-ban.tex": r"""\chapter{Bạn Cùng Bàn Năm Ấy}
\chapterintro{Góc kỷ niệm bàn bên}{Người bạn ngồi chung dãy kỷ niệm, cùng chia nhau vạch phấn giới tuyến, hay bảo bọc những trò ma ranh.}

\begin{poembox}{Bài 41}{Hương dầu gội thoang thoảng của bạn nữ cứ làm tâm trí nam sinh xáo trộn.}
\pline{Bạn cùng bàn năm ấy}{That deskmate of those years,}
\pline{Hay nghiêng tóc che tay}{Often tilted hair over hands,}
\pline{Mùi hương thơm bay nhẹ}{Fragrance drifted softly by,}
\pline{Trôi suốt tháng năm dài}{Flowing through the long months.}
\end{poembox}

\begin{poembox}{Bài 42}{Đôi đũa lệch đôi khi lại chí chóe chỉ vì cuốn vở xấu đẹp.}
\pline{Bạn cùng bàn năm ấy}{That deskmate of those years,}
\pline{Mượn gôm chép bài sai}{Borrowed eraser for wrong notes,}
\pline{Cãi nhau chê chữ xấu}{Argued mocking ugly writing,}
\pline{Lườm nguýt hết một ngày}{Glared through the entire day.}
\end{poembox}

\begin{poembox}{Bài 43}{Khoảnh khắc mùa hè oai ả, chia nhau chút gió quạt mỏng manh.}
\pline{Bạn cùng bàn năm ấy}{That deskmate of those years,}
\pline{Che chung cái áo quài}{Shared a single strapped shirt,}
\pline{Trưa hè oi bức quá}{Summer noon was too hot,}
\pline{Quạt giấy mát hai vai}{Paper fan cooled both shoulders.}
\end{poembox}

\begin{poembox}{Bài 44}{Giây phút nghĩa khí khi hỗ trợ bạn đứng bảng quên bài.}
\pline{Bạn cùng bàn năm ấy}{That deskmate of those years,}
\pline{Lên bảng đứng khoanh tay}{Stood at board with folded arms,}
\pline{Quay nhìn chờ nhắc nhở}{Turned to look waiting for hints,}
\pline{Tôi nhắc gật đầu thay}{I whispered, nodding instead.}
\end{poembox}

\begin{poembox}{Bài 45}{Giọt nước mắt của cô bé yếu đuối và chiếc khăn tay vụng về.}
\pline{Bạn cùng bàn năm ấy}{That deskmate of those years,}
\pline{Khóc nhè mắt sưng mày}{Cried till eyes and brows swelled,}
\pline{Tôi đưa tờ khăn mỏng}{I handed a thin tissue,}
\pline{Lau hết lệ sầu phai}{Wiping fading sorrow tears.}
\end{poembox}

\begin{poembox}{Bài 46}{Nhường nhịn nhau ngay cả khi phân công trực nhật nặng nhọc.}
\pline{Bạn cùng bàn năm ấy}{That deskmate of those years,}
\pline{Lười bôi bảng nhăn mày}{Lazy cleaning board, frowned.}
\pline{Tôi cầm bao giẻ sạch}{I held a clean rag tight,}
\pline{Chùi vội phấn trắng bay}{Hurriedly wiped flying chalk.}
\end{poembox}

\begin{poembox}{Bài 47}{Cái bánh bẻ đôi chan chứa hương vị đoàn kết, đậm đà tuổi thơ.}
\pline{Bạn cùng bàn năm ấy}{That deskmate of those years,}
\pline{Ăn chia nửa bánh này}{Ate and shared half this cake,}
\pline{Ngọt bùi thơm lớp học}{Sweet flavor in the room,}
\pline{Đầy tuổi trẻ ngây ngây}{Filled with innocent youth.}
\end{poembox}

\begin{poembox}{Bài 48}{Người làm bia đỡ đạn mỗi khi bạn mệt lả và ngủ thiếp đi.}
\pline{Bạn cùng bàn năm ấy}{That deskmate of those years,}
\pline{Ngủ quên tiết học dài}{Slept through the long lesson,}
\pline{Tôi làm bia đỡ đạn}{I acted as a shield,}
\pline{Che chắn khỏi thầy la}{Protecting from teacher's scolding.}
\end{poembox}

\begin{poembox}{Bài 49}{Sự im lặng ngậm ngùi lúc hoa phượng rơi giăng lối lúc xa nhau.}
\pline{Bạn cùng bàn năm ấy}{That deskmate of those years,}
\pline{Ngày chia cách chia tay}{On the day of farewell break,}
\pline{Mắt đỏ hoen không nói}{Muted with teary red eyes,}
\pline{In đậm dấu chân mai}{Imprinting footprints of tomorrow.}
\end{poembox}

\begin{poembox}{Bài 50}{Phút nhìn lại quãng thời thanh xuân, chiếc bàn rỗng không chỉ còn ký ức.}
\pline{Bạn cùng bàn năm ấy}{That deskmate of those years,}
\pline{Về đâu phía tương lai}{Wherever the future leads,}
\pline{Xin nhớ bàn hai đứa}{Please recall our shared desk,}
\pline{Lưu bóng khắc chưa phai}{Keeping shadows unfaded.}
\end{poembox}
""",
    "ch06-tan-hoc-doi.tex": r"""\chapter{Tan Học Đợi Nhau Về}
\chapterintro{Đường về chung đôi}{Hình ảnh xe đạp sóng đôi, rảo bước bên nhau dưới hoàng hôn tuổi trẻ - lãng mạn vô cùng tận.}

\begin{poembox}{Bài 51}{Tiếng ve trưa rộn rã kéo hai bóng xe chạy dọc trên triền đê.}
\pline{Tan học đợi nhau về}{After class, waiting to go home,}
\pline{Đường xanh rợp nắng hè}{Green street under summer sun,}
\pline{Xe song quanh con phố}{Bicycles rode along the street,}
\pline{Gió gọi rộn trên đê}{Wind calling loud on the dike.}
\end{poembox}

\begin{poembox}{Bài 52}{Tiếng chuông trường vừa điểm, hấp tấp thu dọn đồ để chờ chung nhịp bước.}
\pline{Tan học đợi nhau về}{After class, waiting to go home,}
\pline{Chờ qua chuông báo lề}{Waiting past the warning bell,}
\pline{Bước nhanh nơi hàng cửa}{Fast steps by the row of doors,}
\pline{Sợ bỏ lỡ câu thề}{Afraid to miss the pledged word.}
\end{poembox}

\begin{poembox}{Bài 53}{Có những khoảng lặng vô hình giữa lúc sóng vai mà nói lên vạn điều.}
\pline{Tan học đợi nhau về}{After class, waiting to go home,}
\pline{Nhìn nhau chẳng dám chê}{Looking, not daring to mock,}
\pline{Lặng im đi một đoạn}{Walking a stretch in silence,}
\pline{Mộng tưởng hóa si mê}{Fantasies turned to passion.}
\end{poembox}

\begin{poembox}{Bài 54}{Chia sẻ tài năng ca hát trên đường rảo bước tự do bung tỏa cảm xúc.}
\pline{Tan học đợi nhau về}{After class, waiting to go home,}
\pline{Bạn khen tiếng hát thề}{You praised my singing vow,}
\pline{Tôi cười trong e lệ}{I smiled in full shyness,}
\pline{Lòng rực ánh say mê}{Heart glowing with fervent joy.}
\end{poembox}

\begin{poembox}{Bài 55}{Kỷ niệm trú tạm dưới mái hiên lúc gặp cơn giông đầu hạ cớ sao thật đẹp.}
\pline{Tan học đợi nhau về}{After class, waiting to go home,}
\pline{Mưa bay ướt góc lề}{Flying rain wetted the curb,}
\pline{Nép hiên nhà trú tạm}{Sheltering at a porch,}
\pline{Nghe giọt nước lê thê}{Hearing drops trickling down.}
\end{poembox}

\begin{poembox}{Bài 56}{Cánh phượng vương làm quãng đường ngắn lại, chia ly kéo tới gần hơn.}
\pline{Tan học đợi nhau về}{After class, waiting to go home,}
\pline{Phượng rơi đỏ lối quê}{Flamboyant fell red on town paths,}
\pline{Tiếc thời gian ngắn quá}{Regretting time overly short,}
\pline{Đâu thỏa hết đam mê}{Could not fulfill all passions.}
\end{poembox}

\begin{poembox}{Bài 57}{Nhân vật kể nhau nghe mọi muộn phiền giận hờn của một ngày đến lớp.}
\pline{Tan học đợi nhau về}{After class, waiting to go home,}
\pline{Lặng ôm cặp mải mê}{Quietly hugging bags, engrossed,}
\pline{Kể bao điều trên lớp}{Told many things in class,}
\pline{Chuyện cô mắng não nề}{Tales of teacher scolding sadly.}
\end{poembox}

\begin{poembox}{Bài 58}{Ly nước mát giải nhiệt ở ngã tư và tiếng pha lê cười khúc khích.}
\pline{Tan học đợi nhau về}{After class, waiting to go home,}
\pline{Trà chanh đá vỉa hè}{Iced lime tea on pavement,}
\pline{Ngồi bên chia ly nước}{Sat beside sharing a glass,}
\pline{Cười nói tiếng pha lê}{Laughed with a crystal tone.}
\end{poembox}

\begin{poembox}{Bài 59}{Nỗi lo đường xa mệt nhọc hoàn toàn bay biến khi song hành cùng "tri kỷ".}
\pline{Tan học đợi nhau về}{After class, waiting to go home,}
\pline{Đường xa chẳng não nề}{Long road isn't depressing,}
\pline{Bởi chung người bạn quý}{Due to sharing a dear friend,}
\pline{Rảo bước mãi không chê}{Striding endlessly, not complaining.}
\end{poembox}

\begin{poembox}{Bài 60}{Hoài niệm về dáng hình thân thuộc tan biến giữa một vùng đất mới.}
\pline{Tan học đợi nhau về}{After class, waiting to go home,}
\pline{Giờ như giấc ngủ mê}{Now it's like a deep sleep,}
\pline{Còn đâu ngày chung lối}{Where are those common paths,}
\pline{Ngơ ngẩn nhớ bến quê}{Blankly missing the hometown pier.}
\end{poembox}
"""
}

for fname, content in files.items():
    path = os.path.join(base_dir, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("GENERATED 6 CHAPTERS!")
