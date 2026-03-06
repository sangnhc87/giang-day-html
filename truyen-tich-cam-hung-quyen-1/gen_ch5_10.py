import os

ch5_content = r"""\chapter{Triết Lý Sống (Philosophy of Life)}

\begin{center}
  \textit{\color{truyenblue}``The unexamined life is not worth living.''}\\
  \textit{(Một cuộc đời không được soi xét thì không đáng sống.)}\\[4pt]
  \small\color{truyengold}--- Socrates ---
\end{center}

\ngancach

\section{The Cup of Tea (Tách Trà)}
\begin{truyen}{Triết Lý Sống}{Thiết Thực}
A wise man \textbf{pours} tea into a \textbf{cup} until it \textbf{overflows}. He says you must \textbf{empty} your mind to \textbf{learn} new things.

\textit{Một người thông thái rót trà vào tách cho đến khi tràn ra ngoài. Ông nói rằng bạn phải làm trống tâm trí của mình để học hỏi những điều mới.}

\begin{baihoc}
Hãy luôn giữ tinh thần học hỏi với một tâm trí cởi mở.
\end{baihoc}
\end{truyen}

\section{The Two Wolves (Hai Con Sói)}
\begin{truyen}{Triết Lý Sống}{Lựa Chọn}
An old man tells his \textbf{grandson} about two \textbf{wolves} fighting inside us: one is \textbf{good} and one is \textbf{bad}. The one you \textbf{feed} will \textbf{win}.

\textit{Một ông lão kể cho cháu trai nghe về hai con sói đang chiến đấu bên trong chúng ta: một con tốt và một con xấu. Con nào bạn nuôi dưỡng sẽ chiến thắng.}

\begin{baihoc}
Những gì bạn nuôi dưỡng trong tâm hồn sẽ định hình con người bạn.
\end{baihoc}
\end{truyen}

\section{The Heavy Glass (Ly Nước Nặng)}
\begin{truyen}{Triết Lý Sống}{Buông Bỏ}
A teacher \textbf{holds} a \textbf{glass} of water. She says the \textbf{weight} depends on how \textbf{long} you hold it.

\textit{Một giáo viên cầm một ly nước. Cô nói rằng trọng lượng phụ thuộc vào việc bạn cầm nó bao lâu.}

\begin{baihoc}
Đừng giữ những muộn phiền quá lâu, hãy học cách buông bỏ để thấy nhẹ nhõm hơn.
\end{baihoc}
\end{truyen}

\section{The Mirror in the Room (Tấm Gương)}
\begin{truyen}{Triết Lý Sống}{Phán Xét}
A man \textbf{looks} in a \textbf{mirror} and sees his \textbf{flaws}. He realizes he must \textbf{fix} himself before \textbf{judging} others.

\textit{Một người đàn ông nhìn vào gương và thấy những khuyết điểm của mình. Anh nhận ra mình phải sửa bản thân trước khi phán xét người khác.}

\begin{baihoc}
Hãy nhìn nhận lại chính mình trước khi chỉ trích người khác.
\end{baihoc}
\end{truyen}

\section{The Broken Vase (Chiếc Bình Vỡ)}
\begin{truyen}{Triết Lý Sống}{Tổn Thương}
A \textbf{beautiful} vase is \textbf{broken}. An artist \textbf{repairs} it with \textbf{gold}, making it more \textbf{valuable} than before.

\textit{Một chiếc bình đẹp bị vỡ. Một nghệ nhân sửa nó bằng vàng, làm cho nó có giá trị hơn trước.}

\begin{baihoc}
Những khó khăn và tổn thương có thể làm cho chúng ta trở nên mạnh mẽ và đáng giá hơn.
\end{baihoc}
\end{truyen}

\section{The Blind Men and the Elephant (Thầy Bói Xem Voi)}
\begin{truyen}{Triết Lý Sống}{Góc Nhìn}
Six \textbf{blind} men \textbf{touch} an elephant. Each thinks it is \textbf{something} else. They \textbf{need} all parts to know the \textbf{truth}.

\textit{Sáu người mù sờ một con voi. Mỗi người nghĩ nó là một thứ khác. Họ cần tất cả các phần để biết sự thật.}

\begin{baihoc}
Mỗi người đều có một góc nhìn riêng, hãy lắng nghe để hiểu được bức tranh toàn cảnh.
\end{baihoc}
\end{truyen}

\section{The Footprints in the Sand (Dấu Chân Trên Cát)}
\begin{truyen}{Triết Lý Sống}{Khó Khăn}
A man \textbf{walks} on the \textbf{beach} and looks back. He sees that in \textbf{hard} times, there is only \textbf{one} set of footprints.

\textit{Một người đàn ông đi dạo trên bãi biển và nhìn lại. Anh thấy rằng trong những lúc khó khăn, chỉ có một hàng dấu chân.}

\begin{baihoc}
Trong những lúc khó khăn nhất, đôi khi bạn cần tự bước đi bằng chính đôi chân của mình.
\end{baihoc}
\end{truyen}

\section{The Empty Boat (Chiếc Thuyền Trống)}
\begin{truyen}{Triết Lý Sống}{Bình Yên}
A man gets \textbf{angry} when a \textbf{boat} hits his. When he sees it is \textbf{empty}, his \textbf{anger} goes \textbf{away}.

\textit{Một người đàn ông tức giận khi một chiếc thuyền đâm vào thuyền của mình. Khi anh thấy nó trống rỗng, cơn giận của anh biến mất.}

\begin{baihoc}
Đừng lãng phí năng lượng vào sự vung vãi vô tình của cuộc đời, hãy giữ tâm hồn bình yên.
\end{baihoc}
\end{truyen}

\section{The Three Questions (Ba Câu Hỏi)}
\begin{truyen}{Triết Lý Sống}{Hiện Tại}
A king \textbf{asks} three \textbf{questions} to find happiness. He \textbf{learns} the most \textbf{important} time is \textbf{now}.

\textit{Một vị vua hỏi ba câu hỏi để tìm hạnh phúc. Ông học được rằng thời điểm quan trọng nhất là hiện tại.}

\begin{baihoc}
Hãy sống trọn vẹn ở hiện tại để tìm thấy hạnh phúc thực sự.
\end{baihoc}
\end{truyen}

\section{The River and the Rock (Sông Và Đá)}
\begin{truyen}{Triết Lý Sống}{Kiên Trì}
A \textbf{river} hits a \textbf{rock}. Over \textbf{time}, the water \textbf{cuts} through the rock with \textbf{persistence}.

\textit{Một con sông đập vào một hòn đá. Qua thời gian, dòng nước xuyên qua hòn đá bằng sự kiên trì.}

\begin{baihoc}
Sự kiên trì và bền bỉ có thể vượt qua mọi chướng ngại vật cứng rắn nhất.
\end{baihoc}
\end{truyen}
"""

