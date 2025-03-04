import json
from src.utils import filter_data
from src.utils import calculate_expenses_and_income
from src.utils import currency_ratings
from src.utils import stock_pricer


def events(transactions_df, date_str: str, range_type: str = "M"):
    """Функция, которая принимает на вход датафрейм с транзакциями, строку с датой и опционально строковый параметр,
    отвечающий за величину диапазона: W - неделя, на которую приходится дата, M - месяц, Y - год, ALL - все данные до
    указанной даты (по умолчанию берется месяц) и возвращает json с информацией о категориях расходов и пополнений, а
    также текущими курсами USD и стоимости акций из S&P 500"""
    start_date, end_date = filter_data(date_str, range_type)
    total_expenses, main_expenses, other_expenses, sorted_cash_and_transfer, total_income, sorted_income = (
        calculate_expenses_and_income(transactions_df, start_date, end_date))
    currencies = currency_ratings()
    stocks = stock_pricer()
    response = {
        "expences": {
            "total_amount": total_expenses,
            "main": main_expenses.append({"Остальное": other_expenses}),
            "transfers and cash": sorted_cash_and_transfer
        },
        "income": {
            "total_amount": total_income,
            "main": sorted_income
        },
        "currency_rates": currencies,
        "stock_prices": stocks
    }
    return json.dumps(response, ensure_ascii=False, indent=4)
