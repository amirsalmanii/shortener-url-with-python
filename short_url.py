class UrlShortener:
    url_to_id = {}
    id = 100
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def shorten_url(self, orginal_url):
        if orginal_url in self.url_to_id:
            id = self.url_to_id.get(orginal_url)
            shorten_url = self.encode_62(id)
        else:
            self.url_to_id[orginal_url] = self.id
            shorten_url = self.encode_62(self.id)
            self.id += 1
        return f"short_url.com/{shorten_url}"

    def encode_62(self, id):
        """
        this function make id to encode 62
        and return
        """
        
        base = len(self.characters)

        return_li = []
        while id > 0:
            val = id % base
            return_li.append(self.characters[val])
            id = id // base
        
        return "".join(return_li[::-1])

    def decode_url(self, short_url):
        """
        this function make base62 to decode int
        and get real url and return
        """
        short_url = short_url.split('/')[1]
        base = len(self.characters)
        strlen = len(short_url)
        num = 0

        idx = 0
        for char in short_url:
            power = (strlen - (idx + 1))
            num += self.characters.index(char) * (base ** power)
            idx += 1
        try:
            value = [i for i in self.url_to_id if self.url_to_id[i]==num][0]
            return value
        except:
            return None
