#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sinh file chapters/loitua.tex và chapters/huong-dan.tex
cho tất cả 24 quyển trong bộ sách Truyện Tích Cảm Hứng Song Ngữ.
Đồng bộ cấu trúc theo chuẩn Quyển I.
"""

import os
import re

BASE = "/Users/admin/Giang-Day-html"

# Volumes that only have truyen + baihoc (no ghinhoanh / tuhocnhanh)
SIMPLE_VOLUMES = {3, 4, 5, 6, 7}

# Dữ liệu từng quyển: (tiêu đề VN, tiêu đề EN, chủ đề, câu mở tựa VN, câu mở tựa EN,
#   mô tả quyển VN, mô tả quyển EN, bài học VN, bài học EN, câu quote)
VOLUMES = {
    1: {
        "so":    "I",
        "title": "Điển Tích \\& Chuyện Kể Truyền Cảm Hứng",
        "title_en": "Inspiring Tales \\& Classic Stories",
        "chu_de": "lòng biết ơn, can đảm, tình bạn nghĩa khí",
        "mo_dau": (
            "Bộ sách này bắt đầu từ một buổi kể chuyện đơn giản trên lớp.",
            "This series began from a simple storytelling session in class.",
        ),
        "gioi_thieu": (
            "Quyển đầu tiên là lời chào của cả bộ sách. "
            "Những điển tích ở đây nói về lòng biết ơn, sự can đảm, "
            "tình bạn nghĩa khí và ý chí vươn lên. "
            "Mỗi câu chuyện kèm song ngữ Việt~-- Anh để người đọc vừa học ý, vừa học tiếng.",
            "The first volume is the greeting of the entire series. "
            "The stories here speak of gratitude, courage, loyal friendship, and the will to rise. "
            "Each story comes with bilingual Vietnamese~-- English so readers learn both meaning and language.",
        ),
        "bai_hoc": (
            "Những câu chuyện hay nhất không cần phải dài~--- "
            "chúng chỉ cần chạm đúng vào điều người ta đang cần nghe.",
            "The best stories do not need to be long~--- "
            "they only need to touch exactly what people need to hear.",
        ),
        "quote": "Mỗi câu chuyện là một hạt giống tốt gieo vào tâm trí.",
        "en_short": [
            "Good stories carry timeless lessons.",
            "Stories teach what lectures cannot.",
        ],
        "tu_hoc": [
            ("Điều gì trong quyển này khiến em suy nghĩ nhất?",
             "Which story in this volume made you think the most?"),
            ("Bài học nào em muốn áp dụng ngay hôm nay?",
             "Which lesson do you want to apply today?"),
            ("Nếu kể lại một câu chuyện cho người khác, em chọn câu nào?",
             "If you were to retell one story to others, which would you choose?"),
        ],
    },
    2: {
        "so":    "II",
        "title": "Điển Tích \\& Chuyện Kể: Đạo Làm Người",
        "title_en": "Tales of Character and Human Values",
        "chu_de": "đạo làm con, làm bạn, làm trò, làm thầy",
        "mo_dau": (
            "Đạo làm người không học một lần rồi thôi~--- "
            "nó cần được nhắc đi nhắc lại suốt đời.",
            "The way of being human is not learned once and forgotten~--- "
            "it needs to be revisited throughout life.",
        ),
        "gioi_thieu": (
            "Quyển hai của bộ sách tiếp tục hành trình đó. "
            "Những câu chuyện ở đây xoay quanh đạo làm con, làm bạn, "
            "làm trò, làm thầy, làm người trong đời. "
            "Mỗi bài học được đặt trong một tình huống quen thuộc "
            "để người đọc dễ liên hệ với cuộc sống thực của chính mình.",
            "The second volume continues that journey. "
            "The stories here revolve around being a good child, friend, student, "
            "teacher, and human being. "
            "Each lesson is placed in a familiar situation "
            "so readers can easily connect it to their own real lives.",
        ),
        "bai_hoc": (
            "Nhân cách không hình thành trong một ngày~--- "
            "nhưng mỗi ngày đều có thể là ngày bắt đầu.",
            "Character is not formed in a day~--- "
            "but every day can be the day it begins.",
        ),
        "quote": "Mỗi câu chuyện là một tấm gương~--- hãy nhìn vào để thấy mình.",
        "en_short": [
            "Good character is built one day at a time.",
            "The way we treat others reflects who we are.",
        ],
        "tu_hoc": [
            ("Trong các vai trò~--- con, bạn, trò, thầy~--- em đang làm tốt nhất ở vai nào?",
             "Among the roles~--- child, friend, student, teacher~--- which do you play best?"),
            ("Câu chuyện nào trong quyển này khiến em nhìn lại cách ứng xử của mình?",
             "Which story here made you reconsider how you treat others?"),
            ("Điều gì trong đạo làm người em muốn rèn luyện thêm?",
             "Which aspect of good character do you want to improve?"),
        ],
    },
    3: {
        "so":    "III",
        "title": "Điển Tích \\& Chuyện Kể: Thiên Nhiên Quanh Ta",
        "title_en": "Tales of Nature Around Us",
        "chu_de": "bài học từ thiên nhiên và muôn loài",
        "mo_dau": (
            "Thiên nhiên ngàn đời nay vẫn đang dạy ta~--- "
            "chỉ là ta hay quên lắng nghe.",
            "Nature has been teaching us for thousands of years~--- "
            "we simply often forget to listen.",
        ),
        "gioi_thieu": (
            "Quyển ba chọn góc nhìn từ thế giới tự nhiên: những loài vật nhỏ bé, "
            "những quy luật vũ trụ, những hiện tượng thường ngày. "
            "Tất cả đều có bài học ẩn bên trong. "
            "Học sinh đọc những chuyện này không chỉ để biết thêm về thiên nhiên, "
            "mà để nhìn lại bản thân mình qua tấm gương của muôn loài.",
            "The third volume chooses the perspective of the natural world: "
            "small creatures, universal laws, everyday phenomena. "
            "Each carries a hidden lesson. "
            "Readers study these stories not only to learn more about nature, "
            "but to see themselves through the mirror of all living things.",
        ),
        "bai_hoc": (
            "Người biết lắng nghe thiên nhiên là người biết lắng nghe chính mình.",
            "Those who know how to listen to nature know how to listen to themselves.",
        ),
        "quote": "Lắng nghe thiên nhiên, ta học được muôn điều.",
        "en_short": [
            "Nature is the oldest and wisest teacher.",
            "Every creature has a lesson to teach.",
        ],
        "tu_hoc": [
            ("Câu chuyện về loài vật nào trong quyển này em thấy gần với mình nhất?",
             "Which animal story in this volume felt most relatable to you?"),
            ("Thiên nhiên đang dạy gì cho em qua những điều em thấy hàng ngày?",
             "What is nature teaching you through what you see every day?"),
            ("Bài học từ thiên nhiên nào em muốn chia sẻ với bạn bè?",
             "Which lesson from nature do you want to share with friends?"),
        ],
    },
    4: {
        "so":    "IV",
        "title": "Điển Tích \\& Chuyện Kể: Triết Lý Nhân Sinh",
        "title_en": "Tales of Life Philosophy",
        "chu_de": "triết lý nhân sinh từ cổ chí kim",
        "mo_dau": (
            "Triết lý nhân sinh không chỉ là của các nhà triết học~--- "
            "nó ở ngay trong những chuyện đời thường.",
            "Life philosophy is not just for philosophers~--- "
            "it lives right inside everyday stories.",
        ),
        "gioi_thieu": (
            "Quyển bốn đưa người đọc đến với những tình huống quen thuộc từ cổ chí kim: "
            "một người thầy thay đổi học trò, một lời khuyên đúng lúc thay đổi số phận, "
            "một bài học từ thất bại mang lại thành công. "
            "Triết lý nhân sinh không phải để tranh luận~--- nó để sống. "
            "Mỗi câu chuyện trong quyển này là một minh chứng cho điều đó.",
            "Volume four takes the reader through familiar situations from ancient to modern times: "
            "a teacher changing a student, timely advice changing a fate, "
            "a lesson from failure leading to success. "
            "Life philosophy is not for debate~--- it is for living. "
            "Each story in this volume is evidence of that.",
        ),
        "bai_hoc": (
            "Người trí không chỉ học từ kinh nghiệm bản thân~--- "
            "mà còn học từ những câu chuyện đã xảy ra trước mình.",
            "The wise learn not only from their own experience~--- "
            "but also from stories that happened before them.",
        ),
        "quote": "Từ những câu chuyện xưa, ta tìm thấy chính mình.",
        "en_short": [
            "Ancient wisdom speaks to modern lives.",
            "Every story is a lesson waiting to be lived.",
        ],
        "tu_hoc": [
            ("Triết lý nhân sinh nào trong quyển này em thấy đúng nhất với cuộc sống hiện tại?",
             "Which life philosophy in this volume rings truest for your life right now?"),
            ("Câu chuyện nào thay đổi cách em nhìn một vấn đề?",
             "Which story changed the way you see a problem?"),
            ("Em học được gì từ những sai lầm và vấp ngã được kể trong quyển này?",
             "What did you learn from the failures and stumbles described in this volume?"),
        ],
    },
    5: {
        "so":    "V",
        "title": "Điển Tích \\& Chuyện Kể: Hai Mặt Của Một Đồng Xu",
        "title_en": "Two Sides of Every Coin",
        "chu_de": "tư duy biện chứng, âm dương, mâu thuẫn và cân bằng",
        "mo_dau": (
            "Không có điều gì là hoàn toàn tốt hay hoàn toàn xấu~--- "
            "điều quan trọng là ta nhìn nó từ góc nào.",
            "Nothing is entirely good or entirely bad~--- "
            "what matters is the angle from which we look at it.",
        ),
        "gioi_thieu": (
            "Quyển năm đặt ra câu hỏi về hai mặt của mọi thứ. "
            "Mỗi câu chuyện được cặp đôi với một câu chuyện đối lập~--- "
            "để người đọc thấy rằng sự thật thường nằm ở giữa, không phải ở một phía. "
            "Tư duy biện chứng không phải là kỹ năng của người lớn~--- "
            "ngay từ trong trường học, học sinh đã cần học nhìn vấn đề từ nhiều chiều.",
            "Volume five raises the question of the two sides of everything. "
            "Each story is paired with an opposing story~--- "
            "so readers see that the truth often lies in the middle, not on one side. "
            "Dialectical thinking is not just an adult skill~--- "
            "from school onwards, students need to learn to see problems from multiple angles.",
        ),
        "bai_hoc": (
            "Người khôn ngoan không chọn một mặt~--- "
            "họ hiểu cả hai và chọn điều cân bằng.",
            "The wise do not choose one side~--- "
            "they understand both and choose the balance.",
        ),
        "quote": "Nhìn được cả hai mặt~--- đó mới là cái nhìn trưởng thành.",
        "en_short": [
            "Every coin has two sides: look at both.",
            "Balance comes from understanding opposites.",
        ],
        "tu_hoc": [
            ("Câu chuyện nào trong quyển này khiến em thay đổi cách nhìn về một vấn đề?",
             "Which story here changed how you see a particular issue?"),
            ("Em thường nghiêng về phía nào khi xem xét một vấn đề? Lý do?",
             "Which side do you usually lean toward when evaluating a situation? Why?"),
            ("Tư duy biện chứng giúp ích gì cho em trong học tập và cuộc sống?",
             "How does seeing both sides help you in study and in life?"),
        ],
    },
    6: {
        "so":    "VI",
        "title": "Vòng Quay Cuộc Đời",
        "title_en": "The Cycle of Life",
        "chu_de": "nhân quả, bản sắc, buông bỏ và người thầy vô hình",
        "mo_dau": (
            "Cuộc đời có những quy luật riêng~--- "
            "ai hiểu sớm thì đỡ phải trả giá.",
            "Life has its own laws~--- "
            "those who understand them early pay fewer prices.",
        ),
        "gioi_thieu": (
            "Quyển sáu mang đến những câu chuyện về vòng quay của cuộc đời: "
            "nhân quả, bản sắc, buông bỏ và những người thầy vô hình "
            "xuất hiện đúng lúc ta cần. "
            "Đôi khi bài học quý nhất không đến từ lớp học, "
            "mà từ một người gặp ngẫu nhiên, một thất bại đúng lúc, "
            "một câu nói vô tình mà ta nhớ mãi.",
            "Volume six brings stories about the cycle of life: "
            "karma, identity, letting go, and the invisible teachers "
            "who appear exactly when we need them. "
            "Sometimes the most valuable lesson comes not from the classroom, "
            "but from a chance encounter, a timely failure, "
            "or a passing remark that stays with us forever.",
        ),
        "bai_hoc": (
            "Những gì ta gieo hôm nay sẽ là những gì ta gặt ngày mai~--- "
            "vòng quay không biết nói dối.",
            "What we sow today will be what we reap tomorrow~--- "
            "the cycle never lies.",
        ),
        "quote": "Hiểu vòng quay cuộc đời là bắt đầu sống có chủ đích.",
        "en_short": [
            "Life cycles come back around: plant wisely.",
            "The invisible teacher appears when you are ready.",
        ],
        "tu_hoc": [
            ("Em đã gặp một người thầy vô hình nào trong cuộc sống chưa? Đó là ai?",
             "Have you encountered an invisible teacher in life? Who was it?"),
            ("Điều gì bạn đang gieo hôm nay mà bạn muốn gặt trong tương lai?",
             "What are you planting today that you hope to harvest in the future?"),
            ("Buông bỏ điều gì khiến em thấy nhẹ lòng nhất?",
             "What is one thing you could let go of to feel lighter?"),
        ],
    },
    7: {
        "so":    "VII",
        "title": "Lời Dạy Của Bậc Hiền Nhân",
        "title_en": "Teachings of the Wise",
        "chu_de": "triết lý từ bậc thầy qua các thời đại Đông~-- Tây",
        "mo_dau": (
            "Những bậc hiền nhân không phải là những người không bao giờ sai~--- "
            "họ là những người học được từ sai lầm của mình và của người khác.",
            "The wise are not those who never make mistakes~--- "
            "they are those who learn from their own mistakes and others'.",
        ),
        "gioi_thieu": (
            "Quyển bảy tập hợp lời dạy từ nhiều bậc thầy qua các thời đại: "
            "triết gia Đông Tây, nhà giáo dục, người kinh doanh, "
            "người sống đến tuổi già với trí tuệ tinh tường. "
            "Những lời này không có tuổi~--- "
            "một câu từ Khổng Tử hay Seneca vẫn còn nguyên giá trị trong lớp học hôm nay.",
            "Volume seven gathers teachings from great teachers across the ages: "
            "Eastern and Western philosophers, educators, businesspeople, "
            "and those who lived to old age with clear wisdom. "
            "These words are timeless~--- "
            "a saying from Confucius or Seneca still holds full value in today's classroom.",
        ),
        "bai_hoc": (
            "Đọc lời của bậc hiền nhân không phải để thuộc lòng~--- "
            "mà để sống theo.",
            "Reading the words of the wise is not to memorize them~--- "
            "it is to live by them.",
        ),
        "quote": "Lời dạy của người xưa vẫn soi sáng những bước đi hôm nay.",
        "en_short": [
            "Wisdom from the past lights the path ahead.",
            "The greatest teachers speak across centuries.",
        ],
        "tu_hoc": [
            ("Lời dạy nào trong quyển này em muốn viết lên bảng lớp?",
             "Which teaching in this volume would you write on the classroom board?"),
            ("Những bậc hiền nhân Đông và Tây có điểm gì giống nhau trong lời dạy của họ?",
             "What do Eastern and Western wise teachers have in common in their teachings?"),
            ("Hôm nay em có thể áp dụng ngay một lời dạy nào từ quyển này không?",
             "Is there a teaching in this volume you can apply today?"),
        ],
    },
    8: {
        "so":    "VIII",
        "title": "Thô Nhưng Thật: Chuyện Học Sinh",
        "title_en": "Rough but Real: Student Stories",
        "chu_de": "điểm số, áp lực, so sánh, bắt nạt và học đường thật",
        "mo_dau": (
            "Những câu chuyện hay nhất về học sinh không phải là những câu chuyện ngọt ngào.",
            "The best stories about students are not the sweet ones.",
        ),
        "gioi_thieu": (
            "Quyển tám chọn những chuyện thô ráp, trực tiếp, đôi khi khó nghe. "
            "Về điểm số, về áp lực, về so sánh, về bắt nạt, về mạng xã hội, "
            "về việc chọn nghề và về nỗi sợ thất bại. "
            "Những chuyện đó không được làm đẹp lên~--- "
            "chúng được kể thật, vì thật mới chạm được vào người đọc.",
            "Volume eight chooses the rough, direct, sometimes hard-to-hear stories. "
            "About grades, pressure, comparison, bullying, social media, "
            "choosing a career, and the fear of failure. "
            "These stories are not made pretty~--- "
            "they are told truthfully, because truth is what reaches the reader.",
        ),
        "bai_hoc": (
            "Câu chuyện thật không cần phải đẹp~--- "
            "nó chỉ cần đủ dũng cảm để được kể.",
            "A true story does not need to be beautiful~--- "
            "it only needs the courage to be told.",
        ),
        "quote": "Thô nhưng thật còn hơn đẹp mà rỗng.",
        "en_short": [
            "Honesty in storytelling creates real connection.",
            "Real student life is rough, and that is okay.",
        ],
        "tu_hoc": [
            ("Câu chuyện nào trong quyển này khiến em cảm thấy mình được hiểu?",
             "Which story in this volume made you feel understood?"),
            ("Áp lực học đường nào em đang chịu mà chưa nói với ai?",
             "What school pressure are you carrying that you haven't shared with anyone?"),
            ("Nếu viết một câu chuyện học đường thật của mình, em sẽ kể chuyện gì?",
             "If you wrote one true story from your own school life, what would it be?"),
        ],
    },
    9: {
        "so":    "IX",
        "title": "Ra Đời Không Có Bản Nháp",
        "title_en": "No Draft for Real Life",
        "chu_de": "công việc đầu tiên, tiền đầu tiên, bị từ chối, sống xa nhà",
        "mo_dau": (
            "Ra đời không ai được phép thử trước rồi làm lại~--- "
            "đó chính là điều khiến những câu chuyện đầu đời đáng nhớ nhất.",
            "No one gets a practice run before real life~--- "
            "that is exactly what makes first-life stories the most memorable.",
        ),
        "gioi_thieu": (
            "Quyển chín dành cho những người đang đứng trước ngưỡng cửa cuộc đời: "
            "công việc đầu tiên, đồng tiền đầu tiên tự kiếm, lần đầu bị từ chối, "
            "lần đầu sống xa nhà, lần đầu phải tự quyết định tất cả. "
            "Không có bản nháp nào cho những khoảnh khắc đó~--- "
            "nhưng có những câu chuyện của người đi trước để ta học.",
            "Volume nine is for those standing at life's threshold: "
            "the first job, the first money earned, the first rejection, "
            "the first time living away from home, the first time deciding everything alone. "
            "There is no draft for those moments~--- "
            "but there are stories from those who went before us to learn from.",
        ),
        "bai_hoc": (
            "Không có bản nháp nào cho cuộc đời thật~--- "
            "nhưng những câu chuyện của người đi trước là bản hướng dẫn tốt nhất.",
            "There is no draft for real life~--- "
            "but stories from those who came before are the best guides.",
        ),
        "quote": "Ai đã từng vấp ngã mà đứng dậy được đều có chuyện đáng kể.",
        "en_short": [
            "Life has no rehearsal: show up fully.",
            "First experiences shape who we become.",
        ],
        "tu_hoc": [
            ("Khoảnh khắc nào trong cuộc đời em sắp bước vào mà em lo nhất?",
             "Which upcoming life moment worries you most?"),
            ("Câu chuyện nào trong quyển này giúp em chuẩn bị tâm lý tốt hơn?",
             "Which story here helped you mentally prepare for what's ahead?"),
            ("Em muốn hỏi người đi trước điều gì về cuộc sống sau khi ra trường?",
             "What would you ask someone ahead of you about life after graduation?"),
        ],
    },
    10: {
        "so":    "X",
        "title": "Những Ảo Tưởng Của Tuổi Trẻ",
        "title_en": "The Illusions of Youth",
        "chu_de": "nhận ra và điều chỉnh ảo tưởng trước khi đặt cược cả cuộc đời",
        "mo_dau": (
            "Ảo tưởng không phải điều xấu~--- "
            "nó là một phần của tuổi trẻ. "
            "Điều xấu là không nhận ra nó kịp.",
            "Illusions are not bad things~--- "
            "they are part of being young. "
            "What is bad is not recognizing them in time.",
        ),
        "gioi_thieu": (
            "Quyển mười đặt tên cho những ảo tưởng phổ biến nhất của tuổi trẻ: "
            "ảo tưởng về tài năng, về tình yêu, về thành công nhanh, "
            "về việc mình đặc biệt hơn người khác. "
            "Không nhằm dập tắt ước mơ~--- "
            "mà nhằm giúp người đọc nhìn thật hơn trước khi đặt cược cả cuộc đời.",
            "Volume ten names the most common illusions of youth: "
            "illusions about talent, love, fast success, "
            "and being more special than others. "
            "Not to crush dreams~--- "
            "but to help readers see more clearly before betting everything.",
        ),
        "bai_hoc": (
            "Nhận ra ảo tưởng của mình không phải là thất bại~--- "
            "đó là bước đầu tiên của sự trưởng thành.",
            "Recognizing your own illusions is not failure~--- "
            "it is the first step toward maturity.",
        ),
        "quote": "Thức tỉnh muộn còn hơn không bao giờ thức tỉnh.",
        "en_short": [
            "Seeing clearly is the beginning of growing up.",
            "Most illusions dissolve only under honest light.",
        ],
        "tu_hoc": [
            ("Em đang mang ảo tưởng nào mà chưa chịu nhìn nhận?",
             "What illusion are you holding onto without admitting it?"),
            ("Điều gì trong quyển này khiến em cảm thấy hơi khó chịu? Tại sao?",
             "What in this volume made you slightly uncomfortable? Why?"),
            ("Sau khi đọc quyển này, em sẽ thay đổi cách nhìn gì về bản thân?",
             "After reading this volume, what will you change about how you see yourself?"),
        ],
    },
    11: {
        "so":    "XI",
        "title": "Những Cái Bẫy Người Trẻ Tự Bước Vào",
        "title_en": "Traps Young People Set for Themselves",
        "chu_de": "tự mãn, cái tôi, so sánh, trì hoãn",
        "mo_dau": (
            "Hiểu tên của cái bẫy là cách đầu tiên để thoát khỏi nó.",
            "Knowing the name of the trap is the first step to escaping it.",
        ),
        "gioi_thieu": (
            "Quyển mười một đặt tên cho những cái bẫy mà người trẻ thường tự giăng: "
            "tự mãn, cái tôi quá lớn, so sánh thường xuyên, trì hoãn mãn tính. "
            "Không ai miễn nhiễm~--- "
            "nhưng ai đọc quyển này với tâm thế thành thật sẽ thấy mình "
            "trong ít nhất một câu chuyện.",
            "Volume eleven names the traps young people commonly set for themselves: "
            "complacency, oversized ego, constant comparison, chronic procrastination. "
            "No one is immune~--- "
            "but anyone who reads this volume with honesty will find themselves "
            "in at least one story.",
        ),
        "bai_hoc": (
            "Bẫy tự bước vào đau hơn bẫy người khác đặt~--- "
            "vì nó thường đi kèm với sự xấu hổ.",
            "Traps we walk into ourselves hurt more than those others set~--- "
            "because they usually come with shame.",
        ),
        "quote": "Thoát bẫy không phải là chuyện xấu hổ~--- đó là chuyện dũng cảm.",
        "en_short": [
            "Name your trap: that is the first step out.",
            "Self-awareness is the sharpest tool against self-sabotage.",
        ],
        "tu_hoc": [
            ("Em đang bước vào cái bẫy nào mà vẫn chưa chịu thừa nhận?",
             "What trap are you walking into that you haven't admitted yet?"),
            ("Điều gì khiến em trì hoãn nhiều nhất? Em đã thử cách nào để thoát chưa?",
             "What do you procrastinate most on? Have you tried any way out?"),
            ("Trong những cái bẫy được kể, cái nào em thấy phổ biến nhất ở bạn bè?",
             "Among the traps described, which do you see most commonly in your friends?"),
        ],
    },
    12: {
        "so":    "XII",
        "title": "Những Điều Thầy Giáo Nhìn Thấy",
        "title_en": "What the Teacher Sees",
        "chu_de": "góc nhìn từ bục giảng về học sinh",
        "mo_dau": (
            "Bục giảng nhìn thấy những gì học sinh chưa tự nhìn thấy ở chính mình.",
            "The chalkboard sees what students have not yet seen in themselves.",
        ),
        "gioi_thieu": (
            "Quyển mười hai tập hợp những câu chuyện từ góc nhìn của người đứng trên bục giảng~--- "
            "không phải để khoe sự quan sát, "
            "mà để chia sẻ những gì thầy giáo thực sự muốn học trò của mình hiểu. "
            "Đây là quyển sách thầy muốn viết cho trò. "
            "Và trò nên đọc với lòng biết ơn.",
            "Volume twelve collects stories from the perspective of those at the chalkboard~--- "
            "not to display their observations, "
            "but to share what teachers truly want their students to understand. "
            "This is the book a teacher wants to write for students. "
            "And students should read it with gratitude.",
        ),
        "bai_hoc": (
            "Thầy giáo không phải là người chỉ dạy chữ~--- "
            "họ là người nhìn thấy tiềm năng trước khi học trò tự nhìn thấy.",
            "Teachers are not just those who teach letters~--- "
            "they are those who see potential before students see it themselves.",
        ),
        "quote": "Thầy nhìn thấy em~--- kể cả khi em chưa thấy chính mình.",
        "en_short": [
            "A teacher sees the student the student cannot see yet.",
            "The classroom reveals what the world will later confirm.",
        ],
        "tu_hoc": [
            ("Điều gì trong quyển này giúp em hiểu thầy cô hơn?",
             "What in this volume helped you understand your teachers better?"),
            ("Em từng được thầy cô nhìn thấy tiềm năng mình không? Lúc đó em cảm thấy thế nào?",
             "Has a teacher ever seen potential in you that you didn't see? How did that feel?"),
            ("Nếu em là thầy giáo, điều đầu tiên em muốn học trò mình hiểu là gì?",
             "If you were a teacher, what is the first thing you would want students to understand?"),
        ],
    },
    13: {
        "so":    "XIII",
        "title": "Những Câu Hỏi Học Trò Không Nói Thẳng",
        "title_en": "Questions Students Never Ask Aloud",
        "chu_de": "trả lời thẳng những câu hỏi bị giữ trong im lặng",
        "mo_dau": (
            "Có những câu hỏi học trò giữ trong lòng mãi~--- "
            "vì không biết hỏi ai, hoặc sợ bị cho là ngớ ngẩn.",
            "Some questions students keep to themselves forever~--- "
            "because they don't know who to ask, or fear being seen as foolish.",
        ),
        "gioi_thieu": (
            "Quyển mười ba chọn những câu hỏi đó ra và trả lời chúng "
            "một cách thẳng thắn, không vòng vo. "
            "Không phải mọi câu trả lời đều dễ nghe~--- "
            "nhưng tất cả đều thật.",
            "Volume thirteen selects those questions and answers them "
            "directly, without detour. "
            "Not every answer is easy to hear~--- "
            "but all of them are honest.",
        ),
        "bai_hoc": (
            "Câu hỏi không được hỏi là câu hỏi không bao giờ được trả lời~--- "
            "và sự im lặng đó tốn nhiều hơn ta nghĩ.",
            "The question never asked is the question never answered~--- "
            "and that silence costs more than we think.",
        ),
        "quote": "Câu hỏi dũng cảm mở ra cánh cửa mà im lặng đã khóa lại.",
        "en_short": [
            "Brave questions deserve honest answers.",
            "The unasked question is the most expensive silence.",
        ],
        "tu_hoc": [
            ("Câu hỏi nào em đang giữ trong lòng mà chưa dám hỏi ai?",
             "What question are you keeping inside that you haven't dared to ask?"),
            ("Câu trả lời nào trong quyển này khiến em ngạc nhiên nhất?",
             "Which answer in this volume surprised you most?"),
            ("Điều gì ngăn cản em đặt câu hỏi trong lớp học?",
             "What stops you from asking questions in class?"),
        ],
    },
    14: {
        "so":    "XIV",
        "title": "100 Câu Hỏi Học Trò Hay Hỏi Về Chuyện Học",
        "title_en": "100 Questions Students Ask About Learning",
        "chu_de": "học, động lực, thói quen, áp lực và con đường tương lai",
        "mo_dau": (
            "Có những câu hỏi học trò đặt ra thành lời. "
            "Và có những câu khác~--- hiện trong ánh mắt, trong cách ngại giơ tay, "
            "trong nỗi sợ kiểm tra.",
            "Some questions students ask aloud. "
            "And others~--- visible in their eyes, in the hesitation to raise a hand, "
            "in the anxiety before tests.",
        ),
        "gioi_thieu": (
            "Quyển mười bốn gom 100 câu hỏi rất gần với đầu óc học sinh. "
            "Không nhằm biến việc học thành một bài giảng đạo đức dài, "
            "mà để trả lời ngắn, rõ, thật, "
            "và đủ gần với những điều các em đang sống trong trường lớp.",
            "Volume fourteen gathers 100 questions that stay close to the student mind. "
            "Not to turn learning into a long moral lecture, "
            "but to answer briefly, clearly, honestly, "
            "and close to school life as students actually live it.",
        ),
        "bai_hoc": (
            "Học không chỉ là chuyện điểm số~--- "
            "học còn là chuyện hiểu mình, hiểu đời, bớt sợ sai, và lớn lên đàng hoàng.",
            "Learning is not only about scores~--- "
            "it is also about understanding oneself, understanding life, "
            "fearing mistakes less, and growing into a grounded person.",
        ),
        "quote": "Câu hỏi đúng dẫn tới bài học đúng~--- dù chưa chắc đến câu trả lời dễ.",
        "en_short": [
            "The right question is already half the answer.",
            "Learning begins the moment you dare to ask why.",
        ],
        "tu_hoc": [
            ("Câu hỏi nào trong 100 câu này em thấy gần với bản thân nhất?",
             "Which of the 100 questions here feels most personal to you?"),
            ("Có câu hỏi nào em muốn thêm vào nếu có một Quyển XV giống quyển này?",
             "Is there a question you'd add to a future volume like this?"),
            ("Điều gì nhất về việc học mà em vẫn chưa tìm được câu trả lời thỏa đáng?",
             "What about learning do you still not have a satisfying answer for?"),
        ],
    },
    15: {
        "so":    "XV",
        "title": "Những Điều Thầy Muốn Nói Với Học Sinh",
        "title_en": "What Teachers Want to Tell Students",
        "chu_de": "thầy nói thẳng, gần và chậm về học tập, tính cách, đường đời",
        "mo_dau": (
            "Có những điều thầy muốn nói với học trò~--- "
            "nhưng tiết học hết quá nhanh, và không phải lúc nào cũng đúng lúc.",
            "There are things teachers want to say to students~--- "
            "but class ends too quickly, and the timing is never quite right.",
        ),
        "gioi_thieu": (
            "Quyển mười lăm chọn một giọng khác: không lên lớp quá cao, "
            "không làm quá nhiều khẩu hiệu. "
            "Mỗi bài ngắn như một lời thầy nói lại một điều quen thuộc "
            "nhưng cố nói gần hơn, thật hơn, và có ích hơn. "
            "Nếu em đang đi học, thầy mong em đọc quyển này "
            "như đang ngồi nghe một người lớn muốn nói chuyện đàng hoàng với mình.",
            "Volume fifteen chooses a different voice: not lecturing from too high above, "
            "not filling pages with empty slogans. "
            "Each short piece is like a teacher saying something familiar again "
            "but closer, truer, and more useful. "
            "If you are a student, read this as though sitting with an adult "
            "who wants to speak properly with you.",
        ),
        "bai_hoc": (
            "Lời thầy gần và thật hơn một nghìn lần so với lời thầy sáo rỗng~--- "
            "học sinh biết ngay sự khác biệt.",
            "A teacher's close and honest word is worth a thousand empty ones~--- "
            "students always know the difference.",
        ),
        "quote": "Thầy nói không phải để em ghi nhớ công thức~--- mà để em sống tốt hơn.",
        "en_short": [
            "What a teacher truly says lives long after the lesson ends.",
            "Speak close to the student, not above them.",
        ],
        "tu_hoc": [
            ("Điều thầy nói nào trong quyển này em ước mình được nghe từ sớm hơn?",
             "What did a teacher say in this volume that you wish you'd heard earlier?"),
            ("Em đã từng thực sự lắng nghe lời thầy cô chưa? Lần nào đáng nhớ nhất?",
             "Have you ever truly listened to a teacher? What was the most memorable time?"),
            ("Nếu em có thể nói một điều thật lòng với thầy cô, đó là điều gì?",
             "If you could say one honest thing to a teacher, what would it be?"),
        ],
    },
    16: {
        "so":    "XVI",
        "title": "Những Bài Học Nhỏ Trong Lớp Học",
        "title_en": "Small Lessons from the Classroom",
        "chu_de": "bài học lớn từ tình huống nhỏ xảy ra mỗi ngày trên lớp",
        "mo_dau": (
            "Người ngoài có thể nghĩ đó chỉ là chuyện vụn vặt của một giờ học~--- "
            "nhưng thật ra, chính từ những điều vụn ấy "
            "mà học sinh học cách nghĩ, cách hỏi, cách sai, cách sửa.",
            "An outsider may think these are just tiny incidents from an ordinary class~--- "
            "but in truth, it is from these small things "
            "that students learn how to think, ask, be wrong, and correct themselves.",
        ),
        "gioi_thieu": (
            "Quyển mười sáu đi vào lớp học từ chính những mẩu nhỏ như thế. "
            "Không phải để làm mọi thứ trở nên to tát, "
            "mà để giữ lại những bài học rất thật thường bị trôi qua quá nhanh. "
            "Nếu em là học sinh, mong em thấy mình ở đâu đó trong những trang này.",
            "Volume sixteen enters the classroom through such small fragments. "
            "Not to make everything seem grand, "
            "but to keep the very real lessons that usually pass too quickly. "
            "If you are a student, I hope you see yourself somewhere in these pages.",
        ),
        "bai_hoc": (
            "Bài học lớn nhất thường đến từ khoảnh khắc nhỏ nhất~--- "
            "vì khoảnh khắc nhỏ là lúc ta không chuẩn bị trước.",
            "The greatest lessons usually come from the smallest moments~--- "
            "because small moments are when we are unprepared.",
        ),
        "quote": "Lớp học không chỉ là nơi học bài~--- đó là nơi học cách làm người.",
        "en_short": [
            "Small classroom moments teach the largest life lessons.",
            "The ordinary class hour holds extraordinary growth.",
        ],
        "tu_hoc": [
            ("Khoảnh khắc nhỏ nào trong lớp học em nhớ mãi? Tại sao?",
             "What small classroom moment do you remember most? Why?"),
            ("Bài học lớn nhất em học được không phải từ sách giáo khoa là gì?",
             "What is the biggest lesson you learned that was not in any textbook?"),
            ("Nếu viết lại một giờ học đáng nhớ, em sẽ kể điều gì xảy ra?",
             "If you wrote about one memorable class, what would you describe?"),
        ],
    },
    17: {
        "so":    "XVII",
        "title": "Những Điều Học Sinh Nên Hiểu Sớm",
        "title_en": "Things Students Should Understand Early",
        "chu_de": "nền tảng quan trọng~--- hiểu sớm thì đỡ vấp về sau",
        "mo_dau": (
            "Những điều trong quyển này không hẳn mới~--- "
            "nhưng nhiều điều tuy quen vẫn cần được nói lại cho rõ, "
            "cho gần, và cho đủ sớm.",
            "The things in this book are not entirely new~--- "
            "but many familiar truths still need to be said again clearly, "
            "closely, and early enough.",
        ),
        "gioi_thieu": (
            "Quyển mười bảy gom lại những nền tảng quan trọng "
            "mà một học sinh hiểu càng sớm thì càng đỡ vấp về sau. "
            "Quyển sách này không cố làm điều lớn lao~--- "
            "nó chỉ muốn nói những điều thật, gần, và đúng lúc.",
            "Volume seventeen gathers important foundations "
            "that, if understood early, can save students from many later stumbles. "
            "This book does not aim to be grand~--- "
            "it only wants to say things that are true, close, and timely.",
        ),
        "bai_hoc": (
            "Hiểu sớm một điều đúng tốt hơn nhiều lần hối tiếc về một điều bỏ lỡ.",
            "Understanding one truth early is far better than many regrets about a missed lesson.",
        ),
        "quote": "Sớm một bước~--- đỡ một đoạn đường lạc.",
        "en_short": [
            "Early understanding saves late regret.",
            "The foundations laid young hold the tallest towers.",
        ],
        "tu_hoc": [
            ("Điều nào trong quyển này em ước mình được biết từ năm ngoái?",
             "What in this volume do you wish you had known a year ago?"),
            ("Bạn bè em có đang hiểu những nền tảng này không? Làm sao em biết?",
             "Do your friends understand these foundations? How can you tell?"),
            ("Em sẽ chia sẻ điều gì từ quyển này với người mình quan tâm?",
             "What from this volume will you share with someone you care about?"),
        ],
    },
    18: {
        "so":    "XVIII",
        "title": "Những Lời Thầy Nói Trong Lớp Học",
        "title_en": "50 Words a Teacher Says in Class",
        "chu_de": "50 câu lời thầy về học tập, nỗ lực, thái độ và tương lai",
        "mo_dau": (
            "Có những câu thầy nói xong~--- và cả lớp im lặng một chút, không phải vì sợ, "
            "mà vì câu đó chạm vào đúng điều ai đó đang cần.",
            "Some sentences a teacher says leave the class silent for a moment~--- "
            "not from fear, but because the words touched exactly what someone needed.",
        ),
        "gioi_thieu": (
            "Quyển mười tám gom 50 câu như thế, chia làm năm nhóm: "
            "về việc học, về nỗ lực, về thái độ sống, về sai lầm, và về tương lai. "
            "Mỗi câu đi kèm một câu chuyện nhỏ, để thầy cô có thể dùng "
            "khi mở bài, kết tiết, viết bảng, hoặc tặng học sinh cuối năm.",
            "Volume eighteen gathers 50 such sentences in five groups: "
            "on learning, on effort, on attitude, on mistakes, and on the future. "
            "Each is paired with a short story so teachers can use them "
            "to open a lesson, close a class, write on the board, or give to students at year's end.",
        ),
        "bai_hoc": (
            "Một câu nói đúng lúc có thể thay đổi cách một học sinh "
            "nghĩ về việc học và về chính mình.",
            "One sentence at the right moment can change how a student "
            "thinks about learning and about themselves.",
        ),
        "quote": "Lời thầy không phải để nhớ mãi~--- mà để sống mãi.",
        "en_short": [
            "The right sentence at the right moment changes everything.",
            "Fifty words can carry a lifetime of lessons.",
        ],
        "tu_hoc": [
            ("Câu nào trong 50 câu em muốn chép vào sổ tay và nhớ mãi?",
             "Which of the 50 sentences do you want to write in your notebook and keep?"),
            ("Em đã từng nghe câu nói nào từ thầy cô khiến em thay đổi cách nghĩ?",
             "Have you heard a sentence from a teacher that changed the way you think?"),
            ("Nếu chỉ nhớ một câu từ quyển này, em sẽ chọn câu nào? Tại sao?",
             "If you could only remember one sentence from this volume, which would it be? Why?"),
        ],
    },
    19: {
        "so":    "XIX",
        "title": "100 Câu Nói Làm Học Sinh Im Lặng Suy Nghĩ",
        "title_en": "100 Sentences That Make Students Fall Silent",
        "chu_de": "những câu ngắn, sâu, khiến học sinh dừng lại và tự hỏi",
        "mo_dau": (
            "Có những câu thầy nói xong, cả lớp im lặng~--- "
            "không phải im vì sợ, mà im vì đang suy nghĩ.",
            "Some sentences the teacher says leave the whole class silent~--- "
            "not from fear, but because they are thinking.",
        ),
        "gioi_thieu": (
            "Quyển mười chín gom 100 câu như thế~--- "
            "ngắn, sâu, khiến học sinh dừng lại và tự hỏi. "
            "Mỗi câu đi kèm một câu chuyện nhỏ và gợi ý để giữ lại. "
            "Mong rằng thầy cô có thêm câu để nói đúng lúc; "
            "học trò có thêm điều để im lặng mà nghĩ.",
            "Volume nineteen gathers 100 such sentences~--- "
            "short, deep, that make students pause and wonder. "
            "Each comes with a short story and a takeaway. "
            "May teachers have more sentences to say at the right moment; "
            "may students have more to ponder in silence.",
        ),
        "bai_hoc": (
            "Im lặng sau khi nghe một câu đúng lúc là dấu hiệu của tư duy, "
            "không phải của thờ ơ.",
            "Silence after the right sentence is a sign of thinking, "
            "not of indifference.",
        ),
        "quote": "Im lặng đôi khi là câu trả lời hay nhất.",
        "en_short": [
            "Silence after a deep sentence means thinking has begun.",
            "One hundred words: one hundred doors to reflection.",
        ],
        "tu_hoc": [
            ("Câu nào trong 100 câu này khiến em im lặng lâu nhất? Vì sao?",
             "Which of the 100 sentences made you silent the longest? Why?"),
            ("Em đã từng tạo ra một khoảnh khắc im lặng suy nghĩ cho người khác chưa?",
             "Have you ever created a moment of silent reflection for someone else?"),
            ("Câu nào em muốn thầy cô nói với cả lớp vào đầu buổi học ngày mai?",
             "Which sentence would you want your teacher to say to the class tomorrow morning?"),
        ],
    },
    20: {
        "so":    "XX",
        "title": "50 Câu Nói Hài Hước Nhưng Sâu Sắc",
        "title_en": "50 Sentences: Funny but Profound",
        "chu_de": "thầy cười mà học trò nghĩ~--- hài hước đúng cách",
        "mo_dau": (
            "Những câu nói hài hước của thầy giáo trong lớp đôi khi khiến cả lớp cười~--- "
            "nhưng cười xong, học sinh nhớ.",
            "Humorous teacher sayings in class sometimes make everyone laugh~--- "
            "but after the laugh, students remember.",
        ),
        "gioi_thieu": (
            "Quyển hai mươi gom 50 câu vừa gây cười vừa gợi suy nghĩ: "
            "ngắn, dễ nhớ, và sau tiếng cười vẫn để lại bài học. "
            "Mong thầy cô thêm vài câu vui mà sâu; "
            "học trò thêm vài kỷ niệm vừa cười vừa nghĩ.",
            "Volume twenty gathers 50 sentences that both amuse and make you think: "
            "short, memorable, and after the laugh they still leave a lesson. "
            "May teachers add a few lines that are funny and deep; "
            "may students keep a few memories that mix laughter and thought.",
        ),
        "bai_hoc": (
            "Hài hước đúng cách không làm mất uy tín~--- "
            "nó làm học trò gần thầy và nhớ lâu hơn.",
            "The right kind of humor doesn't undermine authority~--- "
            "it brings students closer and makes them remember longer.",
        ),
        "quote": "Cười xong nhớ mới là hay.",
        "en_short": [
            "Laughter that leaves a lesson is the best kind.",
            "Humor and wisdom are not opposites.",
        ],
        "tu_hoc": [
            ("Câu nói vừa buồn cười vừa sâu sắc nào em vẫn nhớ sau khi đọc xong?",
             "Which funny yet deep sentence do you still remember after finishing the book?"),
            ("Em có thầy cô nào hay dùng hài hước để dạy không? Kể một ví dụ?",
             "Do you have a teacher who uses humor to teach? Give one example."),
            ("Tự em nghĩ được câu hài hước mà vẫn có bài học không? Thử viết một câu.",
             "Can you write a funny sentence that still carries a lesson? Try one."),
        ],
    },
    21: {
        "so":    "XXI",
        "title": "30 Câu Nói Khiến Học Sinh Lười Học Phải Giật Mình",
        "title_en": "30 Wake-Up Calls for the Reluctant Student",
        "chu_de": "thẳng, rõ, để tỉnh ra trước khi trả giá",
        "mo_dau": (
            "Có những câu thầy nói không la mắng, không dọa~--- "
            "nhưng học sinh lười nghe xong giật mình.",
            "Some things the teacher says are not scolding or threats~--- "
            "but lazy students startle when they hear them.",
        ),
        "gioi_thieu": (
            "Quyển hai mươi mốt gom 30 câu như thế: thẳng, rõ, "
            "để học sinh tỉnh ra trước khi trả giá bằng điểm kém, "
            "bằng cơ hội mất, bằng hối tiếc sau này. "
            "Mong thầy cô dùng đúng lúc; mong học trò đọc khi còn kịp.",
            "Volume twenty-one gathers 30 such sentences: direct and clear, "
            "so students wake up before paying with bad grades, "
            "lost chances, and future regret. "
            "May teachers use them at the right moment; "
            "may students read them while there is still time.",
        ),
        "bai_hoc": (
            "Giật mình một lần có thể thay đổi hướng đi~--- "
            "nếu em chịu lắng nghe và hành động.",
            "One wake-up moment can change your direction~--- "
            "if you listen and act.",
        ),
        "quote": "Lười hôm nay, trả giá ngày mai.",
        "en_short": [
            "A wake-up call now saves a lifetime of regret.",
            "The cost of laziness is always paid with interest.",
        ],
        "tu_hoc": [
            ("Câu nào trong 30 câu này khiến em giật mình nhất? Vì sao?",
             "Which of the 30 sentences gave you the biggest wake-up? Why?"),
            ("Em đang trì hoãn điều gì mà em biết mình sẽ hối tiếc nếu không làm sớm?",
             "What are you delaying that you know you'll regret if you don't act soon?"),
            ("Điều gì giúp em từ lười trở nên chịu cố gắng?",
             "What helps you go from lazy to actually trying?"),
        ],
    },
    22: {
        "so":    "XXII",
        "title": "50 Câu Nói Đỉnh Cao Sư Phạm Khi Học Sinh Nản Học",
        "title_en": "50 Peak Pedagogy Sentences for Discouraged Students",
        "chu_de": "nâng đỡ, động viên, mở lối~--- không la mắng",
        "mo_dau": (
            "Khi học sinh nản học, la mắng đôi khi chỉ làm các em đóng cửa thêm~--- "
            "nhưng một câu nói đúng: ấm, rõ, không đổ lỗi, có thể mở lại cánh cửa.",
            "When students give up on learning, scolding sometimes only makes them shut the door tighter~--- "
            "but the right sentence: warm, clear, without blame, can open it again.",
        ),
        "gioi_thieu": (
            "Quyển hai mươi hai gom 50 câu `đỉnh cao sư phạm': "
            "nâng đỡ khi học trò mệt, động viên khi các em nghi ngờ mình, "
            "và chỉ lối khi các em lạc. "
            "Mong thầy cô có thêm câu để đỡ học trò đứng dậy; "
            "mong học trò gặp đúng câu khi đang cần nhất.",
            "Volume twenty-two gathers 50 `peak pedagogy' sentences: "
            "support when students are tired, encouragement when they doubt themselves, "
            "and direction when they are lost. "
            "May teachers have more sentences to help students stand up; "
            "may students find the right sentence when they need it most.",
        ),
        "bai_hoc": (
            "Nâng đỡ đúng lúc không làm học trò yếu đuối~--- "
            "nó cho các em đủ sức để tự đứng lên.",
            "Support at the right time does not make students weak~--- "
            "it gives them just enough strength to stand on their own.",
        ),
        "quote": "Nản một lúc không sao; đứng dậy mới quan trọng.",
        "en_short": [
            "The right word lifts a student higher than any grade.",
            "Encouragement opens doors that scolding only slams shut.",
        ],
        "tu_hoc": [
            ("Câu nào trong 50 câu này em muốn thầy cô nói với mình nhất lúc em đang nản?",
             "Which of the 50 sentences would you most want a teacher to say when you are discouraged?"),
            ("Em đã từng động viên ai đó học tiếp khi họ muốn bỏ chưa? Bằng lời gì?",
             "Have you ever encouraged someone to keep studying when they wanted to quit? What did you say?"),
            ("Điều gì giúp em tiếp tục khi bản thân không muốn cố gắng nữa?",
             "What keeps you going when you don't feel like trying anymore?"),
        ],
    },
    23: {
        "so":    "XXIII",
        "title": "50 Câu Nói Thầy Nói Cuối Năm Học",
        "title_en": "50 Sentences a Teacher Says at Year's End",
        "chu_de": "rất xúc động~--- để tặng và để giữ lại",
        "mo_dau": (
            "Cuối năm học là lúc thầy và trò nhìn lại~--- "
            "và đôi khi những lời nói đúng lúc đó "
            "theo học sinh suốt cả cuộc đời.",
            "The end of the school year is when teachers and students look back~--- "
            "and sometimes the words said at that moment "
            "stay with students for their whole lives.",
        ),
        "gioi_thieu": (
            "Quyển hai mươi ba gom 50 câu xúc động~--- "
            "để tặng và để giữ lại. "
            "Mỗi câu đi kèm một câu chuyện nhỏ "
            "mang tâm tình của người thầy gửi đến học trò trước khi chia tay. "
            "Mong rằng mỗi trang sách là một lời tạm biệt đáng nhớ.",
            "Volume twenty-three gathers 50 moving sentences~--- "
            "to give and to keep. "
            "Each is paired with a short story "
            "carrying a teacher's heart to students before parting. "
            "May every page be a memorable farewell.",
        ),
        "bai_hoc": (
            "Lời tạm biệt đúng lúc, đúng lời "
            "có thể là điều học sinh mang theo cả đời~--- "
            "lâu hơn bất kỳ bài thi nào.",
            "The right farewell at the right moment "
            "can be what students carry for a lifetime~--- "
            "longer than any exam.",
        ),
        "quote": "Thầy tin em. Dù đi đâu, nhớ câu đó.",
        "en_short": [
            "End of year words carry beyond the school gate.",
            "A teacher's farewell can echo for a lifetime.",
        ],
        "tu_hoc": [
            ("Câu nói cuối năm nào của thầy cô em vẫn nhớ đến tận bây giờ?",
             "What end-of-year words from a teacher do you still remember today?"),
            ("Nếu em phải nói một câu với cả lớp trước khi kết thúc năm học, em nói gì?",
             "If you had to say one thing to your whole class before year's end, what would it be?"),
            ("Bức thư tạm biệt lý tưởng từ thầy cô đến học trò em hình dung như thế nào?",
             "What does an ideal farewell letter from a teacher to students look like?"),
        ],
    },
    24: {
        "so":    "XXIV",
        "title": "Bí Quyết Nhân Sinh",
        "title_en": "Life Secrets: Stories That Hurt but Teach",
        "chu_de": "những câu chuyện đau nhưng rất thật về cuộc sống",
        "mo_dau": (
            "Có những bài học cuộc đời không đến từ sách giáo khoa~--- "
            "chúng đến từ những khoảnh khắc đau, thất bại, và sự chân thật không che đậy.",
            "Some of life's lessons do not come from textbooks~--- "
            "they come from pain, failure, and unfiltered honesty.",
        ),
        "gioi_thieu": (
            "Quyển hai mươi tư là quyển khép lại bộ sách với 13 chương và 190 truyện~--- "
            "những câu chuyện đau nhưng rất thật. "
            "Không phải để làm người đọc buồn, "
            "mà để sau khi đọc xong, "
            "người ta hiểu thêm về cuộc sống và về chính mình.",
            "Volume twenty-four is the closing volume of the series, "
            "with 13 chapters and 190 stories~--- "
            "stories that hurt but are completely true. "
            "Not to sadden the reader, "
            "but so that after reading, "
            "they understand more about life and about themselves.",
        ),
        "bai_hoc": (
            "Những bài học đau nhất thường là những bài học thật nhất~--- "
            "và thật nhất thì sẽ ở lại lâu nhất.",
            "The most painful lessons are usually the truest ones~--- "
            "and the truest ones stay the longest.",
        ),
        "quote": "Đọc xong thấy hơi đau~--- nhưng hiểu thêm về cuộc sống.",
        "en_short": [
            "Truth sometimes hurts: that is how you know it is real.",
            "Life secrets are written in honest stories, not easy ones.",
        ],
        "tu_hoc": [
            ("Câu chuyện nào trong quyển này khiến em thấy đau nhưng đồng thời hiểu ra điều gì đó?",
             "Which story here hurt a little but also helped you understand something?"),
            ("Bí quyết nhân sinh nào trong cả bộ sách 24 quyển em tâm đắc nhất?",
             "Which life secret from all 24 volumes of this series resonated most with you?"),
            ("Nếu có thể tặng một quyển trong bộ sách này cho ai đó, em sẽ tặng quyển nào và tặng ai?",
             "If you could give one volume from this series to someone, which would you give and to whom?"),
        ],
    },
}

# -------------------------------------------------------------------
# Template lời tựa
# -------------------------------------------------------------------
def make_loitua(v, simple=False):
    so = v["so"]
    title = v["title"]
    title_en = v["title_en"]
    mo_vn, mo_en = v["mo_dau"]
    gi_vn, gi_en = v["gioi_thieu"]
    bl_vn, bl_en = v["bai_hoc"]
    quote = v["quote"]
    en_short = v["en_short"]
    tu_hoc = v["tu_hoc"]

    tu_hoc_lines = "\n\n".join(
        f"{i+1}. {q_vn} \\textit{{({q_en})}}"
        for i, (q_vn, q_en) in enumerate(tu_hoc)
    )

    en_short_lines = "\n\n".join(en_short)

    if simple:
        # Inline tcolorbox thay thế ghinhoanh và tuhocnhanh
        ghi_block = rf"""\begin{{tcolorbox}}[
  colback=truyenblue!6, colframe=truyenblue,
  coltitle=white, fonttitle=\bfseries,
  title={{Easy English}},
  arc=4pt, boxrule=1pt, breakable, enhanced
]
\textbf{{Short English to remember:}}

