class SubAssembler:
    def __parse_sub(self, sub):
        sub_info = {
            'name': sub[1],
            'creator_id': sub[2],
            'timestamp': sub[3],
            'description': sub[4],
            'subscribers_count': sub[5],
        }

        return sub[0], sub_info  # sub[0] = sub_id

    def assemble_subs(self, subs_list):
        subs = {}
        for sub in subs_list:
            sub_id, sub_info = self.__parse_sub(sub)
            subs[sub_id] = sub_info
        return subs

    def assemble_sub(self, sub):
        sub_id, sub_info = self.__parse_sub(sub)
        return {sub_id: sub_info}
