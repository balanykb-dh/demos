"""Дані бізнесів для демо. Усі факти (адреса, телефон, графік, рейтинг) — з Google Maps.
Опис послуг спирається на категорію в Maps і відгуки; цін і вигаданих відгуків немає."""

S = 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'


def icon(paths: str) -> str:
    return f'<svg viewBox="0 0 48 48" {S} aria-hidden="true">{paths}</svg>'


# ------------------------------------------------------------------ шиномонтаж
def tire_svg() -> str:
    blocks = "".join(
        f'<rect x="143" y="12" width="14" height="24" rx="2" fill="#363C42" transform="rotate({i * 10} 150 150)"/>'
        for i in range(36))
    spokes = "".join(
        f'<rect x="143" y="80" width="14" height="52" rx="7" fill="url(#rim)" transform="rotate({k * 72} 150 150)"/>'
        for k in range(5))
    return f'''<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="rim" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E6E9EC"/><stop offset="1" stop-color="#8E959C"/></linearGradient></defs>
<g class="tire"><circle cx="150" cy="150" r="142" fill="#24282C"/>{blocks}
<circle cx="150" cy="150" r="112" fill="#2E3338"/><circle cx="150" cy="150" r="104" fill="none" stroke="#3B4147" stroke-width="3"/>
<circle cx="150" cy="150" r="80" fill="#5C636A"/><circle cx="150" cy="150" r="74" fill="#2E3338"/>{spokes}
<circle cx="150" cy="150" r="22" fill="url(#rim)"/><circle cx="150" cy="150" r="8" fill="#F2B01E"/></g></svg>'''


TIRE_LOGO = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="5" fill="#2B3035"/>'
             '<circle cx="16" cy="16" r="9.5" fill="none" stroke="#F2B01E" stroke-width="4"/><circle cx="16" cy="16" r="3" fill="#F2B01E"/></svg>')