{en_short_lines}
\end{{tcolorbox}}"""

        tu_block = rf"""\begin{{tcolorbox}}[
  colback=truyengold!10, colframe=truyengold!70!black,
  coltitle=black, fonttitle=\bfseries,
  title={{T\textit{{ự}} H\textit{{ọ}}c Nhanh}},
  arc=4pt, boxrule=1pt, breakable, enhanced
]
{tu_hoc_lines}
\end{{tcolorbox}}"""
    else:
        ghi_block = rf"""\begin{{ghinhoanh}}
\textbf{{Short English to remember:}}

{en_short_lines}
\end{{ghinhoanh}}"""

        tu_block = rf"""\begin{{tuhocnhanh}}
{tu_hoc_lines}
\end{{tuhocnhanh}}"""

    return rf"""% LỜI TỰA --- Quyển {so}
\chapter*{{Lời Tựa}}
\addcontentsline{{toc}}{{chapter}}{{Lời Tựa}}
\markboth{{Lời Tựa}}{{Lời Tựa}}

\begin{{truyen}}{{Lời Tựa}}{{{title_en}}}
\chuhoa{{G}}{{iáo viên bắt đầu bộ sách này với một câu hỏi đơn giản: làm thế nào để mỗi buổi học có thể để lại thứ gì đó đáng nhớ hơn là bài thi?}}
\textit{{(A teacher began this series with a simple question: how can each class leave behind something more memorable than a test?)}}

