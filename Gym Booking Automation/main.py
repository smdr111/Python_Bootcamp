from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import time

# Setup Chrome driver
ACCOUNT_EMAIL = "samandar@test.com"
ACCOUNT_PASSWORD = "samandargymroutine2026"
GYM_URL = "https://appbrewery.github.io/gym/"

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)

# Simple retry wrapper
def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)

def login():
    login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    submit_btn = driver.find_element(By.ID, "submit-button")
    submit_btn.click()
    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

# Function to book a class process that checks if the button text changed with retry
def book_class(booking_button):
    booking_button.click()
    # Wait for button state to change - will time out if booking failed
    wait.until(lambda d: booking_button.text == "Booked")

retry(login, description="login")

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

class_num = 0
waitlist_num = 0
booked_waitlisted_num = 0
new_bookings = []
new_waitlists = []
classes_booked = []

for card in class_cards:
    # Get the day title from the parent day group
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if this is a Tuesday  or Thursday
    if "Tue" in day_title or "Thu" in day_title:
        # Check if this is a 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            # Get the class name
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            classes_booked.append(class_name)
            # Find and click the book button
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            spot = button.text
            class_info = f"{class_name} on {day_title}"

            if spot == 'Book Class':
                retry(lambda: book_class(button), description="Booking")
                button.click()
                class_num += 1
                new_bookings.append(class_info)
                print(f"✓ Successfully Booked for: {class_info}")
                time.sleep(1)
            elif spot == 'Booked':
                booked_waitlisted_num += 1
                print(f"✓ Already booked for: {class_info}")
            elif spot == 'Join Waitlist':
                retry(lambda: book_class(button), description="Booking")
                button.click()
                waitlist_num += 1
                new_waitlists.append({class_info})
                print(f"✓ Joined waitlist for: {class_info}")
                time.sleep(1)
            elif spot == 'Waitlisted':
                booked_waitlisted_num += 1
                print(f"✓ Already waitlisted for: {class_info}")
            else:
                print('No Class Found!')


print(f"""\n\n\n--- BOOKING SUMMARY ---
Classes booked: {class_num}
Waitlists joined: {waitlist_num}
Already booked/waitlisted: {booked_waitlisted_num}
Total classes processed: {class_num + waitlist_num + booked_waitlisted_num}\n\n\n
--- DETAILED CLASS LIST ---
""")

if new_bookings:
    print('New Bookings:')
    for i in new_bookings: print(i)
else: print("No new Bookings exist!")

if new_waitlists:
    print('New Waitlists:')
    for i in new_waitlists:
        print(i)
else: print('No new Waitlists exist!')
# Function to navigate to my bookings with retry
def get_my_bookings():
    my_bookings_link = wait.until(ec.element_to_be_clickable((By.ID, "my-bookings-link")))
    my_bookings_link.click()
    # Wait for page to load - will time out if navigation failed
    wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

    cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

    # Ensure we actually found cards - if empty, the page might not have loaded
    if not cards:
        raise TimeoutException("No booking cards found - page may not have loaded")
    return cards

my_booking_class_cards = retry(get_my_bookings, description="Get my bookings")
verified_classes = []

try:
    my_booking_class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='booking-card-booking']")
    verified_classes = [i.find_element(By.CSS_SELECTOR,"h3[id^='booking-class-name-']").text for i in my_booking_class_cards]
except NoSuchElementException:
    pass

print('\n\n\n--- VERIFYING ON MY BOOKINGS PAGE ---')
for i in classes_booked:
    if i in verified_classes:
        print(f"✓ Verified: {i}")

n = len(my_booking_class_cards)
print(f"""\n\n\n--- VERIFICATION RESULT ---
Expected: {booked_waitlisted_num} bookings
Found: {n} bookings""")

if booked_waitlisted_num == n:
    print(f"✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {booked_waitlisted_num-n} bookings")






