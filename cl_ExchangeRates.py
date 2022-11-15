import requests as request
import datetime
class Rates:

    _url = " "
    _res = " "
    def Print_information(self):
        Name = input('Enter currency abbreviation: (EUR or USD or ...): ')
        for item in self.res.json():
            if item['CurrencyCodeL'] == Name:
                print("*" * 100)
                print(f"{item['CurrencyCodeL']} to UAH: {item['Amount']}")
                print("*" * 100)
                break

    def write_in_file(self):
        with open('Exchange Rates.txt', 'w', encoding='UTF-8') as file:
            file.write(f"Date: {datetime.datetime.now()}"[:16] + "\n")
            print(f"Date: {datetime.datetime.now()}"[:16])
            for item in self.res.json():
                file.write(f"{item['txt']} to UAH: {item['rate']}\n")
                print(f"{item['txt']} ({item['cc']}) to UAH: {item['rate']}")
            print("*" * 100)

    def __init__(self, url_connect):
        if self.Connect_and_Check(url_connect):
            try:
                if self.res.headers['Content-Type'] == 'application/json; charset=utf-8':
                    if url_connect.find('date=') != -1:
                        self.Print_information()
                    else:
                        self.write_in_file()
            except Exception:
                print("is not json format")
        else:
            print("not connection")

    @property
    def res(self):
        return self._res

    @res.setter
    def res(self, val: str):
        self._res = val

    def Connect_and_Check(self, url):
        try:
            self.res = request.get(url)
            return True
        except request.exceptions.HTTPError as HttpError:
            print(HttpError)
            return False
        except request.exceptions.ConnectionError as ConnectError:
            print(ConnectError)
            return False
        except request.exceptions.URLRequired as UrlError:
            print(UrlError)
            return False
        except request.exceptions.InvalidSchema as SchemaError:
            print(SchemaError)
            return False
        except Exception:
            print(Exception)
            return False

