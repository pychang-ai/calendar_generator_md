from datetime import datetime, timedelta

def generate_dates(start_year, start_month, start_day):
    # 设置起始日期
    start_date = datetime(start_year, start_month, start_day)

    # 找到结束日期（当月的月底）
    if start_day == 1:
        end_date = start_date.replace(day=1, month=start_date.month+1) - timedelta(days=1)
    else:
        end_date = start_date.replace(day=1, month=start_date.month+1) - timedelta(days=start_day)

    # 生成日期列表
    dates = []
    current_date = end_date
    while current_date >= start_date:
        # 添加日期到列表
        dates.append(current_date.strftime("## %Y_%m%d %a"))
        # 减少一天
        current_date -= timedelta(days=1)

    return dates

# 调用函数生成4月份的日期
dates = generate_dates(2024, 5, 1)

# 打印生成的日期ggg
for date in dates:
    print(date)