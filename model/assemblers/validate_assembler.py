class ValidateAssembler:
    def assemble_validation(self, user_id, login_token, login_tokens_repository):
        if self.__check_missing_params(user_id, login_token):
            valid = False
        else:
            valid = login_tokens_repository.validate_login_token(int(user_id), login_token)
        return {'valid': valid}

    def __check_missing_params(self, user_id, login_token):
        if user_id == "undefined" or login_token == "undefined":
            return True
        return False

    def is_requiring_authentication(self, request):
        is_validation_free = request.path.startswith("/login") or request.path == "/users" or request.method == "OPTIONS"
        modifies_data = request.method in ['POST', 'PUT', 'DELETE', 'PATCH']
        is_convo = request.path.startswith("/convo")
        is_subbed = request.path.startswith("/subbed")

        return not is_validation_free and (modifies_data or is_convo or is_subbed)