{mo_vn}
\textit{{({mo_en})}}

{gi_vn}
\textit{{({gi_en})}}

Bộ sách <<Truyện Tích Cảm Hứng Song Ngữ>> gồm 24 quyển, mỗi quyển một chủ đề riêng. Quyển {so} này mang chủ đề: \textbf{{{v["chu_de"]}}}.
\textit{{(The series ``Inspiring Bilingual Tales'' contains 24 volumes, each with its own theme. Volume {so} focuses on: \textbf{{{v["chu_de"]}}}.}})
\end{{truyen}}

\begin{{baihoc}}
{bl_vn}
\textit{{({bl_en})}}
\end{{baihoc}}

{ghi_block}

{tu_block}

\begin{{center}}
\textit{{\color{{truyengold}}``{quote}''}}
\end{{center}}

\ngancach
"""

# -------------------------------------------------------------------
# Template hướng dẫn sử dụng sách
# Same structure for all volumes; ghinhoanh/tuhocnhanh replaced with
# inline tcolorbox for volumes that don't define those environments.
# -------------------------------------------------------------------
HDSD_FULL = r"""% HƯỚNG DẪN SỬ DỤNG SÁCH
\chapter*{Hướng Dẫn Sử Dụng Sách}
\addcontentsline{toc}{chapter}{Hướng Dẫn Sử Dụng Sách}
\markboth{Hướng Dẫn Sử Dụng Sách}{Hướng Dẫn Sử Dụng Sách}

