# Hate speech check (data_analitics)

Проект, определяющий наличие ругательских английских слов в твитах, учитывая контекст сообщения.

**Принцип работы:**
+ Приложение принимает post-запросы, тело которого содержит массив твитов. В качестве ответа он возвращает json с массивами результатов по каждой модели.

**Пробное использование:**
+ Для запуска приложения необходимо перейти по ссылке http://84.201.170.226:8000/message/
+ Пример вводимых данных: 
```
{
   "predict_data": ["i hate you, die please", "im so happy cause today i found my friends", "trump is my president", "i learn colors white, yellow, green"]
} 
```

**Ссылки на блокноты с подробными моделями:**
+ Модель наивного Баеса: https://vk.com/away.php?to=https%3A%2F%2Fcolab.research.google.com%2Fdrive%2F1BHiQho9-M6b6IeQjqtU9OhAKrvfVAOk1%3Fusp%3Dsharing&cc_key=
+ Модель логической регрессии: https://vk.com/away.php?to=https%3A%2F%2Fcolab.research.google.com%2Fdrive%2F1AAi1tZjZE7e1nrBNDviywaH9uxlBZozi%3Fusp%3Dsharing&cc_key=
+ Нейронная сеть: https://vk.com/away.php?utf=1&to=https%3A%2F%2Fcolab.research.google.com%2Fdrive%2F1LjoZTq7JbZUywneom6i80His2ILbCHlF%3Fusp%3Dsharing
