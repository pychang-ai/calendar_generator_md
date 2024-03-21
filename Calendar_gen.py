import sublime
import sublime_plugin
from datetime import datetime, timedelta

class InsertMonthDatesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Show input panel to get year
        self.view.window().show_input_panel("Please enter the year:", "", self.on_year_input, None, None)

    def on_year_input(self, year):
        # Validate the year
        try:
            year = int(year)
        except ValueError:
            sublime.error_message("Invalid year. Please enter a valid year.")
            return

        # Show input panel to get month
        self.view.window().show_input_panel("Please enter the month:", "", lambda month: self.on_month_input(year, month), None, None)

    def on_month_input(self, year, month):
        # Validate the month
        try:
            month = int(month)
            if month < 1 or month > 12:
                raise ValueError
        except ValueError:
            sublime.error_message("Invalid month. Please enter a valid month (1-12).")
            return

        # Generate and insert month dates
        self.insert_month_dates(year, month)

    def insert_month_dates(self, year, month):
        month_name = datetime(year, month, 1).strftime("%B").upper()
        month_content = ""
        for day in range(31, 0, -1):
            try:
                date = datetime(year, month, day)
                formatted_date = date.strftime("%Y_%m%d %a").upper()
                month_content += f"## {formatted_date}\n"
            except ValueError:
                continue
        month_content += f"## {month_name}\n"
        self.view.run_command("insert_snippet", {"contents": month_content})

## 2024_0531 FRI
## 2024_0530 THU
## 2024_0529 WED
## 2024_0528 TUE
## 2024_0527 MON
## 2024_0526 SUN
## 2024_0525 SAT
## 2024_0524 FRI
## 2024_0523 THU
## 2024_0522 WED
## 2024_0521 TUE
## 2024_0520 MON
## 2024_0519 SUN
## 2024_0518 SAT
## 2024_0517 FRI
## 2024_0516 THU
## 2024_0515 WED
## 2024_0514 TUE
## 2024_0513 MON
## 2024_0512 SUN
## 2024_0511 SAT
## 2024_0510 FRI
## 2024_0509 THU
## 2024_0508 WED
## 2024_0507 TUE
## 2024_0506 MON
## 2024_0505 SUN
## 2024_0504 SAT
## 2024_0503 FRI
## 2024_0502 THU
## 2024_0501 WED
## MAY