ch6_content = r"""\chapter{Tình Bạn \& Nghĩa Khí (Friendship \& Loyalty)}

\begin{center}
  \textit{\color{truyenblue}``A friend in need is a friend indeed.''}\\
  \textit{(Bạn trong lúc hoạn nạn mới là bạn đích thực.)}
\end{center}

\ngancach

\section{The Shared Umbrella (Chiếc Ô Chung)}
\begin{truyen}{Tình Bạn}{Sẻ Chia}
Two \textbf{friends} walk in the \textbf{rain}. One has no \textbf{umbrella}. The other \textbf{shares} his, and they both get a little \textbf{wet}.

\textit{Hai người bạn đi dưới mưa. Một người không có ô. Người kia chia sẻ chiếc ô của mình, và cả hai đều bị ướt một chút.}

\begin{baihoc}
Tình bạn đích thực là sẵn sàng chia sẻ khó khăn cùng nhau.
\end{baihoc}
\end{truyen}

\section{The Silent Support (Sự Ủng Hộ Lặng Thầm)}
\begin{truyen}{Tình Bạn}{Cảm Thông}
A boy is \textbf{sad} and sits \textbf{alone}. His friend sits \textbf{quietly} next to him. Words are not \textbf{needed}.

\textit{Một cậu bé buồn bã và ngồi một mình. Bác bạn cậu ngồi lặng lẽ bên cạnh. Không cần đến lời nói.}

\begin{baihoc}
Đôi khi, sự hiện diện lặng thầm còn quý giá hơn ngàn lời an ủi.
\end{baihoc}
\end{truyen}

\section{The Broken Pencil (Chiếc Bút Chì Gãy)}
\begin{truyen}{Tình Bạn}{Giúp Đỡ}
A student \textbf{breaks} his \textbf{pencil} before a \textbf{test}. His \textbf{classmate} snaps his own pencil in \textbf{half} to share.

\textit{Một học sinh làm gãy bút chì trước giờ kiểm tra. Bạn cùng lớp của cậu bẻ đôi chiếc bút chì của mình để chia sẻ.}

\begin{baihoc}
Một hành động nhỏ của sự sẻ chia có thể mang lại ý nghĩa lớn lao.
\end{baihoc}
\end{truyen}

\section{The True Winner (Ngôi Vị Đích Thực)}
\begin{truyen}{Tình Bạn}{Đồng Hành}
Two girls \textbf{run} in a \textbf{race}. One falls down. The other \textbf{stops}, helps her up, and they cross the \textbf{finish} line together.

\textit{Hai cô gái chạy trong một cuộc đua. Một người bị ngã. Người kia dừng lại, giúp cô ấy đứng lên, và họ cùng nhau vượt qua vạch đích.}

\begin{baihoc}
Chiến thắng đích thực không phải là về đích đầu tiên, mà là cùng nhau vượt qua thử thách.
\end{baihoc}
\end{truyen}

\section{The Lost Dog (Chú Chó Bị Lạc)}
\begin{truyen}{Tình Bạn}{Quan Tâm}
A boy \textbf{loses} his dog. All his \textbf{friends} spend the whole \textbf{day} searching the \textbf{neighborhood} until they find him.

\textit{Một cậu bé bị mất con chó của mình. Tất cả bạn bè của cậu dành cả ngày tìm kiếm khắp khu phố cho đến khi họ tìm thấy nó.}

\begin{baihoc}
Những người bạn thực sự sẽ luôn sát cánh bên bạn trong những lúc hoạn nạn.
\end{baihoc}
\end{truyen}

\section{The Secret Keeper (Người Giữ Bí Mật)}
\begin{truyen}{Tình Bạn}{Tin Tưởng}
A girl \textbf{tells} her friend a \textbf{secret}. Even when they are \textbf{mad} at each other, the secret is never \textbf{told}.

\textit{Một cô gái kể cho bạn bè một bí mật. Ngay cả khi họ giận nhau, bí mật đó không bao giờ được tiết lộ.}

\begin{baihoc}
Sự tin tưởng và tôn trọng là nền tảng của một tình bạn lâu bền.
\end{baihoc}
\end{truyen}

\section{The Heavy Books (Những Cuốn Sách Nặng)}
\begin{truyen}{Tình Bạn}{Sẵn Sàng}
A boy \textbf{drops} his heavy \textbf{books}. Everyone \textbf{laughs}, except one \textbf{friend} who helps him \textbf{pick} them up.

\textit{Một cậu bé làm rơi những cuốn sách nặng của mình. Mọi người đều cười, ngoại trừ một người bạn giúp cậu nhặt chúng lên.}

\begin{baihoc}
Một người bạn tốt là người giang tay giúp đỡ khi người khác quay lưng đi.
\end{baihoc}
\end{truyen}

\section{The Honest Friend (Người Bạn Trung Thực)}
\begin{truyen}{Tình Bạn}{Chân Thành}
A boy \textbf{sings} badly on \textbf{stage}. His friend \textbf{tells} him the \textbf{truth} gently, so he can \textbf{practice} more.

\textit{Một cậu bé hát dở trên sân khấu. Bạn của cậu nhẹ nhàng nói sự thật, để cậu có thể luyện tập thêm.}

\begin{baihoc}
Lời nói thật lòng dù khó nghe cũng tốt hơn những lời nịnh bợ giả dối.
\end{baihoc}
\end{truyen}

\section{The Long Distance (Khoảng Cách)}
\begin{truyen}{Tình Bạn}{Gắn Kết}
Two friends move to \textbf{different} cities. They \textbf{write} letters \textbf{every} month to \textbf{keep} their friendship strong.

\textit{Hai người bạn chuyển đến các thành phố khác nhau. Họ viết thư mỗi tháng để giữ cho tình bạn của họ bền chặt.}

\begin{baihoc}
Khoảng cách địa lý không thể chia cắt được những tâm hồn thực sự gắn kết.
\end{baihoc}
\end{truyen}

\section{The Last Slice (Lát Bánh Cuối Cùng)}
\begin{truyen}{Tình Bạn}{Nhường Nhịn}
There is only one \textbf{slice} of pizza \textbf{left}. Two hungry \textbf{friends} insist the \textbf{other} should \textbf{eat} it.

\textit{Chỉ còn lại một lát bánh pizza. Hai người bạn đang đói cứ khăng khăng người kia nên ăn nó.}

\begin{baihoc}
Sự nhường nhịn và quan tâm là biểu hiện đẹp nhất của tình bạn chân thành.
\end{baihoc}
\end{truyen}
"""

