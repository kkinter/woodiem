from rest_framework.exceptions import APIException


class CantFollowYourself(APIException):
    status_code = 403
    default_detail = "스스로를 팔로우 할 수 없습니다."
    default_code = "cant_follow_yourself"