from mta import MtaClass


class MainClass:
    def main(self):
        mta = MtaClass("http://web.mta.info/status/ServiceStatusSubway.xml")
        response_code = mta.mta()
        print(response_code)


if __name__ == '__main__':
    m = MainClass()
    m.main()
