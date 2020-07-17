import os
import sys
import random
import unittest


os.chdir("../")
sys.path[0] = os.getcwd()


import bit_help

class UtilitsTest(unittest.TestCase):
    def setUp(self):
        print("-" * 70)
        pass

    def tearDown(self):
        pass

    def test_convert_satoshis_to_bitcoins(self):
        sum_in_satoshis = 50000
        need_sum_in_bitcoins = 0.0005
        sum_in_bitcoins = bit_help.utilits.convert_satoshis_to_bitcoins(sum_in_satoshis)

        print("Ковертация {} сатошей в биткоины".format(sum_in_satoshis))
        text = "Должно выйти {}. На выходе {}"
        print(text.format(need_sum_in_bitcoins, sum_in_bitcoins))
        
        self.assertEqual(sum_in_bitcoins, need_sum_in_bitcoins)

    def test_convert_bitcoins_to_satoshis(self):
        sum_in_bitcoins = 0.0005
        need_sum_satoshis = 50000
        sum_in_satoshis = bit_help.utilits.convert_bitcoins_to_satoshis(sum_in_bitcoins)

        print("Ковертация {} биткоинов в сатоши".format(sum_in_satoshis))
        text = "Должно выйти {}. На выходе {}"
        print(text.format(need_sum_satoshis, sum_in_satoshis))

        self.assertEqual(sum_in_satoshis, need_sum_satoshis)


    def test_convert_bitcoins_to_satoshis_and_convert_satoshis_to_bitcoins(self):
        print("Проверка верности конвераций")
        random_number = random.randint(10000, 1000000)
        print("Рандомное выпавшее число: {}".format(random_number))
        sum_in_bitcoins = bit_help.utilits.convert_satoshis_to_bitcoins(random_number)
        sum_in_satoshis = bit_help.utilits.convert_bitcoins_to_satoshis(sum_in_bitcoins)

        text = "Сумма в сатошах: {}, сумма в биткоинах: {}"
        print(text.format(sum_in_satoshis, random_number))

        self.assertEqual(sum_in_satoshis, random_number)


    def test_address_validate(self):
        address = "3Cwgr2g7vsi1bXDUkpEnVoRLA9w4FZfC69"
        validate = bit_help.utilits.address_validate(address)
        print("Проверка валидатора адресов")
        print("Адрес {} валидный, ответ {}".format(address, validate))

        self.assertTrue(validate)



if __name__ == "__main__":
    unittest.main()