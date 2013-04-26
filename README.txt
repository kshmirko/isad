isad Проект интерактивной системы анализа данных

Содержание:
-----------

1. Требования к программному обеспечению
2. Порядок установки




1. Требования к программному обеспечению
----------------------------------------

- Linux + python 2.7.3 (версия 3 не пойдет) 
- virtualenv
- pip
- git


2. Порядок установки
--------------------

- Запустите терминал
- создайте виртуальную среду где будет размещаться ваш сайт
  >> bash$ virtualenv --no-site-packages Projects
  >> bash$ cd Projects
  >> bash$ source bin/activate
  после этого приглашение командной строки изменится на 
  >>(Projects) bash$
  
- загружаем проект с git
  >>(Projects) bash$ git clone https://github.com/kshmirko/isad.git
  
- переходим на последнюю ветку
  >>(Projects) bash$ git checkout isad_with_db

- устанавливаем проект
  >>(Projects) bash$ python setup.py develop
  
- запускаем сервер
  >>(Projects) bash$ pserve --reload development.ini
  
- открываем браузер и переходим на страницу http://127.0.0.1:6543/



