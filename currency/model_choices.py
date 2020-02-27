CURR_USD, CURR_EUR = range(1, 3)

CURRENCY_CHOICES = (
    (CURR_USD, 'USD'),
    (CURR_EUR, 'EUR'),
)

SR_PRIVAT, SR_MONO, SR_VKURSE, SR_OTP = range(1, 5)

SOURCE_CHOICES = (
    (SR_PRIVAT, 'PrivetBank'),
    (SR_MONO, 'MonoBank'),
    (SR_VKURSE, 'Vkurse'),
    (SR_OTP, 'OTP-bank'),
)
