# Управление финансами

Этот скрипт позволяет вести учет расходов и доходов, а также просматривать текущий баланс.

## Использование

Приложение имеет простой текстовый интерфейс. Вы можете выбрать один из предложенных пунктов меню, введя соответствующий номер:

1. **Вывод баланса**: Показывает текущий баланс.
2. **Добавление записи**: Позволяет добавить новую запись о расходе или доходе.
3. **Обновление суммы для конкретной даты**: Обновляет сумму для конкретной даты.
4. **Поиск по дате**: Поиск записей по указанной дате.
5. **Просмотр расходов**: Показывает список всех расходов.
6. **Просмотр доходов**: Показывает список всех доходов.
7. **Выход**: Завершает работу приложения.

Приложение сохраняет данные о финансах в текстовом файле `financedoc.txt`.

## Важно

- Для корректной работы приложения убедитесь, что файл `financedoc.txt` существует в корневой директории приложения и имеет правильную структуру.
- Убедитесь, что данные, вводимые в приложение, соответствуют ожидаемому формату (например, дата в формате "YYYY-MM-DD", сумма - целое число).
- Приложение предоставляет только текстовый интерфейс, что делает его легко доступным и простым в использовании.

## Технические требования
- Язык программирования: Python3

# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Mihailprogram/FinanceManage
```
Запустить файл finance.py