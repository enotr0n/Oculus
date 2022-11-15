from bs4 import BeautifulSoup as bs
import requests


class Shodaner:

    def __shodan_ip_data(self, target):
        url = f'https://www.shodan.io/host/{target}'
        res = requests.get(url, headers=self.headers)
        soup = bs(res.text, "html.parser")
        card_general = soup.find(class_ = 'card card-yellow card-padding')
        if card_general:
            ports = soup.find_all(class_ = 'bg-primary')
            card_ports = soup.find_all(class_ = 'card card-padding banner')
            return card_general, ports, card_ports
    
    def shodan_lookup(self, ips):
        for target in ips:
            try:
                card_general, ports, card_ports = self.__shodan_ip_data(target)
                for i in range(len(ports)):
                    print(self.GREEN, f'<+ Port: {ports[i].text}  ::  {target}:{ports[i].text}')
                    print(self.CYAN, card_ports[i].text, self.WHITE)
                    self._write(f'<+ Port: {ports[i].text}  ::  {target}:{ports[i].text}\n', 'records')
                    self._write(f'{card_ports[i].text}\n', 'records')
            except:
                pass
