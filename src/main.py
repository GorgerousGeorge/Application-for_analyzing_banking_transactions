from src.utils import data_path
from src.utils import filereader
from src.views import events
from src.reports import sending_by_category
from src.services import transaction_finder


def main():
    print("Здравствуйте")
    transaction_data = filereader(data_path)
    while True:
        print("Для просмотра общей информации о совершенных вами операциях, введите '1'\nДля того, чтобы найти "
              "операцию, введите '2'\nДля того, чтобы посмотреть отчет о тратах по определенной категории за последние "
              "3 месяца, введите '3'")
        user_choice = int(input())
        if user_choice == 1:
            while True:
                print("Чтобы посмотреть информацию об операциях за неделю - введите 'W'\nЧтобы посмотреть информацию об"
                      "операциях за месяц - введите 'M'\nЧтобы посмотреть информацию за год - введите Y\nЧтобы "
                      "посмотреть информацию за все время - введите 'ALL'")
                user_choice_2 = input()
                user_choice_2 = user_choice_2.upper()
                if user_choice_2 == "W" or user_choice_2 == "M" or user_choice_2 == "Y" or user_choice_2 == "ALL":
                    break
                else:
                    print("Выбор не распознан. Убедитесь, что используете английскую раскладку клавиатуры")
            print("Введите конечную дату интервала, за который будем просматривать информацию в формате дд.мм.гггг")
            end_date = input()
            print(events(transaction_data, end_date, user_choice_2))
        elif user_choice == 2:
            transaction_list = transaction_data.to_dict(orient="records")
            print("Введите словосочетание для поиска")
            search_descr = input()
            print(transaction_finder(transaction_list, search_descr))
        elif user_choice == 3:
            print("Введите название категории")
            category_name = input()
            sending_by_category(transaction_data, category_name))
        else:
            print("Выбор не распознан.")
