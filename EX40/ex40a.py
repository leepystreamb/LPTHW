# dict style
mystuff = {'apple': "I AM APPLES!"}
print mystuff['apple']

# module style
import mystuff
mystuff.apple()
print mystuff.tangerine


# class style
class Mystuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"

thing = Mystuff()
thing.apple()
print thing.tangerine