\begin{truyen}{Bộ Sách Này Dành Cho Ai?}{Who Is This Book For?}
\chuhoa{B}{ộ sách <<Truyện Tích Cảm Hứng Song Ngữ>> được thiết kế cho ba nhóm đối tượng chính.}
\textit{(The ``Inspiring Bilingual Tales'' series is designed for three main audiences.)}

\textbf{Giáo viên:} dùng mỗi câu chuyện ngắn để mở bài, kết tiết, hoặc kể vào những phút cuối giờ.
\textit{(\textbf{Teachers:} use each short story to open a lesson, close a class, or tell in the final minutes of a session.)}

\textbf{Học sinh:} đọc từng câu chuyện và dừng lại suy ngẫm --- không cần đọc liên tiếp, mỗi truyện là một đơn vị độc lập.
\textit{(\textbf{Students:} read each story and pause to reflect --- no need to read continuously, each story stands alone.)}

\textbf{Phụ huynh:} dùng như nội dung kể chuyện buổi tối, thay thế cho màn hình điện thoại, để nuôi dưỡng thói quen đọc và suy nghĩ.
\textit{(\textbf{Parents:} use as bedtime storytelling content, replacing screens, to nurture a habit of reading and reflection.)}
\end{truyen}

\vspace{6pt}

\begin{tcolorbox}[
  colback=truyengold!8,
  colframe=truyengold!70!black,
  coltitle=black,
  fonttitle=\bfseries,
  title={Giải Thích Các Ô Màu Trong Sách \quad\textit{\small(Color-Box Guide)}},
  arc=4pt, boxrule=1pt, breakable, enhanced
]

\smallskip
\textbf{\color{truyenred}Ô Nâu~--- Câu Chuyện Chính (\textit{Main Story})}\\
Phần tường thuật song ngữ Việt -- Anh. Đọc cả hai để vừa hiểu nội dung vừa luyện tiếng Anh. Nếu bận, chỉ cần đọc tiếng Việt; nếu muốn luyện, che tiếng Việt và đọc tiếng Anh.\\
\textit{(Bilingual narrative in Vietnamese and English. Read both to understand content and practise English. If short on time, read only Vietnamese; to practise, cover the Vietnamese and read only English.)}

\medskip
\textbf{\color{truyenblue}Ô Xanh~--- Bài Học (\textit{Lesson Learned})}\\
Một hoặc hai câu tóm tắt bài học cốt lõi. Đây là phần nên ghi lại vào sổ tay.\\
\textit{(One or two sentences summarising the core lesson. This is the part worth noting in a journal.)}

\medskip
\textbf{\color{truyenblue!60}Ô Xanh Nhạt~--- Tiếng Anh Ngắn (\textit{Easy English})}\\
Hai đến ba câu tiếng Anh để nhớ nhanh. Đọc to và lặp lại~--- đây là luyện tập ngôn ngữ hiệu quả nhất.\\
\textit{(Two to three English sentences to remember quickly. Read aloud and repeat~--- this is the most effective language practice.)}

