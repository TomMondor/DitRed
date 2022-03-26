class MessageAssembler:
	def assemble_users(self, users):
		contacts = {}
		for user in users:
			id = user[0]
			username = user[1]
			contacts[id] = username

		return contacts

	def assemble_convo(self, convo):
		assembled_convo = {}
		for message in convo:
			current_message = {}
			current_message["sender_id"] = message[1]
			current_message["receiver_id"] = message[2]
			current_message["timestamp"] = message[3]
			current_message["content"] = message[4]
			assembled_convo[message[0]] = current_message
		
		return assembled_convo

	def assemble_message(self, message):
		assembled_message = {}
		assembled_message["id"] = message[0][0][0]
		assembled_message["sender_id"] = message[1]
		assembled_message["receiver_id"] = message[2]
		assembled_message["timestamp"] = message[3]
		assembled_message["content"] = message[4]

		return assembled_message