ch7_content = r"""\chapter{Gia Đình \& Tình Thương (Family \& Love)}

\begin{center}
  \textit{\color{truyenblue}``Family is not an important thing. It's everything.''}\\
  \textit{(Gia đình không phải là một điều quan trọng. Đó là tất cả mọi thứ.)}
\end{center}

\ngancach

\section{The Warm Dinner (Bữa Tối Ấm Áp)}
\begin{truyen}{Gia Đình}{Gắn Kết}
A father works \textbf{late}. But he always \textbf{makes} time to eat \textbf{dinner} with his \textbf{family} every night.

\textit{Một người cha làm việc muộn. Nhưng ông luôn dành thời gian ăn tối cùng gia đình mỗi tối.}

\begin{baihoc}
Bữa cơm gia đình là khoảnh khắc gắn kết tuyệt vời nhất sau một ngày dài.
\end{baihoc}
\end{truyen}

\section{The Old Blanket (Chiếc Chăn Cũ)}
\begin{truyen}{Gia Đình}{Ấm Áp}
A grandmother \textbf{knits} a blanket for her \textbf{grandson}. He \textbf{keeps} it on his bed, feeling her \textbf{love} every winter.

\textit{Một người bà đan một chiếc chăn cho cháu trai. Cậu giữ nó trên giường, cảm nhận tình yêu của bà mỗi mùa đông.}

\begin{baihoc}
Tình yêu thương gia đình mang lại sự ấm áp xua tan mọi giá lạnh.
\end{baihoc}
\end{truyen}

\section{The Broken Window (Cửa Sổ Vỡ)}
\begin{truyen}{Gia Đình}{Bao Dung}
A boy \textbf{breaks} a window. He is \textbf{scared}, but his mother \textbf{hugs} him first before \textbf{asking} what happened.

\textit{Một cậu bé làm vỡ cửa sổ. Cậu rất sợ, nhưng mẹ cậu ôm cậu trước khi hỏi chuyện gì đã xảy ra.}

\begin{baihoc}
Sự tha thứ và thấu hiểu luôn là sợi dây bền chặt của tình thân.
\end{baihoc}
\end{truyen}

\section{The Quiet Sacrifice (Sự Hy Sinh Lặng Thầm)}
\begin{truyen}{Gia Đình}{Tình Cha}
A father eats the \textbf{burnt} pieces of \textbf{toast} so his children can have the \textbf{good} ones without \textbf{knowing}.

\textit{Một người cha ăn những miếng bánh mì nướng bị cháy để các con có được những miếng ngon mà không hay biết.}

\begin{baihoc}
Tình yêu của cha mẹ thường ẩn chứa trong những hy sinh thầm lặng.
\end{baihoc}
\end{truyen}

\section{The First Bicycle (Chiếc Xe Đạp Đầu Tiên)}
\begin{truyen}{Gia Đình}{Che Chở}
A mother \textbf{runs} behind her daughter's \textbf{bicycle}, holding it \textbf{steady} until the girl can ride \textbf{alone}.

\textit{Một người mẹ chạy sau xe đạp của con gái, giữ nó thăng bằng cho đến khi cô bé có thể tự đi một mình.}

\begin{baihoc}
Gia đình luôn là chỗ dựa vững chắc nâng bước ta trên đường đời.
\end{baihoc}
\end{truyen}

\section{The Wooden Bowl (Chiếc Bát Gỗ)}
\begin{truyen}{Gia Đình}{Gương Mẫu}
An old man \textbf{drops} his food. His son gives him a \textbf{wooden} bowl. The grandson says he will do the \textbf{same} for his father. 

\textit{Một cụ ông làm rơi thức ăn. Con trai đưa cho ông một chiếc bát gỗ. Đứa cháu trai nói rằng cậu cũng sẽ làm như vậy với cha mình.}

\begin{baihoc}
Cách bạn đối xử với cha mẹ hôm nay là tấm gương cho con cái bạn ngày mai.
\end{baihoc}
\end{truyen}

\section{The Rainy Day (Ngày Mưa)}
\begin{truyen}{Gia Đình}{Niềm Vui}
It is \textbf{raining} outside. The family plays \textbf{games} inside and realizes they \textbf{do not} need sunshine to be \textbf{happy}.

\textit{Trời đang mưa bên ngoài. Cả gia đình chơi trò chơi trong nhà và nhận ra họ không cần ánh nắng mặt trời để hạnh phúc.}

\begin{baihoc}
Hạnh phúc gia đình đến từ những khoảnh khắc đơn giản bên nhau, dù ngoài kia có giông bão.
\end{baihoc}
\end{truyen}

\section{The Forgiving Brother (Khóa Chặt Căm Hờn)}
\begin{truyen}{Gia Đình}{Tình Anh Em}
Two brothers \textbf{fight} over a toy. The older brother \textbf{gives} it up, showing that his \textbf{brother} is more important.

\textit{Hai anh em tranh giành một món đồ chơi. Người anh nhường nó, cho thấy em trai mình quan trọng hơn.}

\begin{baihoc}
Trong gia đình, tình yêu thương luôn chiến thắng mọi sự nhỏ nhen ích kỷ.
\end{baihoc}
\end{truyen}

\section{The Handprint (Dấu Bàn Tay)}
\begin{truyen}{Gia Đình}{Kỷ Niệm}
A boy \textbf{puts} a messy \textbf{handprint} on the wall. His parents \textbf{frame} it instead of \textbf{cleaning} it.

\textit{Một cậu bé in một vết tay bẩn lên tường. Bố mẹ cậu đóng khung nó thay vì lau sạch.}

\begin{baihoc}
Những dấu vết tuổi thơ của con cái là tài sản quý giá nhất của cha mẹ.
\end{baihoc}
\end{truyen}

\section{The Evening Walk (Chuyến Đi Dạo)}
\begin{truyen}{Gia Đình}{Bình Dị}
An old couple \textbf{walks} slowly in the \textbf{park}. They hold \textbf{hands}, talking about their \textbf{happy} life together.

\textit{Một cặp đôi già đi dạo chầm chậm trong công viên. Họ nắm tay nhau, nói về cuộc sống hạnh phúc cùng nhau.}

\begin{baihoc}
Tình nghĩa vợ chồng bền chặt là món quà đẹp nhất của thời gian.
\end{baihoc}
\end{truyen}
"""