\medskip
\textbf{\color{truyengold!80!black}Ô Vàng~--- Tự Học Nhanh (\textit{Quick Self-Study})}\\
Ba câu hỏi suy ngẫm. Dành 2--3 phút trả lời trong đầu, hoặc viết ra. Không có câu trả lời đúng duy nhất~--- quan trọng là dừng lại và nghĩ.\\
\textit{(Three reflection questions. Spend 2--3 minutes answering mentally or in writing. There is no single right answer~--- what matters is pausing to think.)}

\smallskip
\end{tcolorbox}

\vspace{6pt}

\begin{baihoc}
\textbf{Gợi Ý Đọc~--- Cách đọc hiệu quả nhất:} 1~truyện mỗi ngày, đọc vào buổi sáng trước khi lên lớp hoặc buổi tối trước khi ngủ. Đừng cố đọc hết cả chương trong một lần.
\textit{(\textbf{Reading Tip~--- Most effective way:} 1~story per day, read in the morning before class or in the evening before sleep. Do not try to finish a whole chapter in one sitting.)}
\end{baihoc}

\vspace{4pt}

\begin{ghinhoanh}
\textbf{Reading tips:}

Read 1 story a day --- slow and steady wins.

Cover the Vietnamese and read only English to practise.

Write down one sentence that stays with you.
\end{ghinhoanh}

