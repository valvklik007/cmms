# cmms


Это web приложения, система управления техническим обслуживанием.

Данное приложения, не предназначена для загрузки на сервер, а предназначена для автономного использования. 
Защиты от воздействия из вне, нет. Так как выше описано это связано из за того, что данное приложения должно использовано,  автономно.

# Техническое описания

Вы можете, создавать именованные карточки оборудования, где можете указать следующие параметры: С которыми вы можете ознакомиться ниже, на скриншоте.

![image](https://github.com/user-attachments/assets/2160724a-1cae-475e-889b-05059d90adf1)

Вы можете, хранить документацию, программное обеспечения к данному оборудованию и т.п, вкладке "Документы", оставлять свои комментарии, вкладке "Комментарии" и создавать регламент обслуживания
Если вы удаляете карточку оборудования, все связи с данной таблицей удаляются автоматически, но загруженная документация и т.п остаются всегда по пути "\static\manual\"

График обслуживания. Вы можете создавать, удалять, редактировать или отмечать выполненное ТО. Красным цветом подсвечивается, за два дня до ТО и продолжает она быть красным, пока вы не отметите, что ТО выполнено. Зеленым цветом обозначено, что ТО обслуживания которое было выполнено. Нейтральный цвет обозначает, что ТО еще не выполнено и еще не подошло его время. 

![image](https://github.com/user-attachments/assets/f0a7199b-b339-4ded-a8af-303465fd89c5)

Создания обслуживания для карточки оборудования. 
Вы можете создать регламент работ, вид работы, тип расписания и дата последнего ТО.

![image](https://github.com/user-attachments/assets/ba7c5320-c0c3-4581-956f-b393f1ffa262)


Как работает "тип расписания". Вы создаете имя варианта, выбираете период, день, неделя и т.п, и период времени. Например: (Пишите, один раз в 5 дней, в "Период" выбираете "дни", в "Время периода" устанавливаете 5)
Это параметр, прибавит к вашему последнему ТО, которое вы установили в "Дата последней работы". Например, вы выбрали один раз в неделю, вы установили дату последнего ТО 12.02.2025 к этой дате прибавиться неделя и в результате мы получим 19.02.2025

![image](https://github.com/user-attachments/assets/deb35c2c-5df3-4f70-8341-4080f858ad5a)

# Установка





























