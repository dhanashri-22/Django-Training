from rest_framework.throttling import UserRateThrottle

class ReviewDetailThrottle(UserRateThrottle):
    scope = 'throttling_for_ReviewDetail'

class ReviewListThrottle(UserRateThrottle):
    scope = 'throttling_for_ReviewList'