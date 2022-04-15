from exceptions.missing_exception.missing_sub_exception import *
from exceptions.invalid_exception.invalid_sub_exception import *


class SubAssembler:
    def __parse_sub(self, sub, author_name):
        sub_info = {
            'name': sub[1],
            'creator_id': sub[2],
            'creator_name': author_name,
            'timestamp': sub[3],
            'description': sub[4],
            'subscribers_count': sub[5],
        }

        return sub[0], sub_info  # sub[0] = sub_id

    def assemble_subs(self, subs_list, authors):
        subs = {}
        for sub in subs_list:
            sub_id, sub_info = self.__parse_sub(sub, authors[sub[2]])
            subs[sub_id] = sub_info
        return subs

    def assemble_sub(self, sub, author_name):
        sub_id, sub_info = self.__parse_sub(sub, author_name)
        return {sub_id: sub_info}

    def check_create_sub_request(self, request):
        self.__check_request_exists(request)
        self.__check_request_parameters_not_empty(request)
        self.__check_request_parameters_length(request)

    def check_subscribe_request(self, request):
        self.__check_request_exists(request)
        self.__check_subscribe_request_parameters_not_empty(request)

    def __check_request_exists(self, request):
        if not request:
            raise MissingSubException()

    def __check_request_parameters_not_empty(self, request):
        if 'name' not in request or 'creator_id' not in request or 'description' not in request:
            raise MissingSubException()

    def __check_subscribe_request_parameters_not_empty(self, request):
        if "user_id" not in request:
            raise MissingSubscribeException()

    def __check_request_parameters_length(self, request):
        if len(request['name']) > 100:
            raise InvalidSubNameException()
        if len(request['description']) > 1000:
            raise InvalidSubDescriptionException()
