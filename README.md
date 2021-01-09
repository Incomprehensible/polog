# Обработчик для логера Polog, основанный на VK API

Используйте его, подключив к [polog](https://github.com/pomponchik/polog), если вам понадобится отправлять логи в vk с помощью бота.

## Оглавление

- [**Быстрый старт**](#быстрый-старт)
- [**Настройки логгера**](#Настройки-логгера)

## Быстрый старт

Установите обработчик через [pip](https://pypi.org/project/polog/):

```
$ pip install vk_polog_handler
```

Прежде чем создавать обработчик для vk, нужно создать вк-бота с помощью [VK API](https://vk.com/dev/bots_docs). Если у вас уже есть свой бот, необходимо узнать его ключ доступа (поле токен). Помимо этого нужно знать peer_id юзера, которому будут приходить логи.
Свой peer_id можно узнать, передав в поле конструктора "peer_id" нулевое значение, после чего сработает код инициализации класса, ожидающий сообщение боту от нужного id.

```python

if not peer_id:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
	    print(event.peer_id) # выведите свой id в stdout
	    self.id = event.peer_id
	    break
```

## Настройки логгера

Свои токен и id необходимо сохранить в отдельных параметрах, и при создании обработчика передать их в параметры конструктора.

Как пример, можно сохранить параметры в отдельном файле my_config.py и импортировать их, после чего создавать обработчик. 

```python
from polog.handlers.vkapi.sender import VK_sender
from polog import config
from my_config import MY_TOKEN, MY_ID

config.add_handlers(VK_sender(MY_TOKEN, MY_ID))
```

После чего можно использовать обработчик по назначению.

```python
from polog import log
import time

def test_send_normal():
    log('kek')
    time.sleep(0.0001)
```

Все просто. Более подробно ознакомиться с логгером можно в документации к нему: [README к polog](https://github.com/pomponchik/polog/blob/master/README.md).
