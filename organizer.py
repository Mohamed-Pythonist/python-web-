import os
import shutil

# تحديد الفولدر المراد ترتيبه
folder_path = "C:/Users/YourName/Downloads" 

def organize_folder(path):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            file_extension = filename.split('.')[-1].lower()
            
            # إنشاء مجلد جديد لكل نوع ملف
            new_folder = os.path.join(path, file_extension)
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
            
            # نقل الملف
            shutil.move(os.path.join(path, filename), os.path.join(new_folder, filename))
            print(f"تم نقل: {filename} إلى مجلد {file_extension}")

if __name__ == "__main__":
    # تأكد من تغيير المسار قبل التشغيل
    organize_folder(folder_path)
    print("✅ تم ترتيب الملفات بنجاح!")
