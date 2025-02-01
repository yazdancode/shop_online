

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('login-form');
    const phoneInput = document.getElementById('phone');

    form.addEventListener('submit', function(event) {
        // چک کردن اینکه فیلد خالی است یا نه
        if (phoneInput.value.trim() === '') {
            event.preventDefault(); // جلوگیری از ارسال فرم
            phoneInput.classList.add('error'); // اضافه کردن کلاس خطا
            alert('لطفاً این قسمت را خالی نگذارید'); // نمایش پیام
        } else {
            phoneInput.classList.remove('error'); // حذف کلاس خطا اگر فیلد پر شده باشد
        }
    });

    // تغییر رنگ باکس هنگام کلیک
    phoneInput.addEventListener('focus', function() {
        phoneInput.classList.remove('error'); // وقتی که کاربر روی فیلد کلیک کند و خالی نباشد
    });
});