\ngancach
"""

HDSD_SIMPLE = r"""% HƯỚNG DẪN SỬ DỤNG SÁCH
\chapter*{Hướng Dẫn Sử Dụng Sách}
\addcontentsline{toc}{chapter}{Hướng Dẫn Sử Dụng Sách}
\markboth{Hướng Dẫn Sử Dụng Sách}{Hướng Dẫn Sử Dụng Sách}

\begin{truyen}{Bộ Sách Này Dành Cho Ai?}{Who Is This Book For?}
\chuhoa{B}{ộ sách <<Truyện Tích Cảm Hứng Song Ngữ>> được thiết kế cho ba nhóm đối tượng chính.}
\textit{(The ``Inspiring Bilingual Tales'' series is designed for three main audiences.)}

\textbf{Giáo viên:} dùng mỗi câu chuyện ngắn để mở bài, kết tiết, hoặc kể vào những phút cuối giờ.
\textit{(\textbf{Teachers:} use each short story to open a lesson, close a class, or tell in the final minutes of a session.)}

\textbf{Học sinh:} đọc từng câu chuyện và dừng lại suy ngẫm --- không cần đọc liên tiếp, mỗi truyện là một đơn vị độc lập.
\textit{(\textbf{Students:} read each story and pause to reflect --- no need to read continuously, each story stands alone.)}

