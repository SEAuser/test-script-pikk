from playwright.sync_api import sync_playwright

USERNAME = "SMMA_Approver"
PASSWORD = "SMMA_Approver"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=["--disable-blink-features=AutomationControlled"]
    )

    context = browser.new_context()
    page = context.new_page()

    # 1. buka login page
    page.goto("http://192.166.1.49:3080/login")

    # 2. isi username & password
    page.fill('input[placeholder="username"]', USERNAME)
    page.fill('input[placeholder="Password"]', PASSWORD)

    # 3. klik SIGN IN
    page.click('button:has-text("SIGN IN")')

    # 4. tunggu dashboard kebuka
    page.wait_for_url("**/home")
    page.wait_for_load_state("networkidle")

    print("✅ Login berhasil")

    # 5. klik tombol LOGOUT (icon button)
    page.click("button.v-btn.v-btn--icon")

    print("✅ Logout berhasil")

    # 6. tahan browser tetap terbuka
    input("Browser masih terbuka. Tekan ENTER untuk keluar...")
