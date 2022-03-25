class MessageAssembler:
	def assemble_convos(self, users):
		contacts = {}
		for user in users:
			id = user[0]
			username = user[1]
			contacts[id] = username

		return contacts
