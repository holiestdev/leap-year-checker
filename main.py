# 闰年判断 照着规则写的

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def main():
    print("=== 闰年检查器 ===")
    
    while True:
        user_input = input("\n输入年份 (q退出): ")
        
        if user_input.lower() == 'q':
            print("拜拜")
            break
        
        try:
            year = int(user_input)
        except:
            print("请输入数字")
            continue
        
        if year < 0:
            print("公元后才有闰年概念")
            continue
        
        if is_leap_year(year):
            print(f"{year} 是闰年 ✅")
        else:
            print(f"{year} 不是闰年 ❌")

if __name__ == "__main__":
    main()