SHYNOMONTAZH = dict(
    slug="shynomontazh-stryiska-12", theme="asphalt", schema_type="TireShop",
    name="Шиномонтаж цілодобово", short_address="Стрийська, 12",
    brand_sub="Сокільники, вул. Стрийська, 12",
    meta_description="Шиномонтаж у Сокільниках на вул. Стрийській, 12: працюємо цілодобово, є генератор. Сезонна заміна шин, балансування, ремонт проколів.",
    og_description="Працюємо цілодобово, навіть під час відключень. Подивіться з телефону.",
    h1="Шиномонтаж цілодобово на Стрийській",
    lead="Працюємо 24/7, навіть коли вимикають світло: є генератор. Перевзуємо, відбалансуємо й залатаємо прокол у порядку живої черги.",
    phone="096 550 3501", phone_e164="+380965503501",
    rating_text="4,7", reviews_text="348 відгуків",
    services_title="Що робимо", services_lead="Ціну й чергу підкажемо телефоном.",
    tiles=[
        dict(name="Сезонна заміна шин", icon=icon('<circle cx="24" cy="24" r="18"/><circle cx="24" cy="24" r="8"/><path d="M24 6v4M24 38v4M6 24h4M38 24h4M11.3 11.3l2.8 2.8M33.9 33.9l2.8 2.8M11.3 36.7l2.8-2.8M33.9 14.1l2.8-2.8"/>')),
        dict(name="Балансування коліс", icon=icon('<circle cx="22" cy="24" r="16"/><circle cx="22" cy="24" r="5"/><rect x="36" y="18" width="7" height="12" rx="2"/><path d="M22 8v3M22 37v3"/>')),
        dict(name="Ремонт проколів", note="Зловили шуруп? Залатаємо.", icon=icon('<path d="M5 36a19 19 0 0 1 38 0"/><path d="M11 36a13 13 0 0 1 26 0"/><path d="M24 7v17"/><path d="M20 7h8"/><path d="M21 12l6 2M21 16l6 2M21 20l6 2"/>')),
        dict(name="Перевірка тиску", icon=icon('<path d="M8 32a16 16 0 1 1 32 0"/><path d="M24 32l7-9"/><circle cx="24" cy="32" r="2.5"/><path d="M8 32h32"/><path d="M13 22l2 1M35 22l-2 1M24 16v2"/>')),
    ],
    cta_tile="Не знаєте, чи можна залатати? Надішліть фото колеса", cta_tile_go="Фото у Viber",
    band=dict(title="Увечері черга менша",
              text="Найменше машин зазвичай після 20:00. Подзвоніть перед виїздом, і ми скажемо, скільки машин попереду.",
              viber=None, call="Запитати про чергу"),
    why_title="Чому сюди їдуть",
    why=[("Цілодобово, без вихідних", "Пробили колесо вночі чи у вихідний — приїжджайте, ми працюємо."),
         ("Є генератор", "Відключення світла роботі не заважають."),
         ("Швидко, у порядку живої черги", "Без запису: приїхали, зробили, поїхали далі."),
         ("Підкажемо телефоном", "Скажемо, коли краще підʼїхати, щоб не чекати.")],
    steps_title="Як усе відбувається",
    steps=[("Подзвоніть", "Запитайте, скільки машин у черзі, або просто приїжджайте."),
           ("Приїжджайте на Стрийську, 12", "Ми в Сокільниках і працюємо цілодобово."),
           ("Їдьте далі", "Перевзуємо чи полагодимо колесо, і можна їхати.")],
    form=dict(title="Передзвонимо вам", lead="Залиште номер, і ми передзвонимо: підкажемо ціну й коли краще приїхати.",
              need_label="Авто й розмір шин", need_placeholder="Наприклад: Skoda Octavia, 205/55 R16",
              button="Передзвоніть мені", aside=None),
    faq=[("Ви справді працюєте вночі?", "Так, цілодобово й без вихідних."),
         ("Що буде, якщо вимкнуть світло?", "У нас є генератор, тож працюємо й під час відключень."),
         ("Чи треба записуватися?", "Ні, обслуговуємо в порядку живої черги. Подзвоніть перед виїздом, і ми скажемо, скільки машин попереду."),
         ("Де ви знаходитеся?", "У Сокільниках, на вул. Стрийській, 12.")],
    address_display="с. Сокільники, вул. Стрийська, 12", address_note=None,
    street="вул. Стрийська, 12", locality="Сокільники", postal="79000",
    geo=(49.7810558, 24.0133064), place_id="ChIJ8_l7iwXnOkcR7s3DJs-YS34",
    hours="24/7",
    logo_svg=TIRE_LOGO, hero_svg=tire_svg(),
)

# ------------------------------------------------------------------ перетяжка меблів
SWATCHES = '''<svg viewBox="0 0 280 320" xmlns="http://www.w3.org/2000/svg">
<g class="swatch" style="--r:-16deg"><rect x="80" y="40" width="120" height="250" rx="10" fill="#8FA58B"/><rect x="90" y="50" width="100" height="230" rx="6" fill="none" stroke="#fff" stroke-opacity=".55" stroke-width="2" stroke-dasharray="6 6"/></g>
<g class="swatch" style="--r:14deg"><rect x="80" y="40" width="120" height="250" rx="10" fill="#C98E9A"/><rect x="90" y="50" width="100" height="230" rx="6" fill="none" stroke="#fff" stroke-opacity=".55" stroke-width="2" stroke-dasharray="6 6"/></g>
<g><rect x="80" y="40" width="120" height="250" rx="10" fill="#C9962B"/><rect x="90" y="50" width="100" height="230" rx="6" fill="none" stroke="#fff" stroke-opacity=".6" stroke-width="2" stroke-dasharray="6 6"/><circle cx="140" cy="80" r="9" fill="#fff" fill-opacity=".9"/></g>
</svg>'''

