# # # debug_utils.py
# # import datetime

# # def debug_parse_datetime(value):
# #     """Функция для отладки парсинга даты и времени."""
# #     print("Value type:", type(value))
# #     return datetime.datetime.fromisoformat(value)


# # В файле dateparse.py

# import datetime

# def parse_datetime(value):
#     """Parse a string and return a datetime.datetime.

#     This function supports time zone offsets. When the input contains one,
#     the output uses a timezone with a fixed offset from UTC.

#     Raise ValueError if the input is well formatted but not a valid datetime.
#     Return None if the input isn't well formatted.
#     """
#     if isinstance(value, str):
#         try:
#             return datetime.datetime.fromisoformat(value)
#         except ValueError:
#             # Обработка ошибок парсинга
#             return None
#     else:
#         # Если значение не является строкой, вернуть None
#         return None