ch8_content = r"""\chapter{Kiên Nhẫn \& Tự Lập (Patience \& Independence)}

\begin{center}
  \textit{\color{truyenblue}``Patience is bitter, but its fruit is sweet.''}\\
  \textit{(Kiên nhẫn là đắng cay, nhưng quả của nó lại ngọt ngào.)}
\end{center}

\ngancach

\section{The Bamboo Tree (Cây Tre Khổ Luyện)}
\begin{truyen}{Kiên Nhẫn}{Kiên Trì}
A farmer \textbf{waters} a bamboo seed for four \textbf{years} with no results. In the \textbf{fifth} year, it grows \textbf{quickly}.

\textit{Một người nông dân tưới nước cho một hạt tre trong bốn năm mà không có kết quả. Vào năm thứ năm, nó lớn lên nhanh chóng.}

\begin{baihoc}
Thành công cần rất nhiều thời gian chuẩn bị và kiên nhẫn tích lũy.
\end{baihoc}
\end{truyen}

\section{The Butterfly (Kén Bướm)}
\begin{truyen}{Kiên Nhẫn}{Trưởng Thành}
A boy \textbf{helps} a butterfly out of its cocoon. Because he didn't let it struggle, it could never \textbf{fly}.

\textit{Một cậu bé giúp một con bướm thoát ra khỏi kén. Bởi vì cậu không để nó tự vật lộn, nó không bao giờ có thể bay.}

\begin{baihoc}
Sự tự lập và những khó khăn rèn luyện đôi cánh để chúng ta có thể bay cao.
\end{baihoc}
\end{truyen}

\section{The Small Steps (Những Bước Đi Nhỏ)}
\begin{truyen}{Kiên Nhẫn}{Vững Vàng}
A turtle \textbf{walks} slowly but never \textbf{stops}. He reaches the \textbf{finish} line before the \textbf{sleeping} rabbit.

\textit{Một con rùa đi chậm nhưng không bao giờ dừng lại. Cậu đến đích trước con thỏ đang ngủ.}

\begin{baihoc}
Kiên trì từng bước nhỏ chắc chắn sẽ dẫn bạn đến thành công cuối cùng.
\end{baihoc}
\end{truyen}

\section{Learning to Tie Shoes (Tự Buộc Dây Giày)}
\begin{truyen}{Tự Lập}{Thực Hành}
A girl \textbf{tries} to tie her shoes ten \textbf{times}. She fails, but on the \textbf{eleventh} try, she \textbf{succeeds} alone.

\textit{Một cô bé cố gắng buộc dây giày mười lần. Cô bé thất bại, nhưng trong lần thử thứ mười một, cô đã tự mình thành công.}

\begin{baihoc}
Đừng bỏ cuộc khi gặp thất bại, tự mình vượt qua sẽ mang lại sự tự tin.
\end{baihoc}
\end{truyen}

\section{The Puzzle (Khối Lắp Ráp)}
\begin{truyen}{Kiên Nhẫn}{Hoàn Thiện}
A boy spends \textbf{hours} on a large \textbf{puzzle}. He \textbf{patiently} finds each piece until the \textbf{picture} is clear.

\textit{Một cậu bé dành hàng giờ đồng hồ cho một trò xếp hình lớn. Cậu kiên nhẫn tìm từng mảnh ghép cho đến khi bức tranh rõ ràng.}

\begin{baihoc}
Mọi vấn đề phức tạp đều có thể được giải quyết nếu có đủ sự kiên nhẫn.
\end{baihoc}
\end{truyen}

\section{The Baker (Thợ Làm Bánh)}
\begin{truyen}{Tự Lập}{Cố Gắng}
A young baker \textbf{makes} many bad cakes. He \textbf{keeps} trying until he bakes the \textbf{perfect} bread by \textbf{himself}.

\textit{Một người thợ làm bánh trẻ tuổi làm ra nhiều cái bánh hỏng. Anh tiếp tục cố gắng cho đến khi tự mình nướng được chiếc bánh mì hoàn hảo.}

\begin{baihoc}
Thất bại là những bài học cần thiết để bạn tự mình vươn tới sự hoàn hảo.
\end{baihoc}
\end{truyen}

\section{The Heavy Rock (Tảng Đá Nặng)}
\begin{truyen}{Kiên Nhẫn}{Rèn Luyện}
A man \textbf{pushes} a rock every \textbf{day}. It doesn't move, but his \textbf{muscles} get very \textbf{strong}.

\textit{Một người đàn ông đẩy một tảng đá mỗi ngày. Nó không di chuyển, nhưng cơ bắp của ông trở nên rất khỏe.}

\begin{baihoc}
Đôi khi nỗ lực có vẻ không mang lại kết quả ngay, nhưng nó đang rèn luyện sức mạnh cho bạn.
\end{baihoc}
\end{truyen}

\section{The Alone Journey (Hành Trình Bắt Đầu)}
\begin{truyen}{Tự Lập}{Độc Lập}
A bird \textbf{leaves} the nest to find \textbf{food}. It is scared at \textbf{first}, but learns to \textbf{survive} in the wild.

\textit{Một chú chim rời tổ để tìm thức ăn. Lúc đầu nó sợ hãi, nhưng nó học được cách sinh tồn trong môi trường hoang dã.}

\begin{baihoc}
Bước ra khỏi vùng an toàn là con đường duy nhất để trưởng thành và tự lập.
\end{baihoc}
\end{truyen}

\section{The Dripping Water (Nước Chảy Đá Mòn)}
\begin{truyen}{Kiên Nhẫn}{Tích Lũy}
Water \textbf{drips} onto a hard \textbf{stone}. After many \textbf{years}, the water makes a deep \textbf{hole} in it.

\textit{Nước nhỏ giọt lên một hòn đá cứng. Sau nhiều năm, nước tạo ra một lỗ sâu trên đó.}

\begin{baihoc}
Sự kiên nhẫn và bền bỉ, dù nhỏ nhặt, có thể tạo nên những thay đổi lớn lao.
\end{baihoc}
\end{truyen}

\section{The First Job (Công Việc Đầu Tiên)}
\begin{truyen}{Tự Lập}{Giá Trị}
A teenager gets his \textbf{first} job. He earns his own \textbf{money} and learns the \textbf{value} of hard \textbf{work}.

\textit{Một thiếu niên có được công việc đầu tiên. Cậu tự kiếm tiền và học được giá trị của sự chăm chỉ.}

\begin{baihoc}
Tự kiếm ra đồng tiền sẽ giúp bạn trân trọng hơn giá trị của sức lao động.
\end{baihoc}
\end{truyen}
"""