VELVET_LOGO = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#4A2C4F"/>'
               '<rect x="5" y="5" width="22" height="22" rx="5" fill="none" stroke="#C9962B" stroke-width="1.6" stroke-dasharray="3 2.5"/>'
               '<circle cx="16" cy="16" r="4" fill="#C9962B"/></svg>')

PERETYAZHKA = dict(
    slug="peretyazhka-shyroka-31", theme="velvet", schema_type="LocalBusiness",
    name="Перетяжка меблів", short_address="Широка, 31",
    brand_sub="майстерня на Широкій, 31",
    meta_description="Перетяжка диванів, крісел і стільців у Львові на вул. Широкій, 31. Заміна наповнювача, чохли на замовлення.",
    og_description="Перетяжка диванів, крісел і стільців. Подивіться з телефону.",
    h1="Перетяжка диванів, крісел і стільців",
    lead="Майстерня на вул. Широкій, 31. Замінимо тканину й наповнювач, пошиємо чохли, і старі меблі виглядатимуть як нові. Надішліть фото, і ми підкажемо, що можна зробити.",
    phone="067 670 5384", phone_e164="+380676705384",
    rating_text="4,8", reviews_text="135 відгуків",
    services_title="Що перетягуємо",
    services_lead="Вартість залежить від розміру меблів і тканини. Орієнтовну ціну скажемо за фото.",
    tiles=[
        dict(name="Дивани", icon=icon('<path d="M7 22v-6a4 4 0 0 1 4-4h26a4 4 0 0 1 4 4v6"/><path d="M4 25a3 3 0 0 1 6 0v6h28v-6a3 3 0 0 1 6 0v9H4z"/><path d="M8 34v4M40 34v4"/><path d="M24 14v12" stroke-dasharray="2 3"/>')),
        dict(name="Крісла", icon=icon('<path d="M13 22v-8a5 5 0 0 1 5-5h12a5 5 0 0 1 5 5v8"/><path d="M8 25a3 3 0 0 1 6 0v6h20v-6a3 3 0 0 1 6 0v9H8z"/><path d="M12 34v5M36 34v5"/>')),
        dict(name="Стільці", icon=icon('<path d="M15 6h18v18H15z"/><path d="M13 24h22v6H13z"/><path d="M15 30v12M33 30v12"/><path d="M19 11h10" stroke-dasharray="2 3"/>')),
        dict(name="Заміна наповнювача", icon=icon('<rect x="8" y="10" width="32" height="8" rx="2"/><rect x="8" y="20" width="32" height="8" rx="2"/><rect x="8" y="30" width="32" height="8" rx="2"/><path d="M14 14h.01M22 14h.01M30 14h.01M18 24h.01M26 24h.01M34 24h.01M14 34h.01M22 34h.01M30 34h.01"/>')),
        dict(name="Чохли на замовлення", note="Навіть для масажних столів.", icon=icon('<path d="M13 8h22l5 26H8z"/><path d="M8 34h32"/><path d="M14 34v6M34 34v6"/><path d="M13 15h22" stroke-dasharray="2 3"/>')),
    ],
    cta_tile="Надішліть фото меблів, і ми оцінимо роботу", cta_tile_go="Фото у Viber",
    band=dict(title="Фото «до» і «після»",
              text="Подивіться, як змінюються меблі після перетяжки.",
              extra_html='<div class="ba"><div class="ba__frame"><b>До</b><span>Тут буде фото меблів до перетяжки</span></div><div class="ba__frame"><b>Після</b><span>А тут результат</span></div></div>',
              viber="Надіслати фото у Viber", call="Подзвонити"),
    why_title="Чому нам довіряють меблі",
    why=[("Як нові", "Після перетяжки дивани й крісла виглядають так, ніби їх щойно купили."),
         ("Тканина й колір на ваш смак", "Підберемо матеріал разом із вами."),
         ("Беремося за нестандартне", "Шиємо чохли навіть для масажних столів."),
         ("У домовлені строки", "Строк погоджуємо до початку роботи.")],
    steps_title="Як замовити",
    steps=[("Надішліть фото", "Сфотографуйте меблі й надішліть у Viber або подзвоніть."),
           ("Узгодимо тканину й ціну", "Підкажемо матеріал, назвемо вартість і строк."),
           ("Отримайте оновлені меблі", "Домовимося, як доставити меблі в майстерню і назад.")],
    form=dict(title="Оцінимо вартість", lead="Залиште номер, і ми передзвонимо, щоб обговорити роботу.",
              need_label="Що треба перетягнути", need_placeholder="Наприклад: кутовий диван і два крісла",
              button="Передзвоніть мені", aside='Фото меблів зручніше надіслати <a href="viber://chat?number=%2B380676705384">у Viber</a>.'),
    faq=[("Скільки коштує перетяжка?", "Залежить від розміру меблів, тканини й наповнювача. Надішліть фото у Viber, і ми назвемо орієнтовну ціну."),
         ("Чи можна вибрати тканину?", "Так, підберемо тканину й колір разом із вами."),
         ("Чи міняєте наповнювач?", "Так, можемо замінити наповнювач під час перетяжки."),
         ("Скільки триває робота?", "Залежить від обсягу. Точний строк назвемо, коли узгодимо замовлення.")],
    address_display="вул. Широка, 31, Львів", address_note=None,
    street="вул. Широка, 31", locality="Львів", postal="79052",
    geo=(49.8421872, 23.9758465), place_id="ChIJQapDQtfdOkcRvpCeVBFZlSw",
    hours={1: (9, 18), 2: (9, 18), 3: (9, 18), 4: (9, 18), 5: (9, 18), 6: None, 0: None},
    logo_svg=VELVET_LOGO, hero_svg=SWATCHES,
)

