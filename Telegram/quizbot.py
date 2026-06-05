import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import html
import os

TOKEN = os.environ.get('BOT_TOKEN', '8903255663:AAGH2-Ak0vZx0iw9Bzkr8t3RtPc0LFS84cg')

import os
TOKEN = os.environ.get('BOT_TOKEN', '8903255663:AAGH2-Ak0vZx0iw9Bzkr8t3RtPc0LFS84cg')

def safe_html(text):
    return html.escape(str(text))

QUIZ_DATA = [
    {
        "question": "An`anaviy marketingning bosh g`oyasi",
        "options": [
            "iste`molchiga kerakli narsani ishlab chiqarish",
            "imkoniyat boricha ishlab chiqarish",
            "kam harajat evaziga mahsulot ishlab chiqarish",
            "resurlar tejamkorligiga rioya qilish"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing kontseptsiyasining ma'nosi:",
        "options": [
            "talabni shakllantirish, sotishni takomillashtirish, ishlab chiqarishni odamlar talabini qondirishga yo'naltirish",
            "mahsulot hajmiy o'sishi bilan tannarxining kamayishi odamlar talabini qondirishga yo'naltirish",
            "mahsulot sifatining o'sishi bilan mahsulot sotish hajmining o'sishi va odamlar talabini qondirishga yo'naltirish",
            "mahsulot sifatining o'sishi bilan mahsulot sotish hajmining o'sishi sotishni takomillashtirish"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing sub'ekti nima?",
        "options": [
            "iste'molchi tashkilotlar, ulgurji savdo, marketing bo'yicha mutaxassislar,ishlab chiqaruvchi va xizmat ko'rsatuvchi tashkilot",
            "ishlab chiqaruvchi va xizmat ko'rsatuvchi tashkilot texnologiya va jihozlar",
            "yangi xorijiy sotish bozorlarini qo'shimcha tadqiq qilish firma tovarlarini xorijiy bozorlarida sotishni tashkil etish",
            "marketing bo'yicha mutaxassislar xizmat ko'rsatuvchi tashkilot texnologiya va jihozlar"
        ],
        "correct_index": 0
    },
    {
        "question": "Tadbirkorning marketing majmuasiga kiradi",
        "options": [
            "tovar, hizmat, uning narxi, yetkazib berish va sotish usullari, reklama, sotishni rag'batlantirish",
            "sotuvchi, iste'molchi, haridor o'rtasidagi vositachi",
            "tovar, bozor, raqobat, raqiblar",
            "ishlab chiqarish, ta'minot, sotish, iste'mol"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing so'zining lug'aviy ma'nosi-bu:",
        "options": [
            "market-bozor, ing-harakat",
            "market-do'kon, ing-harakat",
            "market-bozor, ing-qoshish",
            "market-maskan, ing-harakat"
        ],
        "correct_index": 0
    },
    {
        "question": "Imkoning boricha ko'proq tovar ishlab chiqaraver, chunki bozor talabi cheksiz shiori qaysi kontseptsiyaga xos",
        "options": [
            "ishlab chiqarishga yo'naltirilgan kontseptsiya",
            "ijtimoiy-ahloqiy kontseptsiya",
            "iste'molchiga yo'naltirilgan kontseptsiya",
            "sotishga yo'naltirilgan kontseptsiya"
        ],
        "correct_index": 0
    },
    {
        "question": "Mana tovar tayyor kelavering va savdolashing shiori qaysi kontseptsiyaga xos",
        "options": [
            "sotishga yo'naltirilgan kontseptsiya",
            "ishlab chiqarishga yo'naltirilgan kontseptsiya",
            "iste'molchiga yo'naltirilgan kontseptsiya",
            "ijtimoiy-ahloqiy kontseptsiya"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing tadqiqotlari qanday asosiy elementlardan iborat?",
        "options": [
            "ma'lumotlarni tahlil qilish, yig'ish, qayta ishlash",
            "ma'lumotlarni tahlil qilish, o'rganish, qayta ishlash",
            "ma'lumotlarni o'rganish, yig'ish, qayta ishlash",
            "ma'lumotlarni to'plash, yig'ish, qayta ishlash"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing qanday tizimni ifodalaydi?",
        "options": [
            "ishlab chiqarish - iste'mol",
            "ayirboshlash",
            "ishlab chiqarish - sotish",
            "sotish"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketingning asosiy tamoyillarini aniqlang?",
        "options": [
            "bozorni bilish, bozorga moslashish, bozorga ta'sir o'tkazish",
            "haridor va mijozlarning puxta o'rganish, tahlil qilish, tovar harid qilishga undash",
            "reklama, tovar, markalash, narx",
            "analitik, ishlab chiqarish, savdo-sotiq, boshqaruv va nazorat"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing tamoyili nima?",
        "options": [
            "korxonani ishlab chiqarish, sotish faoliyatini boshqarish to'g'risidagi ilmiy asoslangan tasavvurlar tasnifidir",
            "Bozor iqtisodiyoti sharoitida korxonalarning boshqa korxonalar bilan xamkorlik faoliyeti",
            "Bozor iqtisodiyoti sharoitida barcha korxonalar haqida ma'lumotga ega bo'lumish",
            "korxonani ishlab chiqarish faoliyati to'g'risidagi ma'lumotga ega bo'lish"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketingning asosiy funktsiyalarini aniqlang?",
        "options": [
            "analitik, ishlab chiqarish, savdo-sotiq, boshqaruv va nazorat",
            "ishlab chiqarish va tashkil etish",
            "boshqaruv investitsiyalash va nazorat",
            "analiz va boshqaruv"
        ],
        "correct_index": 0
    },
    {
        "question": "Ishlab chiqarishni xom-ashyo resurslari bilan ta'minlash-bu...",
        "options": [
            "marketingni ishlab chiqarish funktsiyasi",
            "marketingni nazorat funktsiyasi",
            "marketingni sotish funktsiyasi",
            "marketingni tashkiliy funktsiyasi"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing turlaridan qaysisi to'g'ri?",
        "options": [
            "remarketing, demarketing, qo'llab-quvvatlovchi, qarama-qarshi harakatlanuvchi",
            "ishlab chiqarish vositalari tovar va xizmatlar",
            "tijorat va notijorat iste'mol tovarlari xizmatlar va boshqalar",
            "tijorat va notijorat iste'mol tovarlari"
        ],
        "correct_index": 0
    },
    {
        "question": "Noratsional ehtiyojlarni qondiruvchi tovar va hizmatlar bo'lgan talabni kamaytirish yoki butunlay yo'q qilishga xizmat qiladi",
        "options": [
            "antimarketing",
            "rivojlantiruvchi marketing",
            "demarketing",
            "konversion marketing"
        ],
        "correct_index": 0
    },
    {
        "question": "Rivojlantiruvchi marketing turi qaysi holatlarda qo'llaniladi?",
        "options": [
            "potentsial talab mavjud, uni real talabga aylantirish kerak bo'lganda",
            "talab pasayib ketganda",
            "taklif ortib ketganda",
            "talab bilan taklif muvozanatlashganda"
        ],
        "correct_index": 0
    },
    {
        "question": "Antimarketing qaysi holatlarda qo'llaniladi?",
        "options": [
            "noratsional ehtiyojlarni qondiruvchi tovar, hizmatlar bo'lgan talabni kamaytirish yoki butunlay yo'q qilishga xizmat qiladi",
            "talab pasaytirishga xizmat qiladi",
            "taklifni ortishiga xizmat qiladi",
            "talab bilan taklif muvozanatlashtiradi"
        ],
        "correct_index": 0
    },
    {
        "question": "Remarketing qaysi holatalarda qo'llaniladi?",
        "options": [
            "talabning pasayishi yuzaga kelganda",
            "taklif ortib ketganda",
            "talab bilan taklif muvozanatlashganda",
            "taklif pasayib ketganda"
        ],
        "correct_index": 0
    },
    {
        "question": "To'g'ridan-to'g'ri marketing nima?",
        "options": [
            "ehtiyojni hisobga olgan holda, firma ishlab chiqargan mahsulotni sotish",
            "kompyuter baza ma'lumotlari asosida mijozlarni o'rganish",
            "ehtiyojni hisobga olmagan holda firma ishlab chiqargan mahsulotini sotish",
            "tovarni savdo vositalarisiz sotish"
        ],
        "correct_index": 0
    },
    {
        "question": "Mavjud talab darajasini saqlab qolish uchun amalga oshiriladigan hatti-harakatlar-bu",
        "options": [
            "qo'llab-quvvatlovchi marketing",
            "rivojlanuvchi marketing",
            "rag'batlantiruvchi marketing",
            "remarketing"
        ],
        "correct_index": 0
    },
    {
        "question": "Rag'batlantiruvchi marketing",
        "options": [
            "talabni uyg'otadi",
            "talabni rag'batlantiradi",
            "talabni pasaytirish",
            "talabni yo'qotadi"
        ],
        "correct_index": 0
    },
    {
        "question": "Demarketing bu",
        "options": [
            "talabni rag'batlantirishni anglatadi",
            "talabni muvozanatlashtirini anglatadi",
            "talabni qo'llashni anglatadi",
            "talabni tugatishni anglatadi"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing muhitini shakllantiruvchi ichki omillar ...",
        "options": [
            "firma rahbariyati tomonidan nazorat qilinadigan - texnologik jarayon, moliyaviy ahvoli, tashkiliy tuzilishi, bozorni tanlash bilan bog'liqdir",
            "firma rahbariyati tomonidan nazorat qilinmaydigan - texnologik jarayon va moliyaviy ahvoli tashkiliy tuzilishi bozorni tanlash bilan bog'liqdir",
            "firma rahbariyati tomonidan nazorat qilinadigan korxonaning moliyaviy ahvoli va bozorni tanlash bilan bog'liqdir",
            "firma rahbariyati tomonidan nazorat qilinmaydigan korxonaning moliyaviy ahvoli va bozorni tanlash bilan bog'liqdir"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing tashqi muhiti omillari ...",
        "options": [
            "tashkilot va uning marketing xizmatlari tomonidan boshqarila olmaydigan, nazorat qilinmaydigan, faoliyatiga ta'sir ko'rsatuvchi tarkibiy qismlardir",
            "tashkilot va uning marketing xizmatlari tomonidan boshqarila olmaydigan faoliyatiga ta'sir ko'rsatuvchi tarkibiy qismlardir",
            "tashkilot va uning marketing xizmatlari tomonidan boshqarila olmaydigan faoliyatiga ta'sir ko'rsatmaydigan tarkibiy qismlardir",
            "tashkilot va uning marketing xizmatlari tomonidan nazorat qilinmaydigan faoliyatiga ta'sir ko'rsatuvchi tarkibiy qismlardir"
        ],
        "correct_index": 0
    },
    {
        "question": "Mikromuhitda quyidagi omillar nazorat qilinadi:",
        "options": [
            "firmaning infratuzilmasini",
            "iste'molchining xatti-harakatini",
            "siyosiy muhitni",
            "raqobatchilarni"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing tizimi bu...",
        "options": [
            "qo'yilgan maqsadlarga erishish, maqsadli bozor talabini qondirish uchun marketing qismlarining aniq birikuvidir",
            "qo'yilgan maqsadlarga erishish uchun marketing qismlarining aniq birikuvidir",
            "maqsadli bozor talabini qondirish uchun marketing qismlarining aniq birikuvidir",
            "maqsadli bozor talabini aniqlash va qondirish uchun marketing qismlarining aniq birikuvidir"
        ],
        "correct_index": 0
    },
    {
        "question": "Ta'minotchilar",
        "options": [
            "alohida olingan tashkilot, uyushma, shaxslar yig'indisidan tarkib topib, firmani moddiy, moliyaviy va mahsulot resurslari bilan ta'minlaydi",
            "alohida olingan tashkilot, uyushma, shaxslar yig'indisidan tarkib topib, firmani moddiy resurslari bilan ta'minlaydi",
            "alohida olingan tashkilot, uyushma, shaxslar yig'indisidan tarkib topib, firmani moliyaviy va mahsulot resurslari bilan ta'minlaydi",
            "alohida olingan tashkilot, uyushma, shaxslar yig'indisidan tarkib topib, firmani moddiy, moliyaviy resurslari bilan ta'minlaydi"
        ],
        "correct_index": 0
    },
    {
        "question": "Bozor strategiyasini shakllantirish, amalga oshirish, axborot bilan ta'minlash qaysi boshqaruv funksiyasiga mos tushadi?",
        "options": [
            "marketingni boshqarish",
            "ishlab chiqarishni boshqarish",
            "moliyaviy boshqarish",
            "kadrlarni boshqarish"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing bo'yicha vositachilar",
        "options": [
            "tashkilot uchun uning tovarlarini mijozlarga yetkazish, sotish, aloqa o'rnatish bo'yicha yordam ko'rsatuvchilardir",
            "tashkilot uchun uning tovarlarini mijozlarga yetkazish, aloqa o'rnatish bo'yicha yordam ko'rsatuvchilardir",
            "tashkilot uchun uning tovarlarini mijozlarga yetkazish sotish bo'yicha yordam ko'rsatuvchilardir",
            "tashkilot uchun uning tovarlarini sotish aloqa o'rnatish bo'yicha yordam ko'rsatuvchilardir"
        ],
        "correct_index": 0
    },
    {
        "question": "Iste'molchilar",
        "options": [
            "firmalar, alohida fizik shaxslar yoki ularni potentsial guruhi bo'lib, ular bozorda mavjud bo'lgan tovar va xizmatlarni olishga tayyor",
            "alohida fizik shaxslar yoki ularni potentsial guruhi bo'lib ular bozorda mavjud bo'lgan tovar va xizmatlarni olishga tayyor",
            "firmalar va ularni potentsial guruhi bo'lib ular bozorda mavjud bo'lgan tovar va xizmatlarni olishga tayyor",
            "alohida fizik va jismoniy shaxslar bo'lib ular bozorda mavjud bo'lgan tovar va xizmatlarni olishga tayyor"
        ],
        "correct_index": 0
    },
    {
        "question": "Raqobatchilar",
        "options": [
            "istak bo'yicha, safdosh tovar bo'yicha, tovar turi bo'yicha turkumlanadi",
            "alohida olingan tashkilot va uyushma, shaxslar guruhidan tashkil topib firmani moddiy moliyaviy va mahsulot resurslari bilan ta'minlaydi",
            "tashkilot uchun uning tovarlarini mijozlarga yetkazish bo'yicha yordam ko'rsatuvchilar",
            "innovatsiyalarni tadqiq etuvchilar"
        ],
        "correct_index": 0
    },
    {
        "question": "Vertikal marketing tizimi deganda nimani tushunasiz?",
        "options": [
            "bu taqsimot kanallarining shunday strukturasiki, unda ishlab chiqaruvchilar, ulgurji va chakana savdogarlar yagona bitta tizim sifatida faoliyat yuritadilar",
            "bu taqsimot kanallarining shunday strukturasiki unda faqat ishlab chiqaruvchilar va ulgurji savdogarlar yagona bitta tizim sifatida faoliyat yuritadilar",
            "ishlab chiqaruvchilar ham ulgurji va chakana savdogarlar ham alohida-alohida tizim sifatida faoliyat yuritadilar",
            "brokerlar tizimi"
        ],
        "correct_index": 0
    },
    {
        "question": "Vertikal marketing tizimining qanday shakllari mavjud?",
        "options": [
            "bevosita, bilvosita",
            "kuchli va o'rta kuchsiz",
            "shartnoma asosidagi korporativ va ma'muriy",
            "muntazam va nomuntazam"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing tizimi tarkibiga qaysi elementlarni qamrab oladi?",
        "options": [
            "ta'minotchilar, raqobatchilar, iste'molchilar, vositachilar, firma",
            "ta'minotchilar, iste'molchilar, auditorlar, vositachilar",
            "iste'molchilar, auditorlar, firma, ta'minotchilar",
            "firma, raqobatchilar, vositachilar, auditorlar"
        ],
        "correct_index": 0
    },
    {
        "question": "Birlamchi ma'lumotlar manbaalari nimalardan iborat?",
        "options": [
            "kuzatish",
            "so'rov",
            "eksperiment",
            "shaxsiy uchrashuv"
        ],
        "correct_index": 0
    },
    {
        "question": "Qayd etilganlardan qaysi biri reklama vositalariga kirmaydi?",
        "options": [
            "mexanik, fizik, bioreklamalar",
            "bosma reklama",
            "transport vositalari yordamidagi reklama",
            "televidenie va radio reklama vositalari"
        ],
        "correct_index": 0
    },
    {
        "question": "Quyidagilardan qaysi biri reklama turlariga mansub emas?",
        "options": [
            "majburlovchi",
            "uyg'otuvchi (undovchi)",
            "ma'lumot beruvchi",
            "taqqoslama"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing Dasturlari qanday muddatga mo'ljallangan bo'ladi?",
        "options": [
            "qisqa muddatli, o'rta muddatli, uzoq muddatli",
            "qisqa muddatli va uzoq muddatli",
            "qisqa muddatli",
            "faqat uzoq muddatli"
        ],
        "correct_index": 0
    },
    {
        "question": "Makromarketing nima degani?",
        "options": [
            "makromarketing mamlakatning jami xo'jaligi miqyosidagi mahsulotlarni yaratish, uning pirovard iste'molchiga tomon ko'chishi",
            "butun mamlakat bo'yicha moddiy boyliklarni va xizmatlar okimini boshqarishni tartibga solishdan iborat",
            "kontsern va assotsiatsiya vazirliklar darajasidagi bozor muammolarining yechimini topish",
            "korxona miqyosidagi bozor faoliyati"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing maqsadlarining to'g'risini aniqlang?",
        "options": [
            "ehtiyojni qondirish darajasini ko'tarish, foydani oshirish, bozorga yangi tovarlar chiqarish",
            "korxona va tovarlar to'g'risida yaxshi fikrlarni shakllantirish",
            "mo'ljallangan bozorni egallash va g'oyalar sotishni ko'paytirish",
            "ehtiyojni qondirish darajasini ko'tarish va foydani oshirish"
        ],
        "correct_index": 0
    },
    {
        "question": "Nol bosqichli kanal ishtirokchilari kimlar",
        "options": [
            "ishlab chiqaruvchi, iste'molchi",
            "vositachi va iste'molchi",
            "ishlab chiqaruvchi va vositachi",
            "ishlab chiqaruvchi vositachi va iste'molchi"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing strategiyasi-bu",
        "options": [
            "maqsadga erishish uchun, qanday harakat qilish kerak degan savolga javob izlash",
            "ishlab chiqarishni tashkil etish",
            "sotishni rag'batlantirish",
            "iste'molchilarni qo'llab-quvvatlash"
        ],
        "correct_index": 0
    },
    {
        "question": "Taktika deganda nimani tushunasiz?",
        "options": [
            "marketing aniq yo'naltirilgan amaliyotini tanlash",
            "marketing faoliyatini boshqarish",
            "mahsulot assortimenti rejalashtirish va savdoga rag'bat beradigan tadbirlarni shakllantirish",
            "savdo va taqsimot, marketing faoliyatini boshqarish va nazorat qilish"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing faoliyatini bajarilishini nazorat qilishning qanday turlarini bilasiz?",
        "options": [
            "yillik rejani bajarilishini nazorat qilish, foydadorlikni nazorat qilish, strategik nazorat",
            "strategik nazorat",
            "foydadorlikni nazorat qilish",
            "yillik rejani bajarilishini nazorat qilish, strategic nazorat"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing-MIKS ning asosiy to'ldiruvchilarini aniqlang?",
        "options": [
            "narx, mahsulot, o'rin joy, siljish harakat",
            "tovar, pul, munosabat, mijoz, tadqiqot",
            "tovar, pul, ehtiyoj, talab, taklif",
            "narx, taklif, talab, ehtiyoj, haridorlar"
        ],
        "correct_index": 0
    },
    {
        "question": "Kon'yuktura nima?",
        "options": [
            "u bozorda ma'lum bir vaqtda talab va taklif nisbati bilan bog'liq bo'lgan narxlar darajasi orqali yuzaga keladigan iqtisodiy holat",
            "u bozorda ma'lum bir vaqtda talab va narx nisbati orqali yuzaga keladigan iqtisodiy holat",
            "u bozorda talab va narx nisbati orqali vujudga kelayotgan talabdan iborat",
            "u bozorda talab va narx nisbati orqali vujudga keladigan taklifdan iborat"
        ],
        "correct_index": 0
    },
    {
        "question": "Konyuktura so'zining lug'aviy ma'nosi nima?",
        "options": [
            "lotincha holat",
            "inglizcha masofa",
            "lotincha oraliq",
            "yunoncha masofa"
        ],
        "correct_index": 0
    },
    {
        "question": "Bozor innovatsiyasi deganda nima tushuniladi?",
        "options": [
            "yangi mahsulotlarni bozorga chiqarish",
            "yangi mahsulotlarni ishlab chiqish",
            "mahsulot bo'yicha yangi g'oyalar olish",
            "yangi mahsulot bo'yicha reklama uyushtirish"
        ],
        "correct_index": 0
    },
    {
        "question": "Bozor infrastrukturasi nima?",
        "options": [
            "bozor iqtisodiyoti uchun xizmat ko'rsatuvchi, har-xil sohalar tushuniladi",
            "bozordagi talab va taklifni miqdordan va tarkiban bir-biriga muvofiq kelishib tushuniladi",
            "bozor muvozanatining mavjudligi yoki buzulganligi tushuniladi",
            "bozordagi talab va taklifni miqdordan va tarkiban bir-biriga nomuvofiq kelishib tushuniladi"
        ],
        "correct_index": 0
    },
    {
        "question": "Bozor mohiyatini aniqlang?",
        "options": [
            "bozor- mavjud, potentsial haridorlarning majmui",
            "bozor-tovarlarni taklif qilish joyi",
            "bozor-iqtisodiy ayriboshlash joyi",
            "oldi-sotdi munosabatlari yig'indisi"
        ],
        "correct_index": 0
    },
    {
        "question": "Bozor turlaridan qaysilari to'g'ri?",
        "options": [
            "iste'mol tovarlari, ishlab chiqarish vositalari bozori va xizmatlar, qimmatli qog'ozlar, intellektual tovarlar va boshqalar",
            "ishlab chiqarish vositalari bozori agrofirma va halq xo'jaligi ta'minoti",
            "jahon bozori regional bozor va boshqalar",
            "mahalliy bozor va dehqon bozori iste'molchi bozori"
        ],
        "correct_index": 0
    },
    {
        "question": "Bozorga yorib kirish strategiyasining mohiyatini aniqlang?",
        "options": [
            "tovarlarning boshlang'ich bahosi past o'rnatilib, talab rag'batlantiradi, bozorda asosiy ulushni egallab, narx oshiriladi",
            "tovarlar ko'p miqdorda ishlab chiqarilib, yuqori narx belgilanadi",
            "past bahoda, oz miqdorda tovarlar bilan bozorga kiriladi",
            "bozordagi narx bilan tovar ishlab chiqariladi va bozorda o'z o'rnini egallaydi"
        ],
        "correct_index": 0
    },
    {
        "question": "Tovarning yashash davri bosqichlarini ketma-ketligining to'g'riligini ko'rsating?",
        "options": [
            "tatbiq qilish, o'sish, yetuklik, to'yinish, pasayish",
            "to'yinish, tadbiq qilish, o'sish, yetuklik",
            "etuklik, o'sish, pasayish, tadbiq qilish",
            "o'sish, yetuklik, pasayish, to'yinish"
        ],
        "correct_index": 0
    },
    {
        "question": "Tovar belgisi qanday vazifani bajaradi?",
        "options": [
            "sifat kafolati, individuallik va himoya qilish",
            "marka nomi va marka belgisi",
            "tovar sifati va xizmat qilish muddati",
            "individuallik va himoya qilish, kafolatlash"
        ],
        "correct_index": 0
    },
    {
        "question": "Mebel, gilam, telefon, kir yuvish mashinasi tovarning qaysi turiga mansub?",
        "options": [
            "tanlab olinadigan tovarlar",
            "alohida ehtiyojdagi tovarlar",
            "passiv tovarlar",
            "impulsiv tarzda sotib olinadigan tovarlar"
        ],
        "correct_index": 0
    },
    {
        "question": "Tovarni qaysi hayotiylik davrida firma yuqori foyda oladi?",
        "options": [
            "yuksalish",
            "pasayish",
            "hayotga tadbiq etish",
            "etilish"
        ],
        "correct_index": 0
    },
    {
        "question": "General Motors uchun GM- bu...",
        "options": [
            "marka belgisi",
            "tovar markasi",
            "marka nomi",
            "tovar belgisi"
        ],
        "correct_index": 0
    },
    {
        "question": "Coca-cola bu ...",
        "options": [
            "marka nomi",
            "tovar belgisi",
            "tovar markasi",
            "marka belgisi"
        ],
        "correct_index": 0
    },
    {
        "question": "Impulsiv tarzda sotib olinadigan tovarlarga qaysilar kiradi?",
        "options": [
            "saqich, gazeta, kitob",
            "oziq ovqat mahsulotlari",
            "zontik sharf",
            "mashina va uy"
        ],
        "correct_index": 0
    },
    {
        "question": "Demping narx bu ...",
        "options": [
            "tovarni o'z tannarxidan arzon sotish",
            "tovarni bozor narxida sotish",
            "ko'zlangan foydani keltiruvchi narx belgilash san'ati",
            "tovarni bozor narxidan qimmatga sotish"
        ],
        "correct_index": 0
    },
    {
        "question": "SWOT tahlili-bu",
        "options": [
            "ichki imkoniyatlar, ichki xavf-xatar, tashqi imkoniyatlar, tashqi xavf-xatar",
            "ichki imkoniyatlar va ichki xavf-xatar",
            "tashqi imkoniyatlar va tashqi xavf-xatar",
            "ichki imkoniyatlar"
        ],
        "correct_index": 0
    },
    {
        "question": "Monopoliya nima?",
        "options": [
            "bozorda bitta ishlab chiqaruvchi ko'pchilik xaridorlarga xizmat ko'rsatadi",
            "Tadbirkorlarning erkinligi",
            "ko'p sonli kichik firmalarning raqobatlashuvi",
            "bozorda ishlab chiqaruvchilar soni juda ko'p bo'lib, xaridorlarga xizmat qiladilar"
        ],
        "correct_index": 0
    },
    {
        "question": "Monopsoniya- bu",
        "options": [
            "tanho iste'molchining hukmronligi",
            "bozorda u qadar ko'p bo'lmagan iste'molchilarning hukmronligi",
            "bozorda ishlab chiqaruvchilar soni juda ko'p bo'lib, xaridorlarga xizmat qiladilar",
            "tarmoqda u qadar ko'p bo'lmagan korxonalarning hukmronlik qilishi"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing fanining asosiy maqsadi nimadan iborat?",
        "options": [
            "Mamnun xaridorlardan foyda olish ilmlarini tashkillashtirish",
            "Sotuv hajmini oshirish",
            "Reklama siyosatini rivojlantirish",
            "Xaridorlar e'tirozlarini maksimal bartaraf etish"
        ],
        "correct_index": 0
    },
    {
        "question": "Tovarlarning hayotiy tsikli qanday fazalardan iborat",
        "options": [
            "vujudga kelish, o'sish, etuklik, so'nish",
            "narx, manzil, tovar va reklama",
            "moda, stil, fetish",
            "brend, marka, promoshn"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing- inson faoliyati turi bo'lib, zarurat va ehtiyojlarni ayirboshlash vositasida qondirishga yo'naltirilgan degan ibora qaysi olimga taaluqli",
        "options": [
            "Filip Kotlerga",
            "Genri Fordga",
            "Benedjamin Franklinga",
            "Garri Kisenjerga"
        ],
        "correct_index": 0
    },
    {
        "question": "Marketing nazariyasi va amaliyoti qaysi davlatda ilk bor amaliy qaror topdi",
        "options": [
            "AQShda",
            "Xitoyda",
            "Buyuk Britaniyada",
            "Germaniyada"
        ],
        "correct_index": 0
    },
    {
        "question": "Raqamli marketing davri nechanchi yildan boshlab rivojlana boshladi",
        "options": [
            "2000 yildan boshlab",
            "2025 yilda boshlanishi bashorat etilmoqda",
            "1960 yildan boshlab",
            "1945 yildan boshlab"
        ],
        "correct_index": 0
    },
    {
        "question": "Raqobat bu:",
        "options": [
            "bozor iqtisodiyoti sharoitida o'z mavqeini mustahkamlash uchun kurash",
            "Majburiy safarbarlik",
            "sotsialistik musobaqa",
            "tovar ishlab chiqaruvchiga tanho hukmronlikni ta'minlab beruvchi dastak"
        ],
        "correct_index": 0
    },
    {
        "question": "Savdo vositachilari",
        "options": [
            "ulgurji, chakana savdogarlar",
            "bank kredit sug'urta va boshqa moliyaviy xizmatlarni amalga oshiradi",
            "savdo va logistik, marketing vositachilariga bo'linadi",
            "ombor tizimi xizmatlarida tovar va oqim harakatlarini transportirovka qilish bilan shug'ullanadi"
        ],
        "correct_index": 0
    },
    {
        "question": "Moliyaviy vositachilar",
        "options": [
            "bank, kredit, sug'urta va boshqa moliyaviy xizmatlarni amalga oshiradi",
            "savdo va logistik, marketing vositachilariga bo'linadi",
            "ulgurji va chakana savdogarlar",
            "ombor tizimi xizmatlarida tovar va oqim harakatlarini transportirovka qilish bilan shug'ullanadi"
        ],
        "correct_index": 0
    },
    {
        "question": "Logistika vositachilari",
        "options": [
            "ombor tizimi xizmatlarida tovar, oqim harakatlarini transportirovka qilish bilan shug'ullanadi",
            "savdo, logistik, marketing vositachilariga bo'linadi",
            "ulgurji va chakana savdogarlar",
            "bank kredit sug'urta va boshqa moliyaviy xizmatlarni amalga oshiradi"
        ],
        "correct_index": 0
    },
    {
        "question": "Brokerlar- bu",
        "options": [
            "ishlab chiqaruvchi bilan iste'molchini uchrashtiruvcbi firmalar",
            "turli mamlakatlarda eksport ishlarini bajaradigan firmalar",
            "turli mamlakatlarda import ishlarini bajaradigan firmalar",
            "qimmatli qog'ozlar metallar oldi-sotdisi bilan shug'ullanadigan firmalar"
        ],
        "correct_index": 0
    },
    {
        "question": "Neposredstvennaya distributsiyani tanlashning afzalliklari nimada?",
        "options": [
            "Mijoz bilan bevosita aloqa o'rnatish va taqsimot jarayonini to'liq nazorat qilish",
            "Mahsulot tannarxining haddan tashqari oshishi",
            "Savdo kanallari sonining kamayib ketishi",
            "Raqobatchilar bilan hamkorlik qilish zarurati"
        ],
        "correct_index": 0
    },
]

for i, quiz in enumerate(QUIZ_DATA):
    shift = i % 4
    quiz["options"] = quiz["options"][-shift:] + quiz["options"][:-shift]
    quiz["correct_index"] = (quiz["correct_index"] + shift) % 4

@bot.message_handler(commands=['start', 'quiz'])
def send_quiz(message):
    q_index = random.randint(0, len(QUIZ_DATA) - 1)
    quiz = QUIZ_DATA[q_index]

    text = f"❓ <b>Savol:</b> {safe_html(quiz['question'])}\n\n"

    labels = ['A', 'B', 'C', 'D']
    markup = InlineKeyboardMarkup()
    btn_row = []

    for i, option in enumerate(quiz['options']):
        text += f"<b>{labels[i]})</b> {safe_html(option)}\n\n"
        btn_row.append(InlineKeyboardButton(text=labels[i], callback_data=f"quiz_{q_index}_{i}"))

    markup.row(*btn_row)
    bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data.startswith('quiz_'))
def check_answer(call):
    _, q_idx, chosen_idx = call.data.split('_')
    q_idx = int(q_idx)
    chosen_idx = int(chosen_idx)

    quiz = QUIZ_DATA[q_idx]
    correct_idx = quiz['correct_index']
    labels = ['A', 'B', 'C', 'D']

    original_text = call.message.text

    if chosen_idx == correct_idx:
        answer_text = f"\n🎉 <b>To'g'ri!</b> Javobingiz: <b>{labels[chosen_idx]}</b>"
    else:
        answer_text = f"\n❌ <b>Noto'g'ri.</b> Siz {labels[chosen_idx]} variantni tanladingiz.\n"
        answer_text += f"✅ To'g'ri javob: <b>{labels[correct_idx]})</b> {safe_html(quiz['options'][correct_idx])}"

    next_markup = InlineKeyboardMarkup()
    next_markup.add(InlineKeyboardButton(text="➡️ Keyingi savol", callback_data="next_question"))

    try:
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=original_text + f"\n\n---\n{answer_text}",
            reply_markup=next_markup,
            parse_mode="HTML"
        )
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

@bot.callback_query_handler(func=lambda call: call.data == "next_question")
def next_question(call):
    try:
        bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            reply_markup=None
        )
    except Exception:
        pass
    send_quiz(call.message)

print("Quiz Bot muvaffaqiyatli ishga tushdi...")
bot.polling(none_stop=True)