ch9_content = r"""\chapter{Thế Giới Quanh Ta (The World Around Us)}

\begin{center}
  \textit{\color{truyenblue}``The world is hugged by the faithful arms of volunteers.''}\\
  \textit{(Thế giới được ôm trọn bởi những vòng tay chân thành của những tình nguyện viên.)}
\end{center}

\ngancach

\section{The Smiling Stranger (Người Lạ Mỉm Cười)}
\begin{truyen}{Thế Giới}{Lan Tỏa}
A person \textbf{smiles} at a sad man on the \textbf{bus}. The sad man \textbf{feels} better and smiles at \textbf{someone} else.

\textit{Một người mỉm cười với một người đàn ông buồn bã trên xe buýt. Người đàn ông buồn bã cảm thấy tốt hơn và mỉm cười với người khác.}

\begin{baihoc}
Một nụ cười thân thiện có thể lan tỏa niềm vui đến cả thế giới bao la.
\end{baihoc}
\end{truyen}

\section{The Clean Park (Công Viên Sạch Sẽ)}
\begin{truyen}{Thế Giới}{Môi Trường}
A boy \textbf{picks} up trash in the \textbf{park}. Soon, other people \textbf{join} him to make the \textbf{earth} clean.

\textit{Một cậu bé nhặt rác trong công viên. Chẳng bao lâu, những người khác tham gia cùng cậu để làm cho trái đất sạch sẽ.}

\begin{baihoc}
Những hành động tích cực nhỏ bé có thể truyền cảm hứng cho cộng đồng xung quanh.
\end{baihoc}
\end{truyen}

\section{The Lost Tourist (Du Khách Đi Lạc)}
\begin{truyen}{Thế Giới}{Tử Tế}
A tourist is \textbf{lost} in a new city. A local \textbf{person} draws a \textbf{map} and gives her \textbf{directions}.

\textit{Một du khách bị lạc trong một thành phố mới. Một người dân địa phương vẽ bản đồ và chỉ đường cho cô.}

\begin{baihoc}
Lòng tốt của người lạ làm cho thế giới xa lạ trở nên ấm áp và thân thuộc hơn.
\end{baihoc}
\end{truyen}

\section{Different Colors (Sắc Màu Khu Vườn)}
\begin{truyen}{Thế Giới}{Đa Dạng}
A garden has \textbf{many} different flowers. Red, yellow, and blue \textbf{flowers} make the \textbf{garden} beautiful \textbf{together}.

\textit{Một khu vườn có nhiều bông hoa khác nhau. Những bông hoa màu đỏ, vàng và xanh cùng nhau làm cho khu vườn thêm đẹp.}

\begin{baihoc}
Sự đa dạng và khác biệt chính là điều làm nên vẻ đẹp của thế giới này.
\end{baihoc}
\end{truyen}

\section{The Old Bridge (Cây Cầu Cũ)}
\begin{truyen}{Thế Giới}{Kết Nối}
An old \textbf{bridge} connects two \textbf{villages}. People \textbf{work} together to \textbf{repair} it so everyone can \textbf{cross}.

\textit{Một cây cầu cũ kết nối hai ngôi làng. Mọi người làm việc cùng nhau để sửa chữa nó để mọi người có thể đi qua.}

\begin{baihoc}
Sự kết nối và tinh thần hợp tác giúp vượt qua mọi trở ngại ngăn cách.
\end{baihoc}
\end{truyen}

\section{The Street Dog (Chú Chó Hoang)}
\begin{truyen}{Thế Giới}{Trắc Ẩn}
A \textbf{hungry} dog wanders the \textbf{street}. A shop owner \textbf{feeds} him every day, giving him a \textbf{safe} place.

\textit{Một con chó đói đi lang thang trên đường. Một chủ cửa hàng cho nó ăn mỗi ngày, tạo cho nó một nơi an toàn.}

\begin{baihoc}
Lòng trắc ẩn không chỉ dành cho con người mà còn cho muôn loài xung quanh ta.
\end{baihoc}
\end{truyen}

\section{The Rainstorm (Cơn Bão Phố)}
\begin{truyen}{Thế Giới}{Đoàn Kết}
A big \textbf{storm} hits the town. Neighbors \textbf{share} food and \textbf{shelter} until the \textbf{sun} comes out again.

\textit{Một cơn bão lớn tấn công thị trấn. Những người hàng xóm chia sẻ thức ăn và chỗ ở cho đến khi mặt trời ló rạng trở lại.}

\begin{baihoc}
Khó khăn chung là cơ hội để tình người tỏa sáng trong cộng đồng.
\end{baihoc}
\end{truyen}

\section{The New Student (Bạn Mới Chuyển Đến)}
\begin{truyen}{Thế Giới}{Giao Lưu}
A new student \textbf{comes} from a \textbf{far} country. The class \textbf{welcomes} him and learns about his \textbf{culture}.

\textit{Một học sinh mới đến từ một đất nước xa xôi. Lớp học chào đón cậu và học về văn hóa của cậu.}

\begin{baihoc}
Thế giới sẽ rộng lớn hơn khi ta mở lòng đón nhận những nền văn hóa mới.
\end{baihoc}
\end{truyen}

\section{The Night Sky (Bầu Trời Đêm)}
\begin{truyen}{Thế Giới}{Suy Ngẫm}
A girl looks at the \textbf{stars} above. She realizes how \textbf{small} she is, but how \textbf{beautiful} the universe is.

\textit{Một cô gái nhìn những vì sao trên cao. Cô nhận ra mình nhỏ bé thế nào, nhưng vũ trụ lại tươi đẹp ra sao.}

\begin{baihoc}
Hãy nhìn ra thế giới rộng lớn để thấy mình cần phải học hỏi và khiêm tốn hơn.
\end{baihoc}
\end{truyen}

\section{The Quiet Morning (Buổi Sáng Yên Tĩnh)}
\begin{truyen}{Thế Giới}{Yên Bình}
A man \textbf{wakes} up early to watch the \textbf{sunrise}. The world is \textbf{peaceful} before the busy \textbf{day} begins.

\textit{Một người đàn ông thức dậy sớm để ngắm bình minh. Thế giới thật yên bình trước khi một ngày bận rộn bắt đầu.}

\begin{baihoc}
Sự bình yên thực sự của thế giới luôn hiện diện, nếu ta biết dừng lại và cảm nhận.
\end{baihoc}
\end{truyen}
"""