# ------------------------------------------------------------------ ательє
NEEDLE = '''<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="steel" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F2F4F7"/><stop offset="1" stop-color="#8C95A3"/></linearGradient></defs>
<path class="thread" d="M222 70c40 10 52 60 18 86-30 23-80 2-104 34-20 27 4 66 46 64" fill="none" stroke="#B23A2E" stroke-width="3.5" stroke-linecap="round"/>
<g transform="rotate(45 150 150)"><path d="M150 18c5 0 8 4 8 9v196l-8 60-8-60V27c0-5 3-9 8-9z" fill="url(#steel)"/>
<rect x="146" y="30" width="8" height="30" rx="4" fill="#FAFAF8"/></g>
</svg>'''

TAPE_LOGO = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="4" fill="#22324D"/>'
             '<rect x="4" y="20" width="24" height="7" fill="#F0C43A"/><path d="M8 20v3M12 20v2M16 20v3M20 20v2M24 20v3" stroke="#22324D" stroke-width="1"/>'
             '<path d="M9 16L22 5" stroke="#fff" stroke-width="2" stroke-linecap="round"/><circle cx="20.5" cy="6.5" r="1.2" fill="#22324D"/></svg>')

VINTAZH = dict(
    slug="atelie-vintazh-chervonoyi-kalyny-36", theme="tape", schema_type="LocalBusiness",
    name="Ательє «Вінтаж»", short_address="Червоної Калини, 36",
    brand_sub="ремонт і пошиття одягу",
    meta_description="Ательє «Вінтаж» у ТК «Шувар» на просп. Червоної Калини, 36: ремонт і пошиття одягу, вкорочення штанів, ремонт курток і пуховиків.",
    og_description="Ремонт і пошиття одягу на Сихові. Подивіться з телефону.",
    h1="Ремонт і пошиття одягу на Червоної Калини",
    lead="Вкоротимо штани, відремонтуємо куртку чи пуховик, підженемо сукню до свята. Прості роботи часто робимо за кілька годин.",
    phone="067 797 5912", phone_e164="+380677975912",
    rating_text="4,9", reviews_text="172 відгуки",
    services_title="Що робимо", services_lead="Ціну й строк назвемо, коли побачимо річ.",
    tiles=[
        dict(name="Вкорочення штанів і джинсів", icon=icon('<path d="M14 6h20l2 36h-8l-4-24-4 24h-8z"/><path d="M12 35h10M26 35h10" stroke-dasharray="2 3"/>')),
        dict(name="Ремонт курток і пуховиків", icon=icon('<path d="M18 6l6 4 6-4 10 6-4 8-4-2v24H16V18l-4 2-4-8z"/><path d="M24 10v32"/><path d="M16 24h16M16 31h16"/>')),
        dict(name="Підгонка суконь і костюмів", icon=icon('<path d="M19 6h10l-2 8 9 28H12l9-28z"/><path d="M21 14h6"/><path d="M15 33c3 2 6 2 9 0s6-2 9 0" stroke-dasharray="2 3"/>')),
        dict(name="Заміна блискавок", icon=icon('<path d="M24 6v18"/><path d="M20 9h4M24 13h4M20 17h4M24 21h4"/><rect x="19" y="24" width="10" height="9" rx="2"/><path d="M24 33v5"/><circle cx="24" cy="40" r="2"/>')),
        dict(name="Пошиття на замовлення", icon=icon('<circle cx="14" cy="34" r="5"/><circle cx="14" cy="14" r="5"/><path d="M18 17l22 15M18 31l22-15"/>')),
    ],
    cta_tile="Не знаєте, чи можна врятувати річ? Надішліть фото", cta_tile_go="Фото у Viber",
    band=dict(title="Потрібно терміново?",
              text="До свята чи до вечора? Подзвоніть заздалегідь, і ми скажемо, чи встигнемо сьогодні.",
              viber=None, call="Подзвонити"),
    why_title="Чому до нас повертаються",
    why=[("Беремося за складне", "Ремонтуємо речі, від яких відмовилися в інших ательє."),
         ("Акуратні шви", "Шов після ремонту майже не видно."),
         ("Швидко", "Прості роботи часто робимо за кілька годин."),
         ("Уважно до побажань", "Порадимо, як краще зробити, і зробимо так, як ви хочете.")],
    steps_title="Як замовити",
    steps=[("Принесіть річ", "Або надішліть фото у Viber, щоб ми одразу підказали."),
           ("Узгодимо роботу", "Скажемо, що можна зробити, скільки це коштує і коли буде готово."),
           ("Заберіть готове", "Приходьте в зручний час: ми працюємо щодня.")],
    form=dict(title="Передзвонимо вам", lead="Залиште номер, і ми передзвонимо в робочий час.",
              need_label="Що потрібно зробити", need_placeholder="Наприклад: вкоротити джинси на 3 см",
              button="Передзвоніть мені", aside=None),
    faq=[("Скільки часу займає ремонт?", "Прості роботи, як-от вкоротити штани, часто робимо за кілька годин. Точний строк скажемо, коли побачимо річ."),
         ("Чи ремонтуєте пуховики?", "Так, ремонтуємо куртки й пуховики, зокрема шви, з яких лізе пух."),
         ("Чи шиєте на замовлення?", "Так, ательє займається і ремонтом, і пошиттям одягу."),
         ("Де ви знаходитеся?", "Просп. Червоної Калини, 36, у ТК «Шувар». Працюємо щодня з 11:00 до 19:00.")],
    address_display="просп. Червоної Калини, 36, Львів", address_note="у ТК «Шувар»",
    street="просп. Червоної Калини, 36", locality="Львів", postal="79000",
    geo=(49.7988889, 24.046667), place_id="ChIJrVLnNgvoOkcRtSgPhYw_weo",
    hours={d: (11, 19) for d in range(7)},
    logo_svg=TAPE_LOGO, hero_svg=NEEDLE,
)

SITES = [SHYNOMONTAZH, PERETYAZHKA, VINTAZH]
