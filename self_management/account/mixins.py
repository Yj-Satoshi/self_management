import calendar
from collections import deque
import datetime
date_string = datetime.datetime.now()
now_year = date_string.year
now_month = date_string.month
to_day = date_string.day


class BaseCalendarMixin:
    """カレンダー関連Mixinの、基底クラス"""
    first_weekday = 0

    week_names = ['月', '火', '水', '木', '金', '土', '日']

    def setup_calendar(self):
        self._calendar = calendar.Calendar(self.first_weekday)

    def get_week_names(self):
        """first_weekday(最初に表示される曜日)にあわせて、week_namesをシフトする"""
        week_names = deque(self.week_names)
        week_names.rotate(-self.first_weekday)
        return week_names


class MonthCalendarMixin(BaseCalendarMixin):
    def get_month_days(self, date):
        return self._calendar.monthdatescalendar(date.year, date.month)

    def get_current_month(self):
        month = now_month
        year = now_year
        if month and year:
            month = datetime.date(year=int(year), month=int(month), day=1)
        else:
            month = datetime.date.today().replace(day=1)
        return month

    def get_month_calendar(self):
        self.setup_calendar()
        current_month = self.get_current_month()
        calendar_data = {
            'now': datetime.date.today(),
            'month_days': self.get_month_days(current_month),
            'month_current': current_month,
            'week_names': self.get_week_names(),
        }
        return calendar_data


class WeekCalendarMixin(BaseCalendarMixin):
    """週間カレンダーの機能を提供するMixin"""

    def get_week_days(self):
        """その週の日を全て返す"""
        month = now_month
        year = now_year
        day = to_day
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()

        for week in self._calendar.monthdatescalendar(date.year, date.month):
            if date in week:
                return week

    def get_week_calendar(self):
        """週間カレンダー情報の入った辞書を返す"""
        self.setup_calendar()
        days = self.get_week_days()
        calendar_data = {
            'now': datetime.date.today(),
            'week_days': days,
            'week_names': self.get_week_names(),
        }
        return calendar_data