ch10_content = r"""\chapter{Tự Nhiên \& Bài Học (Nature's Lessons)}

\begin{center}
  \textit{\color{truyenblue}``Look deep into nature, and then you will understand everything better.''}\\
  \textit{(Hãy nhìn sâu vào tự nhiên, rồi bạn sẽ thấu hiểu mọi thứ tốt hơn.)}\\
  \small\color{truyengold}--- Albert Einstein ---
\end{center}

\ngancach

\section{The Strong Tree (Cây Cổ Thụ)}
\begin{truyen}{Tự Nhiên}{Thích Nghi}
A tree \textbf{bends} during a heavy \textbf{wind}. An old tree doesn't bend and \textbf{breaks} in the \textbf{storm}.

\textit{Một cái cây uốn cong trong một trận gió lớn. Một cái cây cổ thụ không uốn cong và gãy trong cơn bão.}

\begin{baihoc}
Sự mềm dỏng và linh hoạt giúp chúng ta sống sót qua những cơn bão cuộc đời.
\end{baihoc}
\end{truyen}

\section{The Ant's Winter (Mùa Đông Của Kiến)}
\begin{truyen}{Tự Nhiên}{Chuẩn Bị}
An ant \textbf{collects} food all \textbf{summer}. When \textbf{winter} comes, he is safe and \textbf{warm} inside.

\textit{Một con kiến thu thập thức ăn suốt cả mùa hè. Khi mùa đông đến, nó được an toàn và ấm áp bên trong.}

\begin{baihoc}
Sự chuẩn bị kỹ lưỡng từ hôm nay sẽ mang lại bình an cho ngày mai.
\end{baihoc}
\end{truyen}

\section{The Sun and Wind (Mặt Trời Và Gió)}
\begin{truyen}{Tự Nhiên}{Khuyên Nhủ}
The wind tries to \textbf{force} a man's coat \textbf{off}. The sun simply \textbf{shines} warmly, and the man takes it off \textbf{himself}.

\textit{Gió cố gắng ép người đàn ông cởi áo khoác. Mặt trời chỉ việc tỏa nắng ấm áp, và người đàn ông tự cởi nó ra.}

\begin{baihoc}
Sự ấm áp và nhẹ nhàng luôn có sức thuyết phục mạnh hơn bạo lực.
\end{baihoc}
\end{truyen}

\section{The Flowing Water (Dòng Nước Chảy)}
\begin{truyen}{Tự Nhiên}{Linh Hoạt}
A river never \textbf{goes} backward. It flows \textbf{around} rocks and always \textbf{finds} its way to the \textbf{ocean}.

\textit{Một con sông không bao giờ chảy ngược. Nó chảy quanh những tảng đá và luôn tìm được đường ra đại dương.}

\begin{baihoc}
Hãy tiến về phía trước và linh hoạt tìm cách vượt qua chướng ngại vật như dòng nước.
\end{baihoc}
\end{truyen}

\section{The Falling Leaves (Lá Rơi Mùa Thu)}
\begin{truyen}{Tự Nhiên}{Buông Bỏ}
In \textbf{autumn}, a tree \textbf{drops} its old leaves. This \textbf{allows} new leaves to \textbf{grow} in the spring.

\textit{Vào mùa thu, một cái cây rụng những chiếc lá cũ. Điều này cho phép những chiếc lá mới phát triển vào mùa xuân.}

\begin{baihoc}
Đôi khi ta phải từ bỏ những điều cũ kỹ để đón nhận những cơ hội mới mẻ.
\end{baihoc}
\end{truyen}

\section{The Small Seed (Hạt Giống Nhỏ)}
\begin{truyen}{Tự Nhiên}{Tiềm Năng}
A tiny \textbf{seed} is buried in the \textbf{dark} dirt. With water and \textbf{sun}, it becomes a massive \textbf{tree}.

\textit{Một hạt giống nhỏ bé bị vùi lấp trong lớp đất tối tăm. Với nước và nắng trời, nó trở thành một cái cây khổng lồ.}

\begin{baihoc}
Những khởi đầu nhỏ bé vất vả nhất cũng có thể dẫn đến những thành tựu vĩ đại.
\end{baihoc}
\end{truyen}

\section{The Busy Bee (Ong Chăm Chỉ)}
\begin{truyen}{Tự Nhiên}{Cống Hiến}
A bee flies to \textbf{many} flowers. By taking \textbf{nectar}, it helps the flowers \textbf{grow} beautiful \textbf{fruits}.

\textit{Một con ong bay đến nhiều bông hoa. Bằng cách lấy mật, nó giúp hoa kết thành những trái ngọt.}

\begin{baihoc}
Làm việc chăm chỉ và mang lại giá trị cho người khác cũng là giúp chính mình phát triển.
\end{baihoc}
\end{truyen}

\section{The Changing Seasons (Bốn Mùa Trôi Qua)}
\begin{truyen}{Tự Nhiên}{Hy Vọng}
After a cold \textbf{winter}, spring always \textbf{returns}. Flowers \textbf{bloom} and birds sing \textbf{again}.

\textit{Sau một mùa đông lạnh lẽo, mùa xuân luôn trở lại. Hoa nở rộ và chim chóc hót vang lần nữa.}

\begin{baihoc}
Sau những thời kỳ khó khăn tăm tối nhất, hy vọng tươi sáng sẽ luôn quay trở lại.
\end{baihoc}
\end{truyen}

\section{The Quiet Mountain (Ngọn Núi Lặng Yên)}
\begin{truyen}{Tự Nhiên}{Bình Thản}
A \textbf{mountain} stands still through rain and \textbf{snow}. It does not \textbf{react}, but remains \textbf{strong}.

\textit{Một ngọn núi đứng yên qua mưa và tuyết. Nó không phản ứng, mà vẫn vô cùng vững chãi.}

\begin{baihoc}
Bình thản đối mặt với mọi giông bão là cách thể hiện bản lĩnh kiên cường nhất.
\end{baihoc}
\end{truyen}

\section{The Starfish (Sao Biển Về Bờ)}
\begin{truyen}{Tự Nhiên}{Chất Lượng}
A boy \textbf{throws} one starfish back into the \textbf{ocean}. He can't save \textbf{them} all, but he makes a \textbf{difference} to that one.

\textit{Một cậu bé ném một con sao biển trở lại đại dương. Cậu không thể cứu tất cả, nhưng cậu đã tạo ra sự khác biệt cho con sao biển đó.}

\begin{baihoc}
Dù không thể thay đổi cả thế giới, nhưng một hành động tốt nhỏ bé có ý nghĩa lớn với người nhận.
\end{baihoc}
\end{truyen}
"""

with open("chapters/ch05-triet-ly-song.tex", "w", encoding="utf-8") as f:
    f.write(ch5_content)
with open("chapters/ch06-tinh-ban-nghia-khi.tex", "w", encoding="utf-8") as f:
    f.write(ch6_content)
with open("chapters/ch07-gia-dinh-tinh-thuong.tex", "w", encoding="utf-8") as f:
    f.write(ch7_content)
with open("chapters/ch08-kien-nhan-tu-lap.tex", "w", encoding="utf-8") as f:
    f.write(ch8_content)
with open("chapters/ch09-the-gioi-quanh-ta.tex", "w", encoding="utf-8") as f:
    f.write(ch9_content)
with open("chapters/ch10-tu-nhien-bai-hoc.tex", "w", encoding="utf-8") as f:
    f.write(ch10_content)

print("Generated full chapters 5 to 10 directly in the truyen-tich-cam-hung/chapters directory.")
