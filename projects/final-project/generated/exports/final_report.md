# Фінальний звіт — Retrospective Board (HTML mockup)

Коротко
- Створено статичний HTML/CSS макет дошки: [final project/html_board/index.html](final project/html_board/index.html)
- Згенеровано рендери: PNG і JPG у папці [final project/generated/](final project/generated/)
 - Згенеровано рендери: PNG і JPG у папці [final project/generated/](final project/generated/)
  - [final project/generated/board_render.png](final project/generated/board_render.png)
  - [final project/generated/board_render.jpg](final project/generated/board_render.jpg)
  - [final project/generated/board_render_updated.png](final project/generated/board_render_updated.png)
  - [final project/generated/board_render_updated.jpg](final project/generated/board_render_updated.jpg)
  - [final project/generated/board_A4_portrait.png](final project/generated/board_A4_portrait.png)
  - [final project/generated/board_A4_landscape.png](final project/generated/board_A4_landscape.png)
  - [final project/generated/board_4k.png](final project/generated/board_4k.png)
  - [final project/generated/board_A4_portrait_updated.png](final project/generated/board_A4_portrait_updated.png)
  - [final project/generated/board_4k_updated.png](final project/generated/board_4k_updated.png)
- Підготовлено paste-ready пакет з нотатками: [final project/generated/retrospective_board_package_ua.md](final project/generated/retrospective_board_package_ua.md)

Як це зроблено
- Візуальна теза: спокійна, преміальна робоча панель — одна сильна ідея, чиста ієрархія, обмежена палітра і контрастні наліпки для читабельності.
- Контент план: хедер (тема + оновлена траєкторія), джерела, 5 колонок: Appreciation / Continue Doing / Stop Doing / Start Doing / Actions.
- Реалізація: верстка в `final project/html_board/index.html` (лише HTML+CSS, шрифт Inter з Google Fonts). Колірні варіанти наліпок реалізовані як CSS-класи.
- Рендер згенеровано через headless браузер (Playwright / Puppeteer / або внутрішня автоматизація): знімок повної сторінки збережено як PNG/JPG у [final project/generated/].

Як відтворити
1. Відкрити файл у браузері: `file:///.../final project/html_board/index.html` і зробити повно-сторінковий скріншот або "Print → Save as PDF / Save as image".
2. Програмно (Playwright Python example):

```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width':1400,'height':1000})
    page.goto('file:///D:/School/GoIT/Courses/career_training/final project/html_board/index.html')
    page.screenshot(path='D:/School/GoIT/Courses/career_training/final project/generated/board_render.png', full_page=True)
    page.screenshot(path='D:/School/GoIT/Courses/career_training/final project/generated/board_render.jpg', full_page=True, type='jpeg', quality=90)
    browser.close()
```

Файли у репозиторії
- [final project/html_board/index.html](final project/html_board/index.html)
- [final project/html_board/styles.css](final project/html_board/styles.css)
- [final project/generated/board_render.png](final project/generated/board_render.png)
- [final project/generated/board_render.jpg](final project/generated/board_render.jpg)
 - [final project/generated/board_render.jpg](final project/generated/board_render.jpg)
 - [final project/generated/board_render_updated.jpg](final project/generated/board_render_updated.jpg)
- [final project/generated/retrospective_board_package_ua.md](final project/generated/retrospective_board_package_ua.md)

Наступні кроки (опціонально)
- Затвердити макет та попросити згенерувати присаджені варіанти під різні розміри (A4, 1920×1080 тощо).
- Закомітити артефакти у git та створити реліз для відправки викладачу.

Якщо потрібно — відформатую типографіку, додам експорт для A4 та раніше згенерую PDF/JPG з більшою роздільністю.
