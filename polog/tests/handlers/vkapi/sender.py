# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from polog.handlers.abstract.base import BaseHandler

class VK_sender(BaseHandler):
	"""
	Создание объекта отправки сообщения от vk-бота.
	При вызове объекта данного класса происходит отправка логов в виде автоматических сообщений с помощью VK API.

    Обязательные аргументы:
    token (str) - токен для инициализации бота.
    chat_id (int) -  id чата (пользователя vk), куда отсылать сообщение.
    Необязательные аргументы:
    text_assembler (function) - альтернативная функция для генерации текста сообщений. Должна принимать в себя те же аргументы, что метод .__call__() текущего класса и возвращать строковый объект.
    only_errors (bool) - фильтр на отправку сообщений. В режиме False (то есть по умолчанию) через него проходят все события. В режиме True - только ошибки, т. е., если это не ошибка, сообщение гарантированно отправлено не будет.
    filter (function) - дополнительный пользовательский фильтр на отправку сообщений. По умолчанию он отсутствует, т. е. отправляются сообщения обо всех событиях, прошедших через фильтр "only_errors" (см. строчкой выше). Пользователь может передать сюда свою функцию, которая должна принимать набор аргументов, аналогичный методу .__call__() текущего класса, и возвращать bool. Возвращенное значение True из данной функции будет означать, что сообщение нужно отправлять, а False - что нет.
    alt (function) - функция, которая будет выполнена в случае, если отправка сообщения не удалась или запрещена фильтрами. Должна принимать тот же набор аргументов, что и метод .__call__() текущего класса. Возвращаемые значения не используются.
	"""
	def __init__(self, token, peer_id, only_errors=None, text_assembler=None, filter=None, alt=None):
		vk_session = vk_api.VkApi(token=token)
		vk_session._auth_token()
		longpoll = VkLongPoll(vk_session)
		self.vk = vk_session.get_api()
		self.id = peer_id
		if not peer_id:
			for event in longpoll.listen():
				if event.type == VkEventType.MESSAGE_NEW and event.to_me:
					self.id = event.peer_id
					break
		self.only_errors = only_errors
		self.text_assembler = text_assembler
		self.filter = filter
		self.alt = alt
	
	def __repr__(self):
		return f'VK_sender(peer_id={self.id}, only_errors={self.only_errors}, text_assembler={self.text_assembler}, filter={self.filter}, alt={self.alt})'
	
	def do(self, content):
		"""
		Отправляет сообщение из полностью обработанной строки с логом.
		"""
		self.vk.messages.send(random_id=get_random_id(), peer_id=self.id, message=content)
	
	def get_content(self, args, **kwargs):
		"""
		получает сообщение
		"""
		if callable(self.text_assembler):
			return self.text_assembler(args, **kwargs)
		return self.get_standart_text(args, **kwargs)
	
	def get_standart_text(self, args, **kwargs):
		"""
		Метод, возвращающий текст письма по умолчанию.
		По умолчанию текст письма - это просто перечисление всех переданных в метод __call__() аргументов.
		"""
		elements = [f'{key} = {value}' for key, value in kwargs.items()]
		text = '\n'.join(elements)
		if text:
			text = f'Message from the Polog:\n\n{text}'
			return text
		return 'Empty message from the Polog.'

