import os, datetime

def analyze_project():
    print(' AI Assistant يعمل الآن...')
    print(f' المشروع: {os.getcwd()}')
    print(f' آخر تشغيل: {datetime.datetime.now()}')
    # مستقبلاً: إضافة تحليل كود، اكتشاف أخطاء، اقتراح تحسينات
    print(' التحليل الأولي مكتمل!')

if __name__ == '__main__':
    analyze_project()
