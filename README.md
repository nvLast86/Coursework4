# Coursework4

Проект Парсер вакансий создан для работы с API двух сайтов - hh.ru и superjob.ru.

Принцип работы:
1. Пользователь вводит ключевое слово для поиска
2. На основе него создаются экземпляры классов HeadHunter (hh.ru) и SuperJob c результатами поиска 
   в виде экземпляров класса Vacancy, поля которого содержат всю необходимую информацию о вакансии.
3. Экземпляр класса Connector объединяет в единый список списки вакансий с обоих сайтов.
4. Экземпляр класса ServiceBot делает выборку на основе предпочтений пользователя.
5. По желанию пользователя можно распечатать выборку и полный список в файл.
