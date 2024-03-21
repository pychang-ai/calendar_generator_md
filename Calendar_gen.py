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
    print(dateimport sublime
import sublime_plugin
from datetime import datetime, timedelta

class InsertMonthDatesCommand(sublime_plugin.TextCommand):
    def run(self, edit, year=None, month=None):
        if year is None or month is None:
            sublime.message_dialog("Please provide the year and month.")
            return

        try:
            month_date = datetime(year, month, 1)
        except ValueError:
            sublime.message_dialog("Invalid year or month.")
            return

        last_day = self.get_last_day_of_month(year, month)

        for i in range(last_day, 0, -1):
            date = datetime(year, month, i)
            formatted_date = date.strftime("%Y_%m%d %a").upper()
            self.view.insert(edit, self.view.size(), f"## {formatted_date}\n")

        month_name = month_date.strftime("%B").upper()
        self.view.insert(edit, self.view.size(), f"## {month_name}\n")

    def get_last_day_of_month(self, year, month):
        if month == 12:
            return 31
        else:
            next_month = datetime(year, month + 1, 1)
            return (next_month - timedelta(days=1)).day

def plugin_loaded():
    sublime_plugin.register_command("insert_month_dates", InsertMonthDatesCommand)

## 2024_0430 TUE
## 2024_0429 MON
## 2024_0428 SUN
## 2024_0427 SAT
## 2024_0426 FRI
## 2024_0425 THU
## 2024_0424 WED
## 2024_0423 TUE
## 2024_0422 MON
## 2024_0421 SUN
## 2024_0420 SAT
## 2024_0419 FRI
## 2024_0418 THU
## 2024_0417 WED
## 2024_0416 TUE
## 2024_0415 MON
## 2024_0414 SUN
## 2024_0413 SAT
## 2024_0412 FRI
## 2024_0411 THU
## 2024_0410 WED
## 2024_0409 TUE
## 2024_0408 MON
## 2024_0407 SUN
## 2024_0406 SAT
## 2024_0405 FRI
## 2024_0404 THU
## 2024_0403 WED
## 2024_0402 TUE
## 2024_0401 MON
## APRIL
)