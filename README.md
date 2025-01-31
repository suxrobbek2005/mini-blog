## **📌 Mini Blog – Umumiy Tushuncha**  

Bu **mini blog** loyihasi oddiy Flask ilova bo‘lib, unda foydalanuvchilar **blog postlar yaratishi**, ularni **ko‘rishi**, **qidirishi** va **o‘chirishlari** mumkin.  

💡 **Asosiy xususiyatlar:**  
✅ Blog post qo‘shish (title, content, created_at)  
✅ Barcha bloglarni ko‘rish  
✅ Bloglarni sarlavhasi bo‘yicha qidirish  
✅ Blogni to‘liq ochib ko‘rish  
✅ Blogni o‘chirish  

---

## **📂 Loyiha Tuzilishi**  

📂 **mini_blog/**  
┣ 📄 **app.py** (Flask backend – asosiy kod)  
┣ 📂 **templates/**  
┃ ┣ 📄 **index.html** (Homepage + Search)  
┃ ┣ 📄 **blogs.html** (Barcha bloglar sahifasi)  
┃ ┣ 📄 **detail.html** (Blogni to‘liq ko‘rish)  
┃ ┣ 📄 **add.html** (Yangi post qo‘shish sahifasi)  
┃  
┣ 📄 **data.json** (Bloglarni vaqtinchalik saqlash, agar list ishlatilmasa)  

---

## **📌 Har Bir Sahifa Batafsil**  

### **1️⃣ Homepage (`/`)** – **Bosh sahifa**  
- **Barcha blog postlarni chiqarish**  
- **Search input** orqali bloglarni **title bo‘yicha qidirish**  

🔹 **Frontend (index.html)**  
- Sahifaning yuqori qismida **qidiruv maydoni** bo‘ladi  
- Har bir blog post uchun **title** va **qisqacha content** chiqariladi  
- Title ustiga bossak, **blog tafsilotlari** (`/blogs/<id>`) sahifasi ochiladi  

🔹 **Backend (Flask)**  
- Search orqali **title bo‘yicha filtrlash**  
- Bloglar list yoki JSON fayldan olinadi  

---

### **2️⃣ Bloglar sahifasi (`/blogs`)**  
- Barcha blog postlarni **alohida sahifada ko‘rish**  
- **Homepage** bilan deyarli bir xil, lekin search bo‘lmaydi  

---

### **3️⃣ Blog batafsil (`/blogs/<id>`)**  
- **To‘liq blog kontenti** ko‘rsatiladi  
- **O‘chirish tugmasi** bo‘ladi  

🔹 **Frontend (detail.html)**  
- Blogning **sarlavhasi**  
- To‘liq **content**  
- **O‘chirish tugmasi** (`/delete/<id>`)  

🔹 **Backend (Flask)**  
- Berilgan `id` bo‘yicha postni olish  
- O‘chirish funksiyasi (`/delete/<id>` bilan)  

---

### **4️⃣ Yangi Post Qo‘shish (`/add`)**  
- **Forma orqali yangi blog qo‘shish**  
- Title, content maydonlari bo‘ladi  

🔹 **Frontend (add.html)**  
- 2 ta input: **Title** va **Content**  
- "Qo‘shish" tugmasi  

🔹 **Backend (Flask)**  
- Formadagi ma’lumotlarni olish  
- `created_at` avtomatik qo‘shish  
- Postni list yoki JSON faylga saqlash  

---

### **5️⃣ Postni O‘chirish (`/delete/<id>`)**  
- Berilgan `id` bo‘yicha postni o‘chirish  

🔹 **Frontend (detail.html)**  
- "O‘chirish" tugmasi (`/delete/<id>`)  

🔹 **Backend (Flask)**  
- `id` bo‘yicha blogni list yoki JSONdan o‘chirish  