\textbf{Phụ huynh:} dùng như nội dung kể chuyện buổi tối, thay thế cho màn hình điện thoại, để nuôi dưỡng thói quen đọc và suy nghĩ.
\textit{(\textbf{Parents:} use as bedtime storytelling content, replacing screens, to nurture a habit of reading and reflection.)}
\end{truyen}

\vspace{6pt}

\begin{tcolorbox}[
  colback=truyengold!8,
  colframe=truyengold!70!black,
  coltitle=black,
  fonttitle=\bfseries,
  title={Giải Thích Các Ô Màu Trong Sách \quad\textit{\small(Color-Box Guide)}},
  arc=4pt, boxrule=1pt, breakable, enhanced
]

\smallskip
\textbf{\color{truyenred}Ô Nâu~--- Câu Chuyện Chính (\textit{Main Story})}\\
Phần tường thuật song ngữ Việt -- Anh. Đọc cả hai để vừa hiểu nội dung vừa luyện tiếng Anh.\\
\textit{(Bilingual narrative in Vietnamese and English. Read both to understand content and practise English.)}

\medskip
\textbf{\color{truyenblue}Ô Xanh~--- Bài Học (\textit{Lesson Learned})}\\
Một hoặc hai câu tóm tắt bài học cốt lõi. Đây là phần nên ghi lại vào sổ tay.\\
\textit{(One or two sentences summarising the core lesson. This is the part worth noting in a journal.)}

\smallskip
\end{tcolorbox}

\vspace{6pt}

\begin{baihoc}
\textbf{Gợi Ý Đọc~--- Cách đọc hiệu quả nhất:} 1~truyện mỗi ngày, đọc vào buổi sáng trước khi lên lớp hoặc buổi tối trước khi ngủ. Đừng cố đọc hết cả chương trong một lần.
\textit{(\textbf{Reading Tip~--- Most effective way:} 1~story per day, read in the morning before class or in the evening before sleep. Do not try to finish a whole chapter in one sitting.)}
\end{baihoc}

\vspace{4pt}

\begin{tcolorbox}[
  colback=truyenblue!6, colframe=truyenblue,
  coltitle=white, fonttitle=\bfseries,
  title={Easy English},
  arc=4pt, boxrule=1pt, breakable, enhanced
]
\textbf{Reading tips:}

Read 1 story a day --- slow and steady wins.

Cover the Vietnamese and read only English to practise.

Write down one sentence that stays with you.
\end{tcolorbox}

\ngancach
"""

# -------------------------------------------------------------------
# Cập nhật main.tex: thêm \input{chapters/loitua} và \input{chapters/huong-dan}
# sau \include{cover} / \input{cover} và trước \tableofcontents
# -------------------------------------------------------------------
def patch_main_tex(path, vol_num):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Nếu đã có loitua thì bỏ qua
    if "loitua" in content:
        print(f"  [SKIP] main.tex đã có loitua")
        return

    insert = "\n%------------------------------------------------------------\n% LỜI TỰA\n%------------------------------------------------------------\n\\input{chapters/loitua}\n\n%------------------------------------------------------------\n% HƯỚNG DẪN SỬ DỤNG\n%------------------------------------------------------------\n\\input{chapters/huong-dan}\n"

    # Chiến lược 1: sau \include{cover}\n\n\frontmatter hay \include{cover}\n\frontmatter
    # Chiến lược 2: sau \include{cover} có \tableofcontents liền sau
    # Tìm điểm chèn: ngay sau dòng include/input cover, trước tableofcontents

    # Pattern: dòng chứa cover, rồi tìm tableofcontents
    lines = content.splitlines(keepends=True)
    cover_idx = None
    toc_idx = None

    for i, line in enumerate(lines):
        stripped = line.strip()
        if cover_idx is None and re.search(r'\\(include|input)\{cover\}', stripped):
            cover_idx = i
        if cover_idx is not None and toc_idx is None:
            if '\\tableofcontents' in stripped:
                toc_idx = i
                break

    if cover_idx is not None and toc_idx is not None:
        # Chèn sau cover_idx
        lines.insert(cover_idx + 1, insert)
        new_content = "".join(lines)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  [OK] Đã thêm loitua+huong-dan vào main.tex (sau cover, trước TOC)")
    else:
        print(f"  [WARN] Không tìm được vị trí để chèn trong main.tex (cover_idx={cover_idx}, toc_idx={toc_idx})")
        print(f"         Vui lòng thêm thủ công.")


# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------
def main():
    for vol_num in range(1, 25):
        vol_dir = os.path.join(BASE, f"truyen-tich-cam-hung-quyen-{vol_num}")
        chapters_dir = os.path.join(vol_dir, "chapters")

        if not os.path.isdir(vol_dir):
            print(f"[SKIP] Không tìm thấy thư mục: {vol_dir}")
            continue

        # Tạo thư mục chapters nếu chưa có
        os.makedirs(chapters_dir, exist_ok=True)

        v = VOLUMES[vol_num]
        simple = vol_num in SIMPLE_VOLUMES

        # --- loitua.tex ---
        loitua_path = os.path.join(chapters_dir, "loitua.tex")
        if os.path.exists(loitua_path):
            print(f"[Q{vol_num:2d}] loitua.tex đã tồn tại, ghi đè...")
        loitua_content = make_loitua(v, simple=simple)
        with open(loitua_path, "w", encoding="utf-8") as f:
            f.write(loitua_content)
        print(f"[Q{vol_num:2d}] ✓ chapters/loitua.tex ({'simple' if simple else 'full'})")

        # --- huong-dan.tex ---
        hdsd_path = os.path.join(chapters_dir, "huong-dan.tex")
        if os.path.exists(hdsd_path):
            print(f"[Q{vol_num:2d}] huong-dan.tex đã tồn tại, ghi đè...")
        hdsd_content = HDSD_SIMPLE if simple else HDSD_FULL
        with open(hdsd_path, "w", encoding="utf-8") as f:
            f.write(hdsd_content)
        print(f"[Q{vol_num:2d}] ✓ chapters/huong-dan.tex ({'simple' if simple else 'full'})")

        # --- patch main.tex cho Q2-Q24 ---
        if vol_num >= 2:
            main_tex = os.path.join(vol_dir, "main.tex")
            if os.path.exists(main_tex):
                print(f"[Q{vol_num:2d}] Cập nhật main.tex...")
                patch_main_tex(main_tex, vol_num)
            else:
                print(f"[Q{vol_num:2d}] [WARN] Không tìm thấy main.tex")

    print("\n=== HOÀN THÀNH ===")


if __name__ == "__main__":
    main()
