# Kastro_qa_guru_Browserstack_Mobil_hw23

Task:

- Зарегистрировать аккаунт в https://browserstack.com

- Запустить автотест из занятия локально

- Разработать еще один автотест на открытие любой статьи

*- Вынести данные (логин, пароль, урл браузерстека и т.д.)

*- Сделать аттач видео по аналогии с java-кодом https://github.com/qa-guru/mobile-tests-13/blob/master/src/test/java/helpers/Attach.java

- Сделать сборку в дженкинсе

В качестве ответа на домашнее задание нужно прислать ссылку на репозиторий в гитхаб и аллюр-отчет в дженкинс


Start tests:
Being in the packet test: 
pytest browserstack_test.py
pytest browserstack_tests.py::test_search
pytest browserstack_tests.py::test_search -context=remote